from tkinter import *
from datetime import datetime
import threading
import time
import requests

updates=True
currentDateInfo=datetime.now().strftime("%d-%m-%Y")
currentTimeInfo=datetime.now().strftime("%H:%M:%S")

mainView=Tk()
mainView.geometry('500x700')
mainView.configure(background='black')

myDate=Label(mainView,text=str(currentDateInfo),fg="gray",bg="black",font=("Comic Sans MS", 50))
myDate.pack()
myTime=Label(mainView,text=str(currentTimeInfo),fg="gray",bg="black",font=("Comic Sans MS", 50))
myTime.pack()

api='http://api.openweathermap.org/data/2.5/weather?appid=18e32a0b3135595acace9d680b9f3d29&q=Mumbai'
wData=requests.get(api).json()
weather=wData['weather'][0]['main']
print(weather)


def updateDate():
    while (updates):
        currentDateInfo=datetime.now().strftime("%d-%m-%Y")
        currentTimeInfo=datetime.now().strftime("%H:%M:%S")
        myDate.config(text=str(currentDateInfo))
        myTime.config(text=str(currentTimeInfo))
        time.sleep(0.5)
t=threading.Thread(target=updateDate)
t.start()




mainView.mainloop()
