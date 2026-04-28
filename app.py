# &#x20;import streamlit as st

# import pandas as pd

# from sklearn.ensemble import RandomForestRegressor

# from sklearn.preprocessing import LabelEncoder

# import numpy as np

# 

# \# ---------- Load \& Train ----------

# @st.cache\_resource

# def train\_model():

# &#x20;   df = pd.read\_csv("car\_data.csv")

# 

# &#x20;   # Feature engineering

# &#x20;   df\["car\_age"] = 2024 - df\["year"]

# &#x20;   df.drop("name", axis=1, inplace=True)

# &#x20;   df.drop("year", axis=1, inplace=True)

# 

# &#x20;   # Encode categorical columns

# &#x20;   le = {}

# &#x20;   for col in \["fuel", "seller\_type", "transmission", "owner"]:

# &#x20;       le\[col] = LabelEncoder()

# &#x20;       df\[col] = le\[col].fit\_transform(df\[col])

# 

# &#x20;   X = df.drop("selling\_price", axis=1)

# &#x20;   y = df\["selling\_price"]

# 

# &#x20;   model = RandomForestRegressor(n\_estimators=100, random\_state=42)

# &#x20;   model.fit(X, y)

# 

# &#x20;   return model, le

# 

# model, le = train\_model()

# 

# \# ---------- UI ----------

# st.title("🚗 Car Price Prediction System")

# st.write("Fill in the car details below to get an estimated resale price.")

# 

# col1, col2 = st.columns(2)

# 

# with col1:

# &#x20;   year = st.selectbox("Manufacturing Year", list(range(2024, 1982, -1)))

# &#x20;   km\_driven = st.number\_input("Kilometers Driven", min\_value=1, max\_value=500000, value=30000, step=1000)

# &#x20;   fuel = st.selectbox("Fuel Type", \["Petrol", "Diesel", "CNG", "LPG"])

# &#x20;   seller\_type = st.selectbox("Seller Type", \["Individual", "Dealer", "Trustmark Dealer"])

# 

# with col2:

# &#x20;   transmission = st.selectbox("Transmission", \["Manual", "Automatic"])

# &#x20;   owner = st.selectbox("Owner", \["First Owner", "Second Owner", "Third Owner",

# &#x20;                                   "Fourth \& Above Owner", "Test Drive Car"])

# 

# \# ---------- Predict ----------

# if st.button("Predict Price 💰"):

# &#x20;   car\_age = 2024 - year

# 

# &#x20;   fuel\_enc = le\["fuel"].transform(\[fuel])\[0]

# &#x20;   seller\_enc = le\["seller\_type"].transform(\[seller\_type])\[0]

# &#x20;   trans\_enc = le\["transmission"].transform(\[transmission])\[0]

# &#x20;   owner\_enc = le\["owner"].transform(\[owner])\[0]

# 

# &#x20;   input\_data = pd.DataFrame(\[\[km\_driven, fuel\_enc, seller\_enc, trans\_enc, owner\_enc, car\_age]],

# &#x20;                              columns=\["km\_driven", "fuel", "seller\_type", "transmission", "owner", "car\_age"])

# 

# &#x20;   price = model.predict(input\_data)\[0]

# 

# &#x20;   st.success(f"💵 Estimated Selling Price: ₹ {int(price):,}")

# &#x20;   st.info(f"Car Age: {car\_age} years | KM Driven: {km\_driven:,} km")

