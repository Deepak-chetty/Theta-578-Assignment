import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    "age": [25, 30, 35, 40, 45],
    "height": [150, 160, 170, 180, 190],
    "weight": [75, 80, 85, 90, 95]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df)

normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
print("\nNormalized DataFrame:")
print(normalized_df)

# 28-01-2025

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

data = {
    "customer_id": [1, 2, 3, 4],
    "gender": ["Male", "Female", "Male", "Female"],
    "names": ["Niraj", "Damoder", "Deepak", "Tanush"],
    "fav_food": ["Biryani", "Pav Bhaji", "Burger", "Dosa"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

one_hot_encoder = OneHotEncoder(sparse_output = False)

columns_to_encode = ["gender", "fav_food"]

encoded_data = one_hot_encoder.fit_transform(df[columns_to_encode])

encoded_columns = one_hot_encoder.get_feature_names_out(columns_to_encode)

encoded_df = pd.DataFrame(encoded_data, columns = encoded_columns)

print(encoded_df)

final_df = pd.concat([df.drop(columns = columns_to_encode), encoded_df], axis = 1)
print("\nOne-Hot Encoded DataFrame with sklearn:")
print(final_df)


label_encoder = LabelEncoder()

df['gender'] = label_encoder.fit_transform(df['gender'])
df['fav_food'] = label_encoder.fit_transform(df['fav_food'])

print("\nDataFrame After Label Encoding:")
print(df)

# 29-01-2025

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
data = {
    'Study Hours': np.random.randint(1, 10, 50),
    'Marks': np.random.randint(30, 100, 50),
    'Screen Time': np.random.randint(1, 7, 50),
    'Traveling Time': np.random.randint(0, 3, 50),
    'Sleep Hours': np.random.randint(4, 10, 50)
}

df = pd.DataFrame(data)

corr = df.corr()

plt.figure(figsize = (8, 6))
sns.heatmap(corr, annot = True, cmap = "coolwarm", fmt = ".2f", linewidths = 0.5)
plt.title("Feature Correlation Heatmap")
plt.show()
