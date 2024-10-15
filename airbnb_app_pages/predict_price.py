from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
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
    
   # Perform prediction
    if st.button("Predict"):
        try:
            # Predict the price based on user input
            predicted_log_price = best_gb_pipeline.predict(input_df)
            predicted_price = round(np.expm1(predicted_log_price[0]), 2)
            st.write(f"Predicted Property Price: ${predicted_price}")

            # Load saved test data for calculating performance metrics
            X_test = pd.read_csv("outputs/ml_pipeline/airbnb_price_prediction/v1/X_test.csv")
            y_test = pd.read_csv("outputs/ml_pipeline/airbnb_price_prediction/v1/y_test.csv")

            # Perform predictions on test data
            y_pred_log = best_gb_pipeline.predict(X_test)
            y_pred = np.expm1(y_pred_log)  # Inverse log transform
            y_test_actual = np.expm1(y_test)  # Inverse log transform

            #Calculate performance metrics
            mae = mean_absolute_error(y_test_actual, y_pred)
            

            # Calculate the prediction error for the specific input
            error_margin = mae
            prediction_error = predicted_price - error_margin

            # Display error margin
            st.write(f"The prediction error is ± ${error_margin:.2f} (based on model's MAE)")

        except Exception as e:
            st.error(f"Error during prediction: {e}")    