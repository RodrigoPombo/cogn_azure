import requests
import json
import time
headers = {'Content-Type': 'application/json','Ocp-Apim-Subscription-Key':'1c8d9effe1e74cbe9f48711ca7d694fc'}

r = requests.post('https://rodrigocognitive.cognitiveservices.azure.com/vision/v3.1/read/analyze?language=pt',headers=headers, data="""{'url':'https://pomboadlsgen2.blob.core.windows.net/blobtest/ATAAM.pdf?sp=r&st=2020-10-18T19:38:47Z&se=2020-10-19T03:38:47Z&sip=0.0.0.0-255.255.255.255&spr=https&sv=2019-12-12&sr=b&sig=J9WNZS5rJ7ArtwV1jSPWcxI5%2Bq1%2BBmCxZ48RNJv%2BBRg%3D'}""")
#r = requests.post('https://rodrigocognitive.cognitiveservices.azure.com/vision/v3.1/read/analyze?language=pt',headers=headers, data="""{'url':'https://intelligentkioskstore.blob.core.windows.net/visionapi/suggestedphotos/3.png'}""")
print(r.text)
x1 = (r.headers['apim-request-id'])
print(x1)
#print(x1) print kep from header

headers1 = {'Ocp-Apim-Subscription-Key':'1c8d9effe1e74cbe9f48711ca7d694fc'}

time.sleep(2)

check = "running"

while check=="running":
    try:
        x = requests.get("https://westeurope.api.cognitive.microsoft.com/vision/v3.1/read/analyzeResults/" + x1, headers=headers1)
        #x.json()["status"]
        print(x.text)
        check = x.json()["status"]
    except:
        check = "running"
        print("retry")


def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if (isinstance(v, (dict, list))) and (k!="words"):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

text = json_extract(x.json(), 'text')

#print(text)

#my_final_text = ' '.join(text)

my_final_text1 = []

for i in text:
    if "." == i[-1]:
        my_final_text1.append(i+"/n")
    else:
        my_final_text1.append(i)


my_final_texts = ' '.join(my_final_text1)
print(x)
print(my_final_texts)

#print(my_list)