from skimage import io
import matplotlib.pyplot as plt
import numpy as np
image1 = io.imread('HassInAislada.png')
image2 = io.imread('HassMaAislada.png')

Madura = plt.hist(image1[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)

_ = plt.xlabel('Intensity Value')
_ = plt.ylabel('Count')
_ = plt.legend(['Hass Madura Aislada'])

ax=plt.gca()
p=ax.patches
heights=[patch.get_height() for patch in p]
heights_cut=np.array(heights[100::])
sum=np.cumsum(heights_cut)
umbral=sum[len(sum)-1]
if umbral < 10000:
    print("Palta Madura")
else:
    print("Palta Inmadura")

print(umbral)
plt.show()
