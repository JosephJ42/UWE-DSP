#House Plant Identification CNN
#
# The following code is used to train the CNN using tensorflow lite, for the house plant identification and care mobile application
# Note: this is a prototype version of the CNN that will only consist of two types of houseplant. This is to act as a proof of concept.

#Tensorflow related Imports
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop

#Misc imports
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from tqdm import tqdm
import random


# Image importation and preprocessing 

# training data
def makingDataSets(folderLocation):
    dataSetDirectory = folderLocation

    plantTypes = ["aglonema","calathea"]

    sizeOfImage = 250

    training_data = []

    def create_training_data():
        for category in plantTypes:  

            path = os.path.join(dataSetDirectory,category)  
            plantTypeID = plantTypes.index(category)  

            for img in tqdm(os.listdir(path)): 
                try:
                    img_array = cv2.imread(os.path.join(path,img))  
                    new_array = cv2.resize(img_array, (sizeOfImage, sizeOfImage))  
                    training_data.append([new_array, plantTypeID])  
                except Exception as e:  
                    pass

    create_training_data()

    random.shuffle(training_data)

    X = []
    y = []

    for features,label in training_data:
        X.append(features)
        y.append(label)

    print(X[0].reshape(-1, sizeOfImage, sizeOfImage, 3))

    X = np.array(X).reshape(-1, sizeOfImage , sizeOfImage, 3)
    y = X = np.array(y)

    return X,y
    
trainingDataSet = "prototypeHousePlantTrainingImages/training"
trainingX, trainingY = makingDataSets(trainingDataSet)

validationDataSet = "prototypeHousePlantTrainingImages/validation"
validationX, validationY = makingDataSets(validationDataSet)

#train_data = tf.data.Dataset.from_tensor_slices((trainingX, trainingY))
#valid_data = tf.data.Dataset.from_tensor_slices((validationX, validationY))


# Model


model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=(256,256,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64, activation='relu'))
model.add(Dense(10))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#model.fit(X, y, batch_size=10, epochs=5, validation_split=0.2)
#model.fit(train_data, epochs=5, validation_data=valid_data)

model.fit(trainingX, trainingY, epochs=5, validation_data=(validationX, validationY))

#porting the module to tensorflow lite