import streamlit as st
import pandas as pd

def load_data(file_path):
    data = pd.read_excel(file_path)
    return data

def main():
    st.title("Streamlit Dashboard with Excel Data")

    # Load Excel data
    file_path = "https://github.com/adithapathiraja/Solar-Power-Data-Visualization/blob/main/Dataset%20-%20Nov%2001%20-%20Dec%2001%202023.xlsx"
    data = load_data(file_path)

    # Display the dataset
    st.subheader("Dataset:")
    st.dataframe(data)

    # Display basic statistics
    st.subheader("Basic Statistics:")
    st.write(data.describe())

    # You can add more sections and visualizations as needed

if __name__ == "__main__":
    main()
