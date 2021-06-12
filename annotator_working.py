# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:17:36 2021

@author: max-v
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 17:48:07 2021

@author: max-v
"""

import cv2
import numpy as np
import os

directory = r'C:/Users/max-v/Desktop/Arbeit/Realsens/Images/Side'+'/'   ### image directory
 
# Picture path
for file in os.listdir(directory):
    #filename = os.fsdecode(file)
    if file.endswith(".jpg") or file.endswith(".png"):
        filename=directory+file

        img = cv2.imread(filename)
        (h, w, d) = img.shape
        a = []
        b = []
         
        
         
        def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                xy = "%d,%d" % (x, y)
                a.append(x)
                b.append(y)
                cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
                cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                            1.0, (0, 0, 0), thickness=1)                
                cv2.imshow(file, img)
                print(x,y)
         
        label_path=directory.replace('Side', "keypoints")+file+".txt"

        cv2.namedWindow(file)
        cv2.setMouseCallback(file, on_EVENT_LBUTTONDOWN)
        # with open(label_path, "w") as file:   
                # file.write(a[0]/w, b[0]/h) 
        cv2.imshow(file, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # if cv2.waitKey(33) == ord('a'):
        #     print("pressed a")
        # if cv2.waitKey(0)&0xFF==2555904:
        # #cv2.imshow("image", img)
        #     print("blabla")
        #     cv2.destroyAllWindows()
        with open(label_path, "w") as file:   
                file.write("%f %f" %(a[0]/w, b[0]/h) )
        print(a[0], b[0])
        

        # if cv2.waitKey(0)&0xFF==27:
        #     break
cv2.destroyAllWindows()