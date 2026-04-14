import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import datetime
import time
import os
import glob
import random
import math
import json

# ==============================================================================
# SİTE YAPILANDIRMASI VE ULTRA-LÜKS ANİMASYONLU CSS
# ==============================================================================
st.set_page_config(page_title="Stellaris | Premium Astro-Tourism", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&family=Cinzel:wght@400;600;700&display=swap');

    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #030814; }
    ::-webkit-scrollbar-thumb { background: #B8860B; border-radius: 4px; border: 1px solid #030814; }
    ::-webkit-scrollbar-thumb:hover { background: #D4AF37; }

    .stApp { 
        background-color: #051024 !important; 
        background-image: 
            radial-gradient(white, rgba(255,255,255,.15) 2px, transparent 30px),
            radial-gradient(white, rgba(255,255,255,.1) 1px, transparent 20px),
            radial-gradient(white, rgba(255,255,255,.05) 2px, transparent 40px);
        background-size: 550px 550px, 350px 350px, 250px 250px;
        background-position: 0 0, 40px 60px, 130px 270px;
        animation: starBackground 150s linear infinite;
    }
    @keyframes starBackground { 0% { background-position: 0 0, 40px 60px, 130px 270px; } 100% { background-position: -550px -550px, -310px -290px, 380px 520px; } }

    header { background-color: transparent !important; }
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; color: #E0E0E0; text-align: center; }
    
    [data-testid="stSidebar"] { background: rgba(3, 8, 20, 0.8) !important; backdrop-filter: blur(15px) !important; border-right: 1px solid #B8860B !important; }
    [data-testid="stSidebar"] * { color: #B8860B !important; }

    div[role="radiogroup"] > label > div:first-of-type { display: none !important; }
    div[role="radiogroup"] p { color: #B8860B !important; font-family: 'Cinzel', serif !important; font-size: 1.05rem !important; font-weight: 600 !important; text-align: center !important; visibility: visible !important; display: block !important; width: 100%; margin-top: 5px; transition: all 0.4s ease; padding: 8px 0; border-radius: 4px;}
    div[role="radiogroup"] label:hover p { color: #D4AF37 !important; text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.5); background: rgba(184, 134, 11, 0.1); transform: translateX(5px);}
    div[role="radiogroup"] label[aria-checked="true"] p { color: #FFD700 !important; text-shadow: 0px 0px 15px rgba(255, 215, 0, 0.8); border-bottom: 1px solid #B8860B; background: rgba(184, 134, 11, 0.15);}

    [data-baseweb="select"] { background-color: rgba(3, 8, 20, 0.6) !important; border: 1px solid #B8860B !important; border-radius: 4px; backdrop-filter: blur(5px);}
    [data-testid="stSidebar"] .stAlert div { font-family: 'Montserrat', sans-serif !important; color: #B8860B !important; text-align: center !important; background-color: transparent !important; border: 1px solid #B8860B; }
    
    div[data-testid="stMetricValue"] { color: #D4AF37 !important; font-family: 'Cinzel', serif !important; font-size: 2.5rem !important; text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.5); transition: transform 0.3s ease; display: inline-block;}
    div[data-testid="stMetricValue"]:hover { transform: scale(1.1); color: #FFD700 !important; }
    div[data-testid="stMetricLabel"] { color: #B8860B !important; font-family: 'Montserrat', sans-serif !important; font-size: 1.1rem !important; }
    
    h1, h2, h3, h4, h5, h6 { font-family: 'Cinzel', serif; font-weight: 700; text-align: center !important; width: 100%; background: linear-gradient(45deg, #C5A059, #F3E5AB, #D4AF37, #B8860B); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: shine 5s linear infinite;}
    @keyframes shine { to { background-position: 200% center; } }
    
    .hero-title { font-size: 5rem; letter-spacing: 8px; margin-bottom: 10px; animation: pulseGlow 3s infinite alternate; }
    @keyframes pulseGlow { from { text-shadow: 0 0 10px rgba(212,175,55,0.2); } to { text-shadow: 0 0 25px rgba(212,175,55,0.6); } }

    p { text-align: center !important; margin: 0 auto 15px auto !important; max-width: 900px; line-height: 1.8; color: #a8b2d1 !important; font-weight: 300;}
    hr { border-top: 1px solid rgba(184, 134, 11, 0.3) !important; width: 60%; margin: 40px auto !important; }

    .block-container { animation: fadeSlideUp 1s cubic-bezier(0.165, 0.84, 0.44, 1); }
    @keyframes fadeSlideUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }

    .hero-image { width: 100%; max-width: 1200px; height: 55vh; object-fit: cover; border-radius: 8px; filter: brightness(60%); border: 1px solid rgba(184, 134, 11, 0.4); animation: slowZoom 30s infinite alternate cubic-bezier(0.455, 0.03, 0.515, 0.955); }
    @keyframes slowZoom { from { transform: scale(1); } to { transform: scale(1.08); } }
    .hero-container { position: relative; text-align: center; margin-bottom: 40px; display: flex; justify-content: center; overflow: hidden; border-radius: 8px; box-shadow: 0 15px 40px rgba(0,0,0,0.6);}

    .service-card, .planet-card, .stat-box { background: rgba(5, 16, 36, 0.4) !important; backdrop-filter: blur(12px) !important; border-radius: 12px !important; border: 1px solid rgba(184, 134, 11, 0.3) !important; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5) !important; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; overflow: hidden; }
    .service-card:hover, .planet-card:hover, .stat-box:hover { transform: translateY(-5px) !important; border-color: rgba(212, 175, 55, 0.8) !important; box-shadow: 0 15px 40px rgba(184, 134, 11, 0.2) !important; }
    
    .stat-box { padding: 20px; text-align: center; margin-top: 20px; }
    .stat-number { font-family: 'Cinzel', serif; font-size: 2.5rem; color: #D4AF37; font-weight: bold; margin-bottom: 5px; }
    .stat-label { font-size: 0.9rem; text-transform: uppercase; color: #8892b0; letter-spacing: 1px; }

    .service-img { width: 100%; height: 250px; object-fit: cover; border-bottom: 1px solid rgba(184, 134, 11, 0.3); transition: transform 0.5s; }
    .service-card:hover .service-img { transform: scale(1.05); }
    .service-content { padding: 25px; }
    .price-tag { font-family: 'Cinzel', serif; font-size: 3rem; color: #D4AF37; font-weight: 700; margin: 25px 0; text-align: center; text-shadow: 0px 0px 20px rgba(184, 134, 11, 0.4); }
    
    .stButton { display: flex; justify-content: center; margin-top: 20px; }
    div.stButton > button:first-child { background: linear-gradient(135deg, rgba(3,8,20,0.9) 0%, rgba(17,34,64,0.9) 100%) !important; color: #D4AF37 !important; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 1.1rem; padding: 15px 50px; border: 1px solid rgba(184, 134, 11, 0.5) !important; border-radius: 30px; transition: all 0.4s ease; letter-spacing: 2px; text-transform: uppercase; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    div.stButton > button:first-child:hover { background: linear-gradient(135deg, rgba(184, 134, 11, 0.2) 0%, rgba(212, 175, 55, 0.3) 100%) !important; color: #FFF !important; border-color: #D4AF37 !important; transform: translateY(-3px) scale(1.02); box-shadow: 0 0 20px rgba(212, 175, 55, 0.6) !important; }

    [data-baseweb="tab-list"] { justify-content: center; gap: 8px; flex-wrap: wrap; margin-bottom: 20px;}
    [data-baseweb="tab"] { background: rgba(5, 16, 36, 0.6) !important; color: #B8860B !important; font-family: 'Cinzel', serif; font-size: 0.95rem; padding: 10px 20px; border-radius: 30px; border: 1px solid rgba(184,134,11,0.2) !important; transition: all 0.3s ease;}
    [aria-selected="true"] { background: rgba(184, 134, 11, 0.15) !important; color: #FFD700 !important; border-color: #D4AF37 !important; box-shadow: 0 0 15px rgba(184,134,11,0.2); }
    
    .stProgress > div > div > div > div { background: linear-gradient(90deg, #8B6508, #D4AF37, #F3E5AB) !important; }
    
    .spinning-planet { width: 250px; height: 250px; border-radius: 50%; display: block; margin: 0 auto 20px auto; box-shadow: inset -25px -25px 40px rgba(0,0,0,0.9), 0 0 30px rgba(184, 134, 11, 0.3); animation: spin 40s linear infinite; object-fit: cover;}
    @keyframes spin { 100% { transform: rotate(360deg); } }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    
    .mission-box { background: rgba(3, 8, 20, 0.7); border-left: 4px solid #D4AF37; padding: 30px; margin-bottom: 25px; border-radius: 0 8px 8px 0; text-align: left !important; box-shadow: 0 5px 15px rgba(0,0,0,0.4);}
    .mission-box h3 { text-align: left !important; margin-bottom: 15px; color: #D4AF37; font-size: 1.6rem;}
    .mission-box p { text-align: left !important; font-size: 1.05rem; color: #E0E0E0 !important; line-height: 1.8;}
    
    .checkbox-container { display: flex; justify-content: center; margin-top: 15px; color: #D4AF37; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# SİSTEM DURUMU VE OTURUM KONTROLÜ
# ==============================================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = ""

# ==============================================================================
# AKILLI LOGO BULUCU VE SİDEBAR
# ==============================================================================
bulunan_logo = None
resimler = glob.glob("*.jpeg") + glob.glob("*.jpg") + glob.glob("*.png")
for resim in resimler:
    if "logo" in resim.lower() or "whatsapp" in resim.lower() or "image" in resim.lower():
        bulunan_logo = resim; break
if not bulunan_logo and resimler: bulunan_logo = resimler[0] if resimler else None

if bulunan_logo: st.sidebar.image(bulunan_logo, use_container_width=True)
else: st.sidebar.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin-top: 20px; color: #B8860B;'>Stellaris</h2>", unsafe_allow_html=True)

st.sidebar.write("---")
dil_secimi = st.sidebar.selectbox("DİL / LANGUAGE", ["Türkçe", "English"])
lang = "TR" if dil_secimi == "Türkçe" else "EN"

if st.session_state.logged_in:
    st.sidebar.markdown(f"<div style='text-align:center; color:#D4AF37; font-family:Montserrat; margin-bottom:10px;'><b>👤 {st.session_state.current_user}</b></div>", unsafe_allow_html=True)

st.sidebar.write("---")

# Tamamen Ciddi ve Kurumsal Menü Yapısı (AI ve Pasaport Yok)
menu_secenekleri = [
    "ANA SAYFA", "LOKASYONLARIMIZ", "CANLI GÖZLEMEVİ", "3D SİMÜLASYONLAR", "KARA DELİK SİM.",
    "VİDEOLAR GALERİSİ", "KOZMİK TAKVİM", "UZAY HAVADURUMU", "IŞIK KİRLİLİĞİ", 
    "EKİPMANLAR", "ASTRO-FOTOĞRAF", "VIP REZERVASYON", "VİZYON & SÜRDÜRÜLEBİLİRLİK", "YATIRIMCI PORTALI"
] if lang == "TR" else [
    "HOME", "OUR LOCATIONS", "LIVE OBSERVATORY", "3D SIMULATIONS", "BLACK HOLE SIM.",
    "VIDEO GALLERY", "COSMIC CALENDAR", "SPACE WEATHER", "LIGHT POLLUTION", 
    "EQUIPMENT", "ASTRO-PHOTO", "VIP BOOKING", "VISION & SUSTAINABILITY", "INVESTOR PORTAL"
]

menu_secimi = st.sidebar.radio("Nav", menu_secenekleri, label_visibility="collapsed")
st.sidebar.write("---")

# MÜZİK ÇALAR
st.sidebar.markdown(f"<p style='color:#B8860B; font-size:0.8rem; font-weight:bold; margin-bottom:5px !important;'>{'Kozmik Ambiyans Sesi' if lang == 'TR' else 'Cosmic Ambient Audio'}</p>", unsafe_allow_html=True)
st.sidebar.markdown("""
<audio controls autoplay loop style="width: 100%; height: 30px; outline: none; border-radius: 4px; opacity: 0.8;">
    <source src="https://cdn.pixabay.com/audio/2022/11/22/audio_febc508520.mp3" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)
st.sidebar.write("---")
st.sidebar.info("Sistem: Çevrimiçi" if lang == "TR" else "System: Online")

def auto_refresh_image(img_id, img_url, refresh_rate_ms, title, max_width="600px", filter_css="none"):
    return f"""
    <div style="border: 1px solid rgba(184, 134, 11, 0.3); border-radius: 12px; position: relative; overflow: hidden; text-align: center; background: rgba(5,16,36,0.5); backdrop-filter: blur(10px); padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        <div style="position: absolute; top: 15px; left: 15px; background: rgba(0,0,0,0.7); padding: 6px 15px; color: #00e676; font-family: monospace; font-weight: bold; border: 1px solid rgba(0,230,118,0.4); z-index: 10; border-radius: 30px; font-size:12px; box-shadow: 0 0 10px rgba(0,230,118,0.2);">
            <span style="animation: blink 1s infinite;">●</span> {title}
        </div>
        <img id="{img_id}" src="{img_url}" style="width: 100%; max-width: {max_width}; border-radius: 8px; filter: {filter_css};">
    </div>
    <script>
        setInterval(function() {{ 
            var img = document.getElementById('{img_id}');
            if (img) {{ img.src = '{img_url}?time=' + new Date().getTime(); }}
        }}, {refresh_rate_ms});
    </script>
    """

# ==============================================================================
# SAYFA 1: ANA SAYFA (KURUMSAL DETAYLAR VE İSTATİSTİKLER EKLENDİ)
# ==============================================================================
if menu_secimi in ["ANA SAYFA", "HOME"]:
    col_space1, col_hero, col_space3 = st.columns([1, 2, 1])
    with col_hero:
        if bulunan_logo: st.image(bulunan_logo, use_container_width=True)
        else:
            st.markdown("<h1 class='hero-title'>STELLARIS</h1>", unsafe_allow_html=True)
            st.markdown(f"<p class='hero-subtitle' style='color:#D4AF37; letter-spacing:4px; font-weight:bold;'>{'ULUSLARARASI ASTRO-TURİZM HOLDİNGİ' if lang == 'TR' else 'INTERNATIONAL ASTRO-TOURISM HOLDING'}</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("<h2>{}</h2>".format("Sınırların Ötesinde Bir Lüks" if lang == "TR" else "Luxury Beyond Borders"), unsafe_allow_html=True)
    home_desc = "Stellaris, sıradan tatil anlayışını geride bırakıp gözlerini evrenin derinliklerine çeviren seçkin bireyler için tasarlanmıştır. Işık kirliliğinden %100 arındırılmış dünyanın en karanlık noktalarında, kişiye özel cam fanus (Glass Dome) konaklamaları, Michelin yıldızlı gastronomi deneyimi ve özel jet transferleri ile bilim ve ultra-lüksü kusursuz bir uyumla harmanlıyoruz." if lang == "TR" else "Stellaris is designed for distinguished individuals who leave ordinary holidays behind and turn their eyes to the depths of the universe. In the darkest points of the world, 100% free from light pollution, we blend science and ultra-luxury flawlessly with personalized Glass Dome accommodations, Michelin-starred gastronomy, and private jet transfers."
    st.markdown(f"<p>{home_desc}</p>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown(f"<div class='stat-box'><div class='stat-number'>500+</div><div class='stat-label'>{'Bulutsuz Gece' if lang=='TR' else 'Clear Nights'}</div></div>", unsafe_allow_html=True)
    with c2: st.markdown(f"<div class='stat-box'><div class='stat-number'>$120M</div><div class='stat-label'>{'Yatırım Hacmi' if lang=='TR' else 'Investment Volume'}</div></div>", unsafe_allow_html=True)
    with c3: st.markdown(f"<div class='stat-box'><div class='stat-number'>2</div><div class='stat-label'>{'Özel Rezerv' if lang=='TR' else 'Exclusive Reserves'}</div></div>", unsafe_allow_html=True)
    with c4: st.markdown(f"<div class='stat-box'><div class='stat-number'>%100</div><div class='stat-label'>{'VIP Gizlilik' if lang=='TR' else 'VIP Privacy'}</div></div>", unsafe_allow_html=True)
    
    st.write("---")
    col_space1, col_image, col_space2 = st.columns([1, 8, 1])
    with col_image:
        st.markdown('<div class="hero-container"><img class="hero-image" src="https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=2000&auto=format&fit=crop"></div>', unsafe_allow_html=True)

# ==============================================================================
# SAYFA 2: LOKASYONLARIMIZ (ZENGİNLEŞTİRİLDİ)
# ==============================================================================
elif menu_secimi in ["LOKASYONLARIMIZ", "OUR LOCATIONS"]:
    st.markdown("<h2>{}</h2>".format("Hedef Ülkeler ve Küresel Pazar" if lang == "TR" else "Target Locations & Global Market"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Sıfır ışık kirliliğine sahip, uluslararası koruma altındaki stratejik karanlık gökyüzü rezervleri." if lang == "TR" else "Strategic dark sky reserves under international protection with zero light pollution."), unsafe_allow_html=True)
    st.write("---")
    col_space1, col_chile, col_nz, col_space2 = st.columns([1, 4, 4, 1])
    
    desc_chile = "Dünyanın en kurak çölü olan Atacama'da, 4.000 metre rakımda yer alan tesisimiz, yılda 300 günden fazla bulutsuz gece garantisi sunar. Ünlü ALMA gözlemevine komşu olan bu lokasyonda, size özel panoramik cam fanuslarda (Glass Dome) konaklayarak Samanyolu'nu yatağınızdan izleme ayrıcalığını yaşayacaksınız." if lang == "TR" else "Located at an altitude of 4,000 meters in Atacama, the driest desert in the world, our facility guarantees over 300 clear nights a year. Neighboring the famous ALMA observatory, you will experience the privilege of watching the Milky Way from your bed by staying in personalized panoramic Glass Domes."
    desc_nz = "UNESCO tarafından 'Uluslararası Karanlık Gökyüzü Rezervi' ilan edilen Tekapo Gölü, gezegenimizin en berrak atmosferlerinden birine sahiptir. Mount John Gözlemevi'ne özel VIP erişim hakkı ile Güney Haçı takımyıldızını ve şanslı gecelerde muazzam Aurora Australis (Güney Işıkları) fenomenini deneyimleyin." if lang == "TR" else "Lake Tekapo, declared an 'International Dark Sky Reserve' by UNESCO, has one of the clearest atmospheres on our planet. Experience the Southern Cross constellation and the magnificent Aurora Australis (Southern Lights) phenomenon with exclusive VIP access to the Mount John Observatory."

    with col_chile:
        st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?q=80&w=800"><div class="service-content"><h3 class="service-title">{"Atacama Çölü, Şili" if lang=="TR" else "Atacama Desert, Chile"}</h3><p class="service-desc">{desc_chile}</p></div></div>""", unsafe_allow_html=True)
    with col_nz:
        st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=800"><div class="service-content"><h3 class="service-title">{"Tekapo Gölü, Yeni Zelanda" if lang=="TR" else "Lake Tekapo, New Zealand"}</h3><p class="service-desc">{desc_nz}</p></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 3: CANLI GÖZLEMEVİ
# ==============================================================================
elif menu_secimi in ["CANLI GÖZLEMEVİ", "LIVE OBSERVATORY"]:
    st.markdown("<h2>{}</h2>".format("Stellaris Kesintisiz Uydu Ağı" if lang == "TR" else "Stellaris Live Satellite Network"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Tüm kanallar doğrudan NASA ve NOAA uydularından alınan, askeri sınıf ham veri akışlarıdır." if lang == "TR" else "All channels are military-grade raw data streams pulled directly from NASA and NOAA satellites."), unsafe_allow_html=True)
    st.write("---")
    
    t_labels = ["🌍 GOES-16", "🌍 HIMAWARI", "☀️ SDO 304", "☀️ SDO 171", "🛰️ SOHO C3", "📍 ISS RADAR", "🔭 TELESKOP SİM."] if lang == "TR" else ["🌍 GOES-16", "🌍 HIMAWARI", "☀️ SDO 304", "☀️ SDO 171", "🛰️ SOHO C3", "📍 ISS RADAR", "🔭 TELESCOPE SIM"]
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(t_labels)
    
    with tab1: components.html(auto_refresh_image("goes16_img", "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/latest.jpg", 60000, "LIVE: GOES-16", "550px"), height=650)
    with tab2: components.html(auto_refresh_image("himawari_img", "https://cdn.star.nesdis.noaa.gov/AHI/FD/GEOCOLOR/latest.jpg", 60000, "LIVE: HIMAWARI-9", "550px"), height=650)
    with tab3: components.html(auto_refresh_image("sdo304_img", "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0304.jpg", 60000, "LIVE: SDO 304", "550px"), height=650)
    with tab4: components.html(auto_refresh_image("sdo171_img", "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0171.jpg", 60000, "LIVE: SDO 171", "550px"), height=650)
    with tab5: components.html(auto_refresh_image("sohoc3_img", "https://soho.nascom.nasa.gov/data/realtime/c3/1024/latest.jpg", 60000, "LIVE: SOHO C3", "550px"), height=650)
    with tab6: st.markdown("""<div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; height: 550px; background: rgba(5,16,36,0.5);"><iframe src="https://isstracker.spaceflight.esa.int/" width="100%" height="100%" frameborder="0" style="pointer-events: none;"></iframe></div>""", unsafe_allow_html=True)
    with tab7:
        col_view, col_controls = st.columns([2, 1])
        with col_controls:
            zoom_level = st.slider("Zoom", 1.0, 3.0, 1.0, 0.1)
            filter_type = st.radio("Filtre / Filter" if lang=="TR" else "Filter", ["Görünür / Visible", "H-Alpha", "O-III"])
            css_filter = "sepia(100%) hue-rotate(-50deg) saturate(300%)" if "H-Alpha" in filter_type else "sepia(100%) hue-rotate(130deg) saturate(200%)" if "O-III" in filter_type else "none"
        with col_view:
            st.markdown(f"""<div style="width: 100%; height: 400px; border: 2px solid #B8860B; border-radius: 8px; overflow: hidden; background: #000; position: relative;"><div style="position: absolute; top: 15px; left: 15px; color: red; font-family: monospace; font-weight: bold; z-index: 10;"><span style="animation: blink 1s infinite;">●</span> SIMULATION</div><img src="https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=1200" style="width: 100%; height: 100%; object-fit: cover; transform: scale({zoom_level}); filter: {css_filter}; transition: all 0.5s ease;"></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 4: 3D SİMÜLASYONLAR
# ==============================================================================
elif menu_secimi in ["3D SİMÜLASYONLAR", "3D SIMULATIONS"]:
    st.markdown("<h2>{}</h2>".format("İnteraktif 3D Uzay Simülatörleri" if lang == "TR" else "Interactive 3D Space Simulators"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Tam ekran moduna geçerek uzayın derinliklerinde serbestçe gezinebilirsiniz." if lang == "TR" else "Enter full-screen mode to freely navigate the depths of space."), unsafe_allow_html=True)
    st.write("---")
    
    t_labels = ["🌍 3D DÜNYA", "🪐 GÜNEŞ SİSTEMİ", "☄️ ASTEROİT AVI", "👽 ÖTEGEZEGENLER", "🌌 CANLI GÖKYÜZÜ"] if lang == "TR" else ["🌍 3D EARTH", "🪐 SOLAR SYSTEM", "☄️ ASTEROIDS", "👽 EXOPLANETS", "🌌 LIVE SKY"]
    tab1, tab2, tab3, tab4, tab5 = st.tabs(t_labels)
    
    style_str = "border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5); background: rgba(5,16,36,0.5);"
    
    with tab1: st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/earth/#/" width="100%" height="600" frameborder="0" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
    with tab2: st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/solar-system/#/home?embed=true" width="100%" height="600" frameborder="0" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
    with tab3: st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/asteroids/#/?embed=true" width="100%" height="600" frameborder="0" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
    with tab4: st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/exo/#/?embed=true" width="100%" height="600" frameborder="0" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
    with tab5:
        loc_choice = st.selectbox("Gözlem Noktası / Location:", ["Atacama Çölü, Şili", "Tekapo Gölü, Yeni Zelanda"])
        lat, lon = (-23.0, -67.7) if "Atacama" in loc_choice else (-44.0, 170.4)
        sky_url = f"https://virtualsky.lco.global/embed/index.html?longitude={lon}&latitude={lat}&projection=stereo&constellations=true&constellationlabels=true&meteorshowers=true&showstarlabels=true&live=true&az=180&color=dark"
        components.iframe(sky_url, height=600)

# ==============================================================================
# SAYFA 5: KARA DELİK FİZİK MOTORU
# ==============================================================================
elif menu_secimi in ["KARA DELİK SİM.", "BLACK HOLE SIM."]:
    st.markdown("<h2>{}</h2>".format("Kara Delik & Kütleçekim Simülatörü" if lang == "TR" else "Black Hole & Gravity Simulator"), unsafe_allow_html=True)
    st.write("---")
    bh_html = f"""
    <div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; background: rgba(5,16,36,0.6); backdrop-filter: blur(10px); padding: 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.5);">
        <div style="color: #D4AF37; font-family: 'Cinzel', serif; font-size:1.5rem; margin-bottom: 20px; text-align: center; letter-spacing: 2px;">GRAVITY ENGINE v1.0</div>
        <div style="display: flex; justify-content: center; gap: 30px; margin-bottom: 30px;">
            <label style="color: #E0E0E0; font-family: 'Montserrat', sans-serif;">{"Kütle" if lang=="TR" else "Mass"}: <input type="range" id="massSlider" min="50" max="300" value="150" style="accent-color: #B8860B;"></label>
            <label style="color: #E0E0E0; font-family: 'Montserrat', sans-serif;">{"Hız" if lang=="TR" else "Velocity"}: <input type="range" id="speedSlider" min="1" max="10" value="5" style="accent-color: #B8860B;"></label>
        </div>
        <canvas id="bhCanvas" width="800" height="500" style="display: block; margin: 0 auto; background: radial-gradient(circle at center, #0a1930 0%, #000 100%); border-radius: 8px; border: 1px solid rgba(184,134,11,0.2);"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('bhCanvas'); const ctx = canvas.getContext('2d');
        const massSlider = document.getElementById('massSlider'); const speedSlider = document.getElementById('speedSlider');
        let particles = [];
        for(let i=0; i<350; i++) {{ particles.push({{x: Math.random() * canvas.width, y: Math.random() * canvas.height, vx: (Math.random() - 0.5) * 3, vy: (Math.random() - 0.5) * 3, color: `hsl(${{Math.random() * 50 + 15}}, 100%, 65%)`}}); }}
        function animate() {{
            ctx.fillStyle = 'rgba(0, 0, 0, 0.15)'; ctx.fillRect(0, 0, canvas.width, canvas.height);
            const cx = canvas.width / 2; const cy = canvas.height / 2; const mass = parseInt(massSlider.value); const speedMult = parseInt(speedSlider.value) / 5;
            ctx.beginPath(); ctx.arc(cx, cy, mass / 3, 0, Math.PI * 2); ctx.fillStyle = '#000'; ctx.fill(); ctx.lineWidth = 2; ctx.strokeStyle = 'rgba(212, 175, 55, 0.8)'; ctx.stroke(); ctx.shadowBlur = Math.random() * 20 + 30; ctx.shadowColor = '#D4AF37';
            ctx.shadowBlur = 0;
            particles.forEach(p => {{
                const dx = cx - p.x; const dy = cy - p.y; const dist = Math.sqrt(dx*dx + dy*dy);
                const force = (mass * 6) / (dist * dist); p.vx += (dx / dist) * force; p.vy += (dy / dist) * force;
                p.x += p.vx * speedMult; p.y += p.vy * speedMult;
                if(dist < mass / 3) {{ p.x = Math.random() * canvas.width; p.y = 0; p.vx = (Math.random() - 0.5) * 3; p.vy = Math.random() * 2; }}
                ctx.beginPath(); ctx.arc(p.x, p.y, 1.5, 0, Math.PI * 2); ctx.fillStyle = p.color; ctx.fill();
            }});
            requestAnimationFrame(animate);
        }}
        animate();
    </script>
    """
    components.html(bh_html, height=750)

# ==============================================================================
# SAYFA 6: VİDEOLAR GALERİSİ
# ==============================================================================
elif menu_secimi in ["VİDEOLAR GALERİSİ", "VIDEO GALLERY"]:
    st.markdown("<h2>{}</h2>".format("Stellaris Uzay ve Bilim Sineması" if lang == "TR" else "Stellaris Space Cinema"), unsafe_allow_html=True); st.write("---")
    v_col1, v_col2 = st.columns(2)
    with v_col1: 
        st.markdown(f"<h3>{'James Webb Teleskobu' if lang=='TR' else 'James Webb Telescope'}</h3>", unsafe_allow_html=True); st.video("https://www.youtube.com/watch?v=uD4izuDMUQA")
        st.markdown(f"<br><h3>{'SpaceX Starship Fırlatması' if lang=='TR' else 'SpaceX Starship Launch'}</h3>", unsafe_allow_html=True); st.video("https://www.youtube.com/watch?v=-1wcilQ58hI")
    with v_col2: 
        st.markdown(f"<h3>{'Mars Yüzeyi 4K' if lang=='TR' else 'Mars Surface in 4K'}</h3>", unsafe_allow_html=True); st.video("https://www.youtube.com/watch?v=ZEyAs3NWH4A")
        st.markdown(f"<br><h3>{'Dünya 4K Manzaralar' if lang=='TR' else 'Earth 4K Views'}</h3>", unsafe_allow_html=True); st.video("https://www.youtube.com/watch?v=Un5SEJ8MyPc")

# ==============================================================================
# SAYFA 7: KOZMİK TAKVİM (KIRIK GÖRSELLER TAMAMEN DEĞİŞTİRİLDİ)
# ==============================================================================
elif menu_secimi in ["KOZMİK TAKVİM", "COSMIC CALENDAR"]:
    st.markdown("<h2>{}</h2>".format("Kozmik Takvim & Nadir Fenomenler" if lang == "TR" else "Cosmic Calendar & Phenomena"), unsafe_allow_html=True); st.write("---")
    events = ["Perseid Göktaşı Yağmuru", "Satürn Karşı Konumu", "Tam Güneş Tutulması"] if lang == "TR" else ["Perseid Meteor Shower", "Saturn Opposition", "Total Solar Eclipse"]
    selected_event = st.selectbox("Seçiniz / Select:", events)
    col_info, col_metrics = st.columns([2, 1])
    with col_info:
        # En stabil ve yüksek çözünürlüklü Unsplash görselleri ile güncellendi
        if "Perseid" in selected_event:
            img_url = "https://images.unsplash.com/photo-1541692641319-981cc79ee10a?auto=format&fit=crop&w=800"
        elif "Sat" in selected_event:
            img_url = "https://images.unsplash.com/photo-1614728263610-18fb23c7b505?auto=format&fit=crop&w=800"
        else:
            img_url = "https://images.unsplash.com/photo-1539321908154-049275965646?auto=format&fit=crop&w=800"
            
        st.markdown(f"""<div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; padding: 25px; background: rgba(5,16,36,0.5); backdrop-filter: blur(10px);"><img src="{img_url}" style="width: 100%; height: 350px; object-fit: cover; border-radius: 8px;"></div>""", unsafe_allow_html=True)
    with col_metrics: 
        st.metric("Görüş / Visibility" if lang=="TR" else "Visibility", "Ultra HD", "99%")
        st.progress(60 if "Perseid" in selected_event else 85 if "Sat" in selected_event else 98)
        if st.button("VIP Rezervasyon" if lang=="TR" else "VIP Booking"): st.toast("Talebiniz Alındı!" if lang=="TR" else "Request Received!", icon="🎫")

# ==============================================================================
# SAYFA 8: UZAY HAVADURUMU (GELİŞMİŞ VERİLER VE İKİ GRAFİK)
# ==============================================================================
elif menu_secimi in ["UZAY HAVADURUMU", "SPACE WEATHER"]:
    st.markdown("<h2>{}</h2>".format("Jeomanyetik Fırtına & Uzay Hava Durumu" if lang == "TR" else "Geomagnetic Storm & Space Weather"), unsafe_allow_html=True)
    
    warn_text = "Jeomanyetik fırtınalar (Kp Index) muazzam kutup ışıkları yaratsa da, hassas astrofotografi sensörleri için parazit oluşturabilir. Lütfen turlarınızı bu takvime göre planlayın." if lang == "TR" else "While geomagnetic storms (Kp Index) create magnificent auroras, they can cause noise for sensitive astrophotography sensors. Please plan your tours according to this calendar."
    st.markdown(f"<p>{warn_text}</p>", unsafe_allow_html=True)
    st.write("---")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Kp Index", "6.33", "+1.2 (Storm)" if lang=="EN" else "+1.2 (Fırtına)")
    c2.metric("Solar Wind" if lang=="EN" else "Güneş Rüzgarı", "540 km/s", "+45")
    c3.metric("Aurora Prob." if lang=="EN" else "Aurora Olasılığı", "%85", "+%15")
    c4.metric("Solar Flare" if lang=="EN" else "Parlama Sınıfı", "M1.2", "Moderate")
    st.write("---")
    
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.markdown("<h3>{}</h3>".format("5 Günlük Kp İndeksi Tahmini" if lang == "TR" else "5-Day Kp Index Forecast"), unsafe_allow_html=True)
        days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"] if lang == "TR" else ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        col_name = "Fırtına Gücü (Kp)" if lang == "TR" else "Storm Intensity (Kp)"
        df_kp = pd.DataFrame({col_name: [2.3, 4.0, 6.3, 5.1, 3.2]}, index=days)
        st.bar_chart(df_kp, color="#D4AF37")
        
    with col_chart2:
        st.markdown("<h3>{}</h3>".format("Güneş Rüzgarı Hızı (km/s)" if lang == "TR" else "Solar Wind Speed (km/s)"), unsafe_allow_html=True)
        df_wind = pd.DataFrame({"Hız/Speed": [350, 420, 540, 490, 400]}, index=days)
        st.line_chart(df_wind, color="#B8860B")

# ==============================================================================
# SAYFA 9: IŞIK KİRLİLİĞİ
# ==============================================================================
elif menu_secimi in ["IŞIK KİRLİLİĞİ", "LIGHT POLLUTION"]:
    st.markdown("<h2>{}</h2>".format("Bortle Scale: Işık Kirliliği Simülatörü" if lang == "TR" else "Light Pollution Simulator"), unsafe_allow_html=True); st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl: 
        st.markdown(f"<p style='text-align:left !important;'><b>1:</b> {'Kusursuz Karanlık' if lang=='TR' else 'Perfect Darkness'} <br><b>9:</b> {'Metropol' if lang=='TR' else 'City Center'}</p>", unsafe_allow_html=True)
        bortle_val = st.slider("Gökyüzü Kalitesi / Sky Quality", 1, 9, 1, step=1)
    
    glow_opacity = (bortle_val - 1) / 8.0  
    blur_amount = (bortle_val - 1) * 0.5
    
    with col_view: st.markdown(f"""
        <div style="position: relative; width: 100%; height: 400px; border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            <img src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200" style="width: 100%; height: 100%; object-fit: cover; filter: brightness({1.0 - glow_opacity * 0.5}) blur({blur_amount}px);">
            <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(255, 140, 0, {glow_opacity}), transparent); pointer-events: none;"></div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# SAYFA 10: EKİPMANLAR (SADECE PROFESYONEL LİSTE)
# ==============================================================================
elif menu_secimi in ["EKİPMANLAR", "EQUIPMENT"]:
    st.markdown("<h2>{}</h2>".format("VIP Gözlem Envanteri" if lang == "TR" else "VIP Observation Inventory"), unsafe_allow_html=True)
    
    desc_text = "Gözlemlerimiz sırasında misafirlerimize sunulan en üst düzey teknolojik optik ve askeri sınıf takip ekipmanları kataloğumuzdur." if lang == "TR" else "Our catalog of top-tier optical and military-grade tracking equipment provided to our guests during observations."
    st.markdown(f"<p>{desc_text}</p>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        type_str = "Tür" if lang == "TR" else "Type"
        aper_str = "Diyafram" if lang == "TR" else "Aperture"
        foc_str = "Odak Uzunluğu" if lang == "TR" else "Focal Length"
        use_str = "Kapasite/Özellik" if lang == "TR" else "Capacity/Feature"
        
        st.markdown(f"""
        <div class="service-card" style="padding:25px; text-align:left; height:auto; margin-bottom:20px;">
            <h3 style="color:#D4AF37; margin-bottom:15px; text-align:left !important; border-bottom: 1px solid rgba(184,134,11,0.3); padding-bottom:10px;">🔭 Celestron CPC 1100 GPS (XLT)</h3>
            <p style="text-align:left !important; color:#E0E0E0;"><b>{type_str}:</b> Schmidt-Cassegrain<br>
            <b>{aper_str}:</b> 280mm (11")<br>
            <b>{foc_str}:</b> 2800mm (f/10)<br>
            <b>{use_str}:</b> {"Tam otomatik GPS hizalama ve StarBright XLT kaplaması ile %97 ışık geçirgenliği." if lang=='TR' else "Fully automated GPS alignment and 97% light transmission with StarBright XLT."}</p>
        </div>
        <div class="service-card" style="padding:25px; text-align:left; height:auto; margin-bottom:20px;">
            <h3 style="color:#D4AF37; margin-bottom:15px; text-align:left !important; border-bottom: 1px solid rgba(184,134,11,0.3); padding-bottom:10px;">☀️ Lunt LS100MT Solar Telescope</h3>
            <p style="text-align:left !important; color:#E0E0E0;"><b>{type_str}:</b> Dedicated H-alpha Solar<br>
            <b>{aper_str}:</b> 100mm<br>
            <b>{use_str}:</b> {"Güneş fırtınalarını ve taçküreyi gerçek zamanlı, güvenli izlemek için endüstri standardı filtreleme." if lang=='TR' else "Industry standard filtering for real-time, safe viewing of solar flares and prominences."}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="service-card" style="padding:25px; text-align:left; height:auto; margin-bottom:20px;">
            <h3 style="color:#D4AF37; margin-bottom:15px; text-align:left !important; border-bottom: 1px solid rgba(184,134,11,0.3); padding-bottom:10px;">📸 ZWO ASI 6200MM Pro</h3>
            <p style="text-align:left !important; color:#E0E0E0;"><b>{"Sensör" if lang=="TR" else "Sensor"}:</b> Full Frame CMOS (Monochrome)<br>
            <b>{"Çözünürlük" if lang=="TR" else "Resolution"}:</b> 62 Megapixels<br>
            <b>{use_str}:</b> {"İki aşamalı termoelektrik soğutma (-35°C) ile sıfır parazitli derin uzay fotoğrafçılığı." if lang=='TR' else "Zero-noise deep space photography with two-stage thermoelectric cooling (-35°C)."}</p>
        </div>
        <div class="service-card" style="padding:25px; text-align:left; height:auto;">
            <h3 style="color:#D4AF37; margin-bottom:15px; text-align:left !important; border-bottom: 1px solid rgba(184,134,11,0.3); padding-bottom:10px;">⚙️ Software Bisque Paramount ME II</h3>
            <p style="text-align:left !important; color:#E0E0E0;"><b>{type_str}:</b> Robotic Equatorial Mount<br>
            <b>{"Yük Kapasitesi" if lang=="TR" else "Payload"}:</b> 109 kg (240 lbs)<br>
            <b>{use_str}:</b> {"Dünya&#39;nın dönüş hızıyla birebir senkronize hareket eden titreşimsiz motor sistemi." if lang=='TR' else "Vibration-free motor system synchronized exactly with Earth&#39;s rotation."}</p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# SAYFA 11: ASTRO-FOTOĞRAF
# ==============================================================================
elif menu_secimi in ["ASTRO-FOTOĞRAF", "ASTRO-PHOTO"]:
    st.markdown("<h2>{}</h2>".format("Astro-Fotoğrafçılık Simülatörü" if lang == "TR" else "Astro-Photography Simulator"), unsafe_allow_html=True); st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl: iso_val = st.slider("ISO Değeri / ISO Value", 100, 6400, 800, step=100); exp_val = st.slider("Pozlama Süresi / Exposure (s)", 1, 30, 10, step=1)
    with col_view: st.markdown(f"""<div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);"><img src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200" style="width: 100%; filter: brightness({0.15 + (exp_val / 30.0) * 0.6 + (iso_val / 6400.0) * 0.5});"></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 12: VIP REZERVASYON (YÜKSEK FİYAT VE EKLENTİLER)
# ==============================================================================
elif menu_secimi in ["VIP REZERVASYON", "VIP BOOKING"]:
    st.markdown("<h2>{}</h2>".format("Premium Rezervasyon & VIP Planlama" if lang == "TR" else "Premium Booking & VIP Planning"), unsafe_allow_html=True)
    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    with col_center:
        deneyim_turu = st.radio("Ana Paket / Main Package:", [
            "Atacama Glass Dome VIP (3 Gece / Nights) - $15,000", 
            "Tekapo Observatory Exclusive (2 Gece / Nights) - $12,500", 
            "Ultimate Expedition (Heli-Transfer & Private Chef) - $45,000"
        ])
        
        st.write("---")
        st.markdown(f"<p style='text-align:left !important; color:#D4AF37;'><b>{'Ekstra Hizmetler / Add-ons:' if lang == 'TR' else 'Add-ons:'}</b></p>", unsafe_allow_html=True)
        
        ekstra1 = st.checkbox("Kişisel Astrofotografçı / Personal Astrophotographer (+$2,500)")
        ekstra2 = st.checkbox("Özel Jet Kiralama / Private Jet Charter (Fiyat Sorunuz / Price upon request)")
        
        st.write("---")
        col_form1, col_form2 = st.columns(2)
        with col_form1: secilen_tarih = st.date_input("Tarih / Date", min_value=datetime.date.today())
        with col_form2: kisi_sayisi = st.slider("VIP Konuk Sayısı / VIP Guests", 1, 4, 1)
        
        taban_fiyat = 15000 if "15.000" in deneyim_turu or "15,000" in deneyim_turu else 12500 if "12" in deneyim_turu else 45000
        ekstra_fiyat = 2500 if ekstra1 else 0
        toplam_fiyat = (taban_fiyat * kisi_sayisi) + ekstra_fiyat
        
        st.markdown(f"<div class='price-tag'>${(toplam_fiyat):,} <span style='font-size: 1rem; color: #C5A059;'>USD</span></div>", unsafe_allow_html=True)
        if st.button("Talebi İlet / Submit Request"): 
            st.toast("Talebiniz elit danışmanlarımıza iletilmiştir." if lang == "TR" else "Request sent to our elite advisors.", icon="🥂")
            st.balloons()

# ==============================================================================
# SAYFA 13: VİZYON & SÜRDÜRÜLEBİLİRLİK
# ==============================================================================
elif menu_secimi in ["VİZYON & SÜRDÜRÜLEBİLİRLİK", "VISION & SUSTAINABILITY"]:
    st.markdown("<h2>{}</h2>".format("Vizyonumuz & Gelecek Planlarımız" if lang == "TR" else "Our Vision & Future Plans"), unsafe_allow_html=True)
    st.write("---")
    
    t_vis, t_sus, t_exo = st.tabs(["🌟 Vizyon & Misyon" if lang == "TR" else "🌟 Vision & Mission", "🍃 Sürdürülebilirlik" if lang == "TR" else "🍃 Sustainability", "🚀 Ötegezegen Turizmi" if lang == "TR" else "🚀 Exoplanet Tourism"])
    
    with t_vis:
        col_space1, col_center, col_space2 = st.columns([1, 8, 1])
        with col_center:
            mission_title = "Kurumsal Misyonumuz" if lang=="TR" else "Corporate Mission"
            mission_text = "Evrenin gizemlerini ve uzayın derinliklerini, bilimsel bir ciddiyet ve premium hizmet anlayışıyla misafirlerimize sunmak. Dünyanın ışık kirliliğinden %100 arındırılmış benzersiz lokasyonlarında, uzay keşfini modern, konforlu ve ilham verici elit bir seyahat deneyimine dönüştürüyoruz." if lang=="TR" else "To present the mysteries of the universe to our guests with scientific rigor and a premium service approach. In unique locations 100% free from light pollution, we transform space exploration into a modern, comfortable, and inspiring elite travel experience."
            
            vision_title = "Vizyonumuz" if lang=="TR" else "Our Vision"
            vision_text = "Astro-Turizm kavramını küresel standartlarda yeniden tanımlamak ve insanlığın uzay yolculuğu vizyonuna sivil bir zemin hazırlamak. Amacımız sadece Dünya&#39;dan yıldızları izletmek değil, gelecekteki ticari yıldızlararası seyahatler için ilham veren küresel bir endüstri öncüsü olmaktır." if lang=="TR" else "To redefine Astro-Tourism at global standards and prepare a civilian ground for humanity&#39;s space travel vision. Our goal is to be a global industry pioneer inspiring future commercial interstellar travel."

            st.markdown(f"""
            <div class="mission-box">
                <h3>{mission_title}</h3>
                <p>{mission_text}</p>
            </div>
            <div class="mission-box">
                <h3>{vision_title}</h3>
                <p>{vision_text}</p>
            </div>
            """, unsafe_allow_html=True)

    with t_sus:
        col_space1, col_center, col_space2 = st.columns([1, 6, 1])
        with col_center:
            st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh;" src="https://images.unsplash.com/photo-1502481851512-e9e2529bfbf9?q=80&w=1200"></div>', unsafe_allow_html=True)
            with st.expander("Işık Kirliliği Azaltımı (Zero-Glow)" if lang == "TR" else "Light Pollution Reduction"): st.write("Tesislerimizde gökyüzü silüetini bozmamak adına yalnızca yere dönük, hareket sensörlü ve kırmızı bazlı (600nm) aydınlatmalar kullanılır." if lang == "TR" else "We only use downward-facing, motion-sensored, red-based (600nm) lighting to preserve the sky silhouette.")
            with st.expander("Sıfır Karbon Tesisleri" if lang == "TR" else "Zero Carbon Facilities"): st.write("Cam fanus konaklamalarımız %100 güneş enerjisiyle çalışır ve VIP transferlerimizde yalnızca yüksek menzilli elektrikli SUV'ler kullanılır." if lang == "TR" else "Our glass domes are 100% solar-powered, and we only use long-range electric SUVs for VIP transfers.")
            
    with t_exo:
        exo_intro = "Astro-turizm sadece bir başlangıç. Holdingimizin 2040 vizyonu, galaksinin derinliklerindeki yaşanabilir yeni evlere sivil biletlemeyi başlatmaktır. Projelendirilen rotalarımıza göz atın." if lang == "TR" else "Astro-tourism is just the beginning. Our holding&#39;s 2040 vision is to launch civilian ticketing to habitable new homes in the galaxy."
        st.markdown(f"<p style='margin-top:20px !important;'>{exo_intro}</p>", unsafe_allow_html=True)
        
        dist_str = "Uzaklık" if lang=="TR" else "Distance"
        stat_str = "Durum" if lang=="TR" else "Status"
        tick_str = "PROJE BÜTÇESİ" if lang=="TR" else "PROJECT BUDGET"
        btn_str = "VIP Yatırımcı Bekleme Listesi" if lang=="TR" else "VIP Investor Waitlist"
        succ_str = "Kaydedildi!" if lang=="TR" else "Saved!"
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""<div class="planet-card" style="padding: 30px; text-align: center;"><h3 style="color: #D4AF37; margin-bottom: 20px;">TRAPPIST-1e</h3><img class="spinning-planet" src="https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=400" style="filter: hue-rotate(150deg) saturate(200%);"><p style="color: #E0E0E0; font-size: 0.9rem; text-align: left !important;"><b>{dist_str}:</b> 39 LY<br><b>{stat_str}:</b> {"Okyanus Gezegeni" if lang=="TR" else "Ocean Planet"}</p><div style="color: #B8860B; font-weight: bold; margin-top: 15px;">{tick_str}: $4.5 Milyar</div></div>""", unsafe_allow_html=True)
            if st.button(btn_str, key="b1"): 
                st.toast(succ_str, icon="🚀")
                st.snow()
        with c2:
            st.markdown(f"""<div class="planet-card" style="padding: 30px; text-align: center; border-color: #D4AF37 !important; box-shadow: 0 0 30px rgba(212,175,55,0.2) !important;"><h3 style="color: #D4AF37; margin-bottom: 20px;">Kepler-186f</h3><img class="spinning-planet" src="https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=400" style="filter: hue-rotate(240deg) saturate(150%);"><p style="color: #E0E0E0; font-size: 0.9rem; text-align: left !important;"><b>{dist_str}:</b> 582 LY<br><b>{stat_str}:</b> {"Dünya Benzeri" if lang=="TR" else "Earth-like"}</p><div style="color: #B8860B; font-weight: bold; margin-top: 15px;">{tick_str}: $8.2 Milyar</div></div>""", unsafe_allow_html=True)
            if st.button(btn_str, key="b2"): 
                st.toast(succ_str, icon="🚀")
                st.snow()
        with c3:
            st.markdown(f"""<div class="planet-card" style="padding: 30px; text-align: center;"><h3 style="color: #D4AF37; margin-bottom: 20px;">Proxima b</h3><img class="spinning-planet" src="https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=400" style="filter: hue-rotate(60deg) saturate(80%);"><p style="color: #E0E0E0; font-size: 0.9rem; text-align: left !important;"><b>{dist_str}:</b> 4.2 LY<br><b>{stat_str}:</b> {"Kayaç Gezegen" if lang=="TR" else "Rocky Planet"}</p><div style="color: #B8860B; font-weight: bold; margin-top: 15px;">{tick_str}: $1.2 Milyar</div></div>""", unsafe_allow_html=True)
            if st.button(btn_str, key="b3"): 
                st.toast(succ_str, icon="🚀")
                st.snow()

# ==============================================================================
# SAYFA 14: YATIRIMCI PORTALI (KURUMSAL RAPORLAMA EKLENDİ)
# ==============================================================================
elif menu_secimi in ["YATIRIMCI PORTALI", "INVESTOR PORTAL"]:
    st.markdown("<h2>{}</h2>".format("Holding Yatırımcı Portalı" if lang == "TR" else "Holding Investor Portal"), unsafe_allow_html=True)
    st.write("---")
    
    if st.text_input("Yetkilendirme Şifresi / Authorization Key:", type="password") == "stellaris2026": 
        st.success("Erişim Sağlandı / Access Granted")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("2025 YTD Gelir (USD)" if lang=="TR" else "2025 YTD Revenue", "$24.5M", "+18.2%")
        c2.metric("EBITDA Marjı" if lang=="TR" else "EBITDA Margin", "%42.8", "+3.5%")
        c3.metric("VIP Üye Sayısı" if lang=="TR" else "VIP Members", "1,240", "+120")
        
        st.write("---")
        st.markdown("<h3>{}</h3>".format("Bölgesel Büyüme Projeksiyonu (USD Bin)" if lang == "TR" else "Regional Growth Projection (USD Thousands)"), unsafe_allow_html=True)
        
        df_growth = pd.DataFrame({
            "Şili (Atacama)" if lang=="TR" else "Chile (Atacama)": [1000, 2500, 4800, 7500, 12000], 
            "Yeni Zelanda" if lang=="TR" else "New Zealand": [800, 1900, 3500, 6000, 9500]
        }, index=["2022", "2023", "2024", "2025", "2026 (Tahmin)"])
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.area_chart(df_growth, color=["#B8860B", "#C5A059"])
        with col_c2:
            st.markdown(f"<p style='text-align:left !important; padding:20px; background:rgba(3,8,20,0.8); border-radius:8px;'><b>{'Stratejik Not:' if lang=='TR' else 'Strategic Note:'}</b> {'Gelecek yıl Namibya Çölü\\'nde planlanan 3. faz rezervasyon alanı ile küresel pazar payımızın %65 oranında artması öngörülmektedir.' if lang=='TR' else 'With the 3rd phase reserve planned in the Namib Desert next year, our global market share is projected to increase by 65%.'}</p>", unsafe_allow_html=True)
