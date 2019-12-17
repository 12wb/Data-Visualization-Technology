import numpy as np
from PIL import Image
im = np.array(Image.open(r'F:\文档\qq\天心阁.png'))
print(im)
print(im.shape)
print(type(im))