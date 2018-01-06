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
        return "Error: %s. Cannot get ip." % e

def get_lat_long():
    location_req_url = "http://freegeoip.net/json/%s" % get_ip()
    r = requests.get(location_req_url)
    location_obj = json.loads(r.text)
    global lat, lon
    lat = str(location_obj['latitude'])
    lon = str(location_obj['longitude'])

get_lat_long()

api='http://api.openweathermap.org/data/2.5/weather?appid=18e32a0b3135595acace9d680b9f3d29&lat='+lat+'&lon='+lon

wData=requests.get(api).json()
wInfo=wData['weather'][0]['description']
wTemp=str(int(wData['main']['temp'])- 273.15).split('.')[0]
wWindSpeed=str(wData['wind']['speed'])
wCountry=wData['sys']['country']
wCity=wData['name']
print("General info: "+wInfo)
print("Temperature: "+wTemp)
print("Wind Speed: "+wWindSpeed)
print("Country: "+wCountry)
print("City: "+wCity)
