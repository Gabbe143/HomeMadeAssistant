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
    get_request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Sävja&appid=39e870fdecb055374d029c70bc4ed764')
    json_object = get_request.json()
    temp_K = float(json_object['main']['temp'])
    temp_C = temp_K - 273.15
    return temp_C


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voiceRate = 145
now = datetime.datetime.now().strftime('%H %M')
print(now)

while(now < ):
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
                temp = int(temperature())
                engine.setProperty('rate', 130)
                engine.say('It is ' + str(temp) + 'celsius outside')
                engine.runAndWait()
    except:
        print('error')
        pass
