import requests
import os
import speech_recognition as sr
from io import BufferedReader
import subprocess

def speech_recognition():
    audio_file = 'temp.wav'

    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    try:
        print('Process : Complete \nResult   => ' + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))

    os.remove('temp.wav')


def get_audio():
    print('Process : Download File')
    r = requests.get(url)
    open('temp.mp3', 'wb').write(r.content)
    print('Process : Convert File')
    subprocess.call(['ffmpeg', '-i', 'temp.mp3',
                     'temp.wav'],  stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
    os.remove('temp.mp3')


url = input('Enter Captcha Audio URL: ')
get_audio()
print('Process : Translate File')
speech_recognition()
