import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model = os.getenv("GROQ_MODEL") or "llama-3.3-70b-versatile"

def llm_ans(prompt) :
    message = {
        "role": "user",
        "content": prompt
    }

    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages)
    ans= response.choices[0].message.content
    


bad_prompt="""
This is A User Complaint.My laptop is not working.classify this """

print(llm_ans(bad_prompt)) 