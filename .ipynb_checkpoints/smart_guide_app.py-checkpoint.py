import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors

# Load dataset
data = pd.read_csv("laptop_pred.csv")

# Feature columns
features = data[['brand','price','spec_rating','processor','Ram','ROM','GPU']]

# Encode categorical columns
encoders = {}
for col in ['brand','processor','Ram','ROM','GPU']:
    le = LabelEncoder()
    features[col] = le.fit_transform(features[col])
    encoders[col] = le

# Train model
model = NearestNeighbors(n_neighbors=5)
model.fit(features)

st.title("💻 Smart Guide - AI Laptop Recommendation")

st.write("Answer a few questions to find the best laptop for you.")

# User questions
budget = st.number_input("Enter your budget (₹)", min_value=10000, max_value=200000)

brand = st.selectbox("Preferred Brand", data['brand'].unique())

ram = st.selectbox("Required RAM", data['Ram'].unique())

storage = st.selectbox("Required Storage", data['ROM'].unique())

processor = st.selectbox("Preferred Processor", data['processor'].unique())

gpu = st.selectbox("Graphics Requirement", data['GPU'].unique())

# Recommendation button
if st.button("Find Best Laptops"):

    # Encode user input
    brand_enc = encoders['brand'].transform([brand])[0]
    processor_enc = encoders['processor'].transform([processor])[0]
    ram_enc = encoders['Ram'].transform([ram])[0]
    rom_enc = encoders['ROM'].transform([storage])[0]
    gpu_enc = encoders['GPU'].transform([gpu])[0]

    # Create feature vector
    user_input = [[brand_enc, budget, 70, processor_enc, ram_enc, rom_enc, gpu_enc]]

    # Find similar laptops
    distances, indices = model.kneighbors(user_input)

    result = data.iloc[indices[0]][['brand','name','price','processor','Ram','GPU']]

    st.subheader("Recommended Laptops")
    st.dataframe(result)