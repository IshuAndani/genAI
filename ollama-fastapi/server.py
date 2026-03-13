from fastapi import FastAPI
from ollama import chat

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World", "msg" : response}



response = chat(
    model="gemma:2b",
    messages=[
        {
            "role": "user",
            "content": "Why is the sky blue?",
        },
    ],
)
print(response.message.content)
