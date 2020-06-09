import matplotlib
import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import json
from PIL import Image
from io import BytesIO
from PIL import Image, ImageDraw
import matplotlib.image as mpimg

color="blue"

analyze_url = "https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true"

# Set image_url to the URL of an image that you want to analyze.
image_url = "https://docs.microsoft.com/learn/data-ai-cert/identify-faces-with-computer-vision/media/clo19_ubisoft_azure_068.png"

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



