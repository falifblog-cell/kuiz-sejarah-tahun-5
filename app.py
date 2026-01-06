import streamlit as st
import random
import time

# --- 1. SETUP PAGE ---
st.set_page_config(page_title="Misi Sejarah Tahun 5", page_icon="💣", layout="centered")

# --- CSS (Bagi nampak gempak sikit) ---
st.markdown("""
    <style>
    .stButton button { width: 100%; font-size: 18px; padding: 10px; }
    .status-box { padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; font-size: 20px; margin-bottom: 10px; }
    .safe { background-color: #d4edda; color: #155724; border: 2px solid #c3e6cb; }
    .warning { background-color: #fff3cd; color: #856404; border: 2px solid #ffeeba; }
    .danger { background-color: #f8d7da; color: #721c24; border: 2px solid #f5c6cb; }
    .boom { background-color: #000000; color: #ff0000; font-size: 30px; border: 3px solid red; }
    
    /* CSS Baru untuk Banner Tahniah */
    .celebration-banner {
        background-color: #d1e7dd;
        color: #0f5132;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 24px;
        font-weight: 800;
        border: 3px solid #badbcc;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.02); }
      100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

st.title("💣 Misi Pakar Sejarah: Jangan Sampai Meletup!")
st.caption("Jawab 10 soalan Sejarah Tahun 5. Jika salah 3 kali, bom akan meletup!")

# --- 2. BANK SOALAN (SEJARAH TAHUN 5) ---
soalan_master = [
    {
        "soalan": "Apakah gelaran bagi Ketua Utama Negara Malaysia?",
        "pilihan": ["Yang di-Pertuan Agong", "Perdana Menteri", "Sultan", "Yang di-Pertua Negeri"],
        "jawapan": "Yang di-Pertuan Agong"
    },
    {
        "soalan": "Bunga Raya dipilih sebagai bunga kebangsaan. Berapakah kelopak yang ada padanya?",
        "pilihan": ["4 Kelopak", "5 Kelopak", "6 Kelopak", "7 Kelopak"],
        "jawapan": "5 Kelopak"
    },
    {
        "soalan": "Lagu 'Negaraku' berasal daripada irama lagu negeri mana?",
        "pilihan": ["Johor", "Kedah", "Perak", "Selangor"],
        "jawapan": "Perak"
    },
    {
        "soalan": "Warna kuning pada Jalur Gemilang melambangkan apa?",
        "pilihan": ["Perpaduan Rakyat", "Kesucian Agama", "Keberanian", "Kedaulatan Raja"],
        "jawapan": "Kedaulatan Raja"
    },
    {
        "soalan": "Haiwan apakah yang terdapat pada Jata Negara Malaysia?",
        "pilihan": ["Gajah", "Harimau", "Singa", "Kijang"],
        "jawapan": "Harimau"
    },
    {
        "soalan": "Siapakah Perdana Menteri Malaysia yang pertama (Bapa Kemerdekaan)?",
        "pilihan": ["Tun Abdul Razak", "Tun Hussein Onn", "Tunku Abdul Rahman", "Tun Dr Mahathir"],
        "jawapan": "Tunku Abdul Rahman"
    },
    {
        "soalan": "Bahasa Kebangsaan Malaysia ialah?",
        "pilihan": ["Bahasa Inggeris", "Bahasa Melayu", "Bahasa Ibunda", "Bahasa Baku"],
        "jawapan": "Bahasa Melayu"
    },
    {
        "soalan": "Rukun Negara mempunyai berapa prinsip?",
        "pilihan": ["3 Prinsip", "4 Prinsip", "5 Prinsip", "6 Prinsip"],
        "jawapan": "5 Prinsip"
    },
    {
        "soalan": "Apakah nama bendera Malaysia?",
        "pilihan": ["Sang Saka Merah Putih", "Jalur Gemilang", "Harimau Malaya", "Bintang 14"],
        "jawapan": "Jalur Gemilang"
    },
    {
        "soalan": "Institusi Raja Berperlembagaan bermaksud raja bertindak mengikut?",
        "pilihan": ["Kehendak sendiri", "Perlembagaan Persekutuan", "Nasihat rakyat", "Adat istiadat semata-mata"],
        "jawapan": "Perlembagaan Persekutuan
