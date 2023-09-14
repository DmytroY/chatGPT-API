''' Using openAI chatGPT API '''
import sys
import os
import openai
from config import OPENAI_API_KEY
from stt import recognize_speech
from tts import text_to_speech


# RED = '\033[91m'
# YELLOW = '\033[93m'

GREEN = '\033[92m'
RESET = '\033[0m'

openai.api_key = OPENAI_API_KEY

messages = [ {"role": "system", "content": "You are a intelligent assistant and you speak Ukrainian"} ]

while True:
    # message = input("User: ")
    # розпізнавання усного запитання
    message = ''
    while message == '':
        message = recognize_speech()
    print("User: " + message)

    if message == "quit" or message == "exit" or message == "вийти" or message == "вихід" or message == "годі" or message == "геть":
        sys.exit()

    if message:
        messages.append(
            {"role": "user", "content": message +  "? Обмеж довжину своєї відпові до 10 слів."},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    print(GREEN + f"ChatGPT: {reply}" + RESET)
    print()
    text_to_speech(str(reply))
    messages.append({"role": "assistant", "content": reply})
