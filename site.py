"""
GÖRÜKLE AMANOS GSM - TAM TEŞEKKÜLLÜ WEB UYGULAMASI
Sürüm: 3.0 (Enterprise)
Geliştirici: Kodlama Desteği (Yapay Zeka Asistanı)
Açıklama: Bu dosya SQLite veritabanı, şifreli Admin paneli, gelişmiş CSS animasyonları
ve modüler sayfa yapısı içeren tam kapsamlı bir Streamlit uygulamasıdır.
"""

# ==========================================
# 1. KÜTÜPHANELERİN İÇE AKTARILMASI
# ==========================================
import streamlit as st
import sqlite3 # Gerçek veritabanı işlemleri için
import pandas as pd
from datetime import datetime # Tarih ve saat kayıtları için
import time # Animasyon efektleri için

# ==========================================
# 2. SAYFA YAPILANDIRMASI
# ==========================================
# Bu ayar sayfanın genel genişliğini ve tarayıcıdaki ismini belirler. İlk sırada olmalıdır.
st.set_page_config(page_title="Görükle Amanos GSM | Kurumsal Servis", page_icon="⚙️", layout="wide")

# ==========================================
# 3. VERİTABANI (DATABASE) FONKSİYONLARI
# ==========================================
# Geleneksel Excel yerine çok daha hızlı ve güvenli olan SQLite kullanıyoruz.

def veritabani_olustur():
    """Veritabanını ve gerekli tabloları oluşturur. (Eğer yoksa)"""
    conn = sqlite3.connect('amanos_gsm.db')
    c = conn.cursor()
    # Cihaz Takip Tablosu
    c.execute('''CREATE TABLE IF NOT EXISTS cihaz_takip 
                 (takip_no TEXT PRIMARY KEY, musteri_adi TEXT, cihaz_modeli TEXT, durum TEXT, tarih TEXT)''')
    # İletişim/Servis Formu Tablosu
    c.execute('''CREATE TABLE IF NOT EXISTS mesajlar 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, isim TEXT, tel TEXT, konu TEXT, mesaj TEXT, tarih TEXT)''')
    conn.commit()
    conn.close()

