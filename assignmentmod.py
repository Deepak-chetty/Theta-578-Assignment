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
