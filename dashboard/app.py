import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
day_df = pd.read_csv('../data/day.csv')
hour_df = pd.read_csv('../data/hour.csv')

# Function to calculate average rentals by weekday
def avg_rentals_by_weekday():
    weekday_labels = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    weekday_avg = day_df.groupby('weekday')['cnt'].mean()
    weekday_avg.index = [weekday_labels[i] for i in weekday_avg.index]
    return weekday_avg

# Function to calculate average rentals by hour
def avg_rentals_by_hour():
    hour_avg = hour_df.groupby('hr')['cnt'].mean()
    return hour_avg

# Streamlit app layout
st.title('Bike Rentals Analysis')

# Section for average rentals by weekday
st.header('Average Rentals by Weekday')
weekday_avg = avg_rentals_by_weekday()
weekday_avg_df = pd.DataFrame(weekday_avg).reset_index()
weekday_avg_df.columns = ['Weekday', 'Average Bike Rentals']
st.table(weekday_avg_df)

# Plot average rentals by weekday
plt.figure(figsize=(10, 5))
plt.bar(weekday_avg_df['Weekday'], weekday_avg_df['Average Bike Rentals'], color='skyblue')
plt.title('Average Bike Rentals by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Average Bike Rentals')
plt.xticks(rotation=45)
st.pyplot(plt)

# Section for average rentals by hour
st.header('Average Rentals by Hour')
hour_avg = avg_rentals_by_hour()
hour_avg_df = pd.DataFrame(hour_avg).reset_index()
hour_avg_df.columns = ['Hour', 'Average Bike Rentals']
st.table(hour_avg_df)

# Plot average rentals by hour
plt.figure(figsize=(12, 6))
plt.plot(hour_avg_df['Hour'], hour_avg_df['Average Bike Rentals'], marker='o', color='skyblue')
plt.title('Average Bike Rentals by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Bike Rentals')
plt.xticks(np.arange(0, 24, 1))  # Display hours from 0 to 23
plt.grid(True)
st.pyplot(plt)
