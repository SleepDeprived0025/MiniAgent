import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

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
    args = parser.parse_args()

    response = client.chat.completions.create(
        model="inclusionai/ling-3.0-flash-sante:free",
        messages=[
            {
                "role": "user",
                "content": args.user_prompt,
            }
        ],
    )
    if response.usage == None:
        raise RuntimeError("failed API requests")

    print("Response:")
    print(response.choices[0].message.content)
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")


if __name__ == "__main__":
    main()
