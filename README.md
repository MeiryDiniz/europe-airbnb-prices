# Europe Airbnb Prices  

Visit the live version of the project dashboard: [Airbnb Predict Prices](https://airbnb-predict-prices-fa26d424b166.herokuapp.com/)

## CONTENTS
  
* [Project Overview](#project-overview) 
* [Dataset Content](#dataset-content)   
* [Study Case Requirements](#study-case-requirements) 
* [Hypotheses and Validation](#hypotheses-and-validation)   
* [Data Visualisation and Data Cleaning](#data-visualisation-and-data-cleaning) 
* [Machine Learning Case](#machine-learning-case)
* [Dashboard Design](#dashboard-design) 
* [Deployment](#deployment) 
* [Main Libraries Used](#main-libraries-used)
* [Resources](#resources)
* [Content](#content)
* [Credits](#credits)  

- - - 

## Project Overview

**Europe Airbnb Prices** is a fictitious project created to demonstrate skills acquired on the Software Development + Predictive Analytics course with Code Institute.
This analysis was developed to help a fictitious client (a couple) to decide which would be the best city in Europe to purchase a rental property.
In this case, my clients informed me what their requirements were, and with this information I developed the analysis.

A public dataset from [Kaggle](https://www.kaggle.com/) was used to develop the analysis project. [Clique here](https://www.kaggle.com/datasets/cahyaalkahfi/airbnb-european-cities-join) to see the original dataset.

- - -

## Dataset Content

The dataset used in this project contains Airbnb listing information for properties in European cities. The dataset includes variables such as:
* **Daily Price:** The price of renting the property per night;
* **City:** The city where the property is located;
* **Bedrooms:** Number of bedrooms in the property;
* **City Center Distance:** Distance of the property from the city center (in kilometers);
* **Metro Distance:** Distance to the nearest metro station (in kilometers);
* **Weekends:** Indicator if the price is for a weekend (binary 0/1).

The data is stored in a CSV format and was cleaned, transformed, and used for exploratory data analysis (EDA) and machine learning tasks.

- - -

## Study Case Requirements

The requirements of my clients are:

1. The three cities with the best average daily rental price for an entire house/apt with upm to 3 brdrooms;
2. Considering the number of bedrooms and the distance of the property from the city center and the nearest metro, they would like to:
   * know what influences prices the most;
   * be able to predict price of future acquired properties.

**To develop the second requirement, my clients want to keep the analysis in the average price range that will be found in the first requirement**  

- - -

## Hypotheses and Validation 

### Hypotheses

**Hypothesis 1 (Number of Bedrooms):** Properties with more bedrooms command higher daily prices.
 + **Rationale:** Larger properties, especially those with more bedrooms, tend to have higher daily rates as they can accommodate more guests and offer greater comfort making them more desirable to both families and groups of travelers.

**Hypothesis 2 (City Center Proximity):** Proximity to the city center has a significant impact on the price of an Airbnb property.
 + **Rationale:** Properties closer to city centers are likely to be more expensive due to convenience, accessibility to landmarks, business hubs, and other attractions. We expect a negative correlation between `city_center_dist_km` and `daily_price`, meaning prices decrease as distance from the center increases.

**Hypothesis 3 (Metro Proximity):** Proximity to public transportation (metros) affects property prices, but to a lesser extent compared to city center proximity.
 + **Rationale:** While being near public transportation is beneficial for travelers, we hypothesize that it will have a weaker impact on price compared to the distance from the city center, as travelers prioritize central locations more.

### Validation

**Hypothesis 1 (Number of Bedrooms):** Confirmed. The number of bedrooms is the strongest predictor of daily price, with larger properties commanding higher rates.

**Hypothesis 2 (City Center Proximity):** Confirmed. Properties closer to the city center tend to have higher prices, with the highest demand for properties within a 3-6 km range from the center.

**Hypothesis 3 (Metro Proximity):** Partially Confirmed. While proximity to metro stations has some influence on price, it is weaker than proximity to the city center or the number of bedrooms.

- - -

## Data Visualisation and Data Cleaning  

1. Data Visualization:
   + City Price Trends: Plot the average prices for each city over weekends and weekdays to understand city-specific price variations.
   + Scatter Plots: Explore relationships between property features to validate hypotheses.
2. Data Cleaning:
   + Drop Variables: Based on the analysis, two features were dropped: `room_type` and `weekends`.
   + Feature Selection: Based on the analysis, features like `city`, `bedrooms`, `city_center_dist_km`, and `metro_dist_km` were selected for building the ML to predict prices.
   
- - -

## Machine Learning Case

The ML case revolves around predicting Airbnb prices using a variety of regression models. Key tasks included:

1. Feature Engineering:
   + Apply Box-Cox transformation to `city_center_dist_km` and logarithmic transformation `metro_dist_km` and `daily_price`.
   + Create one-hot encoding for the categorical variable city.
2. Model Selection:
   + Four models were tested: Linear Regression, Ridge Regression, Lasso Regression, and Gradient Boosting Regressor.
   + Gradient Boosting provided the best performance based on Mean Absolute Error (MAE) and R² score.
3. Hyperparameter Tuning:
   + Hyperparameter tuning was done using GridSearchCV to optimize learning_rate, max_depth, and n_estimators for the Gradient Boosting model.
4. Evaluation:
   + The best model achieved a Mean Absolute Error (MAE) of approximately 60.38 and an R² score of 0.58.

---

## Dashboard Design

The dashboard was designed using Streamlit to display key insights and predictions. It includes:

1. Analysis Summary: Introduction to the project analysis.
2. Analysis and Data Visualization: Interactive analysis and plots for average price trends by city, correlation analysis, and scatter plots.
3. Price Prediction Interface: Users can input property features and receive predicted prices using the trained machine learning model.
4. Hypotheses and Validation: Hypotheses validation of wthat could be correlated to the daily rent prices. 
5. Feature Importance: Display a chart showing the most important features contributing to the price prediction model.

- - -

## Deployment

The entire project, including the machine learning pipeline and dashboard, was deployed on Heroku.

- Git and Heroku CLI were used to set the Heroku Stak to `heroku-20`.

- - -

## Main Libraries Used

The project leverages the following key libraries:

- Pandas: For data manipulation and preprocessing.
- NumPy: For numerical computations.
- Matplotlib & Seaborn: For data visualization.
- Scikit-learn: For building and tuning machine learning models.
- Streamlit: For creating an interactive web application.
- Joblib: For saving the trained models.
- Heroku: For cloud deployment.

- - -

## Resources

In addition to the course content I used [Stack Overflow](http://stackoverflow.com) to do research to develop my analysis project:

- [Stack Overflow](http://stackoverflow.com)
- [Streamlit documentation](https://docs.streamlit.io/)
- [Jupyter](https://jupyter.org/)

- - - 

## Content

Some codes and the dashboard idea for my analysis were taken from the Code Intitute's **Churnometer** project. I made modification to the codes to adapt to my analysis requirements.
The content and the majority code of the analysis project were wrote by the developer.

- - - 

## Credits

I used the Code Intitute's **Churnometer** project as a basis to develop the analysis of my project and better understand how to use the necessary features in its development.
