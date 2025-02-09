import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import os

def get_data():
    data = pd.read_csv(r"C:\Users\hasan\Desktop\tennis.csv")
    np_array = data.values
    np_array_specific = data.iloc[:, [2,3,4,5,6,7,8,9]].values
    np_out = data.iloc[:, 12].values
    limited_array_in = np_array_specific[:1000]
    limited_array_out = np_out[:1000]

    x_train = np.array(limited_array_in, dtype=float)
    y_train = np.array(limited_array_out, dtype=float)  # Quadratic relationship

    train_model(x_train,y_train)
def train_model(x_train,y_train):
    model = keras.Sequential()
    model.add(layers.Dense(
        20, # Amount of Neurons
        input_dim=8, # Define an input dimension because this is the first layer
        activation='sigmoid' # Use relu activation function because all inputs are positive
        ))

    model.add(layers.Dense(
        20, 
        activation='sigmoid' 
        ))
    
    model.add(layers.Dense(
        20, 
        activation='sigmoid' 
        ))
    
    model.add(layers.Dense(
        20, 
        activation='sigmoid'
        ))
    
    model.add(layers.Dense(
        1, # Amount of Neurons. We want one output
        activation='sigmoid' # Use sigmoid because we want to output a binary classification
        ))

    load_model(model)

    learning_rate = 1
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    
    model.compile(optimizer=optimizer, loss='binary_crossentropy')
    model.fit(x_train, y_train, epochs=150, batch_size=500)#, batch_size=500

    save_model(model)

def load_model(model):
    while True:
        answer=input('Do you want to load the weights (Y/N)')
        if answer.upper()=='Y':
            try:
                model.load_weights('model_weights.h5')
            except:
                print('Failed')
            return
        if answer.upper()=='N':
            print('Okay')
            return
        else:
            print('Invalid input')
            
def save_model(model):
    while True:
        answer=input('Do you want to save the weights (Y/N)')
        if answer.upper()=='Y':
            try:
                model.save_weights('model_weights.h5')
            except:
                print('Failed')
            return
        if answer.upper()=='N':
            print('Okay')
            return
        else:
            print('Invalid input')

get_data()
