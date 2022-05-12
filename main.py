#############################################################################################
#############################################################################################
################   This is made by Gabriel Jacobsen, a technology student.   ################
###################             This is the main branch                ###################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################


import audioop
import math
import os
import random
import time

import playsound
import datetime
import speech_recognition as sr
import pyttsx3
import requests


# import pyaudio


def microphone_error(engine):
    engine.say('I cannot hear you, perhaps your microphone is inaccurately configured. Please contact your closes '
               'Gabriel')
    engine.runAndWait()


# def check_sound_volume():
# p = pyaudio.PyAudio()
# stream = p.open(source.SAMPLE_RATE, 1, source.format, True, False, source.CHUNK,
# True)  # Error code -1073741819 (0xC0000005)
# data = stream.read(source.CHUNK)
# rms = audioop.rms(data, 2)
# decibel = 20 * math.log10(rms)
# print(decibel)
# time.sleep(1)

# stream.stop_stream()
# stream.close()

# p.terminate()
# if 30 <= decibel <= 50:
#   engine.say('why are you whispering?')
#   engine.runAndWait()
#   This might not work, unsure (stream might be inaccurate or wrong, try).


def say_time(engine):
    todays_time = datetime.datetime.now().strftime('%I:%M %p')
    print(todays_time)
    engine.say('The current time is ' + todays_time)
    engine.runAndWait()


def say_good_morning(engine):
    engine.say('Good morning =)')
    engine.runAndWait()
    true_or_false = False
    return true_or_false


def temperature(engine):
    get_request = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=Sävja&appid=39e870fdecb055374d029c70bc4ed764')
    json_object = get_request.json()
    temp_kelvin = float(json_object['main']['temp'])
    temp_celcius = int(temp_kelvin - 273.15)
    engine.setProperty('rate', 130)
    engine.say('It is ' + str(temp_celcius) + 'celsius outside')  # Risk för regn/snö? Risk för åska?
    engine.runAndWait()


def add_all_jokes_to_list():
    list_of_jokes = []
    number_of_jokes = len([name for name in os.listdir('/someMap') if os.path.isfile(name)])
    #   print len([name for name in os.listdir('.') if os.path.isfile(name)])
    #   list_of_jokes.append(jokes + i)


def main():
    continueSpeech = True
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voiceRate = 145
    morning_saying = True
    # format = pyaudio.paInt16
    while continueSpeech:
        try:
            engine.setProperty('rate', voiceRate)
            if morning_saying:
                if datetime.datetime.now().strftime('%H %M') == datetime.time(22, 34).strftime('%H %M'):
                    morning_saying = say_good_morning(engine)
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                # check_sound_volume()
                if 'hey' in command:
                    engine.say('Yooooooooooooooooo how are you???')
                    engine.runAndWait()
                elif 'time' in command:
                    say_time(engine)
                elif 'temp' in command:
                    temperature(engine)
                elif 'who are you' in command:
                    print('I am Gabbi bla bla bla')
                    #   I am Gabbi bla bla bla
                    #   playsound.playsound('who_are_you.mp4')
                elif 'say joke' or 'tell joke' in command:
                    randomjoke = random.randrange(10)
                    #   Look up words on Wikipedia/Google-jokes & say 'em
                    #   playsound.playsound(jokeEng+randomjoke.mp4)
        except:
            microphone_error(engine)
            print('error')
            pass


main()