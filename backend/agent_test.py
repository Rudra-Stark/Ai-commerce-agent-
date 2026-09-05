from ollama import chat
from .tools import search_products_for_ai

messages = [
    {
        "role": "user",
        "content": "Find me headphones under 3000 Rupees."
    }
]

response = chat(
    model = "qwen3:1.7b",
    messages = messages,
    tools = [search_products_for_ai]
)
# # print(response.message)
# print("Tool calls:")
# print(response.message.tool_calls)

messages.append(response.message)
for tool_call in response.message.tool_calls:

    if tool_call.function.name == "search_products_for_ai":
        arguments = tool_call.function.arguments
        result = search_products_for_ai(**arguments)
        messages.append({
            "role": "tool",
            "tool_name":tool_call.function.name,
            "content": str(result)
        })

final_response = chat(
    model = "qwen3:1.7b",
    messages = messages,
    tools = [search_products_for_ai]
)

print("Final answer:")
print(final_response.message.content)