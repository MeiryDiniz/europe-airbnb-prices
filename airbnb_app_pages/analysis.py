import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def analysis_body():

    st.write("### Airbnb Prices Analysis")

    st.info(
        f"A dataframe from [Kaggle]() was used to develop this analysis.\n"
        f"The dataframe was prepared and processed acordingly to the analysis' requirements.\n"
    )

    df = pd.read_csv("outputs/datasets/collection/EuropeanCitiesAirbnb.csv")
    df_filtered = df[df['room_type'] == 'Entire home/apt']    

    # inspect data
    if st.checkbox("Inspect DataFrame"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows."
        )

        st.write(df.head(10))

    st.write("---")

    st.write("### Analysing Average Daily Prices")

    st.write(
        f"Analysing the average daily price by weekday & weekend chart, was possible to conclude that:\n"
        f"+ The three best cities with the best average daily are: Amsterdam, Barcelona and London\n")
    
    # Filter the DataFrame to exclude daily prices over 2000
    filtered_df_avg = df_filtered[df_filtered['daily_price'] <= 2000]
    average_price2 = filtered_df_avg.groupby(['city', 'weekends'])['daily_price'].mean().reset_index()
    avg_price_pivot2 = average_price2.pivot(index='city', columns='weekends', values='daily_price')
    best_prices2 = avg_price_pivot2.sort_values(by=[0, 1], ascending=False)
    print(best_prices2)
    # code used in the 02-AirbnbCaseStudy notebook to check average price
    # average_price = df_filtered.groupby(['city', 'weekends'])['daily_price'].mean().reset_index()    
    # avg_price_pivot = average_price.pivot(index='city', columns='weekends', values='daily_price')    
    # best_prices = avg_price_pivot.sort_values(by=[0,1], ascending=False)

    # check average price
    if st.checkbox("Check Average Price Data"):
        st.write("Sorted Average Prices by City (Weekdays (0) and Weekends (1)):")

        st.write(best_prices2)    
    
    # code used in the 02-AirbnbCaseStudy notebook to visualise average price chart
    fig, ax = plt.subplots(figsize=(10, 6))
    # Plot the average prices with custom colors and labels
    best_prices2.plot(kind='bar', figsize=(10, 6), color=['grey', 'coral'], ax=ax)

    # Adding labels and title
    ax.set_title('Average Daily Price by City and Weekday/Weekend')
    ax.set_xlabel('City')
    ax.set_ylabel('Average Daily Price')
    ax.set_xticklabels(best_prices2.index, rotation=45)  # Rotate the x-axis labels for readability
    ax.legend(title='Weekends', labels=['No', 'Yes'])
    ax.grid(axis='y')

    # visualise average price chart
    if st.checkbox("Visualise Average Price Chart"):
          
        st.pyplot(fig) 

    st.write("---")

    st.write("### Analysing Correlation")

    st.write(
        f"After analysing `Pearson` and `Spearman` correlation, and also performing `EDA` in the main correlations found, it was possible to conclude that:\n"
        f"+ The number of bedrooms is the most important factor in influencing price. The client's focus should be on larger properties (if available), though the distribution shows that most listings have 1-2 bedrooms;\n"
        f"+ Proximity to the city center is also an important factor, but it shows a peak around 3-6 km, indicating that most properties are located within this range from the city center;\n"
        f"+ Proximity to a metro station has a weaker influence on price. While being near public transport is beneficial, it's less important compared to city center proximity and the number of bedrooms."
    )

    # pearson correlation - code copied from 02-AirbnbCaseStudy notebook
    # Define the list of cities of interest
    cities_of_interest = ['Amsterdam', 'Barcelona', 'London']
    # Filter data to include only the relevant cities and columns of interest
    relevant_columns = ['daily_price', 'bedrooms', 'city_center_dist_km', 'metro_dist_km', 'weekends', 'city']
    df_subset = df_filtered[(df_filtered['city'].isin(cities_of_interest)) & (df_filtered['daily_price'] <= 2000)][relevant_columns]

    # Calculate Pearson correlation
    pearson_correlation = df_subset.corr(method='pearson')
    price_pearson_corr = pearson_correlation['daily_price'].sort_values(key=abs, ascending=False)[1:]
    price_pearson_corr

    # spearman correlation - code copied from 02-AirbnbCaseStudy notebook
    # Calculate Spearman correlation
    spearman_correlation = df_subset.corr(method='spearman')
    price_spearman_corr = spearman_correlation['daily_price'].sort_values(key=abs, ascending=False)[1:]
    price_spearman_corr 
    
    # pearson and spearman correlation
    if st.checkbox("Pearson and Spearman Correlation"):
        st.write(
            f"Pearson Correlation:")

        st.write(price_pearson_corr)

        st.write(
            f"Spearman Correlation:")

        st.write(price_spearman_corr)     

    st.write("Visualising `distribution`, `relationship` and `average` between `daily_price` and main correlations found.")

    # distribution - code used from 02-AirbnbCaseStudy notebook
    best_corr = 3
    set(price_pearson_corr[:best_corr].index.to_list() + price_spearman_corr[:best_corr].index.to_list())

    vars_to_analysis = ['bedrooms', 'city_center_dist_km', 'metro_dist_km']
    vars_to_analysis
    
    variables_to_plot = vars_to_analysis + ['daily_price']    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))  
    df_subset[variables_to_plot].hist(bins=30, ax=axes)
    plt.tight_layout()

    # Checkbox to show distribution plots
    if st.checkbox("Distribution Plots of Numerical Variables"):
        st.write(
            f"Distribution Plots"
        )

        st.pyplot(fig)

    # relationship - code used from 02-AirbnbCaseStudy notebook
    if st.checkbox("Scatter Plots of Variables vs. Daily Price"):
    
        for var in vars_to_analysis:
            fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure for each variable
            ax.scatter(df_subset['daily_price'], df_subset[var], color='blue')
            ax.set_title(f'Scatter Plot of {var.capitalize()} vs. Daily Price')
            ax.set_xlabel('Daily Price')
            ax.set_ylabel(var.capitalize())
            ax.grid()
        
            # Display each scatter plot with its own title and plot
            st.write(f"+ Scatter Plot of {var.capitalize()} vs. Daily Price")
            st.pyplot(fig)         

    # average of variables by city - code used from 02-AirbnbCaseStudy notebook 
    # Define a color scheme for the bar plots
    colors = ['darkblue', 'grey', 'coral']

    # Loop through each variable in vars_to_analysis
    if st.checkbox("Bar Plot for Average of Variables by City"):
       
        # Create a checkbox for each variable
        for var in vars_to_analysis:
        
            # Calculate average for each city for the current variable
            average_price = df_subset.groupby('city')[var].mean().reset_index()
            # Sort the averages in descending order
            average_price = average_price.sort_values(by=var, ascending=False)
        
            # Create a bar plot
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(average_price['city'], average_price[var], color=colors[:len(average_price)])
        
            # Adding labels and title specific to the variable
            ax.set_title(f'{var.capitalize()} Average by City')
            ax.set_xlabel('City')
            ax.set_ylabel(f'Average {var.capitalize()}')
            ax.set_xticks(range(len(average_price['city'])))
            ax.set_xticklabels(average_price['city'], rotation=45)
            ax.grid(axis='y')
        
            # Display the bar plot
            st.write(f"+ Bar Plot of {var.capitalize()} Average by City", key=f"bar_{var}")
            st.pyplot(fig)
     