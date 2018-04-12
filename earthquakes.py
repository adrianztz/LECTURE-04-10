import requests
import json

from geopy.distance import vincenty

allHour = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
allDay = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
some = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"

def getEarthquakesData(url):
    jsonData = requests.get(url)
    eData = json.loads(jsonData.text)
    return eData

def numQuakes(eData):
    return len(eData["features"])

def magnitude(eData,num):
    return eData["features"][num]["properties"]["mag"]

def place(eData,num):
    return eData["features"][num]["properties"]["place"]

def lat(eData,num):
    "return the latitude of this earthquake"
    return eData["features"][num]["geometry"]["coordinates"][1]

def lon(eData,num):
    "return the longitude of this earthquake"
    return eData["features"][num]["geometry"]["coordinates"][0]

def distanceFromIslaVista(edata,num):
    elat = lat(edata,num)
    elon = lon(edata,num)
    return vincenty((elat,elon),(34.41,-119.86)).miles    

def listEarthquakes(d):
    for i in range(numQuakes(d)):
       print(i,magnitude(d,i),place(d,i), "distance from IV",distanceFromIslaVista(d,i))

    return None

def earthquakeHTMLTable(d):
    retVal = "<table>\n"
    retVal += "<tr><th>item</th><th>mag</th><th>place</th></tr>"
    for i in range(numQuakes(d)):
       retVal += "<tr>"
       retVal += "<td>" + str(i) + "</td>"
       retVal += "<td>" + str(magnitude(d,i)) + "</td>"
       retVal += "<td>" + str(place(d,i)) + "</td>"

       #print(magnitude(d,i),place(d,i), "distance from IV",distanceFromIslaVista(d,i))
       retVal += "</tr>\n"
    retVal += "</table>\n"
    return retVal

def listEarthquakesBiggerThan(d, mag):
    for i in range(numQuakes(d)):
       thisMagnitude = magnitude(d,i)
       if thisMagnitude > mag:
         print(i,magnitude(d,i),place(d,i))

    return None

ad = getEarthquakesData(allDay)
s = getEarthquakesData(some)

