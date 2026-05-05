import streamlit as st
import pandas as pd
import os

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Amanos GSM | Teknik Servis", layout="wide", page_icon="📱")

# --- GELİŞMİŞ KOYU TEMA VE STİL (CSS) ---
st.markdown("""
<style>
    .stApp { background-color: #0b0d0e; color: #ffffff; }
    section[data-testid="stSidebar"] { background-color: #16181a !important; border-right: 1px solid #2ecc71; }
    
    /* Takip Kutusu Tasarımı */
    .takip-container {
        background: #1a1d1f;
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #2ecc71;
        text-align: center;
        margin: 20px 0;
    }
    .durum-text { font-size: 24px; font-weight: bold; color: #2ecc71; margin-top: 15px; }
    
    /* Hizmet Kartları */
    .hizmet-card { background: #16181a; padding: 20px; border-radius: 10px; border-bottom: 3px solid #2ecc71; }
    
    /* WhatsApp Yüzen Buton */
    .wa-link {
        position: fixed; bottom: 20px; right: 20px; background-color: #25d366;
        color: white !important; padding: 15px 25px; border-radius: 50px;
        text-decoration: none; font-weight: bold; z-index: 1000;
    }
</style>
""", unsafe_allow_html=True)

# --- YAN MENÜ ---
with st.sidebar:
    st.markdown("<h2 style='color:#2ecc71;'>AMANOS GSM</h2>", unsafe_allow_html=True)
    secim = st.radio("MENÜ", ["Ana Sayfa", "🔍 Cihaz Durum Sorgula", "🛠️ Hizmetlerimiz", "🖼️ Galeri", "📞 İletişim"])
    st.markdown("---")
    st.write("📍 Görükle / BURSA")
    st.write("📞 0530 872 59 79")

# --- SAYFA İÇERİKLERİ ---

# 1. ANA SAYFA
if secim == "Ana Sayfa":
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("<h1 style='font-size:50px;'>Bursa'nın En İyi <br><span style='color:#2ecc71;'>Teknik Servis</span> Deneyimi</h1>", unsafe_allow_html=True)
        st.write("Profesyonel ekipman ve 15 yıllık tecrübeyle tüm markalara garantili tamir hizmeti sunuyoruz.")
        if st.button("Hemen Cihazını Sorgula"):
            st.info("Lütfen sol menüden 'Cihaz Durum Sorgula' sekmesine geçiniz.")
    with col2:
        st.image("https://images.unsplash.com/photo-1512428559087-560ad5185257?auto=format&fit=crop&w=800&q=80")

# 2. CİHAZ DURUM SORGULAMA (YENİ EKLEDİĞİMİZ KISIM)
elif secim == "🔍 Cihaz Durum Sorgula":
    st.markdown("<h1 style='color:#2ecc71;'>🔍 Cihaz Durumu Sorgulama</h1>", unsafe_allow_html=True)
    st.write("Size verilen 4 haneli takip numarasını aşağıya yazarak cihazınızın son durumunu öğrenebilirsiniz.")
    
    takip_no = st.text_input("Takip Numaranızı Giriniz (Örn: 1001)", placeholder="Numarayı buraya yazın...")
    
    if takip_no:
        # Excel dosyasını kontrol et ve oku
        if os.path.exists("takip.xlsx"):
            df = pd.read_excel("takip.xlsx")
            # Numarayı ara
            sonuc = df[df['takip_no'].astype(str) == takip_no]
            
            if not sonuc.empty:
                st.markdown(f"""
                <div class="takip-container">
                    <h3>Cihaz: {sonuc.iloc[0]['cihaz']}</h3>
                    <div class="durum-text">DURUM: {sonuc.iloc[0]['durum']}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Üzgünüz, bu numara ile kayıtlı bir cihaz bulunamadı. Lütfen numarayı kontrol ediniz.")
        else:
            st.warning("Sistem şu an güncelleniyor (takip.xlsx dosyası bulunamadı). Lütfen dükkanla iletişime geçiniz.")

# 3. HİZMETLERİMİZ
elif secim == "🛠️ Hizmetlerimiz":
    st.title("Hizmetlerimiz")
    colA, colB = st.columns(2)
    with colA:
        st.image("https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?auto=format&fit=crop&w=600&q=80")
    with colB:
        st.markdown("## 📱 Ekran Değişimi")
        st.write("Orijinal parçalarla 30 dakikada ekran değişimi yapıyoruz.")
        st.markdown("- 6 Ay Garanti\n- Ücretsiz Ekran Koruyucu Hediye")

# 4. GALERİ
elif secim == "🖼️ Galeri":
    st.title("Teknik Servis Galeri")
    st.image(["https://images.unsplash.com/photo-1540553016722-983e48a2cd10?w=400", 
              "https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=400",
              "https://images.unsplash.com/photo-1588508065123-287b28e013da?w=400"], width=300)

# 5. İLETİŞİM
elif secim == "📞 İletişim":
    st.title("İletişim")
    st.success("📍 Adres: Sakarya Mah. Atatürk Cd. No:35 Görükle/Bursa")
    st.info("📞 Tel: 0530 872 59 79")
    st.markdown("### Konumumuz")
    st.image("https://via.placeholder.com/800x400/16181a/2ecc71?text=Harita+Buraya+Gelecek")

# YÜZEN WHATSAPP BUTONU
st.markdown("""
<a href="https://wa.me/905308725979" class="wa-link">
    💬 WhatsApp'tan Fiyat Al
</a>
""", unsafe_allow_html=True)