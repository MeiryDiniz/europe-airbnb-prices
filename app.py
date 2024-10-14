import streamlit as st
from airbnb_app_pages.multipage import MultiPage


# Load page scripts
from airbnb_app_pages.summary import summary_body
from airbnb_app_pages.analysis import analysis_body
from airbnb_app_pages.predict_price import predict_price_body
from airbnb_app_pages.project_hypothesis import project_hypothesis_body
from airbnb_app_pages.ml_predict import ml_predict_body

# Initialize the multipage app
app = MultiPage(app_name="Airbnb Prices")

# Add app pages
app.add_page("Project Summary", summary_body)
app.add_page("Project Analysis", analysis_body)
app.add_page("Airbnb Predict Price", predict_price_body)  # Note: no need to pass the pipeline here
app.add_page("Project Hypothesis and Validation", project_hypothesis_body)
app.add_page("Ml Pipeline: Predict Price Airbnb", ml_predict_body)

# Run the app
app.run()
