from ollama import chat
from .tools import search_products_for_ai

response = chat(
    model = "qwen3:1.7b",
    messages = [
        {
            "role": "user",
            "content": "Find me headphones under 3000 rupees."
        }
    ],
    tools = [search_products_for_ai]
)
# # print(response.message)
# print("Tool calls:")
# print(response.message.tool_calls)

for tool_call in response.message.tool_calls:
    if tool_call.function.name == "search_products_for_ai":
        arguments = tool_call.function.arguments
        result = search_products_for_ai(**arguments)
        print("Tool result:")
        print(result)