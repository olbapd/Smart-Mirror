from tkinter import *
from datetime import datetime
import threading
import calendar
import time
import requests
import traceback
import json


updates=True
currentDateInfo=datetime.now().strftime("%d-%m-%Y")
currentTimeInfo=datetime.now().strftime("%H:%M:%S")

mainView=Tk()
mainView.geometry('500x700')
mainView.configure(background='black')

myDate=Label(mainView,text=str(currentDateInfo),fg="white",bg="black",font=("Comic Sans MS", 50))
myDate.pack()
myTime=Label(mainView,text=str(currentTimeInfo),fg="white",bg="black",font=("Comic Sans MS", 50))
myTime.pack()

print(str(currentDateInfo)) 
print(str(currentTimeInfo))
def get_ip():
    try:
        ip_url = "http://jsonip.com/"
        req = requests.get(ip_url)
        ip_json = json.loads(req.text)
        return ip_json['ip']
    except Exception as e:
        traceback.print_exc()
        return "Error: %s. Cannot get ip." % e
def updateDate():
    while (updates):
        currentDateInfo=datetime.now().strftime("%a %d %b %Y")
        currentTimeInfo=datetime.now().strftime("%H:%M %p")
        myDate.config(text=str(currentDateInfo))
        myTime.config(text=str(currentTimeInfo))
        print("Running")
        time.sleep(0.5)
t=threading.Thread(target=updateDate)
t.start()
        
def get_lat_long():
    location_req_url = "http://freegeoip.net/json/%s" % get_ip()
    r = requests.get(location_req_url)
    location_obj = json.loads(r.text)
    lat = location_obj['latitude']
    lon = location_obj['longitude']
    print(lat)
    print(lon)

get_lat_long()

mainView.mainloop()
