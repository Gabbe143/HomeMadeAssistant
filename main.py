import playsound
import datetime
import speech_recognition as sr
import pyttsx3
import requests


def say_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    engine.say('The current time is ' + time)
    engine.runAndWait()


def temperature():
    get_request = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=Sävja&appid=39e870fdecb055374d029c70bc4ed764')
    json_object = get_request.json()
    temp_kelvin = float(json_object['main']['temp'])
    temp_celcius = temp_kelvin - 273.15
    engine.setProperty('rate', 130)
    engine.say('It is ' + str(temp_celcius) + 'celsius outside')    # Risk för regn?
    engine.runAndWait()


continueSpeech = True
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voiceRate = 145
now = datetime.datetime.now().strftime('%H %M')
print(now)

while continueSpeech:
    try:
        engine.setProperty('rate', voiceRate)
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey' in command:
                engine.say('Yooooooooooooooooo how are you???')
                engine.runAndWait()
            elif 'time' in command:
                say_time()
            elif 'temp' in command:
                temperature()
            elif 'who are you' in command:
                print('Sound')  # playsound('path')
    except:
        print('error')
        pass
