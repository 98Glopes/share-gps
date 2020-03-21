import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
from pyproj import Proj

from alglin2cv import LinAlg2CV, angle2vec

myProj = Proj("+proj=utm +zone=23K, +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
data = pd.read_csv("record.csv", sep=";")

UTMx, UTMy = myProj(list(data.lon), list(data.lat))
UTMx, UTMy = np.array(UTMx, dtype=int), np.array(UTMy, dtype=int)
utmx = (UTMx - (UTMx.min() - 20))*2
utmy = (UTMy - (UTMy.min() - 20))*2

background = np.zeros((350*2,350*2,3), np.uint8)
background.fill(255)
obj = (140*2, 148*2)
cv2.circle(background, obj, 15, (0,0,255), thickness=-1)
print("utmx;utmy;orix;oriy;goalx;goaly")
while True:

    for i in range(0, utmx.shape[0]):
        
        cv2.circle(background, (int(utmx[i]), int(utmy[i])), 2, (255,0,0), thickness=-1)
        
        new_background = background.copy()

        actual = (utmx[i+10], utmy[i+10])
        last = (utmx[i], utmy[i])

        linalg = LinAlg2CV(actual, last)        
        first_point, last_point = linalg.dirVector()
        cv2.arrowedLine(new_background, first_point, last_point, (0,255,0), 4)
        ori = linalg.direction()

        linalg = LinAlg2CV(actual, obj)
        first_point, last_point = linalg.dir2obj()
        cv2.arrowedLine(new_background, first_point, last_point, (0,0,255), 2)
        goal = linalg.direction()

        angle = angle2vec(obj, actual, last)
        #cv2.putText(new_background, str(angle), (50, 50), cv2.FONT_HERSHEY_COMPLEX,
        #            15, (255,255,255))
        cv2.putText(new_background, str(angle), (150,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255, thickness=3)

        print("{};{};{};{};{};{}".format(utmx[i], utmy[i], ori[0], ori[1], goal[0], goal[1]))

        cv2.imshow("back", new_background)
        if cv2.waitKey(50) == "q":
            break

    break