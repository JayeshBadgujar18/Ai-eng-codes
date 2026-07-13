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
text="Hello ,My name is Jayesh Badgujar and My Hp Victus Laptop is not working properly. I have tried to restart it but it is not working. Can you please help me to fix it? I live in Pune and I have a warranty for my laptop. Please suggest me the best way to get it repaired.my email id is jayesh.badgujar@example.com and my contact number is +91-9876543210. I would appreciate your prompt assistance in resolving this issue. Thank you."
prompt = f"""""This is Customer Ticket . Extract Information from this text: {text} """



#message me role and content
message = {
    "role": role,   
    "content": prompt,
}

messages = [ message]

response = client.chat.completions.create(model=model, messages=messages)

print(response.choices[0].message.content)

