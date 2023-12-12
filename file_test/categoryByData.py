import pandas as pd
import numpy as np
from sklearn.calibration import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data from CSV
df = pd.read_csv("data\\data_emple.csv")

category = df.iloc[0:len(df),0].values

otherData = df.iloc[0:len(df),1:6].values

print(otherData)

# Encode the categorical target variable
label_encoder = LabelEncoder()
category_encoded = label_encoder.fit_transform(category)

model = LinearRegression()

model.fit(otherData,category_encoded)


new_data = np.array([224.0,228.49,346.6000000000000,1.1007253886010361,101]).reshape(1, -1)

# Faites une prédiction avec le modèle entraîné
prediction = model.predict(new_data)

# Affichez la prédiction
print("Prédiction:", prediction)

# Supposons que label_encoder soit l'objet LabelEncoder que vous avez utilisé lors de l'entraînement
inverse_prediction = label_encoder.inverse_transform(prediction.astype(int))

# Affichez la prédiction sous forme de chaîne de caractères
print("Prédiction (en chaîne de caractères):", inverse_prediction)


