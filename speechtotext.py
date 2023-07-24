''' spech recognition '''
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажіть щось...")
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio, language="uk-UA")
        print("Розпізнаний текст: " + recognized_text)
    except sr.UnknownValueError:
        print("Не вдалося розпізнати текст")
    except sr.RequestError as e:
        print("Помилка сервісу розпізнавання: {0}".format(e))

recognize_speech()
