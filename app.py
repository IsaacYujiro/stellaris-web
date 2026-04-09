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

    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background-color: #051024 !important; color: #C5A059; text-align: center; }
    [data-testid="stSidebar"] { background-color: #030814 !important; border-right: 1px solid #B8860B !important; }

    div[role="radiogroup"] > label > div:first-of-type { display: none !important; }
    div[role="radiogroup"] p { color: #B8860B !important; font-family: 'Cinzel', serif !important; font-size: 1.05rem !important; font-weight: 600 !important; text-align: center !important; visibility: visible !important; display: block !important; width: 100%; margin-top: 5px; transition: all 0.3s ease; }
    div[role="radiogroup"] label:hover p { color: #D4AF37 !important; text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.4); }
    div[role="radiogroup"] label[aria-checked="true"] p { color: #D4AF37 !important; text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.8); border-bottom: 1px solid #B8860B; }

    [data-baseweb="select"] { background-color: #030814 !important; border: 1px solid #B8860B !important; border-radius: 4px; }
    [data-baseweb="select"] * { color: #C5A059 !important; font-family: 'Montserrat', sans-serif !important; }
    [data-testid="stSidebar"] .stAlert div { font-family: 'Montserrat', sans-serif !important; color: #B8860B !important; text-align: center !important; background-color: transparent !important; border: 1px solid #B8860B; }
    
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
    .stProgress > div > div > div > div { background-color: #B8860B !important; }
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
dil_secimi = st.sidebar.selectbox("DİL SEÇİMİ / LANGUAGE", ["Türkçe", "English"])
lang = "TR" if dil_secimi == "Türkçe" else "EN"
st.sidebar.write("---")

if lang == "TR":
    menu_secenekleri = [
        "ANA SAYFA", "LOKASYONLARIMIZ", "CANLI GÖZLEMEVİ", "KOZMİK TAKVİM", 
        "UZAY HAVADURUMU", "IŞIK KİRLİLİĞİ", "EKİPMANLAR", "ASTRO-FOTOĞRAF", 
        "YAPAY ZEKA", "REZERVASYON", "SÜRDÜRÜLEBİLİRLİK", "YATIRIMCI PORTALI"
    ]
    sistem_durumu = "Sistem: Çevrimiçi"
else:
    menu_secenekleri = [
        "HOME", "OUR LOCATIONS", "LIVE OBSERVATORY", "COSMIC CALENDAR", 
        "SPACE WEATHER", "LIGHT POLLUTION", "EQUIPMENT", "ASTRO-PHOTO", 
        "AI SIMULATOR", "BOOKING", "SUSTAINABILITY", "INVESTOR PORTAL"
    ]
    sistem_durumu = "System: Online"

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
    else:
        st.markdown("<h2>Discover the Limits of the Sky</h2>", unsafe_allow_html=True)
        st.markdown("<p>Stellaris was born for those who leave ordinary holiday concepts behind and turn their eyes to the depths of the universe. In the darkest and clearest points of the world, completely free from light pollution, we blend science and nature with flawless luxury. Write an unforgettable story under the stars with our night observation tours and premium accommodation options.</p>", unsafe_allow_html=True)
        
    st.write("---")
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
        st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?q=80&w=800&auto=format&fit=crop"><div class="service-content"><h3 class="service-title">{t_chile_title}</h3><p class="service-desc">{t_chile_desc}</p></div></div>""", unsafe_allow_html=True)
    with col_nz:
        st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=800&auto=format&fit=crop"><div class="service-content"><h3 class="service-title">{t_nz_title}</h3><p class="service-desc">{t_nz_desc}</p></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# YENİ SAYFA 3: CANLI GÖZLEMEVİ (TELESKOP KONTROL PANELİ)
# ==============================================================================
elif menu_secimi in ["CANLI GÖZLEMEVİ", "LIVE OBSERVATORY"]:
    if lang == "TR":
        st.markdown("<h2>Gözlemevi Uzaktan Kontrol Paneli</h2>", unsafe_allow_html=True)
        st.markdown("<p>Şili ve Yeni Zelanda'daki robotik teleskoplarımıza şifreli ağ üzerinden bağlanın. Derin uzay nesnelerini gerçek zamanlı inceleyin ve bilimsel ışık filtrelerini test edin.</p>", unsafe_allow_html=True)
        t_select = "Bağlanılacak İstasyonu Seçin:"
        t_opts = ["Atacama Alfa İstasyonu (Celestron 1100 HD)", "Tekapo Güney İstasyonu (Meade LX200 14'')"]
        t_btn = "Uydu Bağlantısı Kur (Uplink)"
        t_conn1 = "Güvenli bağlantı başlatılıyor..."
        t_conn2 = "Lens kapağı açılıyor, sensörler soğutuluyor..."
        t_conn3 = "Canlı yayın aktarıldı."
        t_ctrl = "Kamera Kontrolleri"
        t_zoom = "Dijital Yakınlaştırma (Zoom)"
        t_filter = "Astro-Filtreler (Işık Dalga Boyu)"
        t_f_opts = ["Görünür Işık (Visible Spectrum)", "H-Alpha Filtresi (Kızılötesi Algı)", "O-III Filtresi (Oksijen-3 İyonu)"]
    else:
        st.markdown("<h2>Observatory Remote Control Panel</h2>", unsafe_allow_html=True)
        st.markdown("<p>Connect to our robotic telescopes in Chile and New Zealand via an encrypted network. Examine deep space objects in real-time and test scientific light filters.</p>", unsafe_allow_html=True)
        t_select = "Select Station to Connect:"
        t_opts = ["Atacama Alpha Station (Celestron 1100 HD)", "Tekapo South Station (Meade LX200 14'')"]
        t_btn = "Establish Satellite Uplink"
        t_conn1 = "Initiating secure connection..."
        t_conn2 = "Opening lens cover, cooling sensors..."
        t_conn3 = "Live feed established."
        t_ctrl = "Camera Controls"
        t_zoom = "Digital Zoom"
        t_filter = "Astro-Filters (Light Wavelength)"
        t_f_opts = ["Visible Spectrum", "H-Alpha Filter (Infrared Perception)", "O-III Filter (Oxygen-3 Ion)"]

    st.write("---")
    
    if "telescope_connected" not in st.session_state:
        st.session_state.telescope_connected = False

    col_setup, col_empty = st.columns([1, 2])
    with col_setup:
        istasyon = st.selectbox(t_select, t_opts)
        st.write("")
        if st.button(t_btn):
            with st.spinner(t_conn1): time.sleep(1.5)
            with st.spinner(t_conn2): time.sleep(2)
            st.success(t_conn3)
            st.session_state.telescope_connected = True

    if st.session_state.telescope_connected:
        st.write("---")
        col_view, col_controls = st.columns([2, 1])
        
        with col_controls:
            st.markdown(f"<h3>{t_ctrl}</h3>", unsafe_allow_html=True)
            zoom_level = st.slider(t_zoom, 1.0, 3.0, 1.0, 0.1)
            filter_type = st.radio(t_filter, t_f_opts)
            
            # CSS Filtre Matematiği
            css_filter = "none"
            if "H-Alpha" in filter_type:
                # Kırmızı ağırlıklı yüksek kontrast (Hidrojen Gazı simülasyonu)
                css_filter = "sepia(100%) hue-rotate(-50deg) saturate(300%) contrast(1.5)"
            elif "O-III" in filter_type:
                # Mavi/Yeşil ağırlıklı (Oksijen iyonu simülasyonu)
                css_filter = "sepia(100%) hue-rotate(130deg) saturate(200%) contrast(1.2)"

        with col_view:
            # Orion Bulutsusu veya Andromeda (Teleskopa göre)
            if "Atacama" in istasyon:
                deep_space_img = "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=1200&auto=format&fit=crop"
            else:
                deep_space_img = "https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?q=80&w=1200&auto=format&fit=crop"

            st.markdown(f"""
            <div style="width: 100%; height: 450px; border: 3px solid #B8860B; border-radius: 8px; overflow: hidden; background-color: #000; position: relative; box-shadow: 0 0 30px rgba(184, 134, 11, 0.3);">
                <div style="position: absolute; top: 15px; left: 15px; color: red; font-family: monospace; font-size: 14px; font-weight: bold; z-index: 10;">● REC / LIVE</div>
                <div style="position: absolute; bottom: 15px; right: 15px; color: #B8860B; font-family: monospace; font-size: 12px; z-index: 10;">{istasyon.split(' ')[0]} - FOV: {zoom_level}x</div>
                <img src="{deep_space_img}" style="width: 100%; height: 100%; object-fit: cover; transform: scale({zoom_level}); filter: {css_filter}; transition: all 0.5s ease; transform-origin: center center;">
                <div style="position: absolute; top: 50%; left: 0; width: 100%; height: 1px; background-color: rgba(184, 134, 11, 0.4); pointer-events: none; z-index: 5;"></div>
                <div style="position: absolute; top: 0; left: 50%; width: 1px; height: 100%; background-color: rgba(184, 134, 11, 0.4); pointer-events: none; z-index: 5;"></div>
                <div style="position: absolute; top: 50%; left: 50%; width: 40px; height: 40px; border: 1px solid rgba(184, 134, 11, 0.8); border-radius: 50%; transform: translate(-50%, -50%); pointer-events: none; z-index: 5;"></div>
            </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# SAYFA 4: KOZMİK TAKVİM
# ==============================================================================
elif menu_secimi in ["KOZMİK TAKVİM", "COSMIC CALENDAR"]:
    if lang == "TR":
        st.markdown("<h2>Kozmik Takvim & Nadir Fenomenler</h2>", unsafe_allow_html=True)
        st.markdown("<p>Astro-turizmde zamanlama her şeydir. Dünyanın en karanlık noktalarında, yaklaşan en nadir uzay olaylarına tanıklık etmek için yerinizi ayırtın.</p>", unsafe_allow_html=True)
        ev_label = "Keşfetmek İstediğiniz Etkinliği Seçin:"
        events = ["Perseid Göktaşı Yağmuru (Ağustos)", "Satürn Karşı Konumu - Halka Gözlemi (Eylül)", "Tam Güneş Tutulması Özel Turu (Kış Dönemi)"]
        btn_label = "Bu Tarih İçin VIP Rezervasyon Başlat"
    else:
        st.markdown("<h2>Cosmic Calendar & Rare Phenomena</h2>", unsafe_allow_html=True)
        st.markdown("<p>Timing is everything in astro-tourism. Secure your spot to witness the rarest upcoming space events from the darkest points on Earth.</p>", unsafe_allow_html=True)
        ev_label = "Select the Event You Want to Explore:"
        events = ["Perseid Meteor Shower (August)", "Saturn Opposition - Ring Observation (September)", "Total Solar Eclipse Exclusive Tour (Winter Season)"]
        btn_label = "Start VIP Booking for This Date"

    st.write("---")
    selected_event = st.selectbox(ev_label, events)
    st.write("")
    col_info, col_metrics = st.columns([2, 1])
    
    with col_info:
        if "Perseid" in selected_event:
            img_url, rarity = "https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?q=80&w=800&auto=format&fit=crop", 60
            e_title = "Perseid Göktaşı Şöleni" if lang == "TR" else "Perseid Meteor Spectacle"
            e_desc = "Saatte ortalama 100'den fazla ateş topunun atmosfere girdiği görkemli meteor yağmuru." if lang == "TR" else "Spectacular meteor shower with over 100 fireballs per hour."
            e_equip = "Ekipman: Çıplak Göz & Geniş Açılı Lensler" if lang == "TR" else "Equipment: Naked Eye & Wide Angle Lenses"
        elif "Sat" in selected_event:
            img_url, rarity = "https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=800&auto=format&fit=crop", 85
            e_title = "Satürn Karşı Konumu" if lang == "TR" else "Saturn Opposition"
            e_desc = "Satürn'ün Dünya'ya en yakın ve en parlak olduğu dönem." if lang == "TR" else "The period when Saturn is closest and brightest to Earth."
            e_equip = "Ekipman: Meade LX200 14'' Advanced" if lang == "TR" else "Equipment: Meade LX200 14'' Advanced"
        else:
            img_url, rarity = "https://images.unsplash.com/photo-1539321908154-049275965646?q=80&w=800&auto=format&fit=crop", 98
            e_title = "Tam Güneş Tutulması" if lang == "TR" else "Total Solar Eclipse"
            e_desc = "Gündüzün geceye döndüğü o efsanevi an." if lang == "TR" else "That legendary moment when day turns into night."
            e_equip = "Ekipman: Lunt Solar Systems H-Alpha" if lang == "TR" else "Equipment: Lunt Solar Systems H-Alpha"

        st.markdown(f"""<div style="border: 1px solid #B8860B; border-radius: 8px; padding: 20px; background: #030814;"><h3 style="text-align: left !important; color: #D4AF37 !important;">{e_title}</h3><img src="{img_url}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px; margin-bottom: 15px; border: 1px solid #B8860B;"><p style="text-align: left !important;">{e_desc}</p><p style="text-align: left !important; font-weight: bold; color: #B8860B !important;">{e_equip}</p></div>""", unsafe_allow_html=True)

    with col_metrics:
        st.markdown("<br>", unsafe_allow_html=True)
        st.metric(label="Görüş Kalitesi" if lang=="TR" else "Visibility", value="Ultra HD", delta="Bulutsuzluk %99" if lang=="TR" else "99% Cloudless")
        st.metric(label="Atmosfer" if lang=="TR" else "Atmosphere", value="5/5", delta="Kusursuz" if lang=="TR" else "Flawless")
        st.markdown(f"<p style='text-align: left !important; color: #C5A059;'>{'Nadirlik Derecesi' if lang=='TR' else 'Event Rarity'}</p>", unsafe_allow_html=True)
        st.progress(rarity)
        st.write("")
        if st.button(btn_label): st.success("Talebiniz iletildi." if lang=="TR" else "Request submitted.")

# ==============================================================================
# SAYFA 5: UZAY HAVADURUMU
# ==============================================================================
elif menu_secimi in ["UZAY HAVADURUMU", "SPACE WEATHER"]:
    if lang == "TR":
        st.markdown("<h2>Canlı Uzay Hava Durumu & Aurora Tahmini</h2>", unsafe_allow_html=True)
        st.markdown("<p>Güneş fırtınalarını, jeomanyetik dalgalanmaları canlı izleyin ve Güney Işıkları'nı (Aurora Australis) yakalama ihtimalinizi simüle edin.</p>", unsafe_allow_html=True)
        m1_l, m1_v, m1_d = "Kp İndeksi (Jeomanyetik Güç)", "6.33", "+1.2 (G2 Fırtınası)"
        m2_l, m2_v, m2_d = "Güneş Rüzgarı Hızı", "540 km/s", "+45 km/s"
        m3_l, m3_v, m3_d = "Bz (Manyetik Alan)", "-5.2 nT", "Güneye Yönlü (Olumlu)"
        chart_title, calc_title = "3 Günlük Jeomanyetik Aktivite", "Aurora İhtimal Hesaplayıcı"
        lat_label = "Bulunduğunuz Enlem (Tekapo = 44°)"
    else:
        st.markdown("<h2>Live Space Weather & Aurora Forecast</h2>", unsafe_allow_html=True)
        st.markdown("<p>Monitor solar storms, geomagnetic fluctuations live, and simulate your chances of catching the Southern Lights (Aurora Australis).</p>", unsafe_allow_html=True)
        m1_l, m1_v, m1_d = "Kp Index (Geomagnetic Power)", "6.33", "+1.2 (G2 Storm)"
        m2_l, m2_v, m2_d = "Solar Wind Speed", "540 km/s", "+45 km/s"
        m3_l, m3_v, m3_d = "Bz (Magnetic Field)", "-5.2 nT", "Southward (Favorable)"
        chart_title, calc_title = "3-Day Geomagnetic Activity", "Aurora Probability Calculator"
        lat_label = "Your Latitude (Tekapo = 44°)"

    st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.metric(m1_l, m1_v, m1_d); c2.metric(m2_l, m2_v, m2_d); c3.metric(m3_l, m3_v, m3_d)
    
    st.write("---")
    col_chart, col_calc = st.columns([2, 1])
    
    with col_chart:
        st.markdown(f"<h3>{chart_title}</h3>", unsafe_allow_html=True)
        st.area_chart(pd.DataFrame({"Kp": [2.3, 4.0, 6.3, 5.1, 3.2, 2.0, 4.5, 7.1, 5.0]}, index=["D1-00", "D1-08", "D1-16", "D2-00", "D2-08", "D2-16", "D3-00", "D3-08", "D3-16"]), color="#B8860B")

    with col_calc:
        st.markdown(f"<h3>{calc_title}</h3>", unsafe_allow_html=True)
        st.write("")
        enlem = st.slider(lat_label, min_value=10, max_value=70, value=44, step=1)
        ihtimal = int(min(100, max(0, (enlem * 1.2) + (6.33 * 10) - 60)))
        st.markdown(f"<div class='price-tag' style='font-size:4rem;'>%{ihtimal}</div>", unsafe_allow_html=True)
        if ihtimal > 75: st.success("Mükemmel Koşullar!" if lang == "TR" else "Excellent Conditions!")
        elif ihtimal > 40: st.warning("Ufukta yeşil bir parıltı yakalama şansınız var." if lang == "TR" else "Chance of green glow on the horizon.")
        else: st.error("Aktivite zayıf." if lang == "TR" else "Weak activity.")

# ==============================================================================
# SAYFA 6: IŞIK KİRLİLİĞİ
# ==============================================================================
elif menu_secimi in ["IŞIK KİRLİLİĞİ", "LIGHT POLLUTION"]:
    st.markdown("<h2>Bortle Scale: Light Pollution Simulator</h2>", unsafe_allow_html=True)
    slider_label = "Gökyüzü Kalitesi / Sky Quality (9 = Şehir/City, 1 = Kusursuz/Perfect)"
    st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl:
        bortle_val = st.slider(slider_label, min_value=1, max_value=9, value=9, step=2)
        st.write("")
        if bortle_val == 9: st.info("Bortle 9: Inner City / İç Şehir. No details.")
        elif bortle_val == 1: st.success("Bortle 1: Atacama/Tekapo. Perfect Darkness / Kusursuz Karanlık.")
        else: st.warning(f"Bortle {bortle_val}: Average conditions.")

    sky_glow_opacity = (bortle_val - 1) / 8.0  
    star_brightness = 1.2 - sky_glow_opacity   
    base_stars_img = "https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200&auto=format&fit=crop"

    with col_view:
        st.markdown(f"""
        <div style="position: relative; width: 100%; height: 400px; border: 2px solid #B8860B; border-radius: 4px; overflow: hidden; background-color: #000; box-shadow: 0 5px 25px rgba(0,0,0,0.8);">
            <img src="{base_stars_img}" style="width: 100%; height: 100%; object-fit: cover; filter: brightness({star_brightness}) contrast(1.2); transition: all 0.8s ease;">
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(200,100,50,0.9), rgba(50,70,100,0.8)); opacity: {sky_glow_opacity}; transition: opacity 0.8s ease; pointer-events: none;"></div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# SAYFA 7: GÖZLEM KOŞULLARI & EKİPMAN
# ==============================================================================
elif menu_secimi in ["EKİPMANLAR", "EQUIPMENT"]:
    st.markdown("<h2>VIP Gözlem Ekipmanları / Observation Equipment</h2>", unsafe_allow_html=True)
    st.write("---")
    e1, e2, e3 = st.columns(3)
    with e1: st.markdown(f"""<div class="service-card" style="box-shadow:none; border:none;"><img class="service-img" src="https://images.unsplash.com/photo-1517976487492-5750f3195933?q=80&w=800&auto=format&fit=crop" style="border-radius:8px; border: 1px solid #B8860B;"><div class="service-content" style="padding:15px;"><h3 class="service-title" style="font-size:1.1rem;">Celestron CPC 1100 HD</h3><p class="service-desc">Deep Space / Derin Uzay</p></div></div>""", unsafe_allow_html=True)
    with e2: st.markdown(f"""<div class="service-card" style="box-shadow:none; border:none;"><img class="service-img" src="https://images.unsplash.com/photo-1506443432602-ac2fcd6f54e0?q=80&w=800&auto=format&fit=crop" style="border-radius:8px; border: 1px solid #B8860B;"><div class="service-content" style="padding:15px;"><h3 class="service-title" style="font-size:1.1rem;">Meade LX200 14''</h3><p class="service-desc">Planetary / Gezegen</p></div></div>""", unsafe_allow_html=True)
    with e3: st.markdown(f"""<div class="service-card" style="box-shadow:none; border:none;"><img class="service-img" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop" style="border-radius:8px; border: 1px solid #B8860B;"><div class="service-content" style="padding:15px;"><h3 class="service-title" style="font-size:1.1rem;">Lunt Solar Systems</h3><p class="service-desc">Solar Flares / Güneş Patlamaları</p></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 8: ASTRO-FOTOĞRAF SİMÜLATÖRÜ
# ==============================================================================
elif menu_secimi in ["ASTRO-FOTOĞRAF", "ASTRO-PHOTO"]:
    st.markdown("<h2>Astro-Photography Simulator</h2>", unsafe_allow_html=True)
    st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl:
        st.markdown(f"<h3 style='text-align: left !important;'>Parametreler</h3>", unsafe_allow_html=True)
        iso_val = st.slider("ISO Değeri / ISO Value", 100, 6400, 800, step=100)
        exp_val = st.slider("Pozlama Süresi / Exposure Time (s)", 1, 30, 10, step=1)
        st.write("")
        render_btn = st.button("Deklanşöre Bas / Shutter")

    brightness = 0.15 + (exp_val / 30.0) * 0.6 + (iso_val / 6400.0) * 0.5
    noise_opacity = (iso_val / 6400.0) * 0.70
    base_img = "https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200&auto=format&fit=crop"
    
    with col_view:
        st.markdown(f"""
        <div style="position: relative; width: 100%; border: 2px solid #B8860B; border-radius: 4px; overflow: hidden; background-color: #000; box-shadow: 0 5px 25px rgba(0,0,0,0.8);">
            <img src="{base_img}" style="width: 100%; display: block; filter: brightness({brightness}) contrast(1.2); transition: filter 0.5s ease;">
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-image: url('https://www.transparenttextures.com/patterns/stardust.png'); opacity: {noise_opacity}; mix-blend-mode: screen; pointer-events: none; transition: opacity 0.5s ease;"></div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# SAYFA 9: YAPAY ZEKA SİMÜLATÖRÜ
# ==============================================================================
elif menu_secimi in ["YAPAY ZEKA", "AI SIMULATOR"]:
    st.markdown("<h2>AI-Powered Deep Space Simulation</h2>", unsafe_allow_html=True)
    st.write("---")
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        secilen_cisim = st.selectbox("Celestial Object", ["Sarmal Galaksi / Spiral Galaxy", "Nebula", "Süpernova / Supernova"])
        if st.button("Simülasyonu Başlat / Run AI"):
            with st.spinner("İşleniyor / Processing..."): time.sleep(2)
            st.success("Tamamlandı / Complete")
            if "Galaksi" in secilen_cisim or "Galaxy" in secilen_cisim: gen_img = "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=1200&auto=format&fit=crop"
            elif "Nebula" in secilen_cisim: gen_img = "https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?q=80&w=1200&auto=format&fit=crop"
            else: gen_img = "https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?q=80&w=1200&auto=format&fit=crop"
            st.markdown(f'<div class="hero-container"><img class="hero-image" style="height:auto; filter: brightness(80%); border: 3px solid #D4AF37;" src="{gen_img}"></div>', unsafe_allow_html=True)

# ==============================================================================
# SAYFA 10: REZERVASYON
# ==============================================================================
elif menu_secimi in ["REZERVASYON", "BOOKING"]:
    st.markdown("<h2>Deneyimler & Online Rezervasyon / Booking</h2>", unsafe_allow_html=True)
    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    with col_center:
        deneyim_turu = st.radio("", ["Gece Gözlem Turu ($150)", "Astro-Fotoğrafçılık Workshop ($250)", "VIP Premium Çöl Konaklaması ($800)"], label_visibility="collapsed")
        st.write("---")
        col_form1, col_form2 = st.columns(2)
        with col_form1: secilen_tarih = st.date_input("Tarih / Date", min_value=datetime.date.today())
        with col_form2: kisi_sayisi = st.slider("Misafir / Guests", 1, 8, 2)
        
        fiyat = 150 if "150" in deneyim_turu else 250 if "250" in deneyim_turu else 800
        st.markdown(f"<div class='price-tag'>${(fiyat * kisi_sayisi):,} <span style='font-size: 1rem; color: #C5A059;'>USD Toplam / Total</span></div>", unsafe_allow_html=True)
        if st.button("Rezervasyon Gönder / Send Booking"):
            with st.spinner("Bağlanılıyor / Connecting..."): time.sleep(2) 
            st.success("Talebiniz alınmıştır / Request received.")

# ==============================================================================
# SAYFA 11: SÜRDÜRÜLEBİLİRLİK
# ==============================================================================
elif menu_secimi in ["SÜRDÜRÜLEBİLİRLİK", "SUSTAINABILITY"]:
    st.markdown("<h2>Sürdürülebilir Bilimsel Turizm / Sustainability</h2>", unsafe_allow_html=True)
    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    with col_center:
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh;" src="https://images.unsplash.com/photo-1502481851512-e9e2529bfbf9?q=80&w=1200&auto=format&fit=crop"></div>', unsafe_allow_html=True)
        with st.expander("Işık Kirliliği Azaltımı / Light Pollution Reduction"): st.write("Tesislerimizde yalnızca kırmızı bazlı, düşük lümenli zemin aydınlatmaları kullanılır.")
        with st.expander("Sıfır Karbon Ayak İzi / Zero Carbon"): st.write("Turlarımızda tamamen sıfır emisyonlu elektrikli araçlar kullanılır.")

# ==============================================================================
# SAYFA 12: YATIRIMCI PORTALI
# ==============================================================================
elif menu_secimi in ["YATIRIMCI PORTALI", "INVESTOR PORTAL"]:
    st.markdown("<h2>Kurumsal İş Modeli / Corporate Portal</h2>", unsafe_allow_html=True)
    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 4, 1])
    with col_center:
        sifre = st.text_input("Kurumsal Şifre / Corporate Password (stellaris2026):", type="password")
        if sifre == "stellaris2026":
            st.success("Erişim Sağlandı / Access Granted")
            st.write("---")
            st.area_chart(pd.DataFrame({"Şili / Chile": [1000, 2500, 4800, 7500, 12000], "Yeni Zelanda / NZ": [800, 1900, 3500, 6000, 9500]}, index=["Yıl 1", "Yıl 2", "Yıl 3", "Yıl 4", "Yıl 5"]), color=["#B8860B", "#C5A059"])
        elif sifre != "":
            st.error("Hatalı Şifre / Incorrect Password")
