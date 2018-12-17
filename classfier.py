import skvideo.io
import skvideo.datasets
import cv2
import numpy as np
from matplotlib import pyplot as plt

videodata = skvideo.io.vread(skvideo.datasets.bigbuckbunny()) # loads the in build test video
# you can read your own video with following code
videodata = skvideo.io.vread("FIEC2.mp4")  
edges = np.zeros(videodata.shape[0:3])
for i in range(videodata.shape[0]):
    edges[i] = cv2.Canny(videodata[i],100,200) # canny edge detection
    # you can add othe edge detectors from opencv lib
skvideo.io.vwrite("edge_video.mp4", edges)     # saving edge video


#you can view the video frame and corresponding edge with following code

plt.subplot(2,1,1),plt.imshow(videodata[0],cmap = 'gray')
plt.title('video'), plt.xticks([]), plt.yticks([])
plt.subplot(2,1,2),plt.imshow(edges[0],cmap = 'gray')
plt.title('canny edge'), plt.xticks([]), plt.yticks([])
plt.show()
