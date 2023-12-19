#!/usr/bin/python3

from sklearn.linear_model import LinearRegression
import pandas as pd 
import numpy as np
import logging
import json
from fonction import getUserWithData,generateJsonModel,generateModele,sendJsonToApi


# ---------------- Main ------------------- #
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
      model = generateModele(category["infos"])

      jsonTmp["uuid"] = userUUID
      jsonTmp["category"] = category["name"]
      jsonTmp["model"] = json.dumps(generateJsonModel(model))
      print(json.dumps(generateJsonModel(model)))
      
      sendJsonToApi(urlGetAllData,json.dumps(jsonTmp))
  i+=1
  logging.error("User nb "+str(i)+" finis")

logging.error("Exec Fini")
