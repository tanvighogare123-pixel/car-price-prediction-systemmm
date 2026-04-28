import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import numpy as np

# ---------- Load & Train ----------
@st.cache_resource
def train_model():
    df = pd.read_csv("1777354177537_cardekho_csv.csv")

    df["car_age"] = 2024 - df["year"]
    df.drop("name", axis=1, inplace=True)
    df.drop("year", axis=1, inplace=True)

    le = {}
    for col in ["fuel", "seller_type", "transmission", "owner"]:
        le[col] = LabelEncoder()
        df[col] = le[col].fit_transform(df[col])

    X = df.drop("selling_price", axis=1)
    y = df["selling_price"]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model, le

model, le = train_model()

# ---------- UI ----------
st.title("🚗 Car Price Prediction System")
st.write("Fill in the car details below to get an estimated resale price.")

col1, col2 = st.columns(2)

with col1:
    year = st.selectbox("Manufacturing Year", list(range(2024, 1982, -1)))
    km_driven = st.number_input("Kilometers Driven", min_value=1, max_value=500000, value=30000, step=1000)
    fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG"])
    seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"])

with col2:
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
    owner = st.selectbox("Owner", ["First Owner", "Second Owner", "Third Owner",
                                    "Fourth & Above Owner", "Test Drive Car"])

# ---------- Predict ----------
if st.button("Predict Price 💰"):
    car_age = 2024 - year

    fuel_enc = le["fuel"].transform([fuel])[0]
    seller_enc = le["seller_type"].transform([seller_type])[0]
    trans_enc = le["transmission"].transform([transmission])[0]
    owner_enc = le["owner"].transform([owner])[0]

    input_data = pd.DataFrame([[km_driven, fuel_enc, seller_enc, trans_enc, owner_enc, car_age]],
                               columns=["km_driven", "fuel", "seller_type", "transmission", "owner", "car_age"])

    price = model.predict(input_data)[0]

    st.success(f"💵 Estimated Selling Price: ₹ {int(price):,}")
    st.info(f"Car Age: {car_age} years | KM Driven: {km_driven:,} km")