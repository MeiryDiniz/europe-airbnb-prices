import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

def ml_predict_body():

    version = 'v1'
    
    # Load needed files
    try:
        # Load the entire pipeline (preprocessing + model)
        price_pipeline = joblib.load(f'outputs/ml_pipeline/airbnb_price_prediction/{version}/price_prediction_pipeline.pkl')
        
        # Load the training dataset
        df_train = pd.read_csv(f"outputs/ml_pipeline/airbnb_price_prediction/{version}/TrainSet.csv")

        # Load model performance
        ml_performance = pd.read_csv(f"outputs/ml_pipeline/airbnb_price_prediction/{version}/model_performance.csv")
        
        # Load the feature importance image
        price_feat_importance = plt.imread(f"outputs/ml_pipeline/airbnb_price_prediction/{version}/feature_importance.png")

        st.write("### ML Pipeline: Predict Airbnb Price")        

        # Display pipeline training summary conclusions
        st.info(
            f"* The pipeline was tuned to predict property prices based on features like 'bedrooms', "
            f"'city_center_dist_km', 'metro_dist_km' and 'city'."
        )
        
        st.write("---")        

        # Show the ML pipeline (preprocessor + model)        
        st.write("#### Full ML Pipeline (Preprocessor + Model)")
        st.write(price_pipeline)

        st.write("---")

        st.write("#### Summary of Training Data Used for Model")
        st.write(f"The dataset contains {df_train.shape[0]} rows and {df_train.shape[1]} columns.")

        # Show the training dataset structure        
        st.write("#### Training Data Sample")
        st.write(df_train.head())        

        st.write("---")

        # Show feature importance plot        
        st.write("#### Feature Importance")
        st.image(price_feat_importance)

        st.write("---")

        # Show model performance        
        st.write("#### Model Performance")
        st.write(ml_performance)

        st.write("---")        
        
    except Exception as e:
        st.error(f"Error loading pipeline or files: {e}")
