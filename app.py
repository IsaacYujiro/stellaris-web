import streamlit as st
import pandas as pd
import datetime
import time
import os
import glob

# ==============================================================================
# SİTE YAPILANDIRMASI VE GELİŞMİŞ CSS (GÜVENLİ MENÜ, EMOJİSİZ, KOYU ALTIN)
# ==============================================================================
st.set_page_config(page_title="Stellaris | Premium Astro-Tourism", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&family=Cinzel:wght@400;600;700&display=swap');

    html, body, [class*="css"] { 
        font-family: 'Montserrat', sans-serif; 
        background-color: #02060D; 
        color: #C5A059; 
        text-align: center; 
    }

    [data-testid="stSidebar"] { 
        background-color: #02060D !important; 
        border-right: 1px solid #B8860B !important; 
    }

    /* --- GÜVENLİ MENÜ KODU (TİKLERİ BOZMADAN GİZLE) --- */
    div[role="radiogroup"] > label > div:first-of-type {
        display: none !important; 
    }
    
    div[role="radiogroup"] p {
        color: #B8860B !important; 
        font-family: 'Cinzel', serif !important;
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        text-align: center !important;
        visibility: visible !important;
        display: block !important;
        width: 100%;
        margin-top: 5px;
        transition: all 0.3s ease;
    }

    div[role="radiogroup"] label:hover p {
        color: #D4AF37 !important;
        text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.4);
    }
    div[role="radiogroup"] label[aria-checked="true"] p {
        color: #D4AF37 !important;
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.8);
        border-bottom: 1px solid #B8860B;
    }

    [data-testid="stSidebar"] .stAlert div { 
        font-family: 'Montserrat', sans-serif !important; color: #B8860B !important; text-align: center !important; background-color: transparent !important; border: 1px solid #B8860B;
    }
    [data-testid="stSidebarCollapseButton"] span, .material-symbols-rounded { font-family: "Material Symbols Rounded" !important; color: #B8860B !important; }

    h1, h2, h3, h4, h5, h6 { 
        font-family: 'Cinzel', serif; color: #B8860B !important; font-weight: 600; text-align: center !important; width: 100%; text-shadow: 0px 0px 15px rgba(184, 134, 11, 0.2);
    }
    p { text-align: center !important; margin: 0 auto 15px auto !important; max-width: 800px; line-height: 1.8; }
    hr { border-top: 1px solid #B8860B !important; opacity: 0.3; width: 60%; margin: 40px auto !important; }

    .block-container { animation: fadeIn 1.2s ease-out; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }

    .hero-image { 
        width: 100%; max-width: 1200px; height: 50vh; object-fit: cover; 
        border-radius: 4px; filter: brightness(45%); 
        border: 2px solid #B8860B; 
        animation: slowZoom 25s infinite alternate linear;
    }
    @keyframes slowZoom { from { transform: scale(1); } to { transform: scale(1.05); } }
    .hero-container { position: relative; text-align: center; margin-bottom: 40px; display: flex; justify-content: center; overflow: hidden; }

    .service-card { 
        background: #02060D; border-radius: 8px; padding: 0; margin: 0 auto 30px auto; 
        box-shadow: 0 4px 20px rgba(0,0,0,0.9); transition: transform 0.4s ease, box-shadow 0.4s ease; 
        border: 1px solid #B8860B; overflow: hidden; height: 100%; max-width: 500px;
        animation: float 6s ease-in-out infinite;
    }
    @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-8px); } 100% { transform: translateY(0px); } }
    .service-card:hover { animation-play-state: paused; transform: scale(1.02); box-shadow: 0 10px 30px rgba(184, 134, 11, 0.3); }

    .hero-title { font-size: 5rem; font-family: 'Cinzel', serif; margin-bottom: 10px; letter-spacing: 6px; color: #B8860B !important; text-shadow: 0px 0px 25px rgba(184, 134, 11, 0.5); }
    .hero-subtitle { font-size: 1.2rem; font-weight: 300; letter-spacing: 5px; text-transform: uppercase; color: #C5A059 !important; margin-top: 15px !important; }
    .service-img { width: 100%; height: 220px; object-fit: cover; border-bottom: 1px solid #B8860B; }
    .service-content { padding: 30px; text-align: center; }
    .service-title { font-size: 1.4rem; margin-bottom: 15px; color: #B8860B; font-family: 'Cinzel', serif; text-align: center; }
    .service-desc { font-size: 0.95rem; color: #C5A059; text-align: center; }
    .price-tag { font-family: 'Cinzel', serif; font-size: 3rem; color: #B8860B; font-weight: 700; margin: 25px 0; text-align: center; text-shadow: 0px 0px 10px rgba(184, 134, 11, 0.3); }
    
    .stButton { display: flex; justify-content: center; margin-top: 20px; }
    div.stButton > button:first-child { background-color: #02060D !important; color: #B8860B !important; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 1.1rem; padding: 15px 50px; border: 1px solid #B8860B !important; border-radius: 2px; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); letter-spacing: 2px; text-transform: uppercase; }
    div.stButton > button:first-child:hover { background-color: #B8860B !important; color: #02060D !important; transform: scale(1.05); box-shadow: 0 0 20px rgba(184, 134, 11, 0.4); }

    [data-baseweb="tab-list"] { justify-content: center; gap: 20px; }
    [data-baseweb="tab"] { background-color: transparent !important; color: #C5A059 !important; font-family: 'Cinzel', serif; font-size: 1.2rem; }
    [aria-selected="true"] { color: #B8860B !important; border-bottom: 2px solid #B8860B !important; font-weight: bold; }
    .streamlit-expanderHeader { font-family: 'Cinzel', serif; color: #B8860B !important; text-align: center; font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# AKILLI LOGO BULUCU
# ==============================================================================
bulunan_logo = None
resimler = glob.glob("*.jpeg") + glob.glob("*.jpg") + glob.glob("*.png")
if resimler:
    bulunan_logo = resimler[0]

# ==============================================================================
# SİDEBAR (SOL MENÜ) NAVİGASYONU
# ==============================================================================
if bulunan_logo:
    st.sidebar.image(bulunan_logo, use_container_width=True)
else:
    st.sidebar.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin-top: 20px; color: #B8860B;'>Stellaris</h2>", unsafe_allow_html=True)

st.sidebar.write("---")

menu_secimi = st.sidebar.radio(
    "GizliNavigasyonBasligi",
    ["ANA SAYFA", "LOKASYONLARIMIZ", "DENEYİMLER & REZERVASYON", "ASTRO-GASTRONOMİ", "SÜRDÜRÜLEBİLİRLİK", "YATIRIMCI PORTALI"],
    label_visibility="collapsed"
)

st.sidebar.write("---")
st.sidebar.info("Sistem Durumu: Çevrimiçi")

# ==============================================================================
# SAYFA 1: ANA SAYFA
# ==============================================================================
if menu_secimi == "ANA SAYFA":
    col_space1, col_hero, col_space3 = st.columns([1, 2, 1])
    with col_hero:
        if bulunan_logo:
            st.image(bulunan_logo, use_container_width=True)
        else:
            st.markdown("<h1 class='hero-title'>STELLARIS</h1>", unsafe_allow_html=True)
            st.markdown("<p class='hero-subtitle'>Global Astro-Turizm Lideri</p>", unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("<h2>Gökyüzünün Sınırlarını Keşfedin</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p>
    Stellaris, sıradan tatil anlayışını geride bırakıp gözlerini evrenin derinliklerine çevirenler için doğdu. Işık kirliliğinden tamamen arınmış dünyanın en karanlık ve en berrak noktalarında, bilim ve doğayı kusursuz bir lüksle harmanlıyoruz. Gece gözlem turlarımız ve premium konaklama seçeneklerimizle yıldızların altında unutulmaz bir hikaye yazın.
    </p>
    """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("<h2>Sinematik Marka Vizyonu</h2>", unsafe_allow_html=True)
    
    col_space1, col_image, col_space2 = st.columns([1, 8, 1])
    with col_image:
        # Video yerine yüksek çözünürlüklü derin uzay fotoğrafı (Animasyonlu)
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:45vh; filter: brightness(60%);" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=2000&auto=format&fit=crop"></div>', unsafe_allow_html=True)

# ==============================================================================
# SAYFA 2: LOKASYONLARIMIZ
# ==============================================================================
elif menu_secimi == "LOKASYONLARIMIZ":
    st.markdown("<h2>Hedef Ülkeler ve Küresel Pazar</h2>", unsafe_allow_html=True)
    st.markdown("<p>Evrenin en muazzam manzaralarını sunan stratejik karanlık gökyüzü rezervleri.</p>", unsafe_allow_html=True)
    st.write("---")
    
    col_space1, col_chile, col_nz, col_space2 = st.columns([1, 4, 4, 1])
    with col_chile:
        st.markdown(f"""
        <div class="service-card">
            <img class="service-img" src="https://images.unsplash.com/photo-1549429712-16fc9ebfc4b9?q=80&w=800&auto=format&fit=crop">
            <div class="service-content">
                <h3 class="service-title">Atacama Çölü, Şili</h3>
                <p class="service-desc">Yılda 300'den fazla açık ve bulutsuz gece. Dünyanın en kurak çölünde, en büyük teleskopların bulunduğu coğrafyada evreni yüksek rakımdan izleyin.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        # Video yerine harika bir Atacama Görseli
        st.image("https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=800&auto=format&fit=crop", use_container_width=True)

    with col_nz:
        st.markdown(f"""
        <div class="service-card">
            <img class="service-img" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=800&auto=format&fit=crop">
            <div class="service-content">
                <h3 class="service-title">Tekapo Gölü, Yeni Zelanda</h3>
                <p class="service-desc">Uluslararası Karanlık Gökyüzü rezervi. Güney Haçı takımyıldızını ve büyüleyici Aurora Australis'i el değmemiş bir doğanın kalbinde deneyimleyin.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        # Video yerine harika bir Aurora Görseli
        st.image("https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=800&auto=format&fit=crop", use_container_width=True)

# ==============================================================================
# SAYFA 3: DENEYİMLER & REZERVASYON
# ==============================================================================
elif menu_secimi == "DENEYİMLER & REZERVASYON":
    st.markdown("<h2>Deneyimler & Online Rezervasyon</h2>", unsafe_allow_html=True)
    st.write("---")

    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    
    with col_center:
        st.markdown("<h3>Astro-Deneyiminizi Seçin</h3>", unsafe_allow_html=True)
        deneyim_turu = st.radio(
            "",
            [
                "Gece Gözlem Turu ve Mitoloji ($150 / misafir)",
                "Astro-Fotoğrafçılık Workshop'u ($250 / misafir)",
                "VIP Premium Çöl Konaklaması ve Gözlem ($800 / misafir)"
            ],
            label_visibility="collapsed"
        )
        
        st.write("---")
        st.markdown("<h3>Rezervasyon Detayları</h3>", unsafe_allow_html=True)
        
        col_form1, col_form2 = st.columns(2)
        with col_form1:
            secilen_tarih = st.date_input("Tarih Seçin", min_value=datetime.date.today())
        with col_form2:
            kisi_sayisi = st.slider("Misafir Sayısı", min_value=1, max_value=8, value=2)
        
        if "150" in deneyim_turu: birim_fiyat = 150
        elif "250" in deneyim_turu: birim_fiyat = 250
        else: birim_fiyat = 800
            
        toplam_tutar = birim_fiyat * kisi_sayisi
        
        st.markdown(f"<div class='price-tag'>${toplam_tutar:,} <span style='font-size: 1rem; color: #C5A059;'>USD Toplam</span></div>", unsafe_allow_html=True)
        
        if st.button("Rezervasyon Talebi Gönder"):
            with st.spinner("Şifreli ağ üzerinden global operasyon merkezine bağlanılıyor..."):
                time.sleep(2.5) 
            st.success("Talebiniz başarıyla alınmıştır. Dijital ekibimiz rezervasyon onayı için iletişime geçecektir.")

# ==============================================================================
# SAYFA 4: ASTRO-GASTRONOMI
# ==============================================================================
elif menu_secimi == "ASTRO-GASTRONOMİ":
    st.markdown("<h2>Yıldızların Altında Gastronomi</h2>", unsafe_allow_html=True)
    st.markdown("<p>Yerel lezzetlerin Michelin standartlarında tekniklerle buluştuğu premium tadım deneyimi.</p>", unsafe_allow_html=True)
    st.write("---")

    col_space1, col_center, col_space2 = st.columns([1, 8, 1])
    with col_center:
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh; animation: slowZoom 30s infinite alternate linear;" src="https://images.unsplash.com/photo-1533777857889-4be7c70b33f7?q=80&w=2000&auto=format&fit=crop"></div>', unsafe_allow_html=True)
        st.write("")

        tab1, tab2 = st.tabs(["Atacama Çöl Menüsü (Şili)", "Tekapo Gölü Menüsü (Yeni Zelanda)"])

        with tab1:
            st.markdown(f"""
            <div style="padding: 20px;">
                <div class="menu-item">
                    <div class="menu-title">I. Başlangıç: "Supernova"</div>
                    <div class="menu-desc">Tütsülenmiş Pasifik Okyanusu somonu, taze Şili avokadosu ve limonlu kinoa çıtırları.</div>
                </div>
                <div class="menu-item">
                    <div class="menu-title">II. Ana Yemek: "Dünya'nın Merkezine Seyahat"</div>
                    <div class="menu-desc">Ağır ateşte pişmiş Patagonya kuzusu, kavrulmuş yerel kök sebzeler ve Carmenere şarabı redüksiyonu.</div>
                </div>
                <div class="menu-item" style="border-bottom: none;">
                    <div class="menu-title">III. Tatlı: "Karanlık Madde"</div>
                    <div class="menu-desc">%80 Kakao oranlı organik Şili çikolatası moussé, yenilebilir altın yaprakları ve deniz tuzu karamel.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with tab2:
            st.markdown(f"""
            <div style="padding: 20px;">
                <div class="menu-item">
                    <div class="menu-title">I. Başlangıç: "Aurora Işıkları"</div>
                    <div class="menu-desc">Buzul sularından Marlborough istiridyeleri, vahşi otlar ve yeşil elma granitası.</div>
                </div>
                <div class="menu-item">
                    <div class="menu-title">II. Ana Yemek: "Galaktik Orman"</div>
                    <div class="menu-desc">Manuka balı ve kekik ile sırlanmış Yeni Zelanda geyiği, yer elması püresi.</div>
                </div>
                <div class="menu-item" style="border-bottom: none;">
                    <div class="menu-title">III. Tatlı: "Yıldız Tozu Pavlova"</div>
                    <div class="menu-desc">Geleneksel pavlova, orman meyveleri, taze krema ve yaban mersini tozu.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.info("Sommelier Notu: Tüm menülerimiz ışık kirliliği yaratmayan özel masa aydınlatmaları eşliğinde servis edilmektedir.")

# ==============================================================================
# SAYFA 5: SÜRDÜRÜLEBİLİRLİK
# ==============================================================================
elif menu_secimi == "SÜRDÜRÜLEBİLİRLİK":
    st.markdown("<h2>Sürdürülebilir Bilimsel Turizm</h2>", unsafe_allow_html=True)
    st.write("---")
    
    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    with col_center:
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh;" src="https://images.unsplash.com/photo-1502481851512-e9e2529bfbf9?q=80&w=1200&auto=format&fit=crop"></div>', unsafe_allow_html=True)
        st.markdown("<h3>Doğaya ve Gökyüzüne Saygı</h3>", unsafe_allow_html=True)
        st.markdown("<p>Evrenin güzelliklerini keşfederken dünyamızı korumaktır. Sürdürülebilirlik ilkelerimiz sadece çevresel değil, kültürel uyumu da kapsar.</p>", unsafe_allow_html=True)
        
        st.write("")
        with st.expander("Işık Kirliliği Azaltımı"):
            st.write("Tesislerimizde gökyüzü gözlemini engellememesi için yalnızca kırmızı bazlı, düşük lümenli zemin aydınlatmaları ve harekete duyarlı sensörler kullanılmaktadır.")
        
        with st.expander("Sıfır Karbon Ayak İzi"):
            st.write("Gözlem noktalarına ulaşım sağlayan turlarımızda tamamen sıfır emisyonlu elektrikli araçlar ve enerji ihtiyacını karşılayan güneş paneli destekli üniteler kullanılmaktadır.")
            
        with st.expander("Yerel İş Birliği ve Tasarım"):
            st.write("Bölge halkı istihdam edilmekte, menülerde tamamen yerel üreticilerden alınan ürünler kullanılmaktadır. Mimari yapılarımız doğanın silüetini bozmayan minimal yaklaşımla tasarlanmıştır.")

# ==============================================================================
# SAYFA 6: YATIRIMCI PORTALI
# ==============================================================================
elif menu_secimi == "YATIRIMCI PORTALI":
    st.markdown("<h2>Kurumsal İş Modeli & Gelecek Vizyonu</h2>", unsafe_allow_html=True)
    st.markdown("<p>Sadece yetkili erişim. Lütfen yatırımcı şifrenizi girin. (İpucu: stellaris2026)</p>", unsafe_allow_html=True)
    st.write("---")
    
    col_space1, col_center, col_space2 = st.columns([1, 4, 1])
    with col_center:
        sifre = st.text_input("Kurumsal Şifre:", type="password")
        
        if sifre == "stellaris2026":
            st.success("Güvenlik Duvarı Aşıldı. Yönetici Paneline Erişim Sağlandı.")
            st.write("---")
            st.markdown("<h3>5 Yıllık Büyüme Vizyonu</h3>", unsafe_allow_html=True)
            st.info("Faz 2 (Kuzey Işıkları): İzlanda  |  Faz 3 (Çöl & Galaksi): Namibya")
            
            st.markdown("<h3>Rekabet Analizi (SWOT)</h3>", unsafe_allow_html=True)
            st.markdown("<p><b>Güçlü Yönler:</b> Niş pazar, Premium hizmet, Çoklu-destinasyon.<br><b>Farkımız:</b> Rakiplerimiz tek lokasyona odaklanırken, biz küresel bir lüks marka ağı kuruyoruz.</p>", unsafe_allow_html=True)

            st.write("---")
            st.markdown("<h3>Büyüme Projeksiyonu (Hedef Kitle)</h3>", unsafe_allow_html=True)
            gelir_verisi = pd.DataFrame({
                "Şili Operasyonları": [1000, 2500, 4800, 7500, 12000],
                "Yeni Zelanda Operasyonları": [800, 1900, 3500, 6000, 9500],
                "Gelecek Pazarlar": [0, 0, 1500, 4000, 8000]
            }, index=["Yıl 1", "Yıl 2", "Yıl 3", "Yıl 4", "Yıl 5"])
            st.area_chart(gelir_verisi, color=["#B8860B", "#C5A059", "#4A3B1B"])
        elif sifre != "":
            st.error("Erişim Reddedildi. Hatalı Şifre.")
