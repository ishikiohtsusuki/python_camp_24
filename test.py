import matplotlib.pyplot as plt
import matplotlib.image as img
import time

plt.imshow(img.imread("nami.png"))
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)
plt.pause(3)
plt.close()
