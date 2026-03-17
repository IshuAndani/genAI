from qdrant_client import QdrantClient, models

client = QdrantClient(host="localhost", port=6333)


model_name = "sentence-transformers/all-MiniLM-L6-v2"
payload = [
    {"document": "Ishu Andani is the greatest bowler of all time.", "source": "ishu-ki-kitaab", },
    {"document": "Aryan is the greatest batsman of all time.", "source": "ishu-ki-kitaab"},
]
docs = [models.Document(text=data["document"], model=model_name) for data in payload]
ids = [42, 2]

client.create_collection(
    "demo_collection",
    vectors_config=models.VectorParams(
        size=client.get_embedding_size(model_name), distance=models.Distance.COSINE)
)

client.upload_collection(
    collection_name="demo_collection",
    vectors=docs,
    ids=ids,
    payload=payload,
)

search_result = client.query_points(
    collection_name="demo_collection",
    query=models.Document(text=input("prompt:"), model=model_name)
).points
print(search_result)