from sklearn.linear_model import LinearRegression
import pandas as pd 
import numpy as np

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