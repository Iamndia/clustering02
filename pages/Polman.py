import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import folium 
from streamlit_folium import st_folium

st.title("Kelapa Polewali Mandar")

# Membaca dataset dari file Excel
df = pd.read_excel("kelapaPolman.xlsx")
x = df.iloc[:, [4, 5]].values

st.header("Isi Dataset")
st.write(df)

# Elbow method untuk menentukan jumlah cluster yang tepat
clusters = []
for i in range(1, 6):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)
    clusters.append(kmeans.inertia_)

# Plot Elbow
st.subheader("Elbow Method")
fig1, ax1 = plt.subplots(figsize=(12, 8))
sns.lineplot(x=list(range(1, 6)), y=clusters, ax=ax1)
ax1.set_title("Mencari Elbow")
ax1.set_xlabel("Clusters")
ax1.set_ylabel("Inertia")
st.pyplot(fig1)

# Normalisasi data
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Proses K-Means Clustering dengan jumlah cluster 3
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(x_scaled)

# Mengubah nama kolom untuk lebih rapi
df.columns = df.columns.str.strip()

# Mapping cluster numerik ke kategori
cluster_mapping = {2: 'Rendah', 1: 'Sedang', 0: 'Tinggi'}
df['Cluster'] = df['Cluster'].map(cluster_mapping)

# Mapping warna berdasarkan cluster
cluster_colors = {'Rendah': 'green', 'Sedang': 'blue', 'Tinggi': 'red'}

# Membuat plot scatter
st.subheader("Plot Clustering")
fig2, ax2 = plt.subplots(figsize=(15, 6))
sns.scatterplot(x='Kecamatan', y='Produktivitas(Kg/Ha)', hue='Cluster', palette=cluster_colors, s=150, data=df, ax=ax2)
ax2.set_title("Hasil Clustering")
ax2.set_xlabel("Kecamatan")
ax2.set_ylabel("Produktivitas(Kg/Ha)")
st.pyplot(fig2)

st.header("Hasil Cluster")
st.write(df)

# Menampilkan Peta dengan hasil pengelompokan
st.subheader("Peta Hasil Pengelompokan")
map_loc = folium.Map(location=[df['latitude'].mean(), df['longtitude'].mean()], zoom_start=8)
for idx, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longtitude']], 
        tooltip=f"Kecamatan {row['Kecamatan']} (Cluster: {row['Cluster']})",
        icon=folium.Icon(color='green' if row['Cluster'] == 'Rendah' else 'blue' if row['Cluster'] == 'Sedang' else 'red')
    ).add_to(map_loc)
st_folium(map_loc, width=600)

# Custom CSS untuk mengubah warna latar belakang
st.markdown(
    """
    <style>
    body {
        background-color: #020249FF;
    }
    .stApp {
        background-color: #02023EFF;
    }
    [data-testid="stSidebarContent"] {
    background-color: #020249B9;
    }
    </style>
    """,
    unsafe_allow_html=True
)
