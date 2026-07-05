import urllib.request
from PIL import Image
import io

url = "https://upload.wikimedia.org/wikipedia/commons/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    img_data = response.read()

img = Image.open(io.BytesIO(img_data))
img.thumbnail((600, 900))
img.save("mona_lisa.jpg")
print("Image downloaded and resized!")
