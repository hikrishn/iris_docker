'''
Created on Jul 13, 2022
@author: kchaitanya
'''


from __future__ import print_function
from datetime import datetime, timedelta
import json
import sys
import logging
import time
from config_holder import ConfigHolder
from bottle import Bottle, run, request, response, HTTPResponse, get
#import yaml
from waitress import serve
import os
import pickle
import numpy as np
#import libs for pickled model
#import sklearn
import joblib
from sklearn.datasets import load_iris
#from sklearn.model_selection import train_test_split
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn import metrics

bottleApp = Bottle()

# some code
print("App started", file=sys.stderr)


# DB Connection, once per instance
config_holder = ConfigHolder(
    # Load the config from docker setup
    configFile = '/src/config/application.properties'
    # Load the config locally on my mac
    #configFile = '/Users/krishna/Creative_Man/AI_ML/JobPrep/iris_docker/src/config/application.properties'
)

logger = None


@bottleApp.get('/health')
def healthcheck():
    #return processRequest("/iris/v1/keepAlive", request, {});
    return "ok"


#os.chdir('/home/krishna/Desktop/AI')
# Load the model from docker setup
model = joblib.load('/src/iris_knn.pkl')
# Load the model locally on my mac
#model = joblib.load('/Users/krishna/Creative_Man/AI_ML/JobPrep/iris_docker/src/iris_knn.pkl')

# Load the sample data set
iris = load_iris()

@bottleApp.post('/iris/v1/predict')
def irispredict():
    # Get the data from the POST request.
    print('Hi')
    data = request.json
    print(data)
    # Make prediction using model loaded from disk as per the data.
    predict_request=np.array(data)[np.newaxis, :]
    print(predict_request)
    prediction = model.predict(predict_request)
    print(prediction)
    # Take the first value of prediction
    output = prediction[0]
    print('Final output' , iris.target_names[output])
    return HTTPResponse(status=200, body=json.dumps({'Target Flower': iris.target_names[output]}))




def setLogLevel():
    log_lev       = config_holder.configMap['log_level']
    log_level_val = logging.DEBUG
    if(log_lev.upper() == "DEBUG"):
        log_level_val = logging.DEBUG
    if(log_lev.upper() == "INFO"):
        log_level_val = logging.INFO
    if(log_lev.upper() == "WARNING"):
        log_level_val = logging.WARNING
    if(log_lev.upper() == "ERROR"):
        log_level_val = logging.ERROR
    if(log_lev.upper() == "CRITICAL"):
        log_level_val = logging.CRITICAL
    # Initialize logger
    logging.basicConfig(level=log_level_val, datefmt='%a, %d %b %Y %H:%M:%S', format='%(asctime)s %(levelname)-8s %(message)s')



if __name__ == '__main__':
    setLogLevel()
    logger = logging.getLogger(__name__)
    serve(bottleApp, host='0.0.0.0', port=8080)
    logger.debug("In the enterprise iris bottle main")
