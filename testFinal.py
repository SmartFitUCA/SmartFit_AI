
from sklearn.linear_model import LinearRegression
import pandas as pd 
import numpy as np
import requests
import logging


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
        arrayBpm.append(data["json"]["BpmAvg"])
        arrayTimeOfActivity.append(data["json"]["TimeOfActivity"])

        arrayStartTime.append(data["json"]["StartTime"])
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
    return response.json

def sendJsonToApi(url,json):
    response = requests.post(url,json)
    if ( response.status_code != 200):
        print('Problème lors de l envoi des données avec l api !! -> "sendJsonToApi" (status_code != 200)')
        exit()
    return

# ---------------- Main ------------------- #
logging.error("RUNNNNNNNN !")

urlGetAllData = "https://codefirst.iut.uca.fr/containers/SmartFit-smartfit_api/ia/data"

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
      

for user in dataUser:

    userUUID= user["uuid"]

    for category in user["categories"]:
        jsonTmp = {}
        #Mettre la condition longueur ici
        
        model = generateModele(category["infos"])

        jsonTmp["uuid"] = userUUID
        jsonTmp["category"] = category["name"]
        jsonTmp["model"] = generateJsonModel(model)

        sendJsonToApi(urlGetAllData,jsonTmp)

logging.error("Exec Fini")