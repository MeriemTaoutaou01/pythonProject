import matplotlib.pyplot as plt
from PIL import Image
image = Image.open('C:\\Users\\hp\\exo1_meca.png')
plt.imshow(image)
plt.show()
from PIL import ImageDraw
I1 = ImageDraw.Draw(image)
I1.text((331, 142), "hello world", fill=(255, 255, 255, 255))
