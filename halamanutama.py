import streamlit as st

st.set_page_config(
    page_title="Kelapa Sulbar",
)

st.title("Selamat Datang di Clustering Kelapa Sulawesi Barat")
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