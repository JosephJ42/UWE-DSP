#House Plant Identification CNN dataset preprocessor 

#Misc imports
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from tqdm import tqdm
import random

trainingDataSet = "D:/UWE-DSP/CNN/Prototype/prototypeHousePlantTrainingImages/training"
plantTypes = ["aglonema","calathea"]
sizeOfImage = 180
trainingData = []

def createTrainingData():

    for category in plantTypes:
        
        path = os.path.join(trainingDataSet, category)
        plantTypeID = plantTypes.index(category)

        for img in os.listdir(path):
            
            try:
                tempImgArray = cv2.imread(os.path.join(path,img),cv2.IMREAD_COLOR)

                # convert from cv2 standard bgr to RGB (like most other libaries)
                imgArray = cv2.cvtColor(tempImgArray, cv2.COLOR_BGR2RGB)
            
                resizedImageArray = cv2.resize(imgArray, (sizeOfImage, sizeOfImage))

                trainingData.append([resizedImageArray, plantTypeID])

                #plt.imshow(imgArray)
                #plt.show()
                #plt.imshow(resizedImageArray)
                #plt.show()

            except Exception as e:  
                    pass   

          
          
def makingDataSets():

    createTrainingData()

    print(len(trainingData))

    #shuffle the data to prevent the CNN learning becoming stagnant
    random.shuffle(trainingData)

    X = []
    y = []

    for features,label in trainingData:
        X.append(features)
        y.append(label)

    X = np.array(X).reshape(-1, sizeOfImage , sizeOfImage, 3)
    y = np.array(y)


    #Save each array as a npy array to then be used by the CNN 
    # Doing this allows for more efficient parameter tweaking later
    np.save('D:/UWE-DSP/CNN/Prototype/features.npy',X)
    np.save('D:/UWE-DSP/CNN/Prototype/labels.npy',y)


makingDataSets()



