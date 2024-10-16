import streamlit as st

def summary_body():

    st.write("### Airbnb Prices Project")

    st.info(
        f"This analysis was developed to help a fictitious client (a couple) to decide which would be the best city in Europe to purchase a rental property.\n"
        f"In this case, my clients informed me what their requirements were, and with this information I developed the analysis.\n")

    st.info(
        f"The dataset used to develop this analysis was imported from [Kaggle](https://www.kaggle.com/datasets/cahyaalkahfi/airbnb-european-cities-join).\n"            
    )
    st.write("---")

    st.write("### Clients' Requirement")  
    # text used from the readme 
    st.info(
        f"+ The three cities with the best average daily rental price for an entire house/apt with upm to 3 brdrooms;\n"
        f"+ Considering the number of bedrooms and the distance of the property from the city center and the nearest metro, they would like to:\n"
        f"  + know what influences prices the most:\n"
        f"  + be able to predict price of future acquired properties.\n"
        f"+ **To develop the second requirement, my clients want to keep the analysis in the average price range that will be found in the first requirement.**\n"
        )  