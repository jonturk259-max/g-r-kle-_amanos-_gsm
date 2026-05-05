import streamlit as st
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="Görükle Amanos GSM", layout="wide", page_icon="📱")

# --- PROFESYONEL CSS TASARIMI ---
st.markdown("""
<style>
    /* Arka Plan ve Genel Font */
    .main { background-color: #f8f9fa; }
    font-family: 'Inter', sans-serif;

    /* Başlık Kartı */
    .hero-container {
        background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%);
        padding: 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Hizmet Kartları */
    .hizmet-kart {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-bottom: 5px solid #1e40af;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: transform 0.3s;
        height: 100%;
    }
    .hizmet-kart:hover { transform: translateY(-5px); }

    /* İstatistik Kutuları */
    .stat-box {
        background: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #e5e7eb;
    }
    .stat-number { font-size: 24px; font-weight: bold; color: #1e40af; }
    
    /* WhatsApp Butonu */
    .stButton>button {
        background-color: #25D366 !important;
        color: white !important;
        border-radius: 25px !important;
        width: 100%;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# --- ANA SAYFA (HERO) ---
with st.container():
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.image("tabela.jpg", use_container_width=True) # Dosya adın 'tabela.jpg' ise çalışır
    with col2:
        st.markdown("""
        <div class="hero-container">
            <h1>GÖRÜKLE AMANOS GSM</h1>
            <p>Bursa'nın En Güvenilir Teknik Servis Deneyimi</p>
            <small>Ekran Değişimi | Batarya Yenileme | Anakart Tamiri</small>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💬 WhatsApp'tan Fiyat Al"):
            st.write("WhatsApp'a yönlendiriliyorsunuz...") # Buraya link eklenebilir

# --- İSTATİSTİKLER ---
st.write("---")
s1, s2, s3, s4 = st.columns(4)
stats = [("15+", "Yıllık Deneyim"), ("30 Dk", "Hızlı Teslim"), ("%100", "Müşteri Memnuniyeti"), ("6 Ay", "İşçilik Garantisi")]
for i, col in enumerate([s1, s2, s3, s4]):
    col.markdown(f'<div class="stat-box"><div class="stat-number">{stats[i][0]}</div><div>{stats[i][1]}</div></div>', unsafe_allow_html=True)

# --- CİHAZ TAKİP SİSTEMİ ---
st.write("### 🔍 Cihaz Durumu Sorgulama")
with st.expander("Sorgulamak için buraya tıklayın", expanded=True):
    takip_no = st.text_input("Size verilen 4 haneli takip numarasını giriniz:", placeholder="Örn: 1002")
    if takip_no:
        # Burada takip.xlsx dosyanı okuyabiliriz
        st.info(f"{takip_no} numaralı cihazınız şu an: **TAMİR AŞAMASINDA**")

# --- HİZMETLERİMİZ ---
st.write("### 🛠️ Neler Yapıyoruz?")
h1, h2, h3 = st.columns(3)
with h1:
    st.markdown('<div class="hizmet-kart"><h4>📱 Ekran & Ön Cam</h4><p>Orijinal parça ve garantili değişim.</p></div>', unsafe_allow_html=True)
with h2:
    st.markdown('<div class="hizmet-kart"><h4>🔋 Batarya Değişimi</h4><p>Yüksek kapasiteli ve uzun ömürlü piller.</p></div>', unsafe_allow_html=True)
with h3:
    st.markdown('<div class="hizmet-kart"><h4>💻 Anakart Tamiri</h4><p>Mikro-lehimleme ile profesyonel onarım.</p></div>', unsafe_allow_html=True)