"""
Created on Fri Nov 14 2019

@author: Omkar Nallagoni
"""


import numpy as np
import pickle
import pandas as pd
from flask import Flask, request

#model.pkl is used to get the predictions on new data
# in this page np pd pickle we did not used it is masked
# yellow error 


app=Flask(__name__)

pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)


@app.route('/')      # decorator
def welcome():
    return "Welcome All"