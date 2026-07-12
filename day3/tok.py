import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

client = Groq(api_key=my_api_key)

model = os.getenv("GROQ_MODEL") or "llama-3.3-70b-versatile"

role = "user"
#3 prompts
prompt1 = "Suggest name for my Baby Girl"
prompt2 = "Suggest name for my Baby Boy"
prompt3 = "write a poem about the beauty of nature"

prompts=[prompt1, prompt2, prompt3]
for prompt in prompts:
    message_system = {
        "role": "system"   ,
        "content": "You are a Marathi pandit who is very knowledgeable about Marathi culture and traditions and  give 5 name suggestions."
    }

    #message me role and content
    message = {
        "role": role,   
        "content": prompt ,
    }

    messages = [message_system, message]

    response = client.chat.completions.create(model=model, messages=messages, temperature=0.5 ,max_tokens=100)

    usage = response.usage

    print(f"Prompt: {prompt} --> your tokens: {usage.prompt_tokens}, completion tokens: {usage.completion_tokens}, total tokens: {usage.total_tokens}")




