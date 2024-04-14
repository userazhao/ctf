import numpy as np
from PIL import Image

negative = np.zeros((12,12,3), dtype=np.uint8)

for x in range(0,12):
    for y in range(0,12):
        negative[x, y, 0] = np.random.randint(256)
        negative[x, y, 1] = np.random.randint(256)
        negative[x, y, 2] = np.random.randint(1,255)

negative = Image.fromarray(negative)
negative.save("negative.png")