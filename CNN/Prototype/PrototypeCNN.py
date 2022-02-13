#
#
#
#

#Tensorflow related Imports
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.utils import plot_model

#Misc imports
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from tqdm import tqdm
import random


#import numpy array data from their files

X = np.load('D:/UWE-DSP/CNN/Prototype/features.npy')
y = np.load('D:/UWE-DSP/CNN/Prototype/labels.npy')

#normalise the data
trainingX = X/255.0

#begin to build the CNN

model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(180, 180, 3)))
model.add(MaxPooling2D((2, 2)))
#model.add(Dropout(0.2))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
#model.add(Dropout(0.2))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
#model.add(Dropout(0.2))

model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
#model.add(Dropout(0.2))

model.add(Conv2D(512, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
#model.add(Dropout(0.2))

#model.add(BatchNormalization())
#model.summary()

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10))
#model.add(Activation('sigmoid'))
model.add(Activation('softmax'))

model.summary()

model.compile(optimizer='adamax',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(trainingX, y, epochs=30, validation_split=0.2)

plot_model(model, to_file='D:/UWE-DSP/CNN/Prototype/model.png', show_shapes=True)

model.save("D:/UWE-DSP/CNN/Prototype/identiFloraCNNModel.h5")