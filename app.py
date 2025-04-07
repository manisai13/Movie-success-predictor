import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🎬 Movie Success Predictor")

# User Inputs
budget = st.number_input("Budget (in million $)", min_value=1, step=1)
duration = st.number_input("Duration (in minutes)", min_value=60, step=1)
genre = st.selectbox("Genre", ["Action", "Comedy", "Drama", "Horror", "Sci-Fi"])
director_rep = st.slider("Director's Reputation (1-10)", 1, 10, 5)
actor_popularity = st.slider("Lead Actor Popularity (1-10)", 1, 10, 5)
social_buzz = st.slider("Social Media Buzz (1-100)", 1, 100, 50)
trailer_views = st.number_input("Trailer Views (millions)", min_value=0, step=1)
studio = st.selectbox("Production Studio", ["Big", "Small", "Indie"])

# Encoding categorical features
genre_mapping = {"Action": 1, "Comedy": 2, "Drama": 3, "Horror": 4, "Sci-Fi": 5}
studio_mapping = {"Big": 3, "Small": 2, "Indie": 1}

genre_encoded = genre_mapping[genre]
studio_encoded = studio_mapping[studio]

# Prediction
if st.button("Predict Success"):
    features = np.array([[budget, duration, genre_encoded, director_rep, actor_popularity, social_buzz, trailer_views, studio_encoded]])
    prediction = model.predict(features)[0]
    
    if prediction == 1:
        st.success("🎉 This movie is predicted to be a HIT!")
    else:
        st.error("💀 This movie might be a FLOP!")
