import audioop
import math
import os
import random
import playsound
import datetime
import speech_recognition as sr
import pyttsx3
import requests
import pyaudio


def check_sound_volume():
    p = pyaudio.PyAudio()
    stream = p.open(source.SAMPLE_RATE, 1, source.format, True, False, source.CHUNK)
    data = stream.read(source.CHUNK)
    rms = audioop.rms(data, 2)
    decibel = 20*math.log10(rms)
    print(decibel)
    if 30 <= decibel <= 50:
        engine.say('why are you whispering?')
        engine.runAndWait()
        #   This might not work, unsure (stream might be inaccurate or wrong, try).


def say_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    engine.say('The current time is ' + time)
    engine.runAndWait()


def say_good_morning():
    engine.say('Good morning =)')
    engine.runAndWait()
    true_or_false = False
    return true_or_false


def temperature():
    get_request = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=Sävja&appid=39e870fdecb055374d029c70bc4ed764')
    json_object = get_request.json()
    temp_kelvin = float(json_object['main']['temp'])
    temp_celcius = temp_kelvin - 273.15
    engine.setProperty('rate', 130)
    engine.say('It is ' + str(temp_celcius) + 'celsius outside')  # Risk för regn/snö? Risk för åska?
    engine.runAndWait()


def add_all_jokes_to_list():
    list_of_jokes = []
    number_of_jokes = len([name for name in os.listdir('/someMap') if os.path.isfile(name)])
    #   print len([name for name in os.listdir('.') if os.path.isfile(name)])
    #   list_of_jokes.append(jokes + i)


continueSpeech = True
listener = sr.Recognizer()
engine = pyttsx3.init()
voiceRate = 145
morning_saying = True


while continueSpeech:
    try:
        if morning_saying:
            if datetime.datetime.now().strftime('%H %M') == datetime.time(22, 34).strftime('%H %M'):
                morning_saying = say_good_morning()
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
            #   Look up words on Wikipedia & say 'em
            elif 'say joke' or 'tell joke' in command:
                randomjoke = random.randrange(10)
                #   playsound.playsound(jokeEng+randomjoke)
    except:
        print('error')
        pass
