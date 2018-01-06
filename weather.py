import requests
import traceback
import json

lat=''
lon=''

def get_ip():
    try:
        ip_url = "http://jsonip.com/"
        req = requests.get(ip_url)
        ip_json = json.loads(req.text)
        return ip_json['ip']
    except Exception as e:
        traceback.print_exc()
        print( "Error: %s. Cannot get ip." % e)
        return 0

def get_lat_long():
    global lat, lon
    ip= get_ip()
    if ip != 0:
        location_req_url = "http://freegeoip.net/json/%s" % get_ip()
        r = requests.get(location_req_url)
        location_obj = json.loads(r.text)
        lat = str(location_obj['latitude'])
        lon = str(location_obj['longitude'])
        return 1
    else:
        return 0

def get_Data():
    if get_lat_long() == 1:
        api='http://api.openweathermap.org/data/2.5/weather?appid=18e32a0b3135595acace9d680b9f3d29&lat='+lat+'&lon='+lon
        wData=requests.get(api).json()
        wInfo=wData['weather'][0]['description']
        wTemp=str(int(wData['main']['temp'])- 273.15).split('.')[0]
        wWindSpeed=str(wData['wind']['speed'])
        wCountry=wData['sys']['country']
        wCity=wData['name']
        return [wInfo,wTemp,wWindSpeed,wCountry,wCity]
    else:
        return [None]

