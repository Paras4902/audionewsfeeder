def speak(str1):
    from win32com.client import Dispatch
    speak1 = Dispatch("SAPI.spVoice")
    speak1.Speak(str1)


if __name__ == '__main__':
    import requests
    import json
    url = ('https://newsapi.org/v2/top-headlines?'
           'sources=bbc-sport&'
           'apiKey=49e391e7066c4158937096fb5e55fb5d')
    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(0, 11):
        try:
            speak(my_json['articles'][i]['title'])
        except IndexError:
            speak("News Ended")
