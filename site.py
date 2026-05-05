import streamlit as st

# Sayfa yapılandırması
st.set_page_config(page_title="Amanos GSM | Hizmetlerimiz", layout="wide")

# --- GELİŞMİŞ HİZMET SAYFASI CSS ---
st.markdown("""
<style>
    .stApp { background-color: #0b0d0e; color: #ffffff; }
    
    /* Hizmet Bloğu Konteynırı */
    .hizmet-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 80px 8%;
        gap: 50px;
    }
    
    .hizmet-text { flex: 1; }
    .hizmet-image { flex: 1; text-align: center; }
    .hizmet-image img { 
        max-width: 100%; 
        border-radius: 15px; 
        box-shadow: 0 10px 30px rgba(46, 204, 113, 0.1);
    }

    /* Numara Yuvarlağı */
    .number-circle {
        background-color: #2ecc71;
        color: black;
        width: 35px;
        height: 35px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-bottom: 20px;
    }

    .hizmet-title { font-size: 32px; font-weight: bold; margin-bottom: 15px; text-transform: uppercase; }
    .hizmet-desc { color: #aaa; line-height: 1.6; margin-bottom: 20px; }
    
    /* Liste Maddeleri */
    .hizmet-list { list-style: none; padding: 0; margin-bottom: 25px; }
    .hizmet-list li { margin-bottom: 10px; color: #eee; font-size: 14px; }
    .hizmet-list li::before { content: "• "; color: #2ecc71; font-weight: bold; }

    /* Buton */
    .btn-more {
        background-color: #333;
        color: white !important;
        padding: 10px 25px;
        border-radius: 4px;
        text-decoration: none;
        font-size: 12px;
        font-weight: bold;
        transition: 0.3s;
        border: 1px solid #444;
    }
    .btn-more:hover { background-color: #2ecc71; color: black !important; border-color: #2ecc71; }
</style>
""", unsafe_allow_html=True)

# --- 1. EKRAN DEĞİŞİMİ ---
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="hizmet-text">
        <div class="number-circle">1</div>
        <div class="hizmet-title">EKRAN DEĞİŞİMİ</div>
        <p class="hizmet-desc">AMANOS GSM servis cihazınızın ekranını orijinal olarak değiştirerek sorunsuz çalışmasını sağlar.</p>
        <p><strong>Ekranın Kırılma Nedenleri:</strong></p>
        <ul class="hizmet-list">
            <li>Telefonun darbe alması</li>
            <li>Yüksekten düşme</li>
            <li>Üzerine oturma</li>
        </ul>
        <a href="#" class="btn-more">DEVAMINI OKU ></a>
    </div>
    """, unsafe_allow_html=True)
with col2:
    # Buraya elinde olan kırık ekranlı telefon resmini koyabilirsin
    st.image("https://via.placeholder.com/500x400/1a1d1f/2ecc71?text=Ekran+Degisimi+Gorseli", use_container_width=True)

st.markdown("<hr style='border-color: #222;'>", unsafe_allow_html=True)

# --- 2. BATARYA DEĞİŞİMİ (Ters Düzen) ---
col3, col4 = st.columns(2)
with col3:
    st.image("https://via.placeholder.com/500x400/1a1d1f/2ecc71?text=Batarya+Tamiri+Gorseli", use_container_width=True)
with col4:
    st.markdown("""
    <div class="hizmet-text">
        <div class="number-circle">2</div>
        <div class="hizmet-title">BATARYA DEĞİŞİMİ</div>
        <p class="hizmet-desc">Bataryanızın ömrü bitmişse cihazdan yeteri kadar performans almanız mümkün değildir.</p>
        <ul class="hizmet-list">
            <li>Pil göstergesi %100 olmasına rağmen aniden kapanma</li>
            <li>Pil sağlığının %80 altına düşmesi</li>
            <li>Cihazda donma ve yavaşlama</li>
        </ul>
        <a href="#" class="btn-more">DEVAMINI OKU ></a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border-color: #222;'>", unsafe_allow_html=True)

# --- 3. ANAKART TAMİRİ ---
col5, col6 = st.columns(2)
with col5:
    st.markdown("""
    <div class="hizmet-text">
        <div class="number-circle">3</div>
        <div class="hizmet-title">ANAKART TAMİRİ</div>
        <p class="hizmet-desc">Amanos GSM güvencesiyle iPhone ve diğer marka telefonlarınızın anakart tamiri ile cihazınızı hayata döndürün.</p>
        <ul class="hizmet-list">
            <li>Sıvı teması sonrası oluşan kısa devreler</li>
            <li>Entegre ve mikro-çip değişimleri</li>
            <li>Şebeke ve WiFi sorunları onarımı</li>
        </ul>
        <a href="#" class="btn-more">DEVAMINI OKU ></a>
    </div>
    """, unsafe_allow_html=True)
with col6:
    st.image("https://via.placeholder.com/500x400/1a1d1f/2ecc71?text=Anakart+Tamiri+Gorseli", use_container_width=True)