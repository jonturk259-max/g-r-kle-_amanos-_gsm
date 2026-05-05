import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Görükle Amanos GSM | Kurumsal Teknik Servis", page_icon="📱", layout="wide")

# --- PREMIUM CSS TASARIMI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

    /* Genel Arka Plan ve Yazı Tipi */
    .stApp { background-color: #f1f5f9 !important; }
    * { font-family: 'Inter', sans-serif !important; }
    
    /* Tüm Yazı Renklerini Siyah/Koyu Gri Sabitleme */
    h1, h2, h3, p, span, li, div { color: #0f172a !important; }

    /* Üst Alan (Hero) */
    .hero-container {
        background-color: white;
        padding: 3rem;
        border-radius: 2rem;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }

    /* Buton Yazılarını Beyaz Yapma (Zorunlu) */
    .stButton button p, 
    button[data-testid="stBaseLinkButton"] p, 
    button[data-testid="stBaseLinkButton"] span {
        color: white !important;
        font-weight: 700 !important;
    }

    /* Hizmet Kartları */
    .premium-card {
        background: white;
        padding: 2rem;
        border-radius: 1.5rem;
        border: 1px solid #e2e8f0;
        transition: transform 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .premium-card:hover { transform: translateY(-5px); border-color: #3b82f6; }

    /* İstatistik Paneli */
    .stat-panel {
        background: #1e293b;
        padding: 2.5rem;
        border-radius: 2rem;
        text-align: center;
        margin: 2rem 0;
    }
    .stat-panel h2, .stat-panel p { color: white !important; }

    /* Kampanya Bandı */
    .promo-banner {
        background: linear-gradient(135deg, #ef4444 0%, #b91c1c 100%);
        color: white !important;
        padding: 1.5rem;
        border-radius: 1rem;
        text-align: center;
        border: 2px dashed rgba(255,255,255,0.4);
    }
    .promo-banner h3, .promo-banner p { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- MODERN ÜST MENÜ ---
selected = option_menu(
    menu_title=None,
    options=["Ana Sayfa", "Cihaz Takip", "Hizmetlerimiz", "İletişim"],
    icons=["house-door-fill", "search-heart", "cpu-fill", "map-fill"],
    orientation="horizontal",
    styles={
        "container": {"background-color": "white", "border-radius": "1rem", "padding": "0.5rem"},
        "nav-link-selected": {"background-color": "#2563eb", "color": "white"},
    }
)

# ==========================================
#               ANA SAYFA
# ==========================================
if selected == "Ana Sayfa":
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1.2])
    with c1:
        if os.path.exists("tabela.jpg"):
            st.image("tabela.jpg", use_container_width=True)
        else:
            st.markdown("<h1 style='font-size: 5rem;'>📱</h1>", unsafe_allow_html=True)
    with c2:
        st.markdown("<h1 style='font-size: 3.5rem; line-height: 1;'>Görükle Amanos GSM</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.5rem; color: #475569 !important;'>Teknolojiniz Bizimle Güvende</p>", unsafe_allow_html=True)
        st.write("Bursa'nın en gelişmiş teknik servis altyapısıyla tanışın. Sadece tamir etmiyoruz, cihazınızı ilk günkü performansına kavuşturuyoruz.")
        st.link_button("🚀 Hızlı Teklif Al", "https://wa.me/905308725979")
    st.markdown("</div>", unsafe_allow_html=True)

    # İstatistikler
    st.markdown("""
        <div class='stat-panel'>
            <div style='display: flex; justify-content: space-around; flex-wrap: wrap;'>
                <div><h2 style='font-size: 3rem;'>15+</h2><p>Yıllık Tecrübe</p></div>
                <div><h2 style='font-size: 3rem;'>10k</h2><p>Mutlu Müşteri</p></div>
                <div><h2 style='font-size: 3rem;'>30dk</h2><p>Ortalama Teslim</p></div>
                <div><h2 style='font-size: 3rem;'>%100</h2><p>Müşteri Memnuniyeti</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Kampanya
    st.markdown("""
        <div class='promo-banner'>
            <h3 style='margin:0;'>🎓 GÖRÜKLE ÖĞRENCİLERİNE ÖZEL</h3>
            <p style='margin:0;'>Öğrenci kimliğini gösteren herkese tüm teknik işlemlerde net %20 İndirim!</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
#              CİHAZ TAKİP
# ==========================================
elif selected == "Cihaz Takip":
    st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Cihaz Durumu Sorgulama</h2>", unsafe_allow_html=True)
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("<div style='background: white; padding: 2.5rem; border-radius: 2rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);'>", unsafe_allow_html=True)
        takip_no = st.text_input("Size verilen takip numarasını giriniz:", placeholder="Örn: 1002")
        if takip_no:
            if os.path.exists("takip.xlsx"):
                df = pd.read_excel("takip.xlsx")
                df['takip_no'] = df['takip_no'].astype(str)
                res = df[df['takip_no'] == str(takip_no)]
                if not res.empty:
                    st.balloons()
                    st.success(f"📱 **Cihaz:** {res['çihaz'].values[0]}")
                    st.info(f"👤 **Müşteri:** {res['isim'].values[0]}")
                    st.warning(f"✅ **GÜNCEL DURUM:** {res['durum'].values[0]}")
                else:
                    st.error("Üzgünüz, bu numara ile eşleşen bir kayıt bulunamadı.")
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
#              HİZMETLERİMİZ
# ==========================================
elif selected == "Hizmetlerimiz":
    st.header("Sizin İçin Neler Yapıyoruz?")
    h1, h2 = st.columns(2)
    with h1:
        st.markdown("<div class='premium-card'><h3>🔬 Mikro-Lehimleme</h3><p>Anakart üzerindeki en hassas entegre ve şarj soketi tamirlerini mikroskop altında gerçekleştiriyoruz.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='premium-card'><h3>📱 Ekran & Cam Yenileme</h3><p>Ekranınızı komple değiştirmek yerine, sadece dış camı değiştirerek maliyetinizi yarıya düşürüyoruz.</p></div>", unsafe_allow_html=True)
    with h2:
        st.markdown("<div class='premium-card'><h3>🔋 Batarya Performansı</h3><p>Cihazınızın ömrünü uzatmak için yüksek kapasiteli ve gerçek garantili pil değişimleri yapıyoruz.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='premium-card'><h3>💧 Sıvı Teması Müdahalesi</h3><p>Sıvı teması alan cihazlarınızı ultrasonik temizleme yöntemleriyle kurtarıyoruz.</p></div>", unsafe_allow_html=True)

# ==========================================
#               İLETİŞİM
# ==========================================
elif selected == "İletişim":
    i1, i2 = st.columns(2)
    with i1:
        st.header("Mağazamıza Bekliyoruz")
        st.write("📍 **Adres:** Sakarya Mah. Atatürk Cad. Yerleşim Plaza C Blok No:35 (Görükle/Bursa)")
        st.write("📞 **WhatsApp/Tel:** 0530 872 59 79")
        st.write("⏰ **Çalışma:** 09:00 - 22:00 (Haftanın Her Günü)")
    with i2:
        st.header("Hızlı Navigasyon")
        st.link_button("🗺️ Google Haritalar'da Aç", "https://goo.gl/maps/BURAYA_LINKI_YAPISTIR")
        st.link_button("💬 WhatsApp Destek", "https://wa.me/905308725979")

st.divider()
st.markdown("<p style='text-align: center; opacity: 0.7;'>© 2026 Görükle Amanos GSM - Profesyonel Teknik Servis Merkezi</p>", unsafe_allow_html=True)