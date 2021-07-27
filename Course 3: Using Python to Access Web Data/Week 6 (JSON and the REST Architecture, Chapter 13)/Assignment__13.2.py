import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("\nPlease enter a location:\n")
    if len(address) < 1:
        break

    parameters = dict()
    parameters['address'] = address
    parameters['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parameters)

    print("Retreiving ", url)
    try:
        data = urllib.request.urlopen(url, context=ctx)
    except:
        print("Can not connect to the server!")
        quit()

    decodedData = data.read().decode()

    try:
        parsedJSON = json.loads(decodedData)
    except:
        print("JSON = NONE")
        parsedJSON = None

    if not parsedJSON or 'status' not in parsedJSON or parsedJSON['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        quit()

    #print(parsedJSON)

    for key, value in parsedJSON.items():
        if key == 'place_id':
            print(value)
        else:
            if (type(value)) is list:
                for itemInLIST in value:
                    if (type(itemInLIST)) is dict:
                        dictInList = itemInLIST
                        for key, value in dictInList.items():
                            if key == 'place_id':
                                print("\nPLACE ID FOR: " + address)
                                print(value)
            elif (type(value)) is dict:
                for key, value in value.items():
                    if key == 'place_id':
                        print("\nPLACE ID FOR: " + address)
                        print(value)


# July 27, 2021 

# Kunal Wadhwa
# Contact  : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com
