import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2 
import time

"""
# shows nami image for 3 seconds
plt.imshow(img.imread("nami.png"))
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)
plt.pause(3)
plt.close()

"""

"""
# another solution, arguably better, to show nami image
nami = cv2.imread("nami.png")
cv2.imshow('nami', nami)
cv2.waitKey(3000) # show for 3 seconds
"""

"""
We might want to import this .py file and use the below function
The import statement for this function is "from display import show_img"

def show_img(img_path, time):
    cv2.imshow('image', cv2.imread(img_path))
    cv2.waitKey(time * 1000)

show_img(".png", 3)

"""

"""
# We might make a similar function for Luffy movie 

def show_mov(path, time):
    # shows Luffy movie
    start = time.time()
    cap = cv2.VideoCapture(path)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

        end = time.time()
        if end - start > time: # show for time seconds
            break 

    cap.release()
    cv2.destroyAllWindows()

"""
