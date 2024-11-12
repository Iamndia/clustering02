import streamlit as st
st.set_page_config(
    page_title="Kelapa Sulbar",
)

st.title("Selamat Datang di Clustering Kelapa Sulawesi Barat")
st.sidebar.page_link("halamanutama.py", label="Halaman Utama")
st.sidebar.page_link("pages\sulbar.py", label="Kelapa Sulbar")
st.sidebar.page_link("pages\polewali.py", label="Kelapa Polman")
st.sidebar.page_link("pages\majene.py", label="Kelapa Majene")
