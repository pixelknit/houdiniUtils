from openai import OpenAI
import openai

OPEN_AI_KEY = "your_api_key"

client = OpenAI(
        api_key=OPEN_AI_KEY
        )

def chat_with_gpt(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        )
    return completion.choices[0].message.content



if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
