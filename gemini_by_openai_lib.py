from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        # {   "role": "system",
        #     "content": "You are a helpful assistant."
        # },
        {
            "role": "user",
            "content": "Explain to me how AI works in a few words"
        }
    ]
)

print(response.choices[0].message.content)