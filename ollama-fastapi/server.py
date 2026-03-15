from fastapi import FastAPI
from ollama import chat

app = FastAPI()


@app.get("/")
def read_root(input:str):
    response = chat(
        model="gemma:2b",
        messages=[
            {
                "role": "user",
                "content": input,
            },
        ],
    )
    return response.message.content
