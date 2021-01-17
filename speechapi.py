import requests
import json
import os
import speech_recognition as sr
from io import BufferedReader

api_key = "YOUR CLOUDCONVERT API KEY"

def proses_api():
    prosesBody = json.dumps({
        'apikey': api_key,
        'download': True,
        'filename': "temp.mp3",
        'input': "download",
        'inputformat': "mp3",
        'outputformat': "wav",
        'wait': True
    })

    proses = requests.post(
        'https://api.cloudconvert.com/v1/process', data=prosesBody, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'})

    result = 'https:' + proses.json()['url']
    return result


def convert_api(prosesURL, fileURL):
    convertBody = json.dumps({
        "apikey": api_key,
        "inputformat": "mp3",
        "outputformat": "wav",
        "input": "download",
        "file": fileURL,
        "filename": "temp.mp3",
        "wait": True,
        "download": False
    })

    proses = requests.post(prosesURL, data=convertBody, headers={'Content-Type': 'application/json'})

    result = 'https:' + proses.json()['output']['url']
    return result


def download(convertURL):
    proses = requests.get(convertURL, headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'})

    open('temp.wav', 'wb').write(proses.content)


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


url = input('Enter Captcha Audio URL: ')
proses = proses_api()
print('Process : 25% Complete')
convert = convert_api(proses, url)
print('Process : 50% Complete')
download(convert)
print('Process : 75% Complete')
speech_recognition()
