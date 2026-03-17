from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient, models



file_path = "./assets/project.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()
print(docs[0])

text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=100)
texts = []
ids = []
id = 0
for doc in docs:
    split = text_splitter.split_text(doc.page_content)
    for chunk in split:
        texts.append({"text":chunk})
        ids.append(id)
        id = id + 1
client = QdrantClient(host="localhost", port=6333)


model_name = "sentence-transformers/all-MiniLM-L6-v2"
collection_name = "major-project"
vectors = [models.Document(text=data["text"], model=model_name) for data in texts]

client.create_collection(
    collection_name,
    vectors_config=models.VectorParams(
        size=client.get_embedding_size(model_name), distance=models.Distance.COSINE)
)
client.upload_collection(
    collection_name=collection_name,
    vectors=vectors,
    ids=ids,
    payload=texts,
)
search_result = client.query_points(
    collection_name=collection_name,
    query=models.Document(text=input("prompt:"), model=model_name)
).points
    