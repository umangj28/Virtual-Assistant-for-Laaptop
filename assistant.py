import os
import speech_recognition as sr
from gtts import gTTS
#import datetime
import webbrowser as wb
import calendar
import cv2
import matplotlib.pyplot as plt
#from googletrans import Translator

#warnings.filterwarnings('ignore')
def recordAudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

    data=''
    try: 
        data=r.recognize_google(audio)
        print('You said: '+data)
    except:
        pass 

    return data

def assistantResponse(text):
    print(text)
    myobj= gTTS(text=text, lang='en',slow=False)
    myobj.save('assistant_response.mp3')
    os.system('start assistant_response.mp3')
    return


while True:
    text=recordAudio()
    text=text.lower()
    if('hi' in text):
        assistantResponse('Welcome Umang')
    if('how' in text or 'up' in text):
        assistantResponse('Better than ever, What about you?')
    if('bye' in text):
        assistantResponse('Bye Umang, lets talk soon.')
        break
    if('play' in text):
        #text=text.split()
        os.startfile('G:\Disney\[fmovies.to] Moana - HD 1080p.mp4')
    if('google' in text):
        #base='https://google.com/search?q='
        #url=base+text[7:len(text)]
        wb.open_new('https://google.com/search?q='+text[7:len(text)])
        assistantResponse('Sure, Here are the results for your search')
    if('youtube' in text):
        wb.open_new('https://youtube.com/search?q='+text[8:len(text)])
    if('pic' in text):
        os.startfile('C:\\Users\\UMANG JOSHI\\Pictures\\'+text[13:len(text)]+'.png')
    if('click' in text  or 'snap' in text):
        cap=cv2.VideoCapture(0)
        if cap.isOpened():
            ret,frame=cap.read()
            print(ret)
        else:
            ret=False
        print(frame)

        img1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        plt.imshow(img1)
        plt.title('Color Image RGB')
        plt.xticks([])
        plt.yticks([])
        plt.show()
        cap.release()
    if('calendar' in text):
        assistantResponse("Enter the year number and month number")
        y=int(input())
        m=int(input())
        print(calendar.month(y,m))
    