def cihaz_ekle(takip_no, musteri, cihaz, durum):
    """Admin panelinden veritabanına yeni bir cihaz ekler."""
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M")
    conn = sqlite3.connect('amanos_gsm.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO cihaz_takip VALUES (?, ?, ?, ?, ?)", (takip_no, musteri, cihaz, durum, tarih))
        conn.commit()
        basari = True
    except sqlite3.IntegrityError: # Eğer aynı takip numarası zaten varsa hata vermesini engelleriz.
        basari = False
    conn.close()
    return basari

def cihaz_durum_guncelle(takip_no, yeni_durum):
    """Mevcut bir cihazın tamir durumunu günceller."""
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M")
    conn = sqlite3.connect('amanos_gsm.db')
    c = conn.cursor()
    c.execute("UPDATE cihaz_takip SET durum = ?, tarih = ? WHERE takip_no = ?", (yeni_durum, tarih, takip_no))
    conn.commit()
    conn.close()

def cihaz_sorgula(takip_no):
    """Müşterinin girdiği numaraya göre cihazı veritabanında arar."""
    conn = sqlite3.connect('amanos_gsm.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cihaz_takip WHERE takip_no=?", (takip_no,))
    veri = c.fetchone()
    conn.close()
    return veri

def mesaj_kaydet(isim, tel, konu, mesaj):
    """Müşterinin iletişim formundan gönderdiği mesajı veritabanına yazar."""
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M")
    conn = sqlite3.connect('amanos_gsm.db')
    c = conn.cursor()
    c.execute("INSERT INTO mesajlar (isim, tel, konu, mesaj, tarih) VALUES (?, ?, ?, ?, ?)", (isim, tel, konu, mesaj, tarih))
    conn.commit()
    conn.close()

# Sistemi başlatırken veritabanı tablolarını hazırla
veritabani_olustur()

# ==========================================
# 4. CSS İLE GELİŞMİŞ GÖRSEL TASARIM
# ==========================================
st.markdown("""
<style>
    /* Genel Uygulama Teması */
    .stApp { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', Tahoma, sans-serif; }
    
    /* Menü Çubuğu (Sidebar) */
    section[data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #30363d; }
    
    /* Global Başlıklar ve Yeşil Çizgi */
    h1, h2, h3 { color: #ffffff !important; }
    .baslik-cizgisi { width: 80px; height: 4px; background-color: #2ea043; margin-bottom: 30px; border-radius: 2px; }

    /* Hizmet ve Bilgi Kartları (Gölge ve Animasyonlu) */
    .bilgi-karti {
        background-color: #21262d;
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #30363d;
        border-left: 5px solid #2ea043;
        transition: all 0.3s ease;
        margin-bottom: 25px;
    }
    .bilgi-karti:hover { transform: translateY(-5px); box-shadow: 0 8px 24px rgba(46, 160, 67, 0.2); border-color: #2ea043; }
    
    /* Başarı/Durum Kutuları */
    .durum-kutusu { background: linear-gradient(135deg, #2ea043 0%, #238636 100%); padding: 20px; border-radius: 10px; color: white; text-align: center; }

    /* Standart Streamlit Butonlarını Ezme (Override) */
    div.stButton > button:first-child { background-color: #238636; color: white; border: 1px solid rgba(240, 246, 252, 0.1); border-radius: 6px; font-weight: 600; padding: 10px 20px; width: 100%; transition: 0.2s; }
    div.stButton > button:first-child:hover { background-color: #2ea043; border-color: #8b949e; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 5. MODÜLER SAYFA FONKSİYONLARI
# ==========================================
# Her sayfayı bir fonksiyon (def) olarak tanımlıyoruz. Bu, kodun 10-15 sayfa
# uzunluğunda karmaşık projelere genişletilmesini sağlayan profesyonel bir standarttır.

def sayfa_ana_sayfa():
    """Sitenin karşılama sayfası."""
    col_yazi, col_resim = st.columns([1.2, 1])
    with col_yazi:
        st.markdown("<h1 style='font-size:3.5rem; line-height: 1.2;'>Profesyonel <br><span style='color:#2ea043;'>Teknik Servis</span> Merkezi</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:1.2rem; color:#8b949e;'>Görükle Amanos GSM olarak cihazlarınızı yüksek teknoloji laboratuvarımızda, uzman mühendislik yaklaşımlarıyla hayata döndürüyoruz.</p>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style='display:flex; gap:20px; margin-top:30px;'>
            <div style='background-color:#21262d; padding:15px; border-radius:8px; border:1px solid #30363d;'><h3 style='margin:0; color:#2ea043;'>15+</h3><small>Yıllık Tecrübe</small></div>
            <div style='background-color:#21262d; padding:15px; border-radius:8px; border:1px solid #30363d;'><h3 style='margin:0; color:#2ea043;'>%100</h3><small>Orijinal Parça</small></div>
            <div style='background-color:#21262d; padding:15px; border-radius:8px; border:1px solid #30363d;'><h3 style='margin:0; color:#2ea043;'>6 Ay</h3><small>Servis Garantisi</small></div>
        </div>
        """, unsafe_allow_html=True)
    with col_resim:
        st.image("https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?auto=format&fit=crop&w=800&q=80", use_container_width=True)

def sayfa_hizmetler():
    """Detaylı hizmetler sayfası (Sekmeli Yapı)."""
    st.markdown("<h1>Uzmanlık Alanlarımız</h1><div class='baslik-cizgisi'></div>", unsafe_allow_html=True)
    
    # st.tabs ile içeriği kategorize ediyoruz
    tab_ekran, tab_batarya, tab_anakart = st.tabs(["📱 Ekran & Cam İşlemleri", "🔋 Batarya Sistemleri", "💻 Mikro-Lehim & Anakart"])
    
    with tab_ekran:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='bilgi-karti'><h3>Ekran Revizyonu ve Değişimi</h3><p>Dış camı kırık ancak iç ekranı sağlam cihazlarda maliyetli ekran değişimi yerine, endüstriyel pres makineleri ile sadece ön cam değişimi uyguluyoruz. Komple hasarlarda ise True-Tone aktarımlı orijinal ekran montajı gerçekleştirilir.</p></div>", unsafe_allow_html=True)
        with col2:
            st.image("https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600", use_container_width=True)
            
    with tab_batarya:
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://images.unsplash.com/photo-1625842268584-8f3bf9ff16a0?w=600", use_container_width=True)
        with col2:
            st.markdown("<div class='bilgi-karti'><h3>Hücre Yenileme ve Batarya Testi</h3><p>Pil döngüsü (cycle count) dolmuş bataryaların yerine amper değeri yüksek, onaylı piller takılır. Cihazın güç akımı ölçülerek gizli kaçaklar (kısa devre) varsa tespit edilir.</p></div>", unsafe_allow_html=True)

    with tab_anakart:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='bilgi-karti'><h3>Entegre ve Çip Seviyesi Onarım</h3><p>Açılmayan, şarj almayan veya sıvıya maruz kalmış cihazlar termal kameralar ve osiloskop cihazları ile incelenir. Hasarlı mikroskobik parçalar yenisiyle değiştirilip cihazın anakartı kurtarılır.</p></div>", unsafe_allow_html=True)
        with col2:
            st.image("https://images.unsplash.com/photo-1597733336794-12d05021d510?w=600", use_container_width=True)

def sayfa_cihaz_sorgulama():
    """SQLite veritabanı ile canlı cihaz durumu okuma sayfası."""
    st.markdown("<h1>Cihaz Durum Sorgulama Merkezi</h1><div class='baslik-cizgisi'></div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8b949e;'>Servis formunuzda yer alan 4 haneli PIN numarasını girerek onarım sürecini canlı takip edebilirsiniz.</p>", unsafe_allow_html=True)
    
    takip_kodu = st.text_input("Takip Numarasını Giriniz (Örn: 1001)", max_chars=10)
    
    if st.button("Sistemde Ara 🔍"):
        if takip_kodu:
            with st.spinner('Veritabanına güvenli bağlantı kuruluyor...'):
                time.sleep(1) # Gerçekçi bir sorgu süresi animasyonu
                
            sonuc = cihaz_sorgula(takip_kodu)
            
            if sonuc:
                # Veritabanından gelen veriler: 0:takip_no, 1:musteri, 2:cihaz, 3:durum, 4:tarih
                st.markdown(f"""
                <div class='durum-kutusu'>
                    <h2 style='color:white; margin-bottom:5px;'>📱 {sonuc[2]}</h2>
                    <p style='margin:0; opacity:0.8;'>Sayın {sonuc[1]} adlı müşterimizin cihazı</p>
                    <hr style='border-color:rgba(255,255,255,0.2);'>
                    <h1 style='color:white;'>{sonuc[3]}</h1>
                    <small>Son Güncelleme: {sonuc[4]}</small>
                </div>
                """, unsafe_allow_html=True)
                
                # İlerleme Çubuğu Mantığı (Görsel Zenginlik)
                if "Teslim" in sonuc[3]:
                    st.progress(100)
                elif "Tamir" in sonuc[3] or "Onarım" in sonuc[3]:
                    st.progress(60)
                else:
                    st.progress(25)
            else:
                st.error("Sistemde bu numaraya ait güncel bir kayıt bulunamadı.")
        else:
            st.warning("Lütfen geçerli bir takip numarası yazınız.")

def sayfa_iletisim_ve_form():
    """Müşteri veri girişi ve veritabanına yazma sayfası."""
    st.markdown("<h1>İletişim ve Servis Talebi</h1><div class='baslik-cizgisi'></div>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='bilgi-karti'>", unsafe_allow_html=True)
        st.markdown("### 📋 Online Arıza Kayıt Formu")
        with st.form("ariza_kayit"):
            isim = st.text_input("Adınız ve Soyadınız")
            tel = st.text_input("Telefon Numaranız")
            konu = st.selectbox("Arıza Kategorisi", ["Ekran/Cam Kırık", "Batarya Sorunu", "Cihaz Açılmıyor", "Sıvı Teması", "Diğer"])
            mesaj = st.text_area("Cihazın Şikayetini Kısaca Belirtiniz")
            
            if st.form_submit_button("Talebi Veritabanına İlet"):
                if isim and tel:
                    mesaj_kaydet(isim, tel, konu, mesaj)
                    st.success("Talebiniz güvenli bir şekilde sunucularımıza kaydedildi. Uzmanlarımız size dönüş yapacaktır.")
                else:
                    st.error("Ad ve telefon alanlarının doldurulması zorunludur.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with c2:
        st.markdown("<div class='bilgi-karti'>", unsafe_allow_html=True)
        st.markdown("### 📍 İletişim Bilgilerimiz")
        st.markdown("**Adres:** Sakarya Mah. Atatürk Cd. Yerleşim Plaza C Blok No: 35 Görükle / Bursa")
        st.markdown("**Müşteri Hizmetleri:** 0530 872 59 79")
        st.markdown("**Çalışma Saatleri:** 09:00 - 22:00")
        st.markdown("---")
        st.markdown("Aşağıdaki butona tıklayarak doğrudan teknik personelimizle anlık mesajlaşma başlatabilirsiniz.")
        st.markdown("<a href='https://wa.me/905308725979' style='display:block; text-align:center; background-color:#25d366; color:white; padding:10px; border-radius:5px; text-decoration:none; font-weight:bold;'>WhatsApp Destek Hattına Bağlan</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

def sayfa_admin_paneli():
    """Sadece dükkan sahibinin şifreyle girebildiği, veritabanı yönetim paneli."""
    st.markdown("<h1>⚙️ Gelişmiş Yönetici Paneli</h1><div class='baslik-cizgisi'></div>", unsafe_allow_html=True)
    
    # Basit bir oturum (Session State) kontrolü yapıyoruz.
    if "admin_giris" not in st.session_state:
        st.session_state["admin_giris"] = False

    if not st.session_state["admin_giris"]:
        sifre = st.text_input("Sisteme erişmek için yönetici şifresini giriniz:", type="password")
        if st.button("Giriş Yap"):
            if sifre == "amanos123": # Yönetici şifreniz (Değiştirebilirsiniz)
                st.session_state["admin_giris"] = True
                st.rerun() # Sayfayı yenile ve içeriği göster
            else:
                st.error("Hatalı şifre. Yetkisiz erişim denemesi kaydedildi.")
    
    if st.session_state["admin_giris"]:
        st.success("Güvenli yönetici oturumu açıldı.")
        
        tab_cihazlar, tab_mesajlar = st.tabs(["📲 Cihaz Takip Yönetimi", "📬 Gelen Müşteri Talepleri"])
        
        with tab_cihazlar:
            st.markdown("### Sisteme Yeni Cihaz Ekle")
            with st.form("yeni_cihaz_ekle"):
                c_no = st.text_input("Oluşturulacak Takip No (Örn: 1001)")
                c_ad = st.text_input("Müşteri Adı")
                c_mod = st.text_input("Cihaz Marka/Model")
                c_durum = st.selectbox("Başlangıç Durumu", ["İşleme Alındı", "Arıza Tespiti Yapılıyor", "Parça Bekliyor", "Onarımda", "Tamamlandı - Teslime Hazır"])
                
                if st.form_submit_button("Cihazı Veritabanına Kaydet"):
                    if c_no and c_ad:
                        if cihaz_ekle(c_no, c_ad, c_mod, c_durum):
                            st.success(f"{c_no} numaralı cihaz başarıyla eklendi.")
                        else:
                            st.error("Bu takip numarası sistemde zaten var! Başka bir numara deneyin.")
                    else:
                        st.warning("Numara ve Müşteri Adı boş bırakılamaz.")
            
            st.markdown("---")
            st.markdown("### Mevcut Cihazları Görüntüle ve Güncelle")
            # Pandas kütüphanesi ile SQL'den tüm cihazları çekip tablo olarak gösteriyoruz
            conn = sqlite3.connect('amanos_gsm.db')
            df = pd.read_sql_query("SELECT * FROM cihaz_takip", conn)
            conn.close()
            st.dataframe(df, use_container_width=True)
            
            # Durum Güncelleme Alanı
            st.markdown("#### Durum Güncelle")
            guncellenecek_no = st.selectbox("Durumu güncellenecek cihazı seçin:", df['takip_no'].tolist() if not df.empty else ["Cihaz Yok"])
            yeni_durum = st.text_input("Yeni durum mesajını yazın (Örn: Ekran siparişi verildi)")
            if st.button("Durumu Güncelle"):
                if guncellenecek_no != "Cihaz Yok" and yeni_durum:
                    cihaz_durum_guncelle(guncellenecek_no, yeni_durum)
                    st.success("Durum başarıyla güncellendi!")
                    st.rerun()

        with tab_mesajlar:
            st.markdown("### Web Sitesinden Gelen Mesajlar")
            conn = sqlite3.connect('amanos_gsm.db')
            df_mesajlar = pd.read_sql_query("SELECT id as ID, isim as Müşteri, tel as Telefon, konu as Konu, mesaj as Mesaj, tarih as Tarih FROM mesajlar ORDER BY id DESC", conn)
            conn.close()
            
            if not df_mesajlar.empty:
                st.dataframe(df_mesajlar, use_container_width=True)
            else:
                st.info("Henüz web sitesi üzerinden gönderilmiş bir mesaj bulunmuyor.")
                
        if st.button("Güvenli Çıkış Yap"):
            st.session_state["admin_giris"] = False
            st.rerun()

# ==========================================
# 6. ANA KONTROL BLOĞU (UYGULAMANIN ÇALIŞMA MANTIĞI)
# ==========================================
# Uygulamanın kalbi burasıdır. Sol menüden (Sidebar) seçilen değere göre
# yukarıda yazdığımız modüler fonksiyonları çağırır (çalıştırır).

def main():
    # Yan menü yapısı
    with st.sidebar:
        st.image("https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=200", use_container_width=True)
        st.markdown("<h2 style='color:#2ea043; text-align:center;'>AMANOS GSM</h2>", unsafe_allow_html=True)
        st.markdown("---")
        
        # Gezinme (Routing) Sistemi
        secilen_sayfa = st.radio("MENÜ", [
            "🏠 Ana Sayfa", 
            "🛠️ Hizmetlerimiz", 
            "🔍 Cihaz Durum Sorgula", 
            "📞 İletişim Formu",
            "⚙️ Yönetici Girişi (Admin)"
        ])
        st.markdown("---")
    
    # Seçime Göre İlgili Fonksiyonu Tetikleme
    if secilen_sayfa == "🏠 Ana Sayfa":
        sayfa_ana_sayfa()
    elif secilen_sayfa == "🛠️ Hizmetlerimiz":
        sayfa_hizmetler()
    elif secilen_sayfa == "🔍 Cihaz Durum Sorgula":
        sayfa_cihaz_sorgulama()
    elif secilen_sayfa == "📞 İletişim Formu":
        sayfa_iletisim_ve_form()
    elif secilen_sayfa == "⚙️ Yönetici Girişi (Admin)":
        sayfa_admin_paneli()
        
    # Her sayfanın en altına eklenecek ortak alt bilgi (Footer)
    st.markdown("<div style='text-align:center; padding:30px; margin-top:50px; border-top:1px solid #30363d; color:#8b949e;'><small>Görükle Amanos GSM Web Uygulaması Altyapısı v3.0 | SQLite Veritabanı Sistemleri ile Güçlendirilmiştir.</small></div>", unsafe_allow_html=True)

# Kodun sadece doğrudan çalıştırıldığında main() fonksiyonunu çağırmasını sağlayan Python standardı.
if __name__ == "__main__":
    main()