from time import sleep

import requests
url=requests.get("https://api.ipify.org/?format=json")

print(url.text)
#while True:
    #url=requests.get("https://www.boredapi.com/api/activity")
    #print(url.json()['activity'])
    #sleep(2)
    
