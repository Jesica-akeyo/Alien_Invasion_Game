# importing necessary libraries
import tensorflow as tf
from keras import layers
import warnings
from keras.layers import Flatten
import keras.utils
import numpy as np
import matplotlib.pyplot as plt


# defining the model architecture
model = tf.keras.Sequential()
model.add(layers.Dense(32, activation='relu',
input_shape=(None, None, 11, 17487)))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.add(Flatten())
model.compile(optimizer='rmsprop', loss='binary_crossentropy',
metrics=['accuracy'])

# loading the data into the model
# load mental health data from a numpy array file
stats = np.load('stats_data.npy')
scores = stats[0]
level = stats[1]
X = [stats[0], 121850, 83610, 55560, 36860, 23820,
14740, 9450, 5590, 2900, 1100, 0]  # input features
y = [stats[1], 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # target labels


A = np.arange(scores)
A = np.pad(A, (0, level - scores % level), 'constant')
A = A.reshape(A.shape[0] // level, level, 1).transpose()
B = np.arange(1)


# training the model on the loaded data
tf.divide(X, y)

print(f"{scores} ................................is this a score!")
print(f"{level} .........is the best level you can reach come on!")
print(f"{stats} .....................you are an amateur@ha!ha!ha!")
print(f"{tf.divide(X, y)} Average score!")
print(f"{A} Analysis ")
# plotting the points
plt.plot(X, y)

# naming the x axis
plt.xlabel('score')
# naming the y axis
plt.ylabel('level')

# giving a title to my graph
plt.title('THE INVASION!')

# function to show the plot
plt.show()
# saving the trained model for use in analysis
# training the model on the loaded data

model.fit(A, B,  epochs=50)  # train for 50 epochs
with warnings.catch_warnings(record=True):
 tf.keras.models.save_model(model, 'stats_model_analysis')
