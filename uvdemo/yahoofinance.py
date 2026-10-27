# we will try fetch stockk price of appple

from groq import Groq
from  dotenv import load_dotenv

load_dotenv()

client = Groq()


result = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role":"user",
            "content":"what is apple's stock ticker and current price?"
        }
    ]
   
)

print(result.choices[0].message.content)