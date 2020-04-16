import pandas as pd
import numpy as np
import cv2


s = 2 #image scale
a = 35 #arrow scale

way = pd.read_csv("csv/orientation.csv")

utmx = np.array(way.utmx, dtype=int)*s
utmy = np.array(way.utmy, dtype=int)*s
orix = np.array(way.orix)*a
oriy = np.array(way.oriy)*a 
goalx = np.array(way.goalx)*a 
goaly = np.array(way.goaly)*a 
angle = np.array(way.angle)

background = np.zeros((350*s,350*s,3), np.uint8)
background.fill(255)
obj = (125*s, 125*s)

cv2.circle(background, obj, 7, (0,0,255), thickness=-1)
print("utmx;utmy;orix;oriy;goalx;goaly")
while True:

    for i in range(5, utmx.shape[0]):
        
        cv2.circle(background, (int(utmx[i]), int(utmy[i])), 2, (255,0,0), thickness=-1)
        new_background = background.copy()

        #print direção
        try:
            first_p = (utmx[i], utmy[i])
            last_p = (utmx[i] + int(orix[i]), utmy[i] + int(oriy[i]))
            cv2.arrowedLine(new_background, first_p, last_p, (0,255,0), 4)
        except:
            pass

        #print Goal
        try:
            first_p = (utmx[i], utmy[i])
            last_p = (utmx[i] + int(goalx[i]), utmy[i] + int(goaly[i]))
            cv2.arrowedLine(new_background, first_p, last_p, (0,0,255), 4)
        except:
            pass

        #Write angle
        cv2.putText(new_background, f'Diferenca angular %.1f' % angle[i], (150,50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, 255, thickness=1)

        cv2.imshow("back", new_background)
        if cv2.waitKey(100) == "q":
            break

    break