
from groq import Groq
from dotenv import load_dotenv
from system_prompt import SYSTEM_PROMPT

load_dotenv()


def main():
    try:
        client = Groq()  # Reads GROQ_API_KEY from .env

    except Exception as e:
        print(f"Error creating Groq client: {e}")
        return

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    print("-" * 50)
    print("TaskBuddy: Hey there! What's on your mind?")
    print("Type 'exit' or 'bye' to quit.")
    print("-" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if user_input.lower() in ["exit", "bye"]:
                print("TaskBuddy: Goodbye! Have a productive day.")
                break

            if not user_input:
                continue

            messages.append({
                "role": "user",
                "content": user_input
            })

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=messages
            )

            assistant_reply = response.choices[0].message.content

            print(f"\nTaskBuddy: {assistant_reply}")

            messages.append({
                "role": "assistant",
                "content": assistant_reply
            })

        except KeyboardInterrupt:
            print("\nTaskBuddy: Goodbye!")
            break

        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break


if __name__ == "__main__":
    main()
