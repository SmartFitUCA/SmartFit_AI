import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv("data\\data_emple.csv")
distance = df.iloc[0:len(df),1].values.reshape(-1, 1)
time = df.iloc[0:len(df),2].values.reshape(-1, 1)
 
model = LinearRegression()

# Entrainement 
model.fit(time,distance)

# Afficher les coefficients du modèle
print("Coefficients :", model.coef_)
print("Intercept :", model.intercept_)


# Supposons que vous avez de nouvelles données pour lesquelles vous voulez faire des prédictions
new_time_data = np.array([1000]).reshape(1,-1) # Exemple de nouvelles données pour 'time'

# Faire des prédictions sur les nouvelles données
predicted_distance = model.predict(new_time_data)

# Afficher les prédictions
print("Prédictions de distance :", predicted_distance[0])


