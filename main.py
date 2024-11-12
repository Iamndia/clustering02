import streamlit as st
from PIL import Image
import halamanutama as halamanutama

# Fungsi untuk mengatur halaman
def navigate_to(page_name):
    st.session_state.page = page_name
    st.experimental_rerun()

# Inisialisasi `st.session_state.page` jika belum ada
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Atur lebar halaman
st.set_page_config(page_title="Kelapa Sulawesi Barat", layout="wide")

# Pindah ke halaman sesuai dengan `st.session_state.page`
if st.session_state.page == 'halamanutama':
    halamanutama.tampilkan()
    st.stop()

# Mengatur warna background dan style tombol dengan CSS
st.markdown("""
    <style>
    /* CSS Global */
    .main {
        background-color: #FD4C4C; /* Warna Background Merah */
        padding: 50px;
    }
    
    .button-style {
        background-color: #000000; /* Warna Tombol Hitam */
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
    }
    .button-style:hover {
        background-color: #333333; /* Warna saat di-hover */
    }
    
    .title-text {
        font-family: 'Poppins', sans-serif;
        font-size: 2.5rem;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
    }
    .subtitle-text {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        color: white;
        margin-top: 0;
        margin-bottom: 20px;
    }
    .description-text {
        font-size: 1.1rem;
        color: white;
        margin-bottom: 30px;
    }
    
    /* Media Queries untuk responsivitas */
    @media (max-width: 768px) {
        .title-text {
            font-size: 2rem;
        }
        .subtitle-text {
            font-size: 1.2rem;
        }
        .description-text {
            font-size: 1rem;
        }
        .button-style {
            font-size: 14px;
            padding: 8px 15px;
        }
    }
    
    @media (max-width: 480px) {
        .main {
            padding: 20px;
        }
        .title-text {
            font-size: 1.8rem;
        }
        .subtitle-text {
            font-size: 1rem;
        }
        .description-text {
            font-size: 0.9rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Grid Layout dari Streamlit
col1, col2 = st.columns([1, 1.5])

# Kolom Kiri (Teks dan Tombol)
with col1:
    st.markdown("<p class='title-text'>Kelapa</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle-text'>Sulawesi Barat</p>", unsafe_allow_html=True)
    st.markdown("<p class='description-text'>Klik tombol <b>Lihat Wilayah</b> untuk melihat wilayah dengan produksi kelapa di Sulawesi Barat.</p>", unsafe_allow_html=True)
    
    # Tombol "Lihat Wilayah"
    if st.button("Lihat Wilayah", key="lihat", help="Klik untuk melihat wilayah"):
        navigate_to('halamanutama')

# Kolom Kanan (Gambar Kelapa)
with col2:
    try:
        # Buka dan tampilkan gambar dengan proporsi yang sesuai
        image = Image.open("kelapa.jpg")  # Ganti nama file sesuai dengan gambar Anda
        st.image(image, width=300, use_column_width=False)
    except FileNotFoundError:
        st.error("Gambar kelapa tidak ditemukan. Pastikan file 'kelapa.jpg' ada di folder yang sama.")

# Footer
st.markdown("""
    <hr>
    <footer>
        <div style='text-align: center; font-size: small; color: #000000'>
        &copy; 2024 Sulawesi Barat
        </div>
    </footer>
""", unsafe_allow_html=True)
