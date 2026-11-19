
from PIL import Image
image = Image.open("sample.png")
width, height = size(image)
print(f"{width} x {height} image opened")