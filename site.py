import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu

# --- SAYFA KONFİGÜRASYONU ---
st.set_page_config(page_title="Görükle Amanos GSM | Profesyonel Teknik Servis", page_icon="📱", layout="wide")

# --- GELİŞMİŞ TASARIM (CSS) ---
st.markdown("""
    <style>
           /* Buton yazılarını her zaman beyaz ve görünür yapar */
    .stButton button p, .stElementAction a, .st-emotion-cache-7ym5gk p {
        color: white !important;
    }
    
    /* WhatsApp ve Harita gibi linkli butonların içindeki metni sabitler */
    a[data-testid="stBaseLinkButton"] span {
        color: white !important;
    /* Genel Arka Plan ve Yazı Rengi */
    .stApp { background-color: #fcfcfc !important; }
    h1, h2, h3, p, span, div, li { color: #0f172a !important; font-family: 'Inter', sans-serif; }
    
    /* Kart Tasarımları */
    .hizmet-kart {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        border-left: 5px solid #1e40af;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    /* İstatistik Kutuları */
    .stat-box {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        color: white !important;
        border-radius: 15px;
    }
    .stat-box h2, .stat-box p { color: white !important; margin: 0; }

    /* Kampanya Alanı */
    .promo-card {
        background: #ef4444;
        color: white !important;
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        border: 2px dashed #ffffff;
    }
    .promo-card h2, .promo-card p { color: white !important; }
    
    /* Takip Sistemi Kutusu */
    .takip-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 25px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST NAVİGASYON MENÜSÜ ---
selected = option_menu(
    menu_title=None,
    options=["Ana Sayfa", "Cihaz Takip", "Hizmetlerimiz", "İletişim"],
    icons=["house-fill", "search", "tools", "envelope-fill"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#ffffff"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "#f1f5f9"},
        "nav-link-selected": {"background-color": "#1e40af"},
    }
)

# ==========================================
#               ANA SAYFA
# ==========================================
if selected == "Ana Sayfa":
    # Hero Section (Giriş)
    col_img, col_txt = st.columns([1, 1.5])
    with col_img:
        if os.path.exists("tabela.jpg"):
            st.image("tabela.jpg", use_container_width=True)
        else:
            st.image("https://via.placeholder.com/600x400.png?text=Amanos+GSM+Görükle", use_container_width=True)
    
    with col_txt:
        st.markdown("<h1 style='font-size: 3rem; margin-bottom:0;'>GÖRÜKLE AMANOS GSM</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.5rem; color: #64748b !important;'>Bursa'nın En Güvenilir Teknik Servis Deneyimi</p>", unsafe_allow_html=True)
        st.write("Cihazınızdaki tüm arızalar için profesyonel ekipman ve orijinal yedek parçalarla hizmetinizdeyiz. Görükle Yerleşim Plaza'da sizleri bekliyoruz.")
        st.link_button("🚀 Hemen Fiyat Al (WhatsApp)", "https://wa.me/905308725979", type="primary")

    st.divider()

    # İstatistikler
    s1, s2, s3, s4 = st.columns(4)
    with s1: st.markdown("<div class='stat-box'><h2>15+</h2><p>Yıllık Deneyim</p></div>", unsafe_allow_html=True)
    with s2: st.markdown("<div class='stat-box'><h2>30 Dak</h2><p>Hızlı Teslim</p></div>", unsafe_allow_html=True)
    with s3: st.markdown("<div class='stat-box'><h2>%100</h2><p>Müşteri Memnuniyeti</p></div>", unsafe_allow_html=True)
    with s4: st.markdown("<div class='stat-box'><h2>6 Ay</h2><p>İşçilik Garantisi</p></div>", unsafe_allow_html=True)

    st.write("##")

    # Kampanya Alanı
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='promo-card'><h2>👨‍🎓 ÖĞRENCİ DOSTU</h2><p>Öğrenci kimliğinle gel, tüm işlemlerde <b>%20 İNDİRİMİ</b> kap!</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='promo-card' style='background: #1e40af;'><h2>🎉 AÇILIŞA ÖZEL</h2><p>İlk ziyaretinizde aksesuar alımlarında <b>%15 İNDİRİM</b> fırsatı!</p></div>", unsafe_allow_html=True)

# ==========================================
#              CİHAZ TAKİP
# ==========================================
elif selected == "Cihaz Takip":
    st.markdown("<h2 style='text-align: center;'>🔍 Cihaz Durumu Sorgulama</h2>", unsafe_allow_html=True)
    st.write("---")
    
    col_left, col_mid, col_right = st.columns([1, 2, 1])
    with col_mid:
        st.markdown("<div class='takip-container'>", unsafe_allow_html=True)
        takip_no = st.text_input("Size verilen 4 haneli takip numarasını giriniz:", placeholder="Örn: 1002")
        
        if takip_no:
            if os.path.exists("takip.xlsx"):
                df = pd.read_excel("takip.xlsx")
                df['takip_no'] = df['takip_no'].astype(str)
                sonuc = df[df['takip_no'] == str(takip_no)]
                
                if not sonuc.empty:
                    st.balloons()
                    st.markdown(f"### 📋 Cihaz Bilgisi: {sonuc['çihaz'].values[0]}")
                    st.info(f"👤 **Müşteri:** {sonuc['isim'].values[0]}")
                    st.warning(f"🛠️ **Yapılan İşlem:** {sonuc['işlem'].values[0]}")
                    st.success(f"✅ **GÜNCEL DURUM:** {sonuc['durum'].values[0]}")
                else:
                    st.error("❌ Kayıt bulunamadı. Lütfen numaranızı kontrol edin.")
            else:
                st.error("Veritabanına şu an ulaşılamıyor.")
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
#              HİZMETLERİMİZ
# ==========================================
elif selected == "Hizmetlerimiz":
    st.header("🛠️ Neler Yapıyoruz?")
    h1, h2 = st.columns(2)
    with h1:
        st.markdown("<div class='hizmet-kart'><h3>📱 Ekran & Ön Cam</h3><p>Orijinal ekran değişimi ve sadece ön camı çatlak cihazlar için presleme yöntemiyle ekonomik çözümler.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='hizmet-kart'><h3>🔋 Batarya Yenileme</h3><p>Pil sağlığı düşmüş cihazlarınız için yüksek kapasiteli ve garantili batarya değişimi.</p></div>", unsafe_allow_html=True)
    with h2:
        st.markdown("<div class='hizmet-kart'><h3>⚙️ Anakart Tamiri</h3><p>Sıvı teması, şarj olmama veya açılmayan cihazlar için mikro-lehimleme yöntemiyle profesyonel onarım.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='hizmet-kart'><h3>🎧 Aksesuar Dünyası</h3><p>En trend kılıflar, kırılmaz camlar ve hızlı şarj adaptörleri en uygun fiyatlarla.</p></div>", unsafe_allow_html=True)

# ==========================================
#               İLETİŞİM
# ==========================================
elif selected == "İletişim":
    i1, i2 = st.columns(2)
    with i1:
        st.header("📍 Adres Bilgilerimiz")
        st.write("Sakarya Mahallesi, Atatürk Caddesi")
        st.write("Yerleşim Plaza Sitesi C Blok No: 35")
        st.write("**Görükle / Bursa**")
        st.caption("(Enes Saat ve Okyanus Bar Yanı)")
        st.write("---")
        st.write("📞 **Telefon:** 0530 872 59 79")
        st.write("⏰ **Hafta İçi:** 08:00 - 22:00")
        st.write("⏰ **Hafta Sonu:** 10:00 - 20:00")
    
    with i2:
        st.header("🗺️ Yol Tarifi")
        st.info("Harita üzerinde bizi bulun ve tek tıkla navigasyonu başlatın.")
        st.link_button("📍 Google Haritalar'da Gör", "https://goo.gl/maps/BURAYA_LINKI_YAPISTIR")
        st.link_button("🟢 WhatsApp'tan Soru Sor", "https://wa.me/905308725979")

# --- FOOTER ---
st.write("##")
st.markdown("<p style='text-align: center; color: #94a3b8 !important;'>© 2026 Görükle Amanos GSM. Tüm Hakları Saklıdır.</p>", unsafe_allow_html=True)