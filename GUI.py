from tkinter import *
from datetime import datetime
import threading
import time

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

print(str(currentDateInfo))
print(str(currentTimeInfo))

def updateDate():
    while (updates):
        currentDateInfo=datetime.now().strftime("%d-%m-%Y")
        currentTimeInfo=datetime.now().strftime("%H:%M:%S")
        myDate.config(text=str(currentDateInfo))
        myTime.config(text=str(currentTimeInfo))
        print("Running")
        print(str(currentDateInfo))
        print(str(currentTimeInfo))
        time.sleep(0.5)
t=threading.Thread(target=updateDate)
t.start()




mainView.mainloop()
