from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as plt
img = Image.open('C:\\Users\\hp\\exo1_meca.png')
I1 = ImageDraw.Draw(img)
I1.text((331, 142), "L1=104,7mm", fill=(255,255, 255, 255))
img.save("C:\\Users\\hp\\exo1_meca.png")
plt.imshow(img)