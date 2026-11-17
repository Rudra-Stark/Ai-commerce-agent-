from ollama import chat
from .tools import search_products_for_ai


tools = [search_products_for_ai]

available_functions = {
    "search_products_for_ai": search_products_for_ai
}


def run_agent(user_message: str):

    messages = [
        {
            "role": "user",
            "content": user_message
        }
    ]

    while True:

        response = chat(
            model="qwen3:1.7b",
            messages=messages,
            tools=tools
        )

        messages.append(response.message)

        if response.message.tool_calls:

            for tool_call in response.message.tool_calls:

                function = available_functions.get(
                    tool_call.function.name
                )

                if function:
                    result = function(
                        **tool_call.function.arguments
                    )
                # if function:
                #     arguments = tool_call.function.arguments

                #     print("\n--- AI TOOL DEBUG ---")
                #     print("Tool name:", tool_call.function.name)
                #     print("Arguments:", arguments)

                #     result = function(**arguments)

                #     print("Database result:", result)
                #     print("--- END DEBUG ---\n")

                    messages.append({
                        "role": "tool",
                        "tool_name": tool_call.function.name,
                        "content": str(result)
                    })

        else:
            return response.message.content