import streamlit as st
import random
import time

# --- 1. SETUP PAGE ---
st.set_page_config(page_title="Misi Sejarah Tahun 5", page_icon="💣", layout="centered")

# --- CSS (Bagi nampak gempak sikit) ---
st.markdown("""
    <style>
    .stButton button { width: 100%; font-size: 18px; padding: 10px; }
    .status-box { padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; font-size: 20px; }
    .safe { background-color: #d4edda; color: #155724; }
    .warning { background-color: #fff3cd; color: #856404; }
    .danger { background-color: #f8d7da; color: #721c24; }
    .boom { background-color: #000000; color: #ff0000; font-size: 30px; }
    </style>
""", unsafe_allow_html=True)

st.title("💣 Misi Pakar Sejarah: Jangan Sampai Meletup!")
st.caption("Jawab 10 soalan Sejarah Tahun 5. Jika salah 3 kali, bom akan meletup!")

# --- 2. BANK SOALAN (SEJARAH TAHUN 5) ---
# Format: { "soalan": "...", "pilihan": ["A", "B", "C", "D"], "jawapan": "Jawapan Betul" }
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
        "jawapan": "Perlembagaan Persekutuan"
    }
]

# --- 3. SESSION STATE (MEMORI GAME) ---
if 'game_active' not in st.session_state:
    st.session_state.game_active = False
    st.session_state.current_q_index = 0
    st.session_state.score = 0
    st.session_state.wrong_count = 0
    st.session_state.shuffled_questions = []

# --- 4. FUNGSI START / RESET ---
def start_game():
    st.session_state.game_active = True
    st.session_state.current_q_index = 0
    st.session_state.score = 0
    st.session_state.wrong_count = 0
    # Randomkan soalan setiap kali main
    st.session_state.shuffled_questions = random.sample(soalan_master, len(soalan_master))

# --- 5. LOGIK GAME ---

if not st.session_state.game_active:
    # Muka Depan
    st.info("Adakah anda bersedia menguji ilmu Sejarah?")
    if st.button("🚀 MULA MISI SEKARANG", type="primary"):
        start_game()
        st.rerun()

else:
    # --- VISUAL BOM (NYAWA) ---
    salah = st.session_state.wrong_count
    
    if salah == 0:
        st.markdown('<div class="status-box safe">STATUS: SELAMAT<br>💣〰️〰️〰️〰️〰️🕯️</div>', unsafe_allow_html=True)
    elif salah == 1:
        st.markdown('<div class="status-box warning">STATUS: API DINYALAKAN! (Hati-hati)<br>💣〰️〰️🔥</div>', unsafe_allow_html=True)
    elif salah == 2:
        st.markdown('<div class="status-box danger">STATUS: API DAH SAMPAI HUJUNG!!<br>💣🔥</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-box boom">💥 KABOOM! MELETUP! 💥</div>', unsafe_allow_html=True)

    st.divider()

    # Jika Meletup (Kalah)
    if st.session_state.wrong_count >= 3:
        st.error("Misi Gagal! Anda telah salah 3 kali.")
        st.write(f"Markah Akhir: {st.session_state.score} / 10")
        if st.button("🔄 Cuba Lagi (Revive)"):
            start_game()
            st.rerun()
            
    # Jika Dah Habis Jawab Semua (Menang)
    elif st.session_state.current_q_index >= len(st.session_state.shuffled_questions):
        st.balloons()
        st.success("🎉 TAHNIAH! Anda berjaya selamatkan keadaan!")
        st.write(f"Markah Penuh: {st.session_state.score} / 10")
        if st.button("Main Semula"):
            start_game()
            st.rerun()

    # Jika Sedang Main (Paparkan Soalan)
    else:
        # Ambil soalan semasa
        q_data = st.session_state.shuffled_questions[st.session_state.current_q_index]
        
        # Tunjuk Nombor Soalan
        st.subheader(f"Soalan {st.session_state.current_q_index + 1} / 10")
        st.write(f"**{q_data['soalan']}**")
        
        # Pilihan Jawapan (Button)
        pilihan = q_data['pilihan']
        # Kita tak nak randomkan pilihan ABC supaya tak pening, tapi kalau nak random boleh tambah random.shuffle(pilihan)
        
        col1, col2 = st.columns(2)
        
        for i, option in enumerate(pilihan):
            # Susun butang kiri kanan
            with (col1 if i % 2 == 0 else col2):
                if st.button(option):
                    # Semak Jawapan
                    if option == q_data['jawapan']:
                        st.toast("✅ Betul! Fuh selamat...", icon="😎")
                        st.session_state.score += 1
                        time.sleep(0.5) # Bagi user nampak toast kejap
                    else:
                        st.toast("❌ Salah! Api makin dekat!", icon="🔥")
                        st.session_state.wrong_count += 1
                        time.sleep(0.5)
                    
                    # Pergi soalan seterusnya
                    st.session_state.current_q_index += 1
                    st.rerun()

    # Progress Bar (Soalan)
    if st.session_state.wrong_count < 3:
        st.divider()
        st.caption("Kemajuan Misi:")
        prog = st.session_state.current_q_index / 10
        st.progress(prog)
