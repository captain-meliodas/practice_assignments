#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:10:38 2021
Convolutional Neural Network
@author: ankit
"""
# Convolutional Neural Network

# Importing the libraries
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
tf.__version__

# Part 1 - Data Preprocessing

# Preprocessing the Training set
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

# Preprocessing the Test set
test_datagen = ImageDataGenerator(rescale = 1./255)
test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

#initialising the CNN
cnn = tf.keras.models.Sequential()

#Convolution
cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3, activation='relu', input_shape=[64,64,3]))

#Pooling
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

#adding a second convolutional layer
cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

#adding the flattening layer
cnn.add(tf.keras.layers.Flatten())

#Full connection (number of neurons we choosed is 128)
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))

#adding a output layer (if we need to predict output more than two classes we can use softmax activation function)
#predicts whether the image is of dog or cat
cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

#compling the CNN
cnn.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#Training the CNN on the training set and evaluating it on the test set
cnn.fit(x=training_set, validation_data=test_set, epochs=25)

#Making a single prediction
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('dataset/single_prediction/cat_or_dog_1.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = cnn.predict(test_image)
print(training_set.class_indices)
if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'
print(prediction)