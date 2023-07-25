''' text to speech module '''

from gtts import gTTS
import pydub
import pydub.playback

def text_to_speech(text):
    ''' convert text to mp3 file and play it '''
    tts = gTTS(text, lang='uk', slow=False)  # Specify the language (Ukrainian in this case)
    tts.save('output.mp3')  # Save the speech as an MP3 file

    # convert mp3 to wav and correct speed
    speed_multipl = 1.3 # No puede estar por debajo de 1.0

    sound = pydub.AudioSegment.from_file('output.mp3')
    so = sound.speedup(speed_multipl, 150, 25)
    so.export('output.wav', format = 'wav')

    # Play the MP3 file
    a = pydub.AudioSegment.from_mp3('output.wav')
    pydub.playback.play(a)
    return

# Example usage
# text_to_speech("Привіт!")
# text = '''Звичайно! Венера - друга планета від Сонця і найближча сусідка Землі. Вона отримала своє ім'я на честь римської богині краси та любові.

# Одна з найцікавіших особливостей Венери - це її атмосфера. Вона складається в основному з вуглекислого газу, з 
# малими кількостями азоту та інших газів. Дуже щільна та густа атмосфера створює великий глобальний парниковий ефект,
# що призводить до надзвичайно високої температури на поверхні планети - близько 460 градусів за Цельсієм. 
# Також атмосфера містить сильні вітри та хмарні покриви з кислотними розчинами.

# Поверхня Венери схожа на лавову пустелю, вкриту кратерами, вулканами та гірськими хребтами. Планета не має місяців і
# повільно обертається навколо своєї осі - одне обертання займає близько 243 земних днів. Але її роковий період - час,
# необхідний для здійснення повного обертання навколо Сонця - становить близько 225 земних днів.     

# Венера є однією із найяскравіших планет на небі через відбиття сонячного світла від її атмосфери. Вона може бути помітна
# на ранковому або вечірньому небі як "моргаюча" зірка.

# Хоча навряд чи буде можливість колонізувати Венеру через її непридатність для життя та важкі умови, вивчення цієї планети
# стало важливим для більш глибокого розуміння клімату та еволюції планети взагалі'''
# text_to_speech(text)
# text_to_speech("Як твої справи?")
