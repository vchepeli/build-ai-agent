import argparse
import os
import time
from dotenv import load_dotenv


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY environment variable not found. Please set it in your .env file.")

    from google import genai
    from google.genai import errors, types
    from prompts import system_prompt
    from call_function import available_functions, call_function

    client = genai.Client(api_key=api_key)

    prompt = args.user_prompt

    if args.verbose:
        print(f"User prompt: {prompt}")

    chat = client.chats.create(
        model="gemini-flash-lite-latest",
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
            temperature=0,
        ),
    )

    def send_message_with_retry(message, max_retries=5):
        for attempt in range(max_retries):
            try:
                return chat.send_message(message)
            except errors.ServerError:
                if attempt == max_retries - 1:
                    raise
                time.sleep(2**attempt)

    response = send_message_with_retry(prompt)

    for _ in range(20):

        if response.usage_metadata is None:
            raise RuntimeError("Usage metadata is None. The API request may have failed.")

        if args.verbose:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        # If no function calls, we have a final response
        if not response.function_calls:
            print("Final response:")
            print(response.text)
            break

        # Handle function calls
        function_response_parts = []
        for fc in response.function_calls:
            function_call_result = call_function(fc, verbose=args.verbose)
            if not function_call_result.parts:
                raise RuntimeError("No parts in function call result")
            function_response = function_call_result.parts[0].function_response
            if function_response is None:
                raise RuntimeError("No function response in function call result")
            if function_response.response is None:
                raise RuntimeError("No response in function response")
            if args.verbose:
                print(f" -> {function_call_result.parts[0].function_response.response}")
            function_response_parts.append(
                types.Part.from_function_response(
                    name=fc.name,
                    response=function_call_result.parts[0].function_response.response,
                )
            )

        # Send function results back through the chat session so history/signatures are preserved
        response = send_message_with_retry(function_response_parts)
    else:
        print("Error: Maximum iterations reached without a final response.")
        exit(1)


if __name__ == "__main__":
    main()
