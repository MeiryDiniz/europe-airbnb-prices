import streamlit as st
import pandas as pd
import numpy as np
import joblib

def predict_price_body():
    st.write("### Airbnb Predict Price")

    # Load the pre-trained pipeline
    try:
        best_gb_pipeline = joblib.load("outputs/ml_pipeline/airbnb_price_prediction/v1/price_prediction_pipeline.pkl")        
    except Exception as e:
        st.error(f"Error loading the pipeline: {e}")
        return

    # User input fields for property features 
    bedrooms = st.selectbox('Number of bedrooms', [0, 1, 2, 3])   
    city_center_dist_km = st.number_input('Enter the distance from city center (km)', min_value=0.0, step=0.1, format="%.3f")
    metro_dist_km = st.number_input('Enter the distance from metro (km)', min_value=0.0, step=0.1, format="%.3f")
    # weekends = st.selectbox('Select (0) for weekday and (1) for weekend', [0, 1])
    city = st.selectbox('Select the city', ['Amsterdam', 'Barcelona', 'London'])

    # Create input DataFrame, ensuring it matches the feature order expected by the pipeline
    input_data = {
        'city': [city],
        'bedrooms': [bedrooms],        
        'city_center_dist_km': [city_center_dist_km],
        'metro_dist_km': [metro_dist_km]
        # 'city': [city]  
    }

    input_df = pd.DataFrame(input_data)

    # Show the inputted data
    st.write("Data Inputted for Prediction:")
    st.write(input_df.style.format({"city_center_dist_km": "{:.3f}", "metro_dist_km": "{:.3f}"}))
    
   
    # Access the preprocessor from the pipeline to check feature order
    preprocessor = best_gb_pipeline.named_steps['preprocessor']

    # Get expected column names for the preprocessor (both numerical and one-hot encoded)
    try:
        one_hot_encoder = preprocessor.named_transformers_['cat']
        categorical_columns = one_hot_encoder.get_feature_names_out(['city'])
    except AttributeError:
        categorical_columns = one_hot_encoder.get_feature_names(['city'])  

    # Numerical features that the pipeline was trained on
    numerical_features = ['bedrooms', 'city_center_dist_km', 'metro_dist_km']

    # Combine all expected columns
    expected_columns = list(numerical_features) + list(categorical_columns)    

    # Perform prediction
    if st.button("Predict"):
        try:            
            predicted_log_price = best_gb_pipeline.predict(input_df)
            predicted_price = round(np.expm1(predicted_log_price[0]), 2)
            st.write(f"Predicted Property Price: ${predicted_price}")

        except Exception as e:
            st.error(f"Error during prediction: {e}")
