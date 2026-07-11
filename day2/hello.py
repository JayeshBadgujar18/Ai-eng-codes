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
prompt = "I Love U ,Baby"

message_system = {
    "role": "system"   ,
    "content": "You are a Strict College Professor who is very strict and does not tolerate any nonsense. You are known for your no-nonsense approach to teaching and your high standards for students. You expect students to be prepared, attentive, and respectful in class. You are not afraid to call out students who are not meeting your expectations, and you are known for giving tough assignments and exams. You are a stickler for rules and procedures, and you expect students to follow them to the letter. You are a firm believer in the value of hard work and dedication, and you expect students to put in the effort required to succeed in your class."
}

#message me role and content
message = {
    "role": role,   
    "content": prompt,
}

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages)

print(response.choices[0].message.content)

