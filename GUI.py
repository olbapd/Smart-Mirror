from tkinter import *
from datetime import datetime
import threading
import calendar
import time
import requests
import traceback
import json
from PIL import Image, ImageTk

updates=True

#Font Size
font_type= "Copperplate Gothic Bold"
large_text_size=14
xlarge_text_size=20
small_text_size=14
medium_text_size=18

#Current Date and Day Infor
currentDate=datetime.now().strftime("%d %b %Y")
currentDay=datetime.now().strftime("%A")


#Icons for wheather
weather_icon = {
    'clear-day': "assets/Sun.png", 
    'wind': "assets/Wind.png",  
    'cloudy': "assets/Cloud.png", 
    'partly-cloudy-day': "assets/PartlySunny.png", 
    'rain': "assets/Rain.png", 
    'snow': "assets/Snow.png", 
    'snow-thin': "assets/Snow.png", 
    'fog': "assets/Haze.png", 
    'clear-night': "assets/Moon.png", 
    'partly-cloudy-night': "assets/PartlyMoon.png", 
    'thunderstorm': "assets/Storm.png", 
    'tornado': "assests/Tornado.png",   
    'hail': "assests/Hail.png" 
}

def start_Window():
    global state
    mainView=Tk()
    mainView.configure(background='black')
    state=False

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
            temp_date=datetime.now().strftime("%a %d %b %Y")
            if temp_date != currentDate:
                currentDate=temp_date
                currentDay=datetime.now().strftime("%A")
                dayOWLbl.config(text=str(currentDay)) #Updates Day
                date_Label.config(text=str(temp_date)) #Update Date
            currentTimeInfo=datetime.now().strftime("%I :%M %p")
            time_Label.config(text=str(currentTimeInfo)) #Updates Time
            time.sleep(10)
	
    def updateWeather():
        currently_Label.config(text="Rainy")
        forecast_Label.config(text="Not Rainy")
        temperature_Label.config(text="20 C")
        location_Label.config(text="Cannot Pinpoint Location")

        image = Image.open(weather_icon['clear-day']) #Must change this
        image = image.resize((100, 100), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)
        icon_Label.config(image=photo)

	
    #Frames
    topFrame = Frame(mainView, background = 'black')
    topFrame.pack(side = TOP, fill=BOTH, expand = YES)
    top_rigt_Frame=Frame(topFrame, background = 'black')
    top_rigt_Frame.pack(side = RIGHT, fill=BOTH, expand = YES)
    top_left_Frame=Frame(topFrame, background = 'black')
    top_left_Frame.pack(side = LEFT, fill=BOTH, expand = YES)
    bottomFrame = Frame(mainView, background = 'black')
    bottomFrame.pack(side = BOTTOM, fill=BOTH, expand = YES)

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
    icon_Label = Label(degree_Frame, bg="black")
    icon_Label.pack(side=LEFT, anchor=N, padx=20)
    currently_Label = Label(top_left_Frame, font=(font_type, medium_text_size), fg="white", bg="black")
    currently_Label.pack(side=TOP, anchor=W)
    forecast_Label = Label(top_left_Frame, font=(font_type, small_text_size), fg="white", bg="black")
    forecast_Label.pack(side=TOP, anchor=W)
    location_Label = Label(top_left_Frame, font=(font_type, small_text_size), fg="white", bg="black")
    location_Label.pack(side=TOP, anchor=W)
    
    #Runs threads
    t_date=threading.Thread(target=updateDate)
    t_weather=threading.Thread(target=updateWeather)
    t_date.start()
    t_weather.start()

    mainView.mainloop()
 

    '''    
        # weather
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=LEFT, anchor=N, padx=100, pady=60)
        # news
        self.news = News(self.bottomFrame)
        self.news.pack(side=LEFT, anchor=S, padx=100, pady=60)'''
        




start_Window()
