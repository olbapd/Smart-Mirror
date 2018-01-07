from tkinter import *
from datetime import datetime
import threading
import calendar
import time
import requests
import traceback
import json
from PIL import Image, ImageTk
import speech_recognition as sr


#SM-Imports
import weather as wthr
import news as nw


updates=True
news=True
listening=True

#Search News
search=''
not_waiting=True

#Font Size
font_type= "Copperplate Gothic Bold"
large_text_size=25
xlarge_text_size=60
small_text_size=15
medium_text_size=20

#Current Date and Day Infor
currentDate=datetime.now().strftime("%d %b %Y")
currentDay=datetime.now().strftime("%A")


#Icons for wheather
weather_icon = {
    'clear sky': "assets/Sun.png", 
    'mist': "assets/Haze.png", 
    'snow': "assets/Snow.png", 
    'thunderstorm':"assets/Storm.png", 
    'rain':"assets/Rain.png",
    'frew clouds': "assets/PartlySunny.png", 
    'scattered clouds': "assets/Cloud.png", 
    'broken clouds': "assets/Cloud.png", 
    'shower rain':"assets/Rain.png",
    'few clouds': "assets/Cloud.png"
}
	
def start_Window():
    global state
    mainView=Tk()
    mainView.configure(background='black')
    mainView.attributes("-fullscreen", True)
    state=False

    def hide_message():
        time.sleep(3)
        message_Label.config(text='')

    def display_message(msg):
        message_Label.config(text=msg)
        t=threading.Thread(target=hide_message)
        t.start()
        

    def fullscreen(Event):
        global state
        state = not state
        mainView.attributes("-fullscreen", state)
        return "break"

    def end_fullscreen(Event):
        global state
        state = False
        mainView.attributes("-fullscreen", False)
        return "break"

    def updateDate():
        global currentDate,currentDay,currentTimeInfo
        while (updates):
            temp_date=datetime.now().strftime("%d %b %Y")
            if temp_date != currentDate:
                currentDate=temp_date
                currentDay=datetime.now().strftime("%A")
                dayOWLbl.config(text=str(currentDay)) #Updates Day
                date_Label.config(text=str(temp_date)) #Update Date
            currentTimeInfo=datetime.now().strftime("%I :%M %p")
            time_Label.config(text=str(currentTimeInfo)) #Updates Time
            time.sleep(5)
	
    def updateWeather():
        info=wthr.get_Data()
        if info[0]==None:
            currently_Label.config(text="")
            #forecast_Label.config(text="")
            temperature_Label.config(text="")
            location_Label.config(text="Cannot Pinpoint Location")
        else:
            loc_string=""+info[3]+", "+info[4]
            currently_Label.config(text=info[0])
            #forecast_Label.config(text=info[0])
            temperature_Label.config(text=""+info[1]+"°C")
            location_Label.config(text=loc_string)
            image_weather = Image.open(weather_icon[info[0]])
            image_weather = image_weather.resize((100, 100), Image.ANTIALIAS)
            image_weather = image_weather.convert('RGB')
            photo_weather = ImageTk.PhotoImage(image_weather)
            weather_icon_Label.config(image=photo_weather)
            weather_icon_Label.image=photo_weather
   
    def updateNews():
        global search,not_waiting
        image_news = Image.open("assets/Newspaper.png")
        image_news = image_news.resize((25, 25), Image.ANTIALIAS)
        image_news = image_news.convert('RGB')
        photo_news = ImageTk.PhotoImage(image_news)
        news_icon_Label1.config(image=photo_news)
        news_icon_Label2.config(image=photo_news)
        news_icon_Label3.config(image=photo_news)
        sources=["bbc-news","espn","cnn","fox-sports","marca","the-verge","crypto-coins-news","engadget","ign","abc-news","business-insider",
             "mtv-news","national-geographic","techradar"]
        contSource=0
        while(news):
            if search=='':
                if (contSource<len(sources)):
                    header=nw.getNews(contSource,sources)
                    event_Name_Label1.config(text=header[0])
                    event_Name_Label2.config(text=header[1])
                    event_Name_Label3.config(text=header[2])
                    contSource+=1
                    time.sleep(10)
                else:
                    contSource=0
                    time.sleep(10)
            else:
                display_message("Looking for " + search)
                nw.searchNews(search)
                search=''
                not_waiting=True

    def listen():
        global listening, record,audio
        # Record Audio
        record = sr.Recognizer()
        with sr.Microphone() as source:
            print("Waiting for instructions:")
            audio = record.listen(source)
        while(listening):
            # Speech recognition using Google Speech Recognition
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                if not_waiting:
                    voice=record.recognize_google(audio)
                    if "mirror" in voice.lower():
                        display_message("I'm listening")
                        voice=record.recognize_google(audio)
                        exec_command(voice)
                    else:
                        #listening=False
                        print(voice)
                        print("Ended")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                #listening=False
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                #listening=False
            time.sleep(5)
    
    def exec_command(command):
        global record,audio,search,not_waiting
        if command=="search news":
            display_message("What should I look for?")
            voice=record.recognize_google(audio)
            search=voice
            not_waiting=False

    #Frames
    topFrame = Frame(mainView, background = 'black')
    topFrame.pack(side = TOP, fill=BOTH, expand = YES)
    centerFrame = Frame(mainView, background = 'black')
    centerFrame.pack(side = TOP, fill=BOTH, expand = YES)
    top_rigt_Frame=Frame(topFrame, background = 'black')
    top_rigt_Frame.pack(side = RIGHT, fill=BOTH, expand = YES)
    top_left_Frame=Frame(topFrame, background = 'black')
    top_left_Frame.pack(side = LEFT, fill=BOTH, expand = YES)
    bottomFrame = Frame(mainView, background = 'black')
    bottomFrame.pack(side = BOTTOM, fill=BOTH, expand = YES)

    #Message Label
    message_Label=Label(centerFrame, font=(font_type, large_text_size), fg="white", bg="black")
    message_Label.pack()
    display_message("Greetings Lord Marco of the Macintosh!")

    #FullScreen Binding
    mainView.bind("<Up>", fullscreen)
    mainView.bind("<Escape>", end_fullscreen)

    #Time
    time_Label = Label(top_rigt_Frame, font=(font_type, large_text_size), fg="white", bg="black")
    time_Label.pack(side=TOP, anchor=E)
    #Day of Week
    dayOWLbl = Label(top_rigt_Frame, text=currentDay, font=(font_type, small_text_size), fg="white", bg="black")
    dayOWLbl.pack(side=TOP, anchor=E)

    #Date
    date_Label = Label(top_rigt_Frame, text=currentDate, font=(font_type, small_text_size), fg="white", bg="black")
    date_Label.pack(side=TOP, anchor=E)
    
    #Weather
    degree_Frame = Frame(top_left_Frame, bg="black")
    degree_Frame.pack(side=TOP, anchor=W)
    temperature_Label = Label(degree_Frame, font=(font_type, xlarge_text_size), fg="white", bg="black")
    temperature_Label.pack(side=LEFT, anchor=N)

    weather_icon_Label = Label(degree_Frame, bg="black")
    weather_icon_Label.pack(side=LEFT, anchor=N, padx=20)
    currently_Label = Label(top_left_Frame, font=(font_type, medium_text_size), fg="white", bg="black")
    currently_Label.pack(side=TOP, anchor=W)
    #forecast_Label = Label(top_left_Frame, font=(font_type, small_text_size), fg="white", bg="black")
    #forecast_Label.pack(side=TOP, anchor=W)
    location_Label = Label(top_left_Frame, font=(font_type, small_text_size), fg="white", bg="black")
    location_Label.pack(side=TOP, anchor=W)

    #News
    bottom_left_Frame=Frame(bottomFrame,bg="black")
    bottom_left_Frame.pack(side=LEFT, anchor=SW, padx=100, pady=60)
    news_Label = Label(bottom_left_Frame, text='News', font=(font_type, medium_text_size), fg="white", bg="black")
    news_Label.pack(side=TOP, anchor=NW)
    headlinesContainer1 = Frame(bottom_left_Frame, bg="black")
    headlinesContainer1.pack(anchor=W)
    headlinesContainer2 = Frame(bottom_left_Frame, bg="black")
    headlinesContainer2.pack(anchor=W)
    headlinesContainer3 = Frame(bottom_left_Frame, bg="black")
    headlinesContainer3.pack(anchor=W)

    news_icon_Label1=Label(headlinesContainer1, bg='black', image='')
    news_icon_Label1.pack(side=LEFT)
    event_Name_Label1 = Label(headlinesContainer1, text='', font=(font_type, small_text_size), fg="white", bg="black")
    event_Name_Label1.pack(side=LEFT)
    
    news_icon_Label2=Label(headlinesContainer2, bg='black', image='')
    news_icon_Label2.pack(side=LEFT, anchor=W)
    event_Name_Label2 = Label(headlinesContainer2, text='', font=(font_type, small_text_size), fg="white", bg="black")
    event_Name_Label2.pack(side=LEFT, anchor=W)
    
    news_icon_Label3=Label(headlinesContainer3, bg='black', image='')
    news_icon_Label3.pack(side=LEFT, anchor=W)
    event_Name_Label3 = Label(headlinesContainer3, text='', font=(font_type, small_text_size), fg="white", bg="black")
    event_Name_Label3.pack(side=LEFT, anchor=W)

    #Runs threads
    t_date=threading.Thread(target=updateDate)
    t_news=threading.Thread(target=updateNews)
    t_weather=threading.Thread(target=updateWeather)
    t_listen=threading.Thread(target=listen)
    t_date.start()
    t_news.start()
    t_weather.start()
    t_listen.start()

    mainView.mainloop()
 	 
start_Window()
