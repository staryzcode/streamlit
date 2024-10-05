# Import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/staryzcode/dicoding-task/refs/heads/main/day.csv")

customers_df = load_data()

# Title of the dashboard
st.title("Analisis Penyewaan Sepeda Berdasarkan Cuaca dan Bulan")

# Show raw data
st.write("## Dataframe")
st.write(customers_df.head())

# Convert datetime column
customers_df["dteday"] = pd.to_datetime(customers_df["dteday"])

# Sidebar for user input
st.sidebar.header("Pengaturan Visualisasi")
visual_option = st.sidebar.selectbox("Pilih Variabel Visualisasi:", 
                                     ("Suhu", "Kelembaban", "Kecepatan Angin"))

# EDA 1: Scatter plot (depending on user selection)
st.write(f"## Hubungan {visual_option} dengan Total Penyewaan Sepeda")

if visual_option == "Suhu":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=customers_df, x='temp', y='cnt', hue='weathersit', palette='coolwarm', ax=ax)
    ax.set_title('Hubungan Suhu dengan Total Penyewaan Sepeda')
    ax.set_xlabel('Suhu (Normalized)')
    ax.set_ylabel('Total Penyewaan Sepeda')
    st.pyplot(fig)

elif visual_option == "Kelembaban":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=customers_df, x='hum', y='cnt', hue='weathersit', palette='coolwarm', ax=ax)
    ax.set_title('Hubungan Kelembaban dengan Total Penyewaan Sepeda')
    ax.set_xlabel('Kelembaban (Normalized)')
    ax.set_ylabel('Total Penyewaan Sepeda')
    st.pyplot(fig)

elif visual_option == "Kecepatan Angin":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=customers_df, x='windspeed', y='cnt', hue='weathersit', palette='coolwarm', ax=ax)
    ax.set_title('Hubungan Kecepatan Angin dengan Total Penyewaan Sepeda')
    ax.set_xlabel('Kecepatan Angin (Normalized)')
    ax.set_ylabel('Total Penyewaan Sepeda')
    st.pyplot(fig)

# Heatmap EDA
st.write("## Korelasi antara Variabel Cuaca dan Total Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(customers_df[['temp', 'hum', 'windspeed', 'cnt']].corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Korelasi antara Variabel Cuaca dan Total Penyewaan Sepeda')
st.pyplot(fig)

# Line plot untuk penyewa per bulan
st.write("## Tren Total Penyewa Sepeda per Bulan")
monthly_demand = customers_df.groupby('mnth')['cnt'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='mnth', y='cnt', data=monthly_demand, marker='o', color='b', ax=ax)
ax.set_title('Tren Total Penyewa Sepeda per Bulan')
ax.set_xlabel('Bulan')
ax.set_ylabel('Total Penyewa')
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig)
