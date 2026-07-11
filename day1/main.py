import os
import sys
from dotenv import load_dotenv
from groq import Groq
from groq import NotFoundError

def main():
    load_dotenv()

    my_api_key = os.getenv("GROQ_API_KEY")

    if not my_api_key:
        raise ValueError("GROQ_API_KEY is not set in the environment variables.")

    client = Groq(api_key=my_api_key)

    fallback_models = [
        os.getenv("GROQ_MODEL"),
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "llama3-8b-8192",
        "mixtral-8x7b-32768",
    ]
    models_to_try = [model for model in fallback_models if model]
    prompt = " ".join(sys.argv[1:]).strip() or "Write a poem about the beauty of nature."
    role = "user"

    message = {
        "role": role,
        "content": prompt,
    }

    messages = [message]

    last_error = None
    for model in models_to_try:
        try:
            response = client.chat.completions.create(model=model, messages=messages)
            print(response.choices[0].message.content)
            return
        except NotFoundError as error:
            last_error = error

    raise RuntimeError(
        "None of the configured Groq models were available: " + ", ".join(models_to_try)
    ) from last_error


if __name__ == "__main__":
    main()