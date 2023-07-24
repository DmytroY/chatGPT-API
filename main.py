''' Using openAI chatGPT API '''
import sys
import openai

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

openai.api_key = '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'
messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

while True:
    message = input("User: ")
    if message == "quit" or message == "exit" or message == "вийти" or message == "годі" or message == "геть":
        sys.exit()

    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    print(GREEN + f"ChatGPT: {reply}" + RESET)
    print()
    messages.append({"role": "assistant", "content": reply})