from transformers import pipeline

pipe = pipeline("image-text-to-text", model="google/translategemma-4b-it")

messages = [
    {
        "role": "user",
        "content": [
            # {
            #     "type": "image",
            #     "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG",
            #     "source_lang_code": "en",
            #     "target_lang_code": "en"
            # },
            {
                "type": "text",
                "text": "What animal is on the candy?",
                "source_lang_code": "en",
                "target_lang_code": "hi"
            }
        ]
    }
]

result = pipe(text=messages)

print(result)