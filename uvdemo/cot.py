from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

q = (
    "Roger has 5 tennis balls. He buys 2 cans of tennis balls. "
    "Each can has 3 balls. How many tennis balls does he have now?"
)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "user", "content": q}
    ],
    max_completion_tokens=200,
    temperature=0
)

choice = response.choices[0]

print("Finish reason:", choice.finish_reason)
print("Message:", choice.message)
print("Content:", choice.message.content)
print("Reasoning:", getattr(choice.message, "reasoning", None))