from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client=Groq()

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role":"user",
            "content":"prime minister of uk?"
        }
    ]
)

print(response.choices[0].message.content)