#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox

# Load the trained model
model = load_model("C:\\Users\\one\\Downloads\\best_model1.h5")

# Load the earthquake data
dataframe = pd.read_csv("C:\\Users\\one\\OneDrive\\Desktop\\Eartquakes-1990-2023.csv")

# Parse the date column into datetime format
dataframe['date'] = pd.to_datetime(dataframe['date'])

# Extract year from the date
dataframe['year'] = dataframe['date'].dt.year

# Drop unnecessary columns
dataframe = dataframe.drop(columns=['place', 'status', 'data_type', 'state', 'date', 'time', 'tsunami'])

# Filter out non-positive magnitudes
dataframe = dataframe[dataframe['magnitudo'] > 0]

# Standardize the features
scaler = StandardScaler()
X = dataframe[['year', 'longitude', 'latitude']]
y = dataframe['magnitudo']
X_scaled = scaler.fit_transform(X)

# Function to predict magnitude for a given year, latitude, and longitude
def predict_magnitude(year, latitude, longitude):
    # Prepare input data
    input_data = np.array([[year, longitude, latitude]])  # assuming only one data point
    # Preprocess the input data
    input_data_scaled = scaler.transform(input_data)
    # Make prediction
    magnitude = model.predict(input_data_scaled)[0][0]
    return magnitude

# Create a Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Create a pop-up window for input
input_window = tk.Toplevel(root)
input_window.title("Earthquake Magnitude Prediction")
input_window.geometry("300x200")

# Create entry fields for input
year_label = tk.Label(input_window, text="Year:")
year_entry = tk.Entry(input_window)
year_label.grid(row=0, column=0, padx=10, pady=10)
year_entry.grid(row=0, column=1, padx=10, pady=10)

latitude_label = tk.Label(input_window, text="Latitude:")
latitude_entry = tk.Entry(input_window)
latitude_label.grid(row=1, column=0, padx=10, pady=10)
latitude_entry.grid(row=1, column=1, padx=10, pady=10)

longitude_label = tk.Label(input_window, text="Longitude:")
longitude_entry = tk.Entry(input_window)
longitude_label.grid(row=2, column=0, padx=10, pady=10)
longitude_entry.grid(row=2, column=1, padx=10, pady=10)

# Function to handle prediction
def predict_and_display():
    # Get input values
    year = int(year_entry.get())
    latitude = float(latitude_entry.get())
    longitude = float(longitude_entry.get())
    
    # Predict magnitude
    predicted_magnitude = predict_magnitude(year, latitude, longitude)
    
    # Display predicted magnitude
    output_label.config(text=f'Predicted Magnitude: {predicted_magnitude}')

# Create a button to submit input
submit_button = tk.Button(input_window, text="Submit", command=predict_and_display)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create a Label widget to display the output
output_label = tk.Label(input_window, text="")
output_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
input_window.mainloop()



# In[ ]:




