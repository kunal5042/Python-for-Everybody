import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter address:')
    if len(address) < 1: 
        print('Could not retrieve data from Google API')
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retreivng', url)
    uA = urllib.request.urlopen(url)
    data = uA.read().decode()
    print()
    print('Retrieved', len(data), 'characters')

    try:
        #Receives a dictionary
        js = json.loads(data)
    except:
        print('JSON = NONE')
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('COULD NOT RETRIEVE!')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    print('lat',lat, 'lng',lng)
    location = js['results'][0]['formatted_address']
    print(location)

# July 27, 2021 

# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com
