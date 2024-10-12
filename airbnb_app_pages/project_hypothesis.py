import streamlit as st

def project_hypothesis_body():
    st.write("### Airbnb Prices: Project Hypothesis and Validation")    

    st.write("**Hypothesis**")

    st.write(
        f" 1. **Hypothesis 1 (Number of Bedrooms):** Properties with more bedrooms command higher daily prices.\n"
        f"    + **Rationale:** Larger properties, especially those with more bedrooms, tend to have higher daily rates as they can accommodate more guests and offer greater comfort, making them more desirable to both families and groups of travelers.\n"
        f" 2. **Hypothesis 2 (City Center Proximity):** Proximity to the city center has a significant impact on the price of an Airbnb property.\n"
        f"    + **Rationale:** Properties closer to city centers are likely to be more expensive due to convenience, accessibility to landmarks, business hubs, and other attractions. We expect a negative correlation between `city_center_dist_km` and `daily_price`, meaning prices decrease as distance from the center increases.\n"
        f" 3. **Hypothesis 3 (Metro Proximity):** Proximity to public transportation (metros) affects property prices, but to a lesser extent compared to city center proximity.\n"
        f"    + **Rationale:** While being near public transportation is beneficial for travelers, we hypothesize that it will have a weaker impact on price compared to the distance from the city center, as travelers prioritize central locations more.\n"
    )

    st.write("---")
    
    # conclusions taken from 02-AirbnbCaseStudy notebook
    st.write("**Validation**")

    st.write(
        f" + **Hypothesis 1 (Number of Bedrooms):** Confirmed. The number of bedrooms is the strongest predictor of daily price, with larger properties commanding higher rates.\n"
        f" + **Hypothesis 2 (City Center Proximity):** Confirmed. Properties closer to the city center tend to have higher prices, with the highest demand for properties within a 3-6 km range from the center.\n"
        f" + **Hypothesis 3 (Metro Proximity):** Partially Confirmed. While proximity to metro stations has some influence on price, it is weaker than proximity to the city center or the number of bedrooms.\n"
    )