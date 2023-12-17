from sklearn.linear_model import LinearRegression
import requests
from datetime import datetime, time
import time as sleep_time
import logging
import json

from fonction import generateModele

print("[INFO] STARTING DAILY USERS MODELS TRAINING")

# --------------- Fonction -----------------  #
def generateJsonModel(model:LinearRegression):
    listCoef = []
    listIntercept = []
    for i in range(0,len(model.coef_)):
        listCoef.append(model.coef_[i][0])
        listIntercept.append(model.intercept_[i])
    json = {"coef":listCoef,"intercept":listIntercept}
    return json


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

urlGetAllData = "https://codefirst.iut.uca.fr/containers/SmartFit-smartfit_api/ai/data"
while(True):
    logging.warning("Info - Début de la boucle")
    heure_actuelle = datetime.now().time()
    if ( heure_actuelle == time(8, 0)):
        logging.warning("Info - Procédure de création des modèles ")
        # --- Call Api 
        dataUser = getUserWithData(url=urlGetAllData)
        for user in dataUser:
            userUUID:any = user["uuid"]

            for category in user["categories"]:
                jsonTmp = {}
                #Mettre la condition longueur ici
                
                model = generateModele(category["infos"])

                jsonTmp["uuid"] = userUUID
                jsonTmp["category"] = category["name"]
                jsonTmp["model"] = json.dumps(generateJsonModel(model))

                sendJsonToApi(urlGetAllData,json.dumps(jsonTmp))
        # -- Send Api 
        logging.warning("Info - Procédure de création des modèles fini ")
    else :
        logging.warning("Info - Début sleep")
        if (heure_actuelle < time(7,0) or heure_actuelle > time(8,0) ):
            logging.warning("Sleep -> 1h")
            sleep_time.sleep(3600) # Pause 1 heure 
        elif ( heure_actuelle < time(7,55) ):
            logging.warning("Sleep -> 5m")
            sleep_time.sleep(300)  # Pause de 5 minutes
        else : 
            logging.warning("Sleep -> 30s")
            sleep_time.sleep(30)  # Pause de 30 secondes




    
