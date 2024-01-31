# app.py
import streamlit as st
import pandas as pd
import os

def load_data(file_path):
    data = pd.read_excel(file_path)
    return data

def main():
    st.title("Streamlit Dashboard with Excel Data")

    # Load Excel data
    file_name = "Dataset - Nov 01 - Dec 01 2023.xlsx"
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    if os.path.isfile(file_path):
        data = load_data(file_path)
        # Display the dataset
        st.subheader("Dataset:")
        st.dataframe(data)

        # Display basic statistics
        st.subheader("Basic Statistics:")
        st.write(data.describe())

    else:
        st.error(f"File not found: {file_name}")

    # You can add more sections and visualizations as needed

if __name__ == "__main__":
    main()
