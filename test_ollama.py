import ollama

response = ollama.chat(
    model="llama3.2:1b",
    messages=[
        {
            "role": "user",
            "content": "Say hello and tell me your name."
        }
    ]
)

print(response["message"]["content"])