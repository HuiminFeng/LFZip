from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Bidirectional
from keras.layers import LSTM, Flatten, Conv1D, LocallyConnected1D, CuDNNLSTM, CuDNNGRU, MaxPooling1D, GlobalAveragePooling1D, GlobalMaxPooling1D
from math import sqrt
from keras.layers.embeddings import Embedding
from keras.callbacks import ModelCheckpoint
# from matplotlib import pyplot
import keras
from sklearn.preprocessing import OneHotEncoder
from keras.layers.normalization import BatchNormalization
import tensorflow as tf
import numpy as np
import argparse
import os
from keras.callbacks import CSVLogger



def biGRU(bs,time_steps,alphabet_size):
        model = Sequential()
        model.add(Embedding(alphabet_size, 32, batch_input_shape=(bs, time_steps)))
        model.add(Bidirectional(CuDNNGRU(32, stateful=False, return_sequences=True)))
        model.add(Bidirectional(CuDNNGRU(32, stateful=False, return_sequences=False)))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(alphabet_size, activation='softmax'))
        return model

def biLSTM(bs,time_steps,alphabet_size):
        model = Sequential()
        model.add(Embedding(alphabet_size, 32, batch_input_shape=(bs, time_steps)))
        model.add(Bidirectional(CuDNNLSTM(32, stateful=False, return_sequences=True)))
        model.add(Bidirectional(CuDNNLSTM(32, stateful=False, return_sequences=False)))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(alphabet_size, activation='softmax'))
        return model

def LSTM_multi(bs,time_steps,alphabet_size):
        model = Sequential()
        model.add(Embedding(alphabet_size, 32, batch_input_shape=(bs, time_steps)))
        model.add(CuDNNLSTM(32, stateful=False, return_sequences=True))
        model.add(CuDNNLSTM(32, stateful=False, return_sequences=True))
        model.add(Flatten())
        model.add(Dense(64, activation='relu'))
        model.add(Dense(alphabet_size, activation='softmax'))
        return model

def LSTM_multi_selu(bs,time_steps,alphabet_size):
        model = Sequential()
        model.add(Embedding(alphabet_size, 32, batch_input_shape=(bs, time_steps)))
        model.add(CuDNNLSTM(32, stateful=False, return_sequences=True))
        model.add(CuDNNLSTM(32, stateful=False, return_sequences=True))
        model.add(Flatten())
        model.add(Dense(64, activation=keras.activations.selu, kernel_initializer=init))
        model.add(Dense(alphabet_size, activation='softmax'))
        return model

def GRU_multi(bs,time_steps,alphabet_size):
        model = Sequential()
        model.add(Embedding(alphabet_size, 32, batch_input_shape=(bs, time_steps)))
        model.add(CuDNNGRU(32, stateful=False, return_sequences=True))
        model.add(CuDNNGRU(32, stateful=False, return_sequences=True))
        model.add(Flatten())
        model.add(Dense(64, activation='relu'))
        model.add(Dense(alphabet_size, activation='softmax'))
        return model


def FC(bs,time_steps,alphabet_size):
        model = Sequential()
        init = keras.initializers.lecun_uniform(seed=0)
        model.add(Embedding(alphabet_size, 32, batch_input_shape=(bs, time_steps)))
        model.add(Flatten())
        model.add(Dense(1024, activation='relu', kernel_initializer=init))
        model.add(Dense(64, activation='relu', kernel_initializer=init))
        model.add(Dense(alphabet_size, activation='softmax'))
        return model
