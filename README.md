# recaptcha-bypass
reCaptcha audio bypass using speech recognition.

## Script Tipe

#### 1. Convert File with ffmpeg
```
pros : faster convert
cons : need install ffmpeg & add path in windows
```
#### 2. Convert File with CloudConvert API
```
pros : easy to use
cons : slower & limit 25 request/day
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Usage
```python
#Change with your CloudConvert API

api_key = "YOUR CLOUDCONVERT API KEY"
```

```bash
#How to run
#With ffmpeg => 
python speech.py

#With Cloud API =>
python speechapi.py
```

## Get Link
#### 1. Click Headphone Button
<img src="https://i.postimg.cc/Jzpy8d5J/click.png" height="200" align="center">

#### 2. Inspect Play Button
<img src="https://i.postimg.cc/W1BTZBj0/click.png" height="200" align="center">

#### 3. Type in browser console
```
document.querySelector('#audio-source').getAttribute('src')
```

## Result
<img src="https://i.postimg.cc/sxz6zX3T/click.png" height="200" align="center">
<img src="https://media.giphy.com/media/er6qoXSevhvnM2r6zs/giphy.gif"/>

## Refrence 
https://incolumitas.com/2021/01/02/breaking-audio-recaptcha-with-googles-own-speech-to-text-api/
https://github.com/ecthros/uncaptcha/

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
