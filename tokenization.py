import tiktoken
encoding = tiktoken.encoding_for_model("gpt-4o-mini")
text = "Ishu is great. Mahima is kutti-kamini."
tokens = encoding.encode(text=text)
print(f"Tokens : {tokens}")