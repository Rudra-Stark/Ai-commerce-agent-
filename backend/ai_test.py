from ollama import chat 

response = chat(
    model = "qwen3:1.7b",
    messages = [
        {
            "role": "user",
            "content": "tell me the names of headphones that are less than 3000 rupees"
        }
    ]
)
print(response.message.content)