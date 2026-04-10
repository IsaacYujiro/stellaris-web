import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import datetime
import time
import os
import glob
import random

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
    
    div[data-testid="stMetricValue"] { color: #D4AF37 !important; font-family: 'Cinzel', serif !important; font-size: 2.5rem !important; text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.5); }
    div[data-testid="stMetricLabel"] { color: #B8860B !important; font-family: 'Montserrat', sans-serif !important; font-size: 1.1rem !important; }
    
    h1, h2, h3, h4, h5, h6 { font-family: 'Cinzel', serif; font-weight: 700; text-align: center !important; width: 100%; background: linear-gradient(45deg, #C5A059, #F3E5AB, #D4AF37, #B8860B); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: shine 5s linear infinite;}
    @keyframes shine { to { background-position: 200% center; } }
    
    p { text-align: center !important; margin: 0 auto 15px auto !important; max-width: 800px; line-height: 1.8; color: #a8b2d1 !important; font-weight: 300;}
    hr { border-top: 1px solid rgba(184, 134, 11, 0.3) !important; width: 60%; margin: 40px auto !important; }

    .block-container { animation: fadeSlideUp 1s cubic-bezier(0.165, 0.84, 0.44, 1); }
    @keyframes fadeSlideUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }

    .hero-image { width: 100%; max-width: 1200px; height: 50vh; object-fit: cover; border-radius: 8px; filter: brightness(55%); border: 1px solid rgba(184, 134, 11, 0.4); animation: slowZoom 30s infinite alternate cubic-bezier(0.455, 0.03, 0.515, 0.955); }
    @keyframes slowZoom { from { transform: scale(1); } to { transform: scale(1.08); } }
    .hero-container { position: relative; text-align: center; margin-bottom: 40px; display: flex; justify-content: center; overflow: hidden; border-radius: 8px; box-shadow: 0 15px 40px rgba(0,0,0,0.6);}

    .service-card, .boarding-pass, div[style*="border: 2px solid #B8860B"], .planet-card { background: rgba(5, 16, 36, 0.4) !important; backdrop-filter: blur(12px) !important; border-radius: 12px !important; border: 1px solid rgba(184, 134, 11, 0.3) !important; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5) !important; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; overflow: hidden; }
    .service-card:hover, .planet-card:hover { transform: translateY(-10px) !important; border-color: rgba(212, 175, 55, 0.8) !important; box-shadow: 0 15px 40px rgba(184, 134, 11, 0.2) !important; }
    
    .hero-title { font-size: 5rem; letter-spacing: 8px; margin-bottom: 10px; }
    .service-img { width: 100%; height: 220px; object-fit: cover; border-bottom: 1px solid rgba(184, 134, 11, 0.3); transition: transform 0.5s; }
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
    .stChatMessage { background: rgba(5, 16, 36, 0.5) !important; backdrop-filter: blur(10px); border: 1px solid rgba(184, 134, 11, 0.3); border-radius: 12px; margin-bottom: 10px;}
    
    .boarding-pass { display: flex; justify-content: space-between; max-width: 850px; margin: 0 auto; }
    .pass-left { width: 72%; border-right: 2px dashed rgba(184, 134, 11, 0.5); padding-right: 25px; }
    .pass-right { width: 25%; display: flex; flex-direction: column; align-items: center; justify-content: center; }
    .pass-title { color: #D4AF37; font-family: 'Cinzel', serif; font-size: 2rem; margin-bottom: 10px; text-align: left !important; letter-spacing: 2px;}
    .pass-label { color: #B8860B; font-size: 0.75rem; text-transform: uppercase; margin-bottom: 4px; text-align: left !important; letter-spacing: 1px;}
    .pass-value { color: #FFF; font-size: 1.3rem; font-weight: 600; margin-bottom: 20px; text-align: left !important; }
    .pass-barcode { margin-top: 15px; letter-spacing: 6px; font-family: monospace; color: #D4AF37; font-size: 1.8rem; text-align: center !important; text-shadow: 0 0 10px rgba(212,175,55,0.4);}
    .pass-logo { font-family: 'Cinzel', serif; color: #D4AF37; font-size: 2rem; writing-mode: vertical-rl; text-orientation: mixed; transform: rotate(180deg); letter-spacing: 5px; opacity: 0.8;}
    
    .spinning-planet { width: 250px; height: 250px; border-radius: 50%; display: block; margin: 0 auto 20px auto; box-shadow: inset -25px -25px 40px rgba(0,0,0,0.9), 0 0 30px rgba(184, 134, 11, 0.3); animation: spin 40s linear infinite; object-fit: cover;}
    @keyframes spin { 100% { transform: rotate(360deg); } }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# AKILLI LOGO BULUCU VE SİDEBAR
# ==============================================================================
bulunan_logo = None
resimler = glob.glob("*.jpeg") + glob.glob("*.jpg") + glob.glob("*.png")
for resim in resimler:
    if "logo" in resim.lower() or "whatsapp" in resim.lower() or "image" in resim.lower():
        bulunan_logo = resim; break
if not bulunan_logo and resimler: bulunan_logo = resimler[0]

if bulunan_logo: st.sidebar.image(bulunan_logo, use_container_width=True)
else: st.sidebar.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin-top: 20px; color: #B8860B;'>Stellaris</h2>", unsafe_allow_html=True)

st.sidebar.write("---")
dil_secimi = st.sidebar.selectbox("DİL / LANGUAGE", ["Türkçe", "English"])
lang = "TR" if dil_secimi == "Türkçe" else "EN"
st.sidebar.write("---")

menu_secenekleri = [
    "ANA SAYFA", "LOKASYONLARIMIZ", "ÖTEGEZEGEN TURİZMİ", "CANLI GÖZLEMEVİ", "3D SİMÜLASYONLAR", "KARA DELİK SİM.",
    "UZAY SESLERİ", "KOZMİK BUTİK", "STELLARIS AI", "UZAY PASAPORTU", "VİDEOLAR GALERİSİ", "KOZMİK TAKVİM", 
    "UZAY HAVADURUMU", "IŞIK KİRLİLİĞİ", "EKİPMANLAR", "ASTRO-FOTOĞRAF", 
    "REZERVASYON", "SÜRDÜRÜLEBİLİRLİK", "YATIRIMCI PORTALI"
] if lang == "TR" else [
    "HOME", "OUR LOCATIONS", "EXOPLANET TOURISM", "LIVE OBSERVATORY", "3D SIMULATIONS", "BLACK HOLE SIM.",
    "SPACE SOUNDS", "COSMIC BOUTIQUE", "STELLARIS AI", "SPACE PASSPORT", "VIDEO GALLERY", "COSMIC CALENDAR", 
    "SPACE WEATHER", "LIGHT POLLUTION", "EQUIPMENT", "ASTRO-PHOTO", 
    "BOOKING", "SUSTAINABILITY", "INVESTOR PORTAL"
]

menu_secimi = st.sidebar.radio("Nav", menu_secenekleri, label_visibility="collapsed")
st.sidebar.write("---")

st.sidebar.markdown(f"<p style='color:#B8860B; font-size:0.8rem; font-weight:bold; margin-bottom:5px !important;'>{'Kozmik Ambiyans Sesi' if lang == 'TR' else 'Cosmic Ambient Audio'}</p>", unsafe_allow_html=True)
st.sidebar.markdown("""<audio controls autoplay loop style="width: 100%; height: 30px; outline: none; border-radius: 4px; opacity: 0.8;"><source src="https://cdn.pixabay.com/audio/2022/11/22/audio_febc508520.mp3" type="audio/mpeg"></audio>""", unsafe_allow_html=True)
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
    <script>setInterval(function() {{ document.getElementById('{img_id}').src = '{img_url}?time=' + new Date().getTime(); }}, {refresh_rate_ms});</script>
    """

# ==============================================================================
# SAYFA 1: ANA SAYFA
# ==============================================================================
if menu_secimi in ["ANA SAYFA", "HOME"]:
    col_space1, col_hero, col_space3 = st.columns([1, 2, 1])
    with col_hero:
        if bulunan_logo: st.image(bulunan_logo, use_container_width=True)
        else:
            st.markdown("<h1 class='hero-title'>STELLARIS</h1>", unsafe_allow_html=True)
            st.markdown(f"<p class='hero-subtitle'>{'Global Astro-Turizm Lideri' if lang == 'TR' else 'Global Astro-Tourism Leader'}</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<h2>{}</h2>".format("Gökyüzünün Sınırlarını Keşfedin" if lang == "TR" else "Discover the Limits of the Sky"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Stellaris, sıradan tatil anlayışını geride bırakıp gözlerini evrenin derinliklerine çevirenler için doğdu. Işık kirliliğinden tamamen arınmış dünyanın en karanlık noktalarında, bilim ve lüksü harmanlıyoruz." if lang == "TR" else "Stellaris was born for those who leave ordinary holidays behind and turn their eyes to the depths of the universe. In the darkest points of the world, we blend science and luxury."), unsafe_allow_html=True)
    st.write("---")
    col_space1, col_image, col_space2 = st.columns([1, 8, 1])
    with col_image:
        st.markdown('<div class="hero-container"><img class="hero-image" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=2000&auto=format&fit=crop"></div>', unsafe_allow_html=True)

# ==============================================================================
# SAYFA 2: LOKASYONLARIMIZ
# ==============================================================================
elif menu_secimi in ["LOKASYONLARIMIZ", "OUR LOCATIONS"]:
    st.markdown("<h2>{}</h2>".format("Hedef Ülkeler ve Küresel Pazar" if lang == "TR" else "Target Locations & Global Market"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Evrenin en muazzam manzaralarını sunan stratejik karanlık gökyüzü rezervleri." if lang == "TR" else "Strategic dark sky reserves offering the most magnificent views of the universe."), unsafe_allow_html=True)
    st.write("---")
    col_space1, col_chile, col_nz, col_space2 = st.columns([1, 4, 4, 1])
    with col_chile:
        st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?q=80&w=800"><div class="service-content"><h3 class="service-title">{"Atacama Çölü, Şili" if lang=="TR" else "Atacama Desert, Chile"}</h3><p class="service-desc">{"Yılda 300 günden fazla bulutsuz gece. Dünyanın en kurak çölünde, evreni yüksek rakımdan izleyin." if lang=="TR" else "Over 300 cloudless nights a year. Watch the universe from high altitude in the driest desert."}</p></div></div>""", unsafe_allow_html=True)
    with col_nz:
        st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=800"><div class="service-content"><h3 class="service-title">{"Tekapo Gölü, Y. Zelanda" if lang=="TR" else "Lake Tekapo, New Zealand"}</h3><p class="service-desc">{"Uluslararası karanlık gökyüzü rezervi. Güney Haçı takımyıldızını ve Aurora Australis'i deneyimleyin." if lang=="TR" else "International dark sky reserve. Experience the Southern Cross and Aurora Australis."}</p></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 3: ÖTEGEZEGEN TURİZMİ
# ==============================================================================
elif menu_secimi in ["ÖTEGEZEGEN TURİZMİ", "EXOPLANET TOURISM"]:
    st.markdown("<h2>{}</h2>".format("Geleceğin Turizmi: Ötegezegenler" if lang == "TR" else "Future Tourism: Exoplanets"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Dünya'nın sınırları size yetmiyorsa, galaksinin derinliklerindeki yeni evleri keşfedin." if lang == "TR" else "If Earth's borders aren't enough, discover new homes in the depths of the galaxy."), unsafe_allow_html=True)
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""<div class="planet-card" style="padding: 30px; text-align: center;"><h3 style="color: #D4AF37; margin-bottom: 20px;">TRAPPIST-1e</h3><img class="spinning-planet" src="https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=400" style="filter: hue-rotate(150deg) saturate(200%);"><p style="color: #E0E0E0; font-size: 0.9rem; text-align: left !important;"><b>{"Uzaklık" if lang=="TR" else "Distance"}:</b> 39 LY<br><b>{"Durum" if lang=="TR" else "Status"}:</b> {"Okyanus Gezegeni" if lang=="TR" else "Ocean Planet"}</p><div style="color: #B8860B; font-weight: bold; margin-top: 15px;">{"BİLET" if lang=="TR" else "TICKET"}: $4.5 M</div></div>""", unsafe_allow_html=True)
        if st.button("Yer Ayırt" if lang=="TR" else "Book Now", key="b1"): st.success("Talep alındı!" if lang=="TR" else "Request received!")
    with c2:
        st.markdown(f"""<div class="planet-card" style="padding: 30px; text-align: center; border-color: #D4AF37 !important; box-shadow: 0 0 30px rgba(212,175,55,0.2) !important;"><div style="background: #D4AF37; color: #000; padding: 5px; font-weight: bold; border-radius: 4px; margin-bottom: 10px; display: inline-block;">{"EN POPÜLER" if lang=="TR" else "MOST POPULAR"}</div><h3 style="color: #D4AF37; margin-bottom: 20px;">Kepler-186f</h3><img class="spinning-planet" src="https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=400" style="filter: hue-rotate(240deg) saturate(150%);"><p style="color: #E0E0E0; font-size: 0.9rem; text-align: left !important;"><b>{"Uzaklık" if lang=="TR" else "Distance"}:</b> 582 LY<br><b>{"Durum" if lang=="TR" else "Status"}:</b> {"Kızıl Bitki Örtüsü" if lang=="TR" else "Red Flora"}</p><div style="color: #B8860B; font-weight: bold; margin-top: 15px;">{"BİLET" if lang=="TR" else "TICKET"}: $8.2 M</div></div>""", unsafe_allow_html=True)
        if st.button("Yer Ayırt" if lang=="TR" else "Book Now", key="b2"): st.success("Talep alındı!" if lang=="TR" else "Request received!")
    with c3:
        st.markdown(f"""<div class="planet-card" style="padding: 30px; text-align: center;"><h3 style="color: #D4AF37; margin-bottom: 20px;">Proxima b</h3><img class="spinning-planet" src="https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=400" style="filter: hue-rotate(60deg) saturate(80%);"><p style="color: #E0E0E0; font-size: 0.9rem; text-align: left !important;"><b>{"Uzaklık" if lang=="TR" else "Distance"}:</b> 4.2 LY<br><b>{"Durum" if lang=="TR" else "Status"}:</b> {"Sert İklim" if lang=="TR" else "Harsh Climate"}</p><div style="color: #B8860B; font-weight: bold; margin-top: 15px;">{"BİLET" if lang=="TR" else "TICKET"}: $1.2 M</div></div>""", unsafe_allow_html=True)
        if st.button("Yer Ayırt" if lang=="TR" else "Book Now", key="b3"): st.success("Talep alındı!" if lang=="TR" else "Request received!")

# ==============================================================================
# SAYFA 4: CANLI GÖZLEMEVİ
# ==============================================================================
elif menu_secimi in ["CANLI GÖZLEMEVİ", "LIVE OBSERVATORY"]:
    st.markdown("<h2>{}</h2>".format("Stellaris Kesintisiz Uydu Ağı" if lang == "TR" else "Stellaris Live Satellite Network"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Aşağıdaki tüm kanallar doğrudan NASA ve NOAA uydularından alınan ham veri akışlarıdır." if lang == "TR" else "All channels below are raw data streams pulled directly from NASA and NOAA satellites."), unsafe_allow_html=True)
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
# SAYFA 5: 3D SİMÜLASYONLAR (KARIŞAN SEKMELER %100 DÜZELTİLDİ)
# ==============================================================================
elif menu_secimi in ["3D SİMÜLASYONLAR", "3D SIMULATIONS"]:
    st.markdown("<h2>{}</h2>".format("İnteraktif 3D Uzay Simülatörleri" if lang == "TR" else "Interactive 3D Space Simulators"), unsafe_allow_html=True)
    st.write("---")
    
    t_labels = ["🌍 3D DÜNYA", "🪐 GÜNEŞ SİSTEMİ", "☄️ ASTEROİT AVI", "👽 ÖTEGEZEGENLER", "🌌 CANLI GÖKYÜZÜ"] if lang == "TR" else ["🌍 3D EARTH", "🪐 SOLAR SYSTEM", "☄️ ASTEROIDS", "👽 EXOPLANETS", "🌌 LIVE SKY"]
    tab1, tab2, tab3, tab4, tab5 = st.tabs(t_labels)
    
    style_str = "border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5); background: rgba(5,16,36,0.5);"
    
    with tab1: # DÜNYA
        st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/earth/#/" width="100%" height="600" frameborder="0"></iframe></div>""", unsafe_allow_html=True)
    with tab2: # GÜNEŞ SİSTEMİ
        st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/solar-system/#/home?embed=true" width="100%" height="600" frameborder="0"></iframe></div>""", unsafe_allow_html=True)
    with tab3: # ASTEROİT AVI (Kesinlikle Asteroid Linki)
        st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/asteroids/#/?embed=true" width="100%" height="600" frameborder="0"></iframe></div>""", unsafe_allow_html=True)
    with tab4: # ÖTEGEZEGENLER (Kesinlikle Exo Linki)
        st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/exo/#/?embed=true" width="100%" height="600" frameborder="0"></iframe></div>""", unsafe_allow_html=True)
    with tab5: # GÖKYÜZÜ HARİTASI
        loc_choice = st.selectbox("Gözlem Noktası / Location:", ["Atacama Çölü, Şili", "Tekapo Gölü, Yeni Zelanda"])
        lat, lon = (-23.0, -67.7) if "Atacama" in loc_choice else (-44.0, 170.4)
        sky_url = f"https://virtualsky.lco.global/embed/index.html?longitude={lon}&latitude={lat}&projection=stereo&constellations=true&constellationlabels=true&meteorshowers=true&showstarlabels=true&live=true&az=180&color=dark"
        components.iframe(sky_url, height=600)

# ==============================================================================
# SAYFA 6: KARA DELİK FİZİK MOTORU
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
# SAYFA 7: UZAY SESLERİ (SOUNDCLOUD EMBED - %100 ÇALIŞIR, YOUTUBE YOK)
# ==============================================================================
elif menu_secimi in ["UZAY SESLERİ", "SPACE SOUNDS"]:
    st.markdown("<h2>{}</h2>".format("Uzay Sesleri Laboratuvarı" if lang == "TR" else "Space Sounds Laboratory"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("NASA'nın elektromanyetik dalgaları sese dönüştürdüğü (Sonifikasyon) resmi kayıtlar." if lang == "TR" else "Official NASA sonification records converting electromagnetic waves into sound."), unsafe_allow_html=True)
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""<div class="service-card" style="height:auto; box-shadow:none; border:none; background:transparent !important;"><div class="service-content" style="padding:0;"><h3 class="service-title">{"Jüpiter'in Elektromanyetik Sesi" if lang=="TR" else "Jupiter Electromagnetic Sound"}</h3><p style="font-size:0.85rem; margin-bottom:15px;">{"Juno uzay aracı kaydı." if lang=="TR" else "Juno spacecraft recording."}</p></div></div>""", unsafe_allow_html=True)
        # NASA Juno resmi SoundCloud
        sc_jupiter = '<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/310292212&color=%23B8860B&auto_play=false&hide_related=true&show_comments=false&show_user=false&show_reposts=false&show_teaser=false"></iframe>'
        components.html(sc_jupiter, height=180)
    with col2:
        st.markdown(f"""<div class="service-card" style="height:auto; box-shadow:none; border:none; background:transparent !important;"><div class="service-content" style="padding:0;"><h3 class="service-title">{"Perseus Kara Deliği" if lang=="TR" else "Perseus Black Hole"}</h3><p style="font-size:0.85rem; margin-bottom:15px;">{"Chandra X-Ray Gözlemevi." if lang=="TR" else "Chandra X-Ray Observatory."}</p></div></div>""", unsafe_allow_html=True)
        # NASA Black Hole resmi SoundCloud
        sc_bh = '<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1261314988&color=%23B8860B&auto_play=false&hide_related=true&show_comments=false&show_user=false&show_reposts=false&show_teaser=false"></iframe>'
        components.html(sc_bh, height=180)

# ==============================================================================
# SAYFA 8: KOZMİK BUTİK (GÖRSELLER ONARILDI)
# ==============================================================================
elif menu_secimi in ["KOZMİK BUTİK", "COSMIC BOUTIQUE"]:
    st.markdown("<h2>{}</h2>".format("Kozmik Butik & Koleksiyon" if lang == "TR" else "Cosmic Boutique & Collection"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("VIP müşterilerimiz için tasarlanmış sertifikalı uzay objeleri ve premium gözlem ekipmanları." if lang == "TR" else "Certified space objects and premium observation equipment for VIP clients."), unsafe_allow_html=True)
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1634152962476-4b8a00e1915c?q=80&w=600"><div class="service-content"><h3 class="service-title">Pallasite Meteorit</h3><p class="service-desc">{"4.5 milyar yaşında demir-nikel göktaşı." if lang=="TR" else "4.5 billion years old iron-nickel meteorite."}</p><div class="price-tag" style="font-size: 2rem;">$5,400</div></div></div>""", unsafe_allow_html=True)
        st.button("Sepete Ekle" if lang == "TR" else "Add to Cart", key="m1")
    with c2:
        st.markdown(f"""<div class="service-card" style="border-color: #D4AF37 !important; box-shadow: 0 0 20px rgba(212,175,55,0.3) !important;"><div style="background: #D4AF37; color: #000; padding: 5px; font-weight: bold; text-align:center;">{"LİMİTLİ ÜRETİM" if lang=="TR" else "LIMITED EDITION"}</div><img class="service-img" src="https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?q=80&w=600"><div class="service-content"><h3 class="service-title">EVA Astronot Kostümü</h3><p class="service-desc">{"Giyilebilir tam donanımlı NASA replikası." if lang=="TR" else "Wearable fully equipped NASA replica."}</p><div class="price-tag" style="font-size: 2rem;">$12,000</div></div></div>""", unsafe_allow_html=True)
        st.button("Sepete Ekle" if lang == "TR" else "Add to Cart", key="m2")
    with c3:
        st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1517976487492-5750f3195933?q=80&w=600"><div class="service-content"><h3 class="service-title">Altın Kaplama Teleskop</h3><p class="service-desc">{"Kişiye özel işlenmiş 18 ayar altın teleskop." if lang=="TR" else "Custom engraved 18k gold plated telescope."}</p><div class="price-tag" style="font-size: 2rem;">$8,500</div></div></div>""", unsafe_allow_html=True)
        st.button("Sepete Ekle" if lang == "TR" else "Add to Cart", key="m3")

# ==============================================================================
# SAYFA 9: STELLARIS AI (DİNAMİK ÇEVİRİ VE GELİŞMİŞ CEVAPLAR)
# ==============================================================================
elif menu_secimi in ["STELLARIS AI"]:
    st.markdown("<h2>{}</h2>".format("Stellaris Kozmik Rehber (AI Asistan)" if lang == "TR" else "Stellaris Cosmic Guide (AI Assistant)"), unsafe_allow_html=True)
    st.write("---")
    
    welcome_msg = "Stellaris VIP Kontrol Paneline hoş geldiniz. Ben Stellaris AI. Evren hakkında ne öğrenmek istersiniz?" if lang == "TR" else "Welcome to Stellaris VIP Panel. I am Stellaris AI. What would you like to explore in the universe?"
    
    if "messages" not in st.session_state: 
        st.session_state.messages = [{"role": "assistant", "content": welcome_msg}]
        
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])
        
    if prompt := st.chat_input("Mesajınızı yazın / Type your message..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Taranıyor / Scanning..." if lang == "TR" else "Scanning..."):
                time.sleep(1)
                lower_prompt = prompt.lower()
                if lang == "TR":
                    if "atacama" in lower_prompt: response = "Şili'deki Atacama Çölü, yılda 300'den fazla bulutsuz gecesi ile dünyanın en iyi gözlem noktasıdır. Rezervasyon sekmesinden VIP tur alabilirsiniz."
                    elif "tekapo" in lower_prompt: response = "Yeni Zelanda'daki Tekapo Gölü, Uluslararası Karanlık Gökyüzü Rezervidir. Güney Haçı takımyıldızı mükemmel görünür."
                    elif "bilet" in lower_prompt or "fiyat" in lower_prompt: response = "Turlarımız $150 ile $800 arasında değişmektedir. Detaylar Rezervasyon sekmesinde."
                    elif "kara delik" in lower_prompt: response = "Kara delikler ışığın bile kaçamayacağı kadar güçlü kütleçekimine sahip kozmik canavarlardır. Simülasyon sekmesinde test edebilir, Uzay Sesleri sekmesinde NASA'nın kaydettiği Perseus kara deliğinin sesini dinleyebilirsiniz!"
                    else: response = "Bu harika bir soru. Müşteri temsilcilerimiz ve uzman astronomlarımız size en iyi deneyimi sunmak için menüden 'Uzay Pasaportu' oluşturmanızı öneriyor."
                else:
                    if "atacama" in lower_prompt: response = "Atacama Desert in Chile is the best observation point with over 300 clear nights a year. You can book a VIP tour from the Booking tab."
                    elif "tekapo" in lower_prompt: response = "Lake Tekapo in New Zealand is an International Dark Sky Reserve. The Southern Cross constellation is perfectly visible."
                    elif "ticket" in lower_prompt or "price" in lower_prompt: response = "Our tours range from $150 to $800. See the Booking tab for details."
                    elif "black hole" in lower_prompt: response = "Black holes have immense gravity that not even light can escape. Try our simulation tab or listen to the Perseus black hole in the Space Sounds tab!"
                    else: response = "That's a great question. We recommend generating a 'Space Passport' from the menu to begin your VIP journey."
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

# ==============================================================================
# SAYFA 10: UZAY PASAPORTU (GALERİ EKLENDİ, İSİM BOŞALTILDI)
# ==============================================================================
elif menu_secimi in ["UZAY PASAPORTU", "SPACE PASSPORT"]:
    st.markdown("<h2>{}</h2>".format("Kişisel Uzay Biniş Kartı" if lang == "TR" else "Personal Space Boarding Pass"), unsafe_allow_html=True)
    st.write("---")
    
    if "passports" not in st.session_state: st.session_state.passports = []

    col_form, col_pass = st.columns([1, 2])
    with col_form:
        pass_name = st.text_input("Yolcu Adı / Passenger Name:", "")
        pass_dest = st.selectbox("Hedef / Destination:", ["Atacama Çölü", "Tekapo Gölü", "TRAPPIST-1e", "Kepler-186f"])
        pass_class = st.selectbox("Sınıf / Class:", ["VIP Astro-Turist", "Uzay Komutanı", "Bilim İnsanı"])
        pass_date = st.date_input("Tarih / Date:", datetime.date.today())
        generate_btn = st.button("Kartı Oluştur" if lang == "TR" else "Generate Pass")
    
    with col_pass:
        display_name = pass_name if pass_name else ("ADINIZI GİRİN" if lang == "TR" else "ENTER YOUR NAME")
        random_barcode = "".join([str(random.randint(0, 9)) for _ in range(12)])
        pass_html = f"""
        <div class="boarding-pass"><div class="pass-left"><div class="pass-title">STELLARIS ASTRO-LINES</div><br>
        <div style="display: flex; justify-content: space-between;"><div><div class="pass-label">PASSENGER NAME</div><div class="pass-value">{display_name.upper()}</div></div>
        <div><div class="pass-label">FLIGHT CLASS</div><div class="pass-value">{pass_class.upper()}</div></div></div>
        <div style="display: flex; justify-content: space-between;"><div><div class="pass-label">DESTINATION</div><div class="pass-value">{pass_dest.upper()}</div></div>
        <div><div class="pass-label">DATE</div><div class="pass-value">{pass_date.strftime('%d %b %Y')}</div></div></div>
        <div class="pass-barcode">||| | || ||| | ||| || {random_barcode}</div></div><div class="pass-right"><div class="pass-logo">STELLARIS</div></div></div>
        """
        st.markdown(pass_html, unsafe_allow_html=True)
        
        if generate_btn:
            st.session_state.passports.append({"name": display_name, "dest": pass_dest, "class": pass_class})
            st.success("Biniş kartı oluşturuldu!" if lang == "TR" else "Boarding pass generated!")

    if len(st.session_state.passports) > 0:
        st.write("---")
        st.markdown("<h3>{}</h3>".format("Yolcu Panosu (Oluşturulan Kartlar)" if lang == "TR" else "Passenger Board (Generated Passes)"), unsafe_allow_html=True)
        g_cols = st.columns(3)
        for i, p in enumerate(reversed(st.session_state.passports[-6:])):
            with g_cols[i % 3]:
                st.markdown(f"""<div style="border:1px solid rgba(184, 134, 11, 0.4); border-radius:8px; padding:15px; background:rgba(5,16,36,0.6); backdrop-filter:blur(5px); margin-bottom:15px; text-align:center;"><h4 style="color:#D4AF37; margin:0; font-size:1.1rem; padding-bottom:5px;">{p['name'].upper()}</h4><p style="margin:0; font-size:0.85rem; color:#E0E0E0;">{p['dest']}<br><span style="color:#B8860B; font-size:0.7rem;">{p['class']}</span></p></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 11: VİDEOLAR GALERİSİ
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
# SAYFA 12: KOZMİK TAKVİM (GÖRSELLER GÜNCELLENDİ)
# ==============================================================================
elif menu_secimi in ["KOZMİK TAKVİM", "COSMIC CALENDAR"]:
    st.markdown("<h2>{}</h2>".format("Kozmik Takvim & Nadir Fenomenler" if lang == "TR" else "Cosmic Calendar & Phenomena"), unsafe_allow_html=True); st.write("---")
    events = ["Perseid Göktaşı Yağmuru", "Satürn Karşı Konumu", "Tam Güneş Tutulması"] if lang == "TR" else ["Perseid Meteor Shower", "Saturn Opposition", "Total Solar Eclipse"]
    selected_event = st.selectbox("Seçiniz / Select:", events)
    col_info, col_metrics = st.columns([2, 1])
    with col_info:
        # Doğru Unsplash görselleri
        img_url = "https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?q=80&w=800" if "Perseid" in selected_event else "https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=800" if "Sat" in selected_event else "https://images.unsplash.com/photo-1485795959911-ea5ebf41b6ae?q=80&w=800"
        st.markdown(f"""<div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; padding: 25px; background: rgba(5,16,36,0.5); backdrop-filter: blur(10px);"><img src="{img_url}" style="width: 100%; height: 300px; object-fit: cover; border-radius: 8px;"></div>""", unsafe_allow_html=True)
    with col_metrics: 
        st.metric("Görüş / Visibility" if lang=="TR" else "Visibility", "Ultra HD", "99%")
        st.progress(60 if "Perseid" in selected_event else 85 if "Sat" in selected_event else 98)
        st.button("Rezervasyon" if lang=="TR" else "Book")

# ==============================================================================
# SAYFA 13: UZAY HAVADURUMU (BAR CHART GÜNCELLENDİ)
# ==============================================================================
elif menu_secimi in ["UZAY HAVADURUMU", "SPACE WEATHER"]:
    st.markdown("<h2>{}</h2>".format("Canlı Uzay Hava Durumu & Fırtına İndeksi" if lang == "TR" else "Live Space Weather & Storm Index"), unsafe_allow_html=True); st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("Kp Index", "6.33", "+1.2 (Storm)" if lang=="EN" else "+1.2 (Fırtına)")
    c2.metric("Solar Wind" if lang=="EN" else "Güneş Rüzgarı", "540 km/s", "+45")
    c3.metric("Bz (Magnetic)" if lang=="EN" else "Bz (Manyetik Yön)", "-5.2 nT", "South" if lang=="EN" else "Güney")
    st.write("---")
    st.markdown("<h3>{}</h3>".format("5 Günlük Jeomanyetik Fırtına Yoğunluğu (Kp)" if lang == "TR" else "5-Day Geomagnetic Storm Intensity (Kp)"), unsafe_allow_html=True)
    
    # Net anlaşılan basit Çubuk Grafiği
    days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"] if lang == "TR" else ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    col_name = "Fırtına Gücü (Kp)" if lang == "TR" else "Storm Intensity (Kp)"
    df = pd.DataFrame({col_name: [2.3, 4.0, 6.3, 5.1, 3.2]}, index=days)
    st.bar_chart(df, color="#D4AF37")

# ==============================================================================
# SAYFA 14: IŞIK KİRLİLİĞİ (SİMYA KARARMASI VE ADIM DÜZELTİLDİ)
# ==============================================================================
elif menu_secimi in ["IŞIK KİRLİLİĞİ", "LIGHT POLLUTION"]:
    st.markdown("<h2>{}</h2>".format("Bortle Scale: Işık Kirliliği Simülatörü" if lang == "TR" else "Light Pollution Simulator"), unsafe_allow_html=True); st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl: 
        st.markdown(f"<p style='text-align:left !important;'><b>1:</b> {'Kusursuz Karanlık' if lang=='TR' else 'Perfect Darkness'} <br><b>9:</b> {'Metropol' if lang=='TR' else 'City Center'}</p>", unsafe_allow_html=True)
        # Adım 1 yapıldı
        bortle_val = st.slider("Gökyüzü Kalitesi / Sky Quality", 1, 9, 1, step=1)
    
    # Şehir ışığı simülasyonu (blur ve orange gradient)
    glow_opacity = (bortle_val - 1) / 8.0  
    blur_amount = (bortle_val - 1) * 0.5
    
    with col_view: st.markdown(f"""
        <div style="position: relative; width: 100%; height: 400px; border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            <img src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200" style="width: 100%; height: 100%; object-fit: cover; filter: brightness({1.0 - glow_opacity * 0.5}) blur({blur_amount}px);">
            <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(255, 140, 0, {glow_opacity}), transparent); pointer-events: none;"></div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# SAYFA 15: EKİPMANLAR
# ==============================================================================
elif menu_secimi in ["EKİPMANLAR", "EQUIPMENT"]:
    st.markdown("<h2>{}</h2>".format("VIP Gözlem Ekipmanları" if lang == "TR" else "VIP Observation Equipment"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Gözlemlerimiz sırasında misafirlerimize sunulan en üst düzey teknolojik optik ekipmanlar." if lang == "TR" else "Top-tier optical equipment provided during our sessions."), unsafe_allow_html=True)
    st.write("---")
    e1, e2, e3 = st.columns(3)
    with e1: st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1517976487492-5750f3195933?q=80&w=800"><div class="service-content"><h3 class="service-title">Celestron CPC 1100</h3><p class="service-desc">{"Derin uzay nesneleri (Galaksiler ve Bulutsular) için tasarlanmış ultra HD teleskop." if lang=="TR" else "Ultra HD telescope for deep space objects."}</p></div></div>""", unsafe_allow_html=True)
    with e2: st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1506443432602-ac2fcd6f54e0?q=80&w=800"><div class="service-content"><h3 class="service-title">Meade LX200 14''</h3><p class="service-desc">{"Gezegenlerin ince detaylarını yakalamak için devasa diyaframlı profesyonel araç." if lang=="TR" else "Massive aperture for capturing planetary details."}</p></div></div>""", unsafe_allow_html=True)
    with e3: st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800"><div class="service-content"><h3 class="service-title">Lunt Solar Systems</h3><p class="service-desc">{"Güneş patlamalarını güvenle izlemenizi sağlayan teleskop." if lang=="TR" else "Specialized telescope for viewing solar flares safely."}</p></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 16: ASTRO-FOTOĞRAF
# ==============================================================================
elif menu_secimi in ["ASTRO-FOTOĞRAF", "ASTRO-PHOTO"]:
    st.markdown("<h2>{}</h2>".format("Astro-Fotoğrafçılık Simülatörü" if lang == "TR" else "Astro-Photography Simulator"), unsafe_allow_html=True); st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl: iso_val = st.slider("ISO Değeri / ISO Value", 100, 6400, 800, step=100); exp_val = st.slider("Pozlama Süresi / Exposure (s)", 1, 30, 10, step=1)
    with col_view: st.markdown(f"""<div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);"><img src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200" style="width: 100%; filter: brightness({0.15 + (exp_val / 30.0) * 0.6 + (iso_val / 6400.0) * 0.5});"></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 17: REZERVASYON
# ==============================================================================
elif menu_secimi in ["REZERVASYON", "BOOKING"]:
    st.markdown("<h2>{}</h2>".format("Online Rezervasyon & Biletleme" if lang == "TR" else "Online Booking & Ticketing"), unsafe_allow_html=True)
    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    with col_center:
        deneyim_turu = st.radio("Seçiminiz / Choice:", ["Gece Gözlem Turu ($150)", "Astro-Fotoğrafçılık ($250)", "VIP Konaklama ($800)"])
        col_form1, col_form2 = st.columns(2)
        with col_form1: secilen_tarih = st.date_input("Tarih / Date", min_value=datetime.date.today())
        with col_form2: kisi_sayisi = st.slider("Misafir Sayısı / Guests", 1, 8, 2)
        fiyat = 150 if "150" in deneyim_turu else 250 if "250" in deneyim_turu else 800
        st.markdown(f"<div class='price-tag'>${(fiyat * kisi_sayisi):,} <span style='font-size: 1rem; color: #C5A059;'>USD</span></div>", unsafe_allow_html=True)
        if st.button("Gönder / Submit"): st.success("Talebiniz başarıyla alınmıştır." if lang == "TR" else "Request submitted successfully.")

# ==============================================================================
# SAYFA 18: SÜRDÜRÜLEBİLİRLİK
# ==============================================================================
elif menu_secimi in ["SÜRDÜRÜLEBİLİRLİK", "SUSTAINABILITY"]:
    st.markdown("<h2>{}</h2>".format("Sürdürülebilir Bilimsel Turizm" if lang == "TR" else "Sustainable Science Tourism"), unsafe_allow_html=True)
    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    with col_center:
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh;" src="https://images.unsplash.com/photo-1502481851512-e9e2529bfbf9?q=80&w=1200"></div>', unsafe_allow_html=True)
        with st.expander("Işık Kirliliği Azaltımı" if lang == "TR" else "Light Pollution Reduction"): st.write("Tesislerimizde yalnızca kırmızı bazlı aydınlatmalar kullanılır." if lang == "TR" else "We only use red-based, low lumen lighting.")
        with st.expander("Sıfır Karbon Ayak İzi" if lang == "TR" else "Zero Carbon Footprint"): st.write("Turlarımızda elektrikli araçlar kullanılır." if lang == "TR" else "We use 100% zero-emission electric vehicles.")

# ==============================================================================
# SAYFA 19: YATIRIMCI PORTALI
# ==============================================================================
elif menu_secimi in ["YATIRIMCI PORTALI", "INVESTOR PORTAL"]:
    st.markdown("<h2>{}</h2>".format("Yatırımcı Portalı" if lang == "TR" else "Investor Portal"), unsafe_allow_html=True); st.write("---")
    if st.text_input("Şifre / Password (stellaris2026):", type="password") == "stellaris2026": 
        st.area_chart(pd.DataFrame({"Şili" if lang=="TR" else "Chile": [1000, 2500, 4800, 7500], "Yeni Zelanda" if lang=="TR" else "New Zealand": [800, 1900, 3500, 6000]}), color=["#B8860B", "#C5A059"])
