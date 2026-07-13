import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    issue: str
    location: str
    warranty_status: bool
    email_id: str
    contact_number: str



load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

client = Groq(api_key=my_api_key)

model = os.getenv("GROQ_MODEL") or "llama-3.3-70b-versatile"

role = "user"
# structured it by pydantic model

Schema = Ticket.model_json_schema() 

response_format={
    "type": "json_object",
    "schema": Schema
}






text="Hello ,My name is Jayesh Badgujar and My Hp Victus Laptop is not working properly. I have tried to restart it but it is not working. Can you please help me to fix it? I live in Pune and I have a warranty for my laptop. Please suggest me the best way to get it repaired.my email id is jayesh.badgujar@example.com and my contact number is +91-9876543210. I would appreciate your prompt assistance in resolving this issue. Thank you."
prompt = f"""""This is Customer Ticket . Extract Information from this text: {text} """



System_prompt=f"""Extract the personal information strictly the Schema provided in the response format {Schema} and return the output in JSON format. If any information is missing, return null for that field. Do not include any additional text or explanations in the response. Only provide the JSON object with the extracted information."""




#message me role and content
message = {
    "role": role,   
    "content": prompt,
}

message_system = {
    "role": "system",
    "content": System_prompt,
}
messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)

print(response.choices[0].message.content)


import json
raw_json = response.choices[0].message.content
try:
    parsed_data = json.loads(raw_json)
    ticket = Ticket(**parsed_data)
    print(ticket.contact_number)
    print(ticket.email_id)
    print(ticket.issue)
    print(ticket.location)
    print(ticket.name)
except json.JSONDecodeError:
    print("Failed to decode JSON")  
