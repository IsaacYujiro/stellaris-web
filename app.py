import streamlit as st
import pandas as pd
import datetime
import time
import os
import glob

# ==============================================================================
# SİTE YAPILANDIRMASI VE AGRESİF LÜKS CSS (TİKLER İPTAL, GECE MAVİSİ)
# ==============================================================================
st.set_page_config(page_title="Stellaris | Premium Astro-Tourism", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&family=Cinzel:wght@400;600;700&display=swap');

    /* STREAMLIT'IN BEYAZ TEMASINI ZORUNLU OLARAK GECE MAVİSİ YAP */
    .stApp {
        background-color: #051024 !important; /* Derin Gece Mavisi */
    }
    
    header {
        background-color: transparent !important;
    }

    html, body, [class*="css"] { 
        font-family: 'Montserrat', sans-serif; 
        background-color: #051024 !important; 
        color: #C5A059; 
        text-align: center; 
    }

    [data-testid="stSidebar"] { 
        background-color: #030814 !important; 
        border-right: 1px solid #B8860B !important; 
    }

    /* --- GÜVENLİ MENÜ KODU (TİKLERİ GİZLE VE ALTIN YAP) --- */
    div[role="radiogroup"] > label > div:first-of-type { display: none !important; }
    
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

    div[role="radiogroup"] label:hover p { color: #D4AF37 !important; text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.4); }
    div[role="radiogroup"] label[aria-checked="true"] p { color: #D4AF37 !important; text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.8); border-bottom: 1px solid #B8860B; }

    /* Dil Seçici (Selectbox) Özel Tasarımı */
    [data-baseweb="select"] { background-color: #030814 !important; border: 1px solid #B8860B !important; border-radius: 4px; }
    [data-baseweb="select"] * { color: #C5A059 !important; font-family: 'Montserrat', sans-serif !important; }

    [data-testid="stSidebar"] .stAlert div { font-family: 'Montserrat', sans-serif !important; color: #B8860B !important; text-align: center !important; background-color: transparent !important; border: 1px solid #B8860B; }
    [data-testid="stSidebarCollapseButton"] span, .material-symbols-rounded { font-family: "Material Symbols Rounded" !important; color: #B8860B !important; }

    h1, h2, h3, h4, h5, h6 { font-family: 'Cinzel', serif; color: #B8860B !important; font-weight: 600; text-align: center !important; width: 100%; text-shadow: 0px 0px 15px rgba(184, 134, 11, 0.2); }
    p { text-align: center !important; margin: 0 auto 15px auto !important; max-width: 800px; line-height: 1.8; color: #E0E0E0 !important; }
    hr { border-top: 1px solid #B8860B !important; opacity: 0.3; width: 60%; margin: 40px auto !important; }

    .block-container { animation: fadeIn 1.2s ease-out; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }

    .hero-image { width: 100%; max-width: 1200px; height: 50vh; object-fit: cover; border-radius: 4px; filter: brightness(45%); border: 2px solid #B8860B; animation: slowZoom 25s infinite alternate linear; }
    @keyframes slowZoom { from { transform: scale(1); } to { transform: scale(1.05); } }
    .hero-container { position: relative; text-align: center; margin-bottom: 40px; display: flex; justify-content: center; overflow: hidden; }

    .service-card { background: #030814; border-radius: 8px; padding: 0; margin: 0 auto 30px auto; box-shadow: 0 4px 20px rgba(0,0,0,0.9); transition: transform 0.4s ease, box-shadow 0.4s ease; border: 1px solid #B8860B; overflow: hidden; height: 100%; max-width: 500px; animation: float 6s ease-in-out infinite; }
    @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-8px); } 100% { transform: translateY(0px); } }
    .service-card:hover { animation-play-state: paused; transform: scale(1.02); box-shadow: 0 10px 30px rgba(184, 134, 11, 0.3); }

    .hero-title { font-size: 5rem; font-family: 'Cinzel', serif; margin-bottom: 10px; letter-spacing: 6px; color: #B8860B !important; text-shadow: 0px 0px 25px rgba(184, 134, 11, 0.5); }
    .hero-subtitle { font-size: 1.2rem; font-weight: 300; letter-spacing: 5px; text-transform: uppercase; color: #C5A059 !important; margin-top: 15px !important; }
    .service-img { width: 100%; height: 220px; object-fit: cover; border-bottom: 1px solid #B8860B; }
    .service-content { padding: 30px; text-align: center; }
    .service-title { font-size: 1.4rem; margin-bottom: 15px; color: #B8860B; font-family: 'Cinzel', serif; text-align: center; }
    .service-desc { font-size: 0.95rem; color: #E0E0E0 !important; text-align: center; }
    .price-tag { font-family: 'Cinzel', serif; font-size: 3rem; color: #B8860B; font-weight: 700; margin: 25px 0; text-align: center; text-shadow: 0px 0px 10px rgba(184, 134, 11, 0.3); }
    
    .stButton { display: flex; justify-content: center; margin-top: 20px; }
    div.stButton > button:first-child { background-color: #030814 !important; color: #B8860B !important; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 1.1rem; padding: 15px 50px; border: 1px solid #B8860B !important; border-radius: 2px; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); letter-spacing: 2px; text-transform: uppercase; }
    div.stButton > button:first-child:hover { background-color: #B8860B !important; color: #051024 !important; transform: scale(1.05); box-shadow: 0 0 20px rgba(184, 134, 11, 0.4); }

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
# SİDEBAR & DİL SEÇİMİ YÖNETİMİ
# ==============================================================================
if bulunan_logo:
    st.sidebar.image(bulunan_logo, use_container_width=True)
else:
    st.sidebar.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin-top: 20px; color: #B8860B;'>Stellaris</h2>", unsafe_allow_html=True)

st.sidebar.write("---")

dil_secimi = st.sidebar.selectbox("🌍 Dil / Language", ["Türkçe", "English"])
lang = "TR" if dil_secimi == "Türkçe" else "EN"

st.sidebar.write("---")

if lang == "TR":
    menu_secenekleri = ["ANA SAYFA", "LOKASYONLARIMIZ", "DENEYİMLER & REZERVASYON", "ASTRO-GASTRONOMİ", "SÜRDÜRÜLEBİLİRLİK", "YATIRIMCI PORTALI"]
    sistem_durumu = "Sistem Durumu: Çevrimiçi"
else:
    menu_secenekleri = ["HOME", "OUR LOCATIONS", "EXPERIENCES & BOOKING", "ASTRO-GASTRONOMY", "SUSTAINABILITY", "INVESTOR PORTAL"]
    sistem_durumu = "System Status: Online"

menu_secimi = st.sidebar.radio("GizliNavigasyonBasligi", menu_secenekleri, label_visibility="collapsed")

st.sidebar.write("---")
st.sidebar.info(sistem_durumu)

# ==============================================================================
# SAYFA 1: ANA SAYFA
# ==============================================================================
if menu_secimi in ["ANA SAYFA", "HOME"]:
    col_space1, col_hero, col_space3 = st.columns([1, 2, 1])
    with col_hero:
        if bulunan_logo:
            st.image(bulunan_logo, use_container_width=True)
        else:
            st.markdown("<h1 class='hero-title'>STELLARIS</h1>", unsafe_allow_html=True)
            st_sub = "Global Astro-Turizm Lideri" if lang == "TR" else "Global Astro-Tourism Leader"
            st.markdown(f"<p class='hero-subtitle'>{st_sub}</p>", unsafe_allow_html=True)
    
    st.write("---")
    if lang == "TR":
        st.markdown("<h2>Gökyüzünün Sınırlarını Keşfedin</h2>", unsafe_allow_html=True)
        st.markdown("<p>Stellaris, sıradan tatil anlayışını geride bırakıp gözlerini evrenin derinliklerine çevirenler için doğdu. Işık kirliliğinden tamamen arınmış dünyanın en karanlık ve en berrak noktalarında, bilim ve doğayı kusursuz bir lüksle harmanlıyoruz. Gece gözlem turlarımız ve premium konaklama seçeneklerimizle yıldızların altında unutulmaz bir hikaye yazın.</p>", unsafe_allow_html=True)
        st.write("---")
        st.markdown("<h2>Sinematik Marka Vizyonu</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2>Discover the Limits of the Sky</h2>", unsafe_allow_html=True)
        st.markdown("<p>Stellaris was born for those who leave ordinary holiday concepts behind and turn their eyes to the depths of the universe. In the darkest and clearest points of the world, completely free from light pollution, we blend science and nature with flawless luxury. Write an unforgettable story under the stars with our night observation tours and premium accommodation options.</p>", unsafe_allow_html=True)
        st.write("---")
        st.markdown("<h2>Cinematic Brand Vision</h2>", unsafe_allow_html=True)
        
    col_space1, col_image, col_space2 = st.columns([1, 8, 1])
    with col_image:
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:45vh; filter: brightness(60%);" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=2000&auto=format&fit=crop"></div>', unsafe_allow_html=True)

# ==============================================================================
# SAYFA 2: LOKASYONLARIMIZ (RESİMLER DÜZELTİLDİ)
# ==============================================================================
elif menu_secimi in ["LOKASYONLARIMIZ", "OUR LOCATIONS"]:
    if lang == "TR":
        st.markdown("<h2>Hedef Ülkeler ve Küresel Pazar</h2>", unsafe_allow_html=True)
        st.markdown("<p>Evrenin en muazzam manzaralarını sunan stratejik karanlık gökyüzü rezervleri.</p>", unsafe_allow_html=True)
        t_chile_title = "Atacama Çölü, Şili"
        t_chile_desc = "Yılda 300'den fazla açık ve bulutsuz gece. Dünyanın en kurak çölünde, en büyük teleskopların bulunduğu coğrafyada evreni yüksek rakımdan izleyin."
        t_nz_title = "Tekapo Gölü, Yeni Zelanda"
        t_nz_desc = "Uluslararası Karanlık Gökyüzü rezervi. Güney Haçı takımyıldızını ve büyüleyici Aurora Australis'i el değmemiş bir doğanın kalbinde deneyimleyin."
    else:
        st.markdown("<h2>Target Countries and Global Market</h2>", unsafe_allow_html=True)
        st.markdown("<p>Strategic dark sky reserves offering the most magnificent views of the universe.</p>", unsafe_allow_html=True)
        t_chile_title = "Atacama Desert, Chile"
        t_chile_desc = "Over 300 clear and cloudless nights a year. Watch the universe from high altitude in the driest desert in the world, home to the largest telescopes."
        t_nz_title = "Lake Tekapo, New Zealand"
        t_nz_desc = "International Dark Sky reserve. Experience the Southern Cross constellation and the fascinating Aurora Australis in the heart of untouched nature."

    st.write("---")
    col_space1, col_chile, col_nz, col_space2 = st.columns([1, 4, 4, 1])
    
    with col_chile:
        st.markdown(f"""
        <div class="service-card">
            <img class="service-img" src="https://images.unsplash.com/photo-1504333638930-c8787321efa0?q=80&w=800&auto=format&fit=crop">
            <div class="service-content">
                <h3 class="service-title">{t_chile_title}</h3>
                <p class="service-desc">{t_chile_desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        # Sağlam Alternatif Atacama Görseli
        st.image("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=800&auto=format&fit=crop", use_container_width=True)

    with col_nz:
        st.markdown(f"""
        <div class="service-card">
            <img class="service-img" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=800&auto=format&fit=crop">
            <div class="service-content">
                <h3 class="service-title">{t_nz_title}</h3>
                <p class="service-desc">{t_nz_desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=800&auto=format&fit=crop", use_container_width=True)

# ==============================================================================
# SAYFA 3: DENEYİMLER & REZERVASYON
# ==============================================================================
elif menu_secimi in ["DENEYİMLER & REZERVASYON", "EXPERIENCES & BOOKING"]:
    if lang == "TR":
        st.markdown("<h2>Deneyimler & Online Rezervasyon</h2>", unsafe_allow_html=True)
        exp_title = "Astro-Deneyiminizi Seçin"
        exp_options = ["Gece Gözlem Turu ve Mitoloji ($150 / misafir)", "Astro-Fotoğrafçılık Workshop'u ($250 / misafir)", "VIP Premium Çöl Konaklaması ve Gözlem ($800 / misafir)"]
        res_details = "Rezervasyon Detayları"
        date_label = "Tarih Seçin"
        guest_label = "Misafir Sayısı"
        total_label = "USD Toplam"
        btn_label = "Rezervasyon Talebi Gönder"
        msg_loading = "Şifreli ağ üzerinden global operasyon merkezine bağlanılıyor..."
        msg_success = "Talebiniz başarıyla alınmıştır. Dijital ekibimiz rezervasyon onayı için iletişime geçecektir."
    else:
        st.markdown("<h2>Experiences & Online Booking</h2>", unsafe_allow_html=True)
        exp_title = "Choose Your Astro-Experience"
        exp_options = ["Night Observation Tour and Mythology ($150 / guest)", "Astro-Photography Workshop ($250 / guest)", "VIP Premium Desert Stay and Observation ($800 / guest)"]
        res_details = "Booking Details"
        date_label = "Select Date"
        guest_label = "Number of Guests"
        total_label = "USD Total"
        btn_label = "Send Booking Request"
        msg_loading = "Connecting to global operations center via encrypted network..."
        msg_success = "Your request has been successfully received. Our digital team will contact you for booking confirmation."

    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    
    with col_center:
        st.markdown(f"<h3>{exp_title}</h3>", unsafe_allow_html=True)
        deneyim_turu = st.radio("", exp_options, label_visibility="collapsed")
        
        st.write("---")
        st.markdown(f"<h3>{res_details}</h3>", unsafe_allow_html=True)
        
        col_form1, col_form2 = st.columns(2)
        with col_form1:
            secilen_tarih = st.date_input(date_label, min_value=datetime.date.today())
        with col_form2:
            kisi_sayisi = st.slider(guest_label, min_value=1, max_value=8, value=2)
        
        if "150" in deneyim_turu: birim_fiyat = 150
        elif "250" in deneyim_turu: birim_fiyat = 250
        else: birim_fiyat = 800
            
        toplam_tutar = birim_fiyat * kisi_sayisi
        
        st.markdown(f"<div class='price-tag'>${toplam_tutar:,} <span style='font-size: 1rem; color: #C5A059;'>{total_label}</span></div>", unsafe_allow_html=True)
        
        if st.button(btn_label):
            with st.spinner(msg_loading):
                time.sleep(2.5) 
            st.success(msg_success)

# ==============================================================================
# SAYFA 4: ASTRO-GASTRONOMI
# ==============================================================================
elif menu_secimi in ["ASTRO-GASTRONOMİ", "ASTRO-GASTRONOMY"]:
    if lang == "TR":
        st.markdown("<h2>Yıldızların Altında Gastronomi</h2>", unsafe_allow_html=True)
        st.markdown("<p>Yerel lezzetlerin Michelin standartlarında tekniklerle buluştuğu premium tadım deneyimi.</p>", unsafe_allow_html=True)
        t_tab1 = "Atacama Çöl Menüsü (Şili)"
        t_tab2 = "Tekapo Gölü Menüsü (Yeni Zelanda)"
        
        t_chile_s = "Tütsülenmiş Pasifik Okyanusu somonu, taze Şili avokadosu ve limonlu kinoa çıtırları."
        t_chile_m = "Ağır ateşte pişmiş Patagonya kuzusu, kavrulmuş yerel kök sebzeler ve Carmenere şarabı redüksiyonu."
        t_chile_d = "%80 Kakao oranlı organik Şili çikolatası moussé, yenilebilir altın yaprakları ve deniz tuzu karamel."
        
        t_nz_s = "Buzul sularından Marlborough istiridyeleri, vahşi otlar ve yeşil elma granitası."
        t_nz_m = "Manuka balı ve kekik ile sırlanmış Yeni Zelanda geyiği, yer elması püresi."
        t_nz_d = "Geleneksel pavlova, orman meyveleri, taze krema ve yaban mersini tozu."
        
        t_note = "Sommelier Notu: Tüm menülerimiz ışık kirliliği yaratmayan özel masa aydınlatmaları eşliğinde servis edilmektedir."
    else:
        st.markdown("<h2>Gastronomy Under the Stars</h2>", unsafe_allow_html=True)
        st.markdown("<p>A premium tasting experience where local flavors meet the dark sky with Michelin standard techniques.</p>", unsafe_allow_html=True)
        t_tab1 = "Atacama Desert Menu (Chile)"
        t_tab2 = "Lake Tekapo Menu (New Zealand)"
        
        t_chile_s = "Smoked Pacific Ocean salmon, fresh Chilean avocado and lemon quinoa crisps."
        t_chile_m = "Slow-cooked Patagonian lamb, roasted local root vegetables and Carmenere wine reduction."
        t_chile_d = "80% Cacao organic Chilean chocolate moussé, edible gold leaves and sea salt caramel."
        
        t_nz_s = "Marlborough oysters from glacial waters, wild herbs and green apple granita."
        t_nz_m = "New Zealand venison glazed with Manuka honey and thyme, Jerusalem artichoke puree."
        t_nz_d = "Traditional pavlova, forest fruits, fresh cream and blueberry dust."
        
        t_note = "Sommelier Note: All our menus are served with special table lighting that does not create light pollution."

    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 8, 1])
    with col_center:
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh; animation: slowZoom 30s infinite alternate linear;" src="https://images.unsplash.com/photo-1533777857889-4be7c70b33f7?q=80&w=2000&auto=format&fit=crop"></div>', unsafe_allow_html=True)
        st.write("")

        tab1, tab2 = st.tabs([t_tab1, t_tab2])

        with tab1:
            st.markdown(f"""
            <div style="padding: 20px;">
                <div class="menu-item"><div class="menu-title">I. "Supernova"</div><div class="menu-desc">{t_chile_s}</div></div>
                <div class="menu-item"><div class="menu-title">II. "Journey to the Center"</div><div class="menu-desc">{t_chile_m}</div></div>
                <div class="menu-item" style="border-bottom: none;"><div class="menu-title">III. "Dark Matter"</div><div class="menu-desc">{t_chile_d}</div></div>
            </div>
            """, unsafe_allow_html=True)

        with tab2:
            st.markdown(f"""
            <div style="padding: 20px;">
                <div class="menu-item"><div class="menu-title">I. "Aurora Lights"</div><div class="menu-desc">{t_nz_s}</div></div>
                <div class="menu-item"><div class="menu-title">II. "Galactic Forest"</div><div class="menu-desc">{t_nz_m}</div></div>
                <div class="menu-item" style="border-bottom: none;"><div class="menu-title">III. "Stardust Pavlova"</div><div class="menu-desc">{t_nz_d}</div></div>
            </div>
            """, unsafe_allow_html=True)

        st.info(t_note)

# ==============================================================================
# SAYFA 5: SÜRDÜRÜLEBİLİRLİK
# ==============================================================================
elif menu_secimi in ["SÜRDÜRÜLEBİLİRLİK", "SUSTAINABILITY"]:
    if lang == "TR":
        st.markdown("<h2>Sürdürülebilir Bilimsel Turizm</h2>", unsafe_allow_html=True)
        st.write("---")
        title = "Doğaya ve Gökyüzüne Saygı"
        desc = "Evrenin güzelliklerini keşfederken dünyamızı korumaktır. Sürdürülebilirlik ilkelerimiz sadece çevresel değil, kültürel uyumu da kapsar."
        ex1_t, ex1_d = "Işık Kirliliği Azaltımı", "Tesislerimizde gökyüzü gözlemini engellememesi için yalnızca kırmızı bazlı, düşük lümenli zemin aydınlatmaları ve harekete duyarlı sensörler kullanılmaktadır."
        ex2_t, ex2_d = "Sıfır Karbon Ayak İzi", "Gözlem noktalarına ulaşım sağlayan turlarımızda tamamen sıfır emisyonlu elektrikli araçlar ve enerji ihtiyacını karşılayan güneş paneli destekli üniteler kullanılmaktadır."
        ex3_t, ex3_d = "Yerel İş Birliği ve Tasarım", "Bölge halkı istihdam edilmekte, menülerde tamamen yerel üreticilerden alınan ürünler kullanılmaktadır. Mimari yapılarımız doğanın silüetini bozmayan minimal yaklaşımla tasarlanmıştır."
    else:
        st.markdown("<h2>Sustainable Scientific Tourism</h2>", unsafe_allow_html=True)
        st.write("---")
        title = "Respect for Nature and the Sky"
        desc = "Our fundamental mission while exploring the universe is to protect our world. Our sustainability principles cover not only environmental but also cultural harmony."
        ex1_t, ex1_d = "Light Pollution Reduction", "To prevent interfering with sky observation, only red-based, low-lumen floor lighting and motion-sensitive sensors are used in our facilities."
        ex2_t, ex2_d = "Zero Carbon Footprint", "Our tours providing access to observation points use completely zero-emission electric vehicles and solar panel-supported units."
        ex3_t, ex3_d = "Local Collaboration and Design", "Local people are employed, and products sourced entirely from local producers are used in menus. Our architectural structures are designed with a minimal approach that preserves nature's silhouette."

    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    with col_center:
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh;" src="https://images.unsplash.com/photo-1502481851512-e9e2529bfbf9?q=80&w=1200&auto=format&fit=crop"></div>', unsafe_allow_html=True)
        st.markdown(f"<h3>{title}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p>{desc}</p>", unsafe_allow_html=True)
        
        st.write("")
        with st.expander(ex1_t): st.write(ex1_d)
        with st.expander(ex2_t): st.write(ex2_d)
        with st.expander(ex3_t): st.write(ex3_d)

# ==============================================================================
# SAYFA 6: YATIRIMCI PORTALI
# ==============================================================================
elif menu_secimi in ["YATIRIMCI PORTALI", "INVESTOR PORTAL"]:
    if lang == "TR":
        st.markdown("<h2>Kurumsal İş Modeli & Gelecek Vizyonu</h2>", unsafe_allow_html=True)
        st.markdown("<p>Sadece yetkili erişim. Lütfen yatırımcı şifrenizi girin. (İpucu: stellaris2026)</p>", unsafe_allow_html=True)
        pw_label = "Kurumsal Şifre:"
        msg_success = "Güvenlik Duvarı Aşıldı. Yönetici Paneline Erişim Sağlandı."
        msg_error = "Erişim Reddedildi. Hatalı Şifre."
        t_vision = "5 Yıllık Büyüme Vizyonu"
        t_phases = "Faz 2 (Kuzey Işıkları): İzlanda  |  Faz 3 (Çöl & Galaksi): Namibya"
        t_swot = "Rekabet Analizi (SWOT)"
        t_swot_desc = "<b>Güçlü Yönler:</b> Niş pazar, Premium hizmet, Çoklu-destinasyon.<br><b>Farkımız:</b> Rakiplerimiz tek lokasyona odaklanırken, biz küresel bir lüks marka ağı kuruyoruz."
        t_chart = "Büyüme Projeksiyonu (Hedef Kitle)"
        d_cols = {"Şili Operasyonları": [1000, 2500, 4800, 7500, 12000], "Yeni Zelanda Operasyonları": [800, 1900, 3500, 6000, 9500], "Gelecek Pazarlar": [0, 0, 1500, 4000, 8000]}
        d_index = ["Yıl 1", "Yıl 2", "Yıl 3", "Yıl 4", "Yıl 5"]
    else:
        st.markdown("<h2>Corporate Business Model & Future Vision</h2>", unsafe_allow_html=True)
        st.markdown("<p>Authorized access only. Please enter your investor password. (Hint: stellaris2026)</p>", unsafe_allow_html=True)
        pw_label = "Corporate Password:"
        msg_success = "Security Firewall Breached. Access Granted to Admin Panel."
        msg_error = "Access Denied. Incorrect Password."
        t_vision = "5-Year Growth Vision"
        t_phases = "Phase 2 (Northern Lights): Iceland  |  Phase 3 (Desert & Galaxy): Namibia"
        t_swot = "Competitor Analysis (SWOT)"
        t_swot_desc = "<b>Strengths:</b> Niche market, Premium service, Multi-destination.<br><b>Our Difference:</b> While competitors focus on a single location, we are building a global luxury brand network."
        t_chart = "Growth Projection (Target Audience)"
        d_cols = {"Chile Operations": [1000, 2500, 4800, 7500, 12000], "New Zealand Operations": [800, 1900, 3500, 6000, 9500], "Future Markets": [0, 0, 1500, 4000, 8000]}
        d_index = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]

    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 4, 1])
    with col_center:
        sifre = st.text_input(pw_label, type="password")
        
        if sifre == "stellaris2026":
            st.success(msg_success)
            st.write("---")
            st.markdown(f"<h3>{t_vision}</h3>", unsafe_allow_html=True)
            st.info(t_phases)
            
            st.markdown(f"<h3>{t_swot}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p>{t_swot_desc}</p>", unsafe_allow_html=True)

            st.write("---")
            st.markdown(f"<h3>{t_chart}</h3>", unsafe_allow_html=True)
            gelir_verisi = pd.DataFrame(d_cols, index=d_index)
            st.area_chart(gelir_verisi, color=["#B8860B", "#C5A059", "#4A3B1B"])
        elif sifre != "":
            st.error(msg_error)
