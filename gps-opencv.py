import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
from pyproj import Proj

from alglin2cv import LinAlg2CV

myProj = Proj("+proj=utm +zone=23K, +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
data = pd.read_csv("record.csv", sep=";")

UTMx, UTMy = myProj(list(data.lon), list(data.lat))
UTMx, UTMy = np.array(UTMx, dtype=int), np.array(UTMy, dtype=int)
utmx = (UTMx - (UTMx.min() - 20))*2
utmy = (UTMy - (UTMy.min() - 20))*2

background = np.zeros((350*2,350*2,3), np.uint8)
background.fill(255)
obj = (350*2, 350*2)
cv2.circle(background, obj, 15, (0,0,255), thickness=-1)

while True:

    for i in range(0, utmx.shape[0]):
        
        cv2.circle(background, (int(utmx[i]), int(utmy[i])), 2, (255,0,0), thickness=-1)
        
        new_background = background.copy()

        linalg = LinAlg2CV((utmx[i+10], utmy[i+10]), (utmx[i], utmy[i]))        
        first_point, last_point = linalg.dirVector()
        cv2.arrowedLine(new_background, first_point, last_point, (0,255,0), 4)

        linalg = LinAlg2CV((utmx[i+10], utmy[i+10]), obj)
        first_point, last_point = linalg.dir2obj()
        cv2.arrowedLine(new_background, first_point, last_point, (0,0,255), 2)

        cv2.imshow("back", new_background)
        if cv2.waitKey(20) == "q":
            break

    break