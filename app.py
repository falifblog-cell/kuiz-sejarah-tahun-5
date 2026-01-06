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
    # State baru untuk trigger celebration
    st.session_state.just_got_correct = False 

# --- 4. FUNGSI START / RESET ---
def start_game():
    st.session_state.game_active = True
    st.session_state.current_q_index = 0
    st.session_state.score = 0
    st.session_state.wrong_count = 0
    st.session_state.just_got_correct = False
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

    # --- CELEBRATION BLOCK (YANG MERIAH TU) ---
    # Ini akan muncul di atas soalan seterusnya jika jawapan SEBELUM ini betul
    if st.session_state.just_got_correct:
        st.balloons() # Lepaskan belon!
        st.markdown("""
            <div class="celebration-banner">
            ✨ TAHNIAH! JAWAPAN TEPAT! ✨<br>
            Fuh selamat... Teruskan misi!
            </div>
        """, unsafe_allow_html=True)
        # Reset balik trigger supaya tak keluar lagi next round
        st.session_state.just_got_correct = False

    st.divider()

    # Jika Meletup (Kalah)
    if st.session_state.wrong_count >= 3:
        st.error("Misi Gagal! Anda telah salah 3 kali dan bom meletup.")
        st.write(f"Markah Akhir: {st.session_state.score} / 10")
        if st.button("🔄 Cuba Lagi (Revive)"):
            start_game()
            st.rerun()
            
    # Jika Dah Habis Jawab Semua (Menang)
    elif st.session_state.current_q_index >= len(st.session_state.shuffled_questions):
        st.balloons() # Belon lagi untuk kemenangan besar
        st.success("🎉 TAHNIAH! MISI BERJAYA! Anda pakar sejarah sebenar.")
        st.metric("Markah Penuh", f"{st.session_state.score} / 10")
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
        
        col1, col2 = st.columns(2)
        
        for i, option in enumerate(pilihan):
            # Susun butang kiri kanan
            with (col1 if i % 2 == 0 else col2):
                if st.button(option):
                    # --- SEMAK JAWAPAN ---
                    if option == q_data['jawapan']:
                        # Kalau betul: Set trigger untuk celebration nanti
                        st.session_state.score += 1
                        st.session_state.just_got_correct = True 
                    else:
                        # Kalau salah: Toast kecil je cukup sebagai amaran
                        st.toast("❌ Salah! Api makin dekat!", icon="🔥")
                        st.session_state.wrong_count += 1
                        st.session_state.just_got_correct = False
                        time.sleep(0.5) # Delay sikit untuk toast salah
                    
                    # Pergi soalan seterusnya
                    st.session_state.current_q_index += 1
                    st.rerun()

    # Progress Bar (Soalan)
    if st.session_state.wrong_count < 3 and st.session_state.game_active:
        st.divider()
        st.caption(f"Kemajuan: {st.session_state.current_q_index}/10 Soalan")
        prog = st.session_state.current_q_index / 10
        # Elak progress bar error kalau dah lebih 10
        st.progress(min(prog, 1.0))
