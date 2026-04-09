import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time
import os
import glob

# ==============================================================================
# SİTE YAPILANDIRMASI VE AGRESİF LÜKS CSS (GECE MAVİSİ, TİKSİZ, EMOJİSİZ)
# ==============================================================================
st.set_page_config(page_title="Stellaris | Premium Astro-Tourism", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&family=Cinzel:wght@400;600;700&display=swap');

    .stApp { background-color: #051024 !important; }
    header { background-color: transparent !important; }

    html, body, [class*="css"] { 
        font-family: 'Montserrat', sans-serif; 
        background-color: #051024 !important; 
        color: #C5A059; 
        text-align: center; 
    }

    [data-testid="stSidebar"] { background-color: #030814 !important; border-right: 1px solid #B8860B !important; }

    /* --- GÜVENLİ MENÜ KODU --- */
    div[role="radiogroup"] > label > div:first-of-type { display: none !important; }
    div[role="radiogroup"] p {
        color: #B8860B !important; font-family: 'Cinzel', serif !important; font-size: 1.15rem !important;
        font-weight: 600 !important; text-align: center !important; visibility: visible !important;
        display: block !important; width: 100%; margin-top: 5px; transition: all 0.3s ease;
    }
    div[role="radiogroup"] label:hover p { color: #D4AF37 !important; text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.4); }
    div[role="radiogroup"] label[aria-checked="true"] p { color: #D4AF37 !important; text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.8); border-bottom: 1px solid #B8860B; }

    [data-baseweb="select"] { background-color: #030814 !important; border: 1px solid #B8860B !important; border-radius: 4px; }
    [data-baseweb="select"] * { color: #C5A059 !important; font-family: 'Montserrat', sans-serif !important; }

    [data-testid="stSidebar"] .stAlert div { font-family: 'Montserrat', sans-serif !important; color: #B8860B !important; text-align: center !important; background-color: transparent !important; border: 1px solid #B8860B; }
    
    /* Gelişmiş Metrik Tasarımı (Canlı Veri Ekranı İçin) */
    div[data-testid="stMetricValue"] { color: #D4AF37 !important; font-family: 'Cinzel', serif !important; font-size: 2.5rem !important; text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.4); }
    div[data-testid="stMetricLabel"] { color: #C5A059 !important; font-family: 'Montserrat', sans-serif !important; font-size: 1.1rem !important; }
    div[data-testid="stMetricDelta"] svg { fill: #D4AF37 !important; color: #D4AF37 !important; }

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
for resim in resimler:
    if "logo" in resim.lower() or "whatsapp" in resim.lower() or "image" in resim.lower():
        bulunan_logo = resim
        break
if not bulunan_logo and resimler:
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
    # YENİ MENÜ MADDESİ EKLENDİ
    menu_secenekleri = ["ANA SAYFA", "LOKASYONLARIMIZ", "GÖZLEM KOŞULLARI & EKİPMAN", "DENEYİMLER & REZERVASYON", "ASTRO-GASTRONOMİ", "SÜRDÜRÜLEBİLİRLİK", "YATIRIMCI PORTALI"]
    sistem_durumu = "Sistem Durumu: Çevrimiçi"
else:
    menu_secenekleri = ["HOME", "OUR LOCATIONS", "CONDITIONS & EQUIPMENT", "EXPERIENCES & BOOKING", "ASTRO-GASTRONOMY", "SUSTAINABILITY", "INVESTOR PORTAL"]
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
# SAYFA 2: LOKASYONLARIMIZ
# ==============================================================================
elif menu_secimi in ["LOKASYONLARIMIZ", "OUR LOCATIONS"]:
    if lang == "TR":
        st.markdown("<h2>Hedef Ülkeler ve Küresel Pazar</h2>", unsafe_allow_html=True)
        st.markdown("<p>Evrenin en muazzam manzaralarını sunan stratejik karanlık gökyüzü rezervleri.</p>", unsafe_allow_html=True)
        t_chile_title, t_chile_desc = "Atacama Çölü, Şili", "Yılda 300'den fazla açık ve bulutsuz gece. Dünyanın en kurak çölünde, en büyük teleskopların bulunduğu coğrafyada evreni yüksek rakımdan izleyin."
        t_nz_title, t_nz_desc = "Tekapo Gölü, Yeni Zelanda", "Uluslararası Karanlık Gökyüzü rezervi. Güney Haçı takımyıldızını ve büyüleyici Aurora Australis'i el değmemiş bir doğanın kalbinde deneyimleyin."
    else:
        st.markdown("<h2>Target Countries and Global Market</h2>", unsafe_allow_html=True)
        st.markdown("<p>Strategic dark sky reserves offering the most magnificent views of the universe.</p>", unsafe_allow_html=True)
        t_chile_title, t_chile_desc = "Atacama Desert, Chile", "Over 300 clear and cloudless nights a year. Watch the universe from high altitude in the driest desert in the world, home to the largest telescopes."
        t_nz_title, t_nz_desc = "Lake Tekapo, New Zealand", "International Dark Sky reserve. Experience the Southern Cross constellation and the fascinating Aurora Australis in the heart of untouched nature."

    st.write("---")
    col_space1, col_chile, col_nz, col_space2 = st.columns([1, 4, 4, 1])
    with col_chile:
        st.markdown(f"""
        <div class="service-card">
            <img class="service-img" src="https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?q=80&w=800&auto=format&fit=crop">
            <div class="service-content"><h3 class="service-title">{t_chile_title}</h3><p class="service-desc">{t_chile_desc}</p></div>
        </div>
        """, unsafe_allow_html=True)
    with col_nz:
        st.markdown(f"""
        <div class="service-card">
            <img class="service-img" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=800&auto=format&fit=crop">
            <div class="service-content"><h3 class="service-title">{t_nz_title}</h3><p class="service-desc">{t_nz_desc}</p></div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# YENİ SAYFA 3: GÖZLEM KOŞULLARI & EKİPMAN
# ==============================================================================
elif menu_secimi in ["GÖZLEM KOŞULLARI & EKİPMAN", "CONDITIONS & EQUIPMENT"]:
    if lang == "TR":
        st.markdown("<h2>Gözlem Koşulları ve VIP Ekipmanlar</h2>", unsafe_allow_html=True)
        st.markdown("<p>Kusursuz bir deneyim için anlık gökyüzü berraklık oranları ve teknoloji harikası teleskoplarımız.</p>", unsafe_allow_html=True)
        m1, m2, m3 = "Atacama Berraklık", "Tekapo Berraklık", "Ay Evresi"
        m1_v, m2_v, m3_v = "%98", "%92", "Yeni Ay"
        m1_d, m2_d, m3_d = "+2% (Mükemmel)", "-1% (Çok İyi)", "Gözlem İçin Kusursuz"
        t_eq = "VIP Gözlem Ekipmanlarımız"
        eq1_t, eq1_d = "Celestron CPC Deluxe 1100 HD", "Derin uzay nesneleri (Galaksiler ve Bulutsular) için ultra yüksek çözünürlüklü bilgisayarlı teleskop."
        eq2_t, eq2_d = "Meade LX200 14'' Advanced", "Gezegenlerin ve ay kraterlerinin en ince detaylarını yakalamak için devasa diyaframlı profesyonel gözlem aracı."
        eq3_t, eq3_d = "Lunt Solar Systems", "Gündüz aktiviteleri için güneş patlamalarını ve taçküreyi güvenle izlemenizi sağlayan özel H-Alpha teleskobu."
    else:
        st.markdown("<h2>Observation Conditions and VIP Equipment</h2>", unsafe_allow_html=True)
        st.markdown("<p>Real-time sky clarity rates and our state-of-the-art telescopes for a flawless experience.</p>", unsafe_allow_html=True)
        m1, m2, m3 = "Atacama Clarity", "Tekapo Clarity", "Moon Phase"
        m1_v, m2_v, m3_v = "98%", "92%", "New Moon"
        m1_d, m2_d, m3_d = "+2% (Perfect)", "-1% (Excellent)", "Flawless for Observation"
        t_eq = "Our VIP Observation Equipment"
        eq1_t, eq1_d = "Celestron CPC Deluxe 1100 HD", "Ultra-high-definition computerized telescope designed specifically for deep space objects (Galaxies and Nebulae)."
        eq2_t, eq2_d = "Meade LX200 14'' Advanced", "A massive aperture professional observation tool for capturing the finest details of planets and lunar craters."
        eq3_t, eq3_d = "Lunt Solar Systems", "Specialized H-Alpha telescope allowing you to safely observe solar flares and the corona during daytime activities."

    st.write("---")
    # Veri Metrikleri
    col1, col2, col3 = st.columns(3)
    col1.metric(label=m1, value=m1_v, delta=m1_d)
    col2.metric(label=m2, value=m2_v, delta=m2_d)
    col3.metric(label=m3, value=m3_v, delta=m3_d, delta_color="off")
    
    st.write("---")
    st.markdown(f"<h3>{t_eq}</h3>", unsafe_allow_html=True)
    st.write("")
    
    # Ekipman Vitrini
    e1, e2, e3 = st.columns(3)
    with e1:
        st.markdown(f"""
        <div class="service-card" style="box-shadow:none; border:none;">
            <img class="service-img" src="https://images.unsplash.com/photo-1517976487492-5750f3195933?q=80&w=800&auto=format&fit=crop" style="border-radius:8px; border: 1px solid #B8860B;">
            <div class="service-content" style="padding:15px;"><h3 class="service-title" style="font-size:1.1rem;">{eq1_t}</h3><p class="service-desc">{eq1_d}</p></div>
        </div>
        """, unsafe_allow_html=True)
    with e2:
        st.markdown(f"""
        <div class="service-card" style="box-shadow:none; border:none;">
            <img class="service-img" src="https://images.unsplash.com/photo-1506443432602-ac2fcd6f54e0?q=80&w=800&auto=format&fit=crop" style="border-radius:8px; border: 1px solid #B8860B;">
            <div class="service-content" style="padding:15px;"><h3 class="service-title" style="font-size:1.1rem;">{eq2_t}</h3><p class="service-desc">{eq2_d}</p></div>
        </div>
        """, unsafe_allow_html=True)
    with e3:
        st.markdown(f"""
        <div class="service-card" style="box-shadow:none; border:none;">
            <img class="service-img" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop" style="border-radius:8px; border: 1px solid #B8860B;">
            <div class="service-content" style="padding:15px;"><h3 class="service-title" style="font-size:1.1rem;">{eq3_t}</h3><p class="service-desc">{eq3_d}</p></div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# SAYFA 4: DENEYİMLER & REZERVASYON
# ==============================================================================
elif menu_secimi in ["DENEYİMLER & REZERVASYON", "EXPERIENCES & BOOKING"]:
    if lang == "TR":
        st.markdown("<h2>Deneyimler & Online Rezervasyon</h2>", unsafe_allow_html=True)
        exp_title = "Astro-Deneyiminizi Seçin"
        exp_options = ["Gece Gözlem Turu ve Mitoloji ($150 / misafir)", "Astro-Fotoğrafçılık Workshop'u ($250 / misafir)", "VIP Premium Çöl Konaklaması ve Gözlem ($800 / misafir)"]
        res_details, date_label, guest_label, total_label, btn_label = "Rezervasyon Detayları", "Tarih Seçin", "Misafir Sayısı", "USD Toplam", "Rezervasyon Talebi Gönder"
        msg_loading, msg_success = "Şifreli ağ üzerinden global operasyon merkezine bağlanılıyor...", "Talebiniz başarıyla alınmıştır. Dijital ekibimiz rezervasyon onayı için iletişime geçecektir."
    else:
        st.markdown("<h2>Experiences & Online Booking</h2>", unsafe_allow_html=True)
        exp_title = "Choose Your Astro-Experience"
        exp_options = ["Night Observation Tour and Mythology ($150 / guest)", "Astro-Photography Workshop ($250 / guest)", "VIP Premium Desert Stay and Observation ($800 / guest)"]
        res_details, date_label, guest_label, total_label, btn_label = "Booking Details", "Select Date", "Number of Guests", "USD Total", "Send Booking Request"
        msg_loading, msg_success = "Connecting to global operations center via encrypted network...", "Your request has been successfully received. Our digital team will contact you for booking confirmation."

    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    
    with col_center:
        st.markdown(f"<h3>{exp_title}</h3>", unsafe_allow_html=True)
        deneyim_turu = st.radio("", exp_options, label_visibility="collapsed")
        
        st.write("---")
        st.markdown(f"<h3>{res_details}</h3>", unsafe_allow_html=True)
        
        col_form1, col_form2 = st.columns(2)
        with col_form1: secilen_tarih = st.date_input(date_label, min_value=datetime.date.today())
        with col_form2: kisi_sayisi = st.slider(guest_label, min_value=1, max_value=8, value=2)
        
        if "150" in deneyim_turu: birim_fiyat = 150
        elif "250" in deneyim_turu: birim_fiyat = 250
        else: birim_fiyat = 800
            
        st.markdown(f"<div class='price-tag'>${(birim_fiyat * kisi_sayisi):,} <span style='font-size: 1rem; color: #C5A059;'>{total_label}</span></div>", unsafe_allow_html=True)
        if st.button(btn_label):
            with st.spinner(msg_loading): time.sleep(2.5) 
            st.success(msg_success)

# ==============================================================================
# SAYFA 5: ASTRO-GASTRONOMI
# ==============================================================================
elif menu_secimi in ["ASTRO-GASTRONOMİ", "ASTRO-GASTRONOMY"]:
    if lang == "TR":
        st.markdown("<h2>Yıldızların Altında Gastronomi</h2>", unsafe_allow_html=True)
        st.markdown("<p>Yerel lezzetlerin Michelin standartlarında tekniklerle buluştuğu premium tadım deneyimi.</p>", unsafe_allow_html=True)
        t_tab1, t_tab2 = "Atacama Çöl Menüsü (Şili)", "Tekapo Gölü Menüsü (Yeni Zelanda)"
        t_chile = ["Tütsülenmiş Pasifik Okyanusu somonu, taze Şili avokadosu ve limonlu kinoa çıtırları.", "Ağır ateşte pişmiş Patagonya kuzusu, kavrulmuş yerel kök sebzeler ve Carmenere şarabı redüksiyonu.", "%80 Kakao oranlı organik Şili çikolatası moussé, yenilebilir altın yaprakları ve deniz tuzu karamel."]
        t_nz = ["Buzul sularından Marlborough istiridyeleri, vahşi otlar ve yeşil elma granitası.", "Manuka balı ve kekik ile sırlanmış Yeni Zelanda geyiği, yer elması püresi.", "Geleneksel pavlova, orman meyveleri, taze krema ve yaban mersini tozu."]
        t_note = "Sommelier Notu: Tüm menülerimiz ışık kirliliği yaratmayan özel masa aydınlatmaları eşliğinde servis edilmektedir."
    else:
        st.markdown("<h2>Gastronomy Under the Stars</h2>", unsafe_allow_html=True)
        st.markdown("<p>A premium tasting experience where local flavors meet the dark sky with Michelin standard techniques.</p>", unsafe_allow_html=True)
        t_tab1, t_tab2 = "Atacama Desert Menu (Chile)", "Lake Tekapo Menu (New Zealand)"
        t_chile = ["Smoked Pacific Ocean salmon, fresh Chilean avocado and lemon quinoa crisps.", "Slow-cooked Patagonian lamb, roasted local root vegetables and Carmenere wine reduction.", "80% Cacao organic Chilean chocolate moussé, edible gold leaves and sea salt caramel."]
        t_nz = ["Marlborough oysters from glacial waters, wild herbs and green apple granita.", "New Zealand venison glazed with Manuka honey and thyme, Jerusalem artichoke puree.", "Traditional pavlova, forest fruits, fresh cream and blueberry dust."]
        t_note = "Sommelier Note: All our menus are served with special table lighting that does not create light pollution."

    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 8, 1])
    with col_center:
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh; animation: slowZoom 30s infinite alternate linear;" src="https://images.unsplash.com/photo-1533777857889-4be7c70b33f7?q=80&w=2000&auto=format&fit=crop"></div>', unsafe_allow_html=True)
        st.write("")
        tab1, tab2 = st.tabs([t_tab1, t_tab2])
        with tab1:
            st.markdown(f"""<div style="padding: 20px;"><div class="menu-item"><div class="menu-title">I. "Supernova"</div><div class="menu-desc">{t_chile[0]}</div></div><div class="menu-item"><div class="menu-title">II. "Journey to the Center"</div><div class="menu-desc">{t_chile[1]}</div></div><div class="menu-item" style="border-bottom: none;"><div class="menu-title">III. "Dark Matter"</div><div class="menu-desc">{t_chile[2]}</div></div></div>""", unsafe_allow_html=True)
        with tab2:
            st.markdown(f"""<div style="padding: 20px;"><div class="menu-item"><div class="menu-title">I. "Aurora Lights"</div><div class="menu-desc">{t_nz[0]}</div></div><div class="menu-item"><div class="menu-title">II. "Galactic Forest"</div><div class="menu-desc">{t_nz[1]}</div></div><div class="menu-item" style="border-bottom: none;"><div class="menu-title">III. "Stardust Pavlova"</div><div class="menu-desc">{t_nz[2]}</div></div></div>""", unsafe_allow_html=True)
        st.info(t_note)

# ==============================================================================
# SAYFA 6: SÜRDÜRÜLEBİLİRLİK
# ==============================================================================
elif menu_secimi in ["SÜRDÜRÜLEBİLİRLİK", "SUSTAINABILITY"]:
    if lang == "TR":
        st.markdown("<h2>Sürdürülebilir Bilimsel Turizm</h2>", unsafe_allow_html=True)
        title, desc = "Doğaya ve Gökyüzüne Saygı", "Evrenin güzelliklerini keşfederken dünyamızı korumaktır. Sürdürülebilirlik ilkelerimiz sadece çevresel değil, kültürel uyumu da kapsar."
        ex1 = ("Işık Kirliliği Azaltımı", "Tesislerimizde gökyüzü gözlemini engellememesi için yalnızca kırmızı bazlı, düşük lümenli zemin aydınlatmaları ve harekete duyarlı sensörler kullanılmaktadır.")
        ex2 = ("Sıfır Karbon Ayak İzi", "Gözlem noktalarına ulaşım sağlayan turlarımızda tamamen sıfır emisyonlu elektrikli araçlar ve enerji ihtiyacını karşılayan güneş paneli destekli üniteler kullanılmaktadır.")
        ex3 = ("Yerel İş Birliği ve Tasarım", "Bölge halkı istihdam edilmekte, menülerde tamamen yerel üreticilerden alınan ürünler kullanılmaktadır. Mimari yapılarımız doğanın silüetini bozmayan minimal yaklaşımla tasarlanmıştır.")
    else:
        st.markdown("<h2>Sustainable Scientific Tourism</h2>", unsafe_allow_html=True)
        title, desc = "Respect for Nature and the Sky", "Our fundamental mission while exploring the universe is to protect our world. Our sustainability principles cover not only environmental but also cultural harmony."
        ex1 = ("Light Pollution Reduction", "To prevent interfering with sky observation, only red-based, low-lumen floor lighting and motion-sensitive sensors are used in our facilities.")
        ex2 = ("Zero Carbon Footprint", "Our tours providing access to observation points use completely zero-emission electric vehicles and solar panel-supported units.")
        ex3 = ("Local Collaboration and Design", "Local people are employed, and products sourced entirely from local producers are used in menus. Our architectural structures are designed with a minimal approach that preserves nature's silhouette.")

    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    with col_center:
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh;" src="https://images.unsplash.com/photo-1502481851512-e9e2529bfbf9?q=80&w=1200&auto=format&fit=crop"></div>', unsafe_allow_html=True)
        st.markdown(f"<h3>{title}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p>{desc}</p>", unsafe_allow_html=True)
        st.write("")
        with st.expander(ex1[0]): st.write(ex1[1])
        with st.expander(ex2[0]): st.write(ex2[1])
        with st.expander(ex3[0]): st.write(ex3[1])

# ==============================================================================
# SAYFA 7: YATIRIMCI PORTALI
# ==============================================================================
elif menu_secimi in ["YATIRIMCI PORTALI", "INVESTOR PORTAL"]:
    if lang == "TR":
        st.markdown("<h2>Kurumsal İş Modeli & Gelecek Vizyonu</h2>", unsafe_allow_html=True)
        st.markdown("<p>Sadece yetkili erişim. Lütfen yatırımcı şifrenizi girin. (İpucu: stellaris2026)</p>", unsafe_allow_html=True)
        pw_label, msg_success, msg_error = "Kurumsal Şifre:", "Güvenlik Duvarı Aşıldı. Yönetici Paneline Erişim Sağlandı.", "Erişim Reddedildi. Hatalı Şifre."
        t_vision, t_phases = "5 Yıllık Büyüme Vizyonu", "Faz 2 (Kuzey Işıkları): İzlanda  |  Faz 3 (Çöl & Galaksi): Namibya"
        t_swot, t_swot_desc = "Rekabet Analizi (SWOT)", "<b>Güçlü Yönler:</b> Niş pazar, Premium hizmet, Çoklu-destinasyon.<br><b>Farkımız:</b> Rakiplerimiz tek lokasyona odaklanırken, biz küresel bir lüks marka ağı kuruyoruz."
        t_chart = "Büyüme Projeksiyonu (Hedef Kitle)"
        d_cols = {"Şili Operasyonları": [1000, 2500, 4800, 7500, 12000], "Yeni Zelanda Operasyonları": [800, 1900, 3500, 6000, 9500], "Gelecek Pazarlar": [0, 0, 1500, 4000, 8000]}
        d_index = ["Yıl 1", "Yıl 2", "Yıl 3", "Yıl 4", "Yıl 5"]
    else:
        st.markdown("<h2>Corporate Business Model & Future Vision</h2>", unsafe_allow_html=True)
        st.markdown("<p>Authorized access only. Please enter your investor password. (Hint: stellaris2026)</p>", unsafe_allow_html=True)
        pw_label, msg_success, msg_error = "Corporate Password:", "Security Firewall Breached. Access Granted to Admin Panel.", "Access Denied. Incorrect Password."
        t_vision, t_phases = "5-Year Growth Vision", "Phase 2 (Northern Lights): Iceland  |  Phase 3 (Desert & Galaxy): Namibia"
        t_swot, t_swot_desc = "Competitor Analysis (SWOT)", "<b>Strengths:</b> Niche market, Premium service, Multi-destination.<br><b>Our Difference:</b> While competitors focus on a single location, we are building a global luxury brand network."
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
            st.area_chart(pd.DataFrame(d_cols, index=d_index), color=["#B8860B", "#C5A059", "#4A3B1B"])
        elif sifre != "":
            st.error(msg_error)
