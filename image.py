import matplotlib
import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import json
from PIL import Image
from io import BytesIO
from PIL import Image, ImageDraw
import matplotlib.image as mpimg
#tocommit
color="blue"

analyze_url = "https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true&returnFaceAttributes=age,gender"

# Set image_url to the URL of an image that you want to analyze.
#image_url = "https://docs.microsoft.com/learn/data-ai-cert/identify-faces-with-computer-vision/media/clo19_ubisoft_azure_068.png"
#image_url = "https://pomboadlsgen2.dfs.core.windows.net/blobtest/Photo.jpg?sv=2019-10-10&ss=bfqt&srt=sco&sp=rwdlacupx&se=2020-06-11T19:06:20Z&st=2020-06-10T11:06:20Z&spr=https&sig=onIpxkT3f6MYIAWDtE5r9I%2Fx6zlVbeEjG741%2FyQxxi8%3D"

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

local_path = "./data"
local_file_name = "quickstart" + str(uuid.uuid4()) + ".txt"
download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
print("\nDownloading blob to \n\t" + download_file_path)

with open(download_file_path, "wb") as download_file:
    download_file.write(blob_client.download_blob().readall())


headers = {'Ocp-Apim-Subscription-Key': "a2d94b7d0d334e95a329d11bbaa5fed5","Content-Type":"application/json"}
#params = {'visualFeatures': 'Categories,Description,Color'}
data = {'url': image_url}
response = requests.post(analyze_url, headers=headers, json=data)
response.raise_for_status()

#response from the api
analysis = response.json()
print(analysis)
top = analysis[0]["faceRectangle"]["top"]
height = analysis[0]["faceRectangle"]["height"]
left = analysis[0]["faceRectangle"]["left"]
width = analysis[0]["faceRectangle"]["width"]

#print("age: "+ analysis[0]["faceAttributes"]["age"])

response = requests.get(image_url)
#img = Image.open(BytesIO(response.content))

img = Image.open(BytesIO(response.content))
draw = ImageDraw.Draw(img)
draw.line([(left,top),(left+width,top)],fill=color, width=5)
draw.line([(left+width,top),(left+width,top+height)],fill=color , width=5)
draw.line([(left+width,top+height),(left, top+height)],fill=color , width=5)
draw.line([(left,top+height),(left, top)],fill=color , width=5)

plt.imshow(img)
plt.show()
print("done")



