import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors
import time

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(page_title="Smart Guide AI", page_icon="💻", layout="wide")

# ------------------------------------------------
# INTRO SECTION (HTML DESIGN)
# ------------------------------------------------

st.markdown("""
<style>

.main-title{
font-size:50px;
font-weight:bold;
text-align:center;
color:#4169E1;
}

.sub-title{
font-size:22px;
text-align:center;
color:#444;
margin-bottom:20px;
}

.intro-box{
background-color:#f5f7ff;
padding:25px;
border-radius:15px;
text-align:center;
box-shadow:0px 4px 12px rgba(0,0,0,0.1);
margin-bottom:30px;
}

</style>

<div class="intro-box">

<div class="main-title">
💻 Smart Guide
</div>

<div class="sub-title">
AI Powered Laptop Recommendation System
</div>

<p>
Choosing the right laptop can be difficult with so many options available.
<strong>Smart Guide</strong> simplifies this by asking a few questions about your needs and using AI to recommend the best laptops for you.
</p>

<p>
Just select your preferences below and let Smart Guide find the perfect laptop.
</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------

data = pd.read_csv("laptop_pred.csv")

features = data[['brand','price','spec_rating','processor','Ram','ROM','GPU']].copy()

# Encode categorical features
encoders = {}

for col in ['brand','processor','Ram','ROM','GPU']:
    le = LabelEncoder()
    features[col] = le.fit_transform(features[col])
    encoders[col] = le

# Train model
model = NearestNeighbors(n_neighbors=5)
model.fit(features)

# ------------------------------------------------
# USER INPUT SECTION
# ------------------------------------------------

st.subheader("🔎 Select Laptop Preferences")

col1, col2, col3 = st.columns(3)

with col1:
    budget = st.slider("💰 Budget (₹)", 10000, 200000, 50000)

with col2:
    brand = st.selectbox("🏷 Preferred Brand", sorted(data['brand'].unique()))

with col3:
    ram = st.selectbox("🧠 RAM", sorted(data['Ram'].unique()))

col4, col5, col6 = st.columns(3)

with col4:
    storage = st.selectbox("💾 Storage", sorted(data['ROM'].unique()))

with col5:
    processor = st.selectbox("⚙ Processor", sorted(data['processor'].unique()))

with col6:
    gpu = st.selectbox("🎮 Graphics", sorted(data['GPU'].unique()))

st.write("")

# ------------------------------------------------
# RECOMMEND BUTTON
# ------------------------------------------------

if st.button("🚀 Find Best Laptops"):

    with st.spinner("🤖 Smart Guide AI is analyzing your preferences..."):
        time.sleep(2)

    # Encode user input
    brand_enc = encoders['brand'].transform([brand])[0]
    processor_enc = encoders['processor'].transform([processor])[0]
    ram_enc = encoders['Ram'].transform([ram])[0]
    rom_enc = encoders['ROM'].transform([storage])[0]
    gpu_enc = encoders['GPU'].transform([gpu])[0]

    user_input = [[brand_enc, budget, 70, processor_enc, ram_enc, rom_enc, gpu_enc]]

    # Budget filter
    filtered_data = data[data['price'] <= budget]

    if filtered_data.empty:
        st.error("❌ No laptops found within this budget.")

    else:

        distances, indices = model.kneighbors(user_input)

        result = data.iloc[indices[0]][['brand','name','price','processor','Ram','GPU']]

        result = result.sort_values(by="price")

        st.subheader("⭐ Top Laptop Recommendations")

        for i, row in result.iterrows():

            with st.container():

                colA, colB = st.columns([4,1])

                with colA:
                    st.markdown(f"### 💻 {row['name']}")
                    st.write(f"**Brand:** {row['brand']}")
                    st.write(f"**Processor:** {row['processor']}")
                    st.write(f"**RAM:** {row['Ram']}")
                    st.write(f"**GPU:** {row['GPU']}")

                with colB:
                    st.metric("Price", f"₹{row['price']}")

                st.progress(80)

                st.divider()

# ------------------------------------------------
# FOOTER
# ------------------------------------------------

st.write("")
st.write("---")
st.caption("Smart Guide AI | Laptop Recommendation System")
st.caption("Developed using Machine Learning & Streamlit")