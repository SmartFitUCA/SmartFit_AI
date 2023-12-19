from sklearn.linear_model import LinearRegression
import pandas as pd 
import numpy as np
import json
from datetime import datetime
import requests

def generateModele(dataJson):
    # -- Préparation des données 
    arrayBpm = []
    arrayStartTime = []
    arrayTimeOfActivity = []
    arrayVitesse = []
    arrayDistance = []

    for data in dataJson:
        
      info = json.loads(data["json"])

      arrayBpm.append(int(info["bpmAvg"]))
      arrayTimeOfActivity.append(float(info["timeOfActivity"]))
      arrayVitesse.append(float(info["vitesseAvg"]))
      arrayDistance.append(float(info["distance"]))

      # Convertir la chaîne en objet datetime
      dt_object = datetime.strptime(info["startTime"], "%Y-%m-%dT%H:%M:%S.%f")
      # Convertir l'objet datetime en millisecondes depuis l'époque
      milliseconds_since_epoch = int(dt_object.timestamp() * 1000)
      arrayStartTime.append(milliseconds_since_epoch)
    # -- DataFrame 
    data = pd.DataFrame({
        "Bpm": arrayBpm,
        "TimeOfActivity": arrayTimeOfActivity,
        "Vitesse" : arrayVitesse,
        "Distance" : arrayDistance
    })
    # -- Régression linéaire 
    model = LinearRegression()
    model.fit(np.array(arrayStartTime).reshape(-1,1),data)
    return model


def generateJsonModel(model:LinearRegression):
    listCoef = []
    listIntercept = []
    for i in range(0,len(model.coef_)):
        listCoef.append(model.coef_[i][0])
        listIntercept.append(model.intercept_[i])
    json = {"coef":listCoef,"intercept":listIntercept}
    return json



def getUserWithData(url:str):
    response = requests.get(url)
    if ( response.status_code != 200):
        print('problème lors de l extraction des données avec l api !! ->  "getUserWithData" (status_code != 200)')
        exit()
    return response.json()

def sendJsonToApi(url,json):
    header = {"Content-type": "application/json"}
    response = requests.post(url,json,headers=header)
    if ( response.status_code != 200):
        print('Problème lors de l envoi des données avec l api !! -> "sendJsonToApi" (status_code != 200)')
        exit()
    return 