#!/usr/bin/python3

from sklearn.linear_model import LinearRegression
import pandas as pd 
import numpy as np
import requests
import logging
import json
from datetime import datetime

# --------------- Fonction -----------------  #
def generateJsonModel(model:LinearRegression):
    listCoef = []
    listIntercept = []
    for i in range(0,len(model.coef_)):
        listCoef.append(model.coef_[i][0])
        listIntercept.append(model.intercept_[i])
    json = {"coef":listCoef,"intercept":listIntercept}
    return json

def generateModele(dataJson):
    # -- Préparation des données 
    arrayBpm = []
    arrayStartTime = []
    arrayTimeOfActivity = []

    for data in dataJson:
        
      info = json.loads(data["json"])

      arrayBpm.append(int(info["bpmAvg"]))
      arrayTimeOfActivity.append(float(info["timeOfActivity"]))

      # Convertir la chaîne en objet datetime
      dt_object = datetime.strptime(info["startTime"], "%Y-%m-%dT%H:%M:%S.%f")
      # Convertir l'objet datetime en millisecondes depuis l'époque
      milliseconds_since_epoch = int(dt_object.timestamp() * 1000)
      arrayStartTime.append(milliseconds_since_epoch)
    # -- DataFrame 
    data = pd.DataFrame({
        "Bpm": arrayBpm,
        "TimeOfActivity": arrayTimeOfActivity
    })
    # -- Régression linéaire 
    model = LinearRegression()
    model.fit(np.array(arrayStartTime).reshape(-1,1),data)
    return model


def getUserWithData(url:str):
    response = requests.get(urlGetAllData)
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

# ---------------- Main ------------------- #
logging.error("RUNNNNNNNN !")

urlGetAllData = "https://codefirst.iut.uca.fr/containers/SmartFit-smartfit_api/ai/data"

# --- Call Api 
dataUser = getUserWithData(url=urlGetAllData)
'''
dataUser = [{
  "uuid": "xxxx",
  "categories": [
    {
      "name": "walking",
      "infos": [
        {
          "json": {"BpmAvg":100,"TimeOfActivity":225,"StartTime":1234}
        }
      ]
    },
    {
      "name": "cycling",
      "infos": [
        {
          "json":  {"BpmAvg":110,"TimeOfActivity":225,"StartTime":12345}
        }
      ]
    }
  ]
}
]'''

logging.error("Nombre de User : "+str(len(dataUser)))
i = 0

for user in dataUser:

  userUUID = user["uuid"]

  for category in user["categories"]:
      jsonTmp = {}
      #Mettre la condition longueur ici
      
      model = generateModele(category["infos"])

      jsonTmp["uuid"] = userUUID
      jsonTmp["category"] = category["name"]
      jsonTmp["model"] = json.dumps(generateJsonModel(model))

      sendJsonToApi(urlGetAllData,json.dumps(jsonTmp))
  i+=1
  logging.error("User nb "+str(i)+" finis")

logging.error("Exec Fini")
