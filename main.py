import os
import argparse
import json
import sys


from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages= [
            {
            "role": "system",
            "content": system_prompt},
            {
            "role": "user",
            "content": args.user_prompt,
            }
        ]

    iteration_limit = 20

    for i in range(iteration_limit):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions
        )
        message = response.choices[0].message
        if not message.tool_calls:
            messages.append(message)
            print(message.content)
            break
        messages.append(message)
        for tool_call in message.tool_calls:
            if tool_call.type != "function":
                continue
            result_message = call_function(tool_call, args.verbose)
            messages.append(result_message)
            if not result_message.get("content"):
                raise RuntimeError(f"Empty function response for {tool_call.function.name}")
            if args.verbose:
                print(f"-> {result_message['content']}")

        if response.usage == None:
            raise RuntimeError("failed API requests")
    else:
        print("Answer not found")
        sys.exit(1)
        


if __name__ == "__main__":
    main()
