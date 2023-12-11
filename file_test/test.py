
from sklearn.linear_model import LinearRegression
import pandas as pd 
import numpy as np
import requests
from datetime import datetime, time
import time as sleep_time

# --------------- Fonction -----------------  #
def generateJsonModel(model:LinearRegression):
    listCoef = []
    listIntercept = []
    for i in range(0,len(model.coef_)):
        listCoef.append(model.coef_[i][0])
        listIntercept.append(model.intercept_[i])
    json = {"coef":listCoef,"intercept":listIntercept}
    return json

def generateModele(dataJson:dict[str,str]):
    # -- Préparation des données 
    arrayBpm = []
    arrayStartTime = []
    arrayTimeOfActivity = []

    for data in dataJson["Data"]:
        arrayBpm.append(data["BpmAvg"])
        arrayTimeOfActivity.append(data["TimeOfActivity"])

        arrayStartTime.append(data["StartTime"])
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

#urlGetAllData = "https://codefirst.iut.uca.fr/containers/SmartFit-smartfit_api/xxx"

#jsonBack = { "Users" : []}

dataUser = {
    "Users": [
        {
            "Identifiant": "x",
            "Info": [
                {"Category": "walking", "Data": [{"StartTime": 1234, "BpmAvg": 100,"TimeOfActivity": 1716.5}, {"StartTime" : 123456789,"BpmAvg":100,"TimeOfActivity": 1716.5}]},
                {"Category": "Cycling", "Data": [{"StartTime": 1234, "BpmAvg": 100,"TimeOfActivity": 1716.5}, {"StartTime" : 123456087,"BpmAvg":100,"TimeOfActivity": 1716.5}]},
            ]
        },
        {   "Identifiant": "x",
            "Info": [
                {"Category": "walking", "Data": [{"StartTime": 1234, "BpmAvg": 120,"TimeOfActivity": 1716.5}, {"StartTime" : 123456789,"BpmAvg":120,"TimeOfActivity": 1716.5}]},
                {"Category": "Cycling", "Data": [{"StartTime": 1234, "BpmAvg": 120,"TimeOfActivity": 1716.5}, {"StartTime" : 123456087,"BpmAvg":120,"TimeOfActivity": 1716.5}]},
            ]
        }
    ]
}
'''
# -- Call Api
#dataUser = getUserWithData(url=urlGetAllData)

for user in dataUser["Users"]:
    jsonTmp = {}

    jsonTmp["Identifiant"] = user["Identifiant"]
    jsonTmp["Info"] = []

    for category in user["Info"]:
        #Mettre la condition longueur ici
        model = generateModele(category)
        jsonTmp["Info"].append({"Category": category["Category"],"Model" : generateJsonModel(model)})

    # Add User
    jsonBack["Users"].append(jsonTmp)
print(jsonBack)
# -- Send Data to Api 
#sendJsonToApi(urlGetAllData,jsonBack)
'''






urlGetAllData = "https://codefirst.iut.uca.fr/containers/SmartFit-smartfit_api/xxx"
while(True):
    print("Boucle")
    jsonBack = { "Users" : []}
    heure_actuelle = datetime.now().time()
    if ( heure_actuelle == time(8, 0)):
        # --- Call Api 
        #dataUser = getUserWithData(url=urlGetAllData)
        for user in dataUser["Users"]:
            jsonTmp = {}

            jsonTmp["Identifiant"] = user["Identifiant"]
            jsonTmp["Info"] = []

            for category in user["Info"]:
                #Mettre la condition longueur ici
                model = generateModele(category)
                jsonTmp["Info"].append({"Category": category["Category"],"Model" : generateJsonModel(model)})

            # Add User
            jsonBack["Users"].append(jsonTmp)
        # -- Send Api 
        #sendJsonToApi(urlGetAllData,jsonBack)
    else : 
        print("Sleep")
        if (heure_actuelle < time(7,0) and heure_actuelle > time(8,0) ):
            sleep_time.sleep(3600) # Pause 1 heure 
        elif ( heure_actuelle < time(7,55) ):
            sleep_time.sleep(300)  # Pause de 5 minutes
        else : 
            sleep_time.sleep(30)  # Pause de 30 secondes




    
