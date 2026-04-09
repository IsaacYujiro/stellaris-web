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

# MÜZİK ÇALAR (KOZMİK AMBİYANS)
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
    st.markdown("<p>Stellaris, sıradan tatil anlayışını geride bırakıp gözlerini evrenin derinliklerine çevirenler için doğdu. Işık kirliliğinden tamamen arınmış dünyanın en karanlık ve en berrak noktalarında, bilim ve doğayı kusursuz bir lüksle harmanlıyoruz.</p>", unsafe_allow_html=True)
    st.write("---")
    col_space1, col_image, col_space2 = st.columns([1, 8, 1])
    with col_image:
        st.markdown('<div class="hero-container"><img class="hero-image" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=2000&auto=format&fit=crop"></div>', unsafe_allow_html=True)

# ==============================================================================
# SAYFA 2: LOKASYONLARIMIZ
# ==============================================================================
elif menu_secimi in ["LOKASYONLARIMIZ", "OUR LOCATIONS"]:
    st.markdown("<h2>Hedef Ülkeler ve Küresel Pazar</h2>", unsafe_allow_html=True)
    st.markdown("<p>Evrenin en muazzam manzaralarını sunan stratejik karanlık gökyüzü rezervleri.</p>", unsafe_allow_html=True)
    st.write("---")
    col_space1, col_chile, col_nz, col_space2 = st.columns([1, 4, 4, 1])
    with col_chile:
        st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?q=80&w=800"><div class="service-content"><h3 class="service-title">Atacama Çölü, Şili</h3><p class="service-desc">Yılda 300 günden fazla bulutsuz gece. Dünyanın en kurak çölünde, evreni yüksek rakımdan izleyin.</p></div></div>""", unsafe_allow_html=True)
    with col_nz:
        st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=800"><div class="service-content"><h3 class="service-title">Tekapo Gölü, Yeni Zelanda</h3><p class="service-desc">Uluslararası karanlık gökyüzü rezervi. Güney Haçı takımyıldızını ve Aurora Australis'i deneyimleyin.</p></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 3: ÖTEGEZEGEN TURİZMİ
# ==============================================================================
elif menu_secimi in ["ÖTEGEZEGEN TURİZMİ", "EXOPLANET TOURISM"]:
    st.markdown("<h2>Geleceğin Turizmi: Ötegezegenler</h2>", unsafe_allow_html=True)
    st.markdown("<p>Dünya'nın sınırları size yetmiyorsa, galaksinin derinliklerindeki yeni evleri keşfedin.</p>", unsafe_allow_html=True)
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="planet-card" style="padding: 30px; text-align: center;"><h3 style="color: #D4AF37; margin-bottom: 20px;">TRAPPIST-1e</h3><img class="spinning-planet" src="https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=400" style="filter: hue-rotate(150deg) saturate(200%);"><p style="color: #E0E0E0; font-size: 0.9rem; text-align: left !important;"><b>Uzaklık:</b> 39 Işık Yılı<br><b>Durum:</b> Okyanus Gezegeni</p><div style="color: #B8860B; font-weight: bold; margin-top: 15px;">BİLET: $4.5 Milyon</div></div>""", unsafe_allow_html=True)
        st.button("Yer Ayırt", key="b1")
    with c2:
        st.markdown("""<div class="planet-card" style="padding: 30px; text-align: center; border-color: #D4AF37 !important; box-shadow: 0 0 30px rgba(212,175,55,0.2) !important;"><div style="background: #D4AF37; color: #000; padding: 5px; font-weight: bold; border-radius: 4px; margin-bottom: 10px; display: inline-block;">EN POPÜLER</div><h3 style="color: #D4AF37; margin-bottom: 20px;">Kepler-186f</h3><img class="spinning-planet" src="https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=400" style="filter: hue-rotate(240deg) saturate(150%);"><p style="color: #E0E0E0; font-size: 0.9rem; text-align: left !important;"><b>Uzaklık:</b> 582 Işık Yılı<br><b>Durum:</b> Kızıl Bitki Örtüsü</p><div style="color: #B8860B; font-weight: bold; margin-top: 15px;">BİLET: $8.2 Milyon</div></div>""", unsafe_allow_html=True)
        st.button("Yer Ayırt", key="b2")
    with c3:
        st.markdown("""<div class="planet-card" style="padding: 30px; text-align: center;"><h3 style="color: #D4AF37; margin-bottom: 20px;">Proxima Centauri b</h3><img class="spinning-planet" src="https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=400" style="filter: hue-rotate(60deg) saturate(80%);"><p style="color: #E0E0E0; font-size: 0.9rem; text-align: left !important;"><b>Uzaklık:</b> 4.2 Işık Yılı<br><b>Durum:</b> Sert İklim</p><div style="color: #B8860B; font-weight: bold; margin-top: 15px;">BİLET: $1.2 Milyon</div></div>""", unsafe_allow_html=True)
        st.button("Yer Ayırt", key="b3")

# ==============================================================================
# SAYFA 4: CANLI GÖZLEMEVİ 
# ==============================================================================
elif menu_secimi in ["CANLI GÖZLEMEVİ", "LIVE OBSERVATORY"]:
    st.markdown("<h2>Stellaris Kesintisiz Uydu Ağı</h2>", unsafe_allow_html=True)
    st.markdown("<p>Aşağıdaki tüm kanallar doğrudan NASA ve NOAA uydularından alınan ham veri akışlarıdır.</p>", unsafe_allow_html=True)
    st.write("---")
    t1, t2, t3, t4, t5, t6, t7 = st.tabs(["🌍 GOES-16", "🌍 HIMAWARI", "☀️ SDO 304", "☀️ SDO 171", "🛰️ SOHO C3", "📍 ISS RADAR", "🔭 TELESKOP SİM."])
    with t1: components.html(auto_refresh_image("goes16_img", "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/latest.jpg", 60000, "LIVE: GOES-16", "550px"), height=650)
    with t2: components.html(auto_refresh_image("himawari_img", "https://cdn.star.nesdis.noaa.gov/AHI/FD/GEOCOLOR/latest.jpg", 60000, "LIVE: HIMAWARI-9", "550px"), height=650)
    with t3: components.html(auto_refresh_image("sdo304_img", "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0304.jpg", 60000, "LIVE: SDO 304", "550px"), height=650)
    with t4: components.html(auto_refresh_image("sdo171_img", "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0171.jpg", 60000, "LIVE: SDO 171", "550px"), height=650)
    with t5: components.html(auto_refresh_image("sohoc3_img", "https://soho.nascom.nasa.gov/data/realtime/c3/1024/latest.jpg", 60000, "LIVE: SOHO C3", "550px"), height=650)
    with t6: st.markdown("""<div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; height: 550px; background: rgba(5,16,36,0.5);"><iframe src="https://isstracker.spaceflight.esa.int/" width="100%" height="100%" frameborder="0" style="pointer-events: none;"></iframe></div>""", unsafe_allow_html=True)
    with t7:
        if "telescope_connected" not in st.session_state: st.session_state.telescope_connected = False
        istasyon = st.selectbox("İstasyon / Station:", ["Atacama Alpha (Celestron 1100 HD)", "Tekapo South (Meade LX200 14'')"])
        if st.button("Sanal Bağlantı Kur / Connect"):
            with st.spinner("Bağlanılıyor..."): time.sleep(1)
            st.session_state.telescope_connected = True
        if st.session_state.telescope_connected:
            col_view, col_controls = st.columns([2, 1])
            with col_controls:
                zoom_level = st.slider("Zoom", 1.0, 3.0, 1.0, 0.1)
                filter_type = st.radio("Filtre / Filter", ["Görünür / Visible", "H-Alpha (Kızıl)", "O-III (Mavi)"])
                css_filter = "sepia(100%) hue-rotate(-50deg) saturate(300%)" if "H-Alpha" in filter_type else "sepia(100%) hue-rotate(130deg) saturate(200%)" if "O-III" in filter_type else "none"
            with col_view:
                deep_space_img = "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=1200" if "Atacama" in istasyon else "https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?q=80&w=1200"
                st.markdown(f"""<div style="width: 100%; height: 400px; border: 2px solid #B8860B; border-radius: 8px; overflow: hidden; background: #000; position: relative;"><div style="position: absolute; top: 15px; left: 15px; color: red; font-family: monospace; font-weight: bold; z-index: 10;"><span style="animation: blink 1s infinite;">●</span> SIMULATION</div><img src="{deep_space_img}" style="width: 100%; height: 100%; object-fit: cover; transform: scale({zoom_level}); filter: {css_filter}; transition: all 0.5s ease;"></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 5: 3D SİMÜLASYONLAR (GÖKYÜZÜ İFRAME İLE DÜZELTİLDİ)
# ==============================================================================
elif menu_secimi in ["3D SİMÜLASYONLAR", "3D SIMULATIONS"]:
    st.markdown("<h2>İnteraktif 3D Uzay Simülatörleri</h2>", unsafe_allow_html=True)
    st.write("---")
    t_earth, t_solar, t_exo, t_ast, t_sky = st.tabs(["🌍 3D DÜNYA", "🪐 GÜNEŞ SİSTEMİ", "☄️ ASTEROİT AVI", "👽 ÖTEGEZEGENLER", "🌌 CANLI GÖKYÜZÜ"])
    style_str = "border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5); background: rgba(5,16,36,0.5);"
    with t_earth: st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/earth/#/" width="100%" height="600" frameborder="0"></iframe></div>""", unsafe_allow_html=True)
    with t_solar: st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/solar-system/#/home?embed=true" width="100%" height="600" frameborder="0"></iframe></div>""", unsafe_allow_html=True)
    with t_ast: st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/asteroids/#/?embed=true" width="100%" height="600" frameborder="0"></iframe></div>""", unsafe_allow_html=True)
    with t_exo: st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/exo/#/?embed=true" width="100%" height="600" frameborder="0"></iframe></div>""", unsafe_allow_html=True)
    with t_sky:
        loc_choice = st.selectbox("Gözlem Noktası Seçin:", ["Atacama Çölü, Şili", "Tekapo Gölü, Yeni Zelanda", "Kuzey Kutbu"])
        lat, lon = (-23.0, -67.7) if "Atacama" in loc_choice else (-44.0, 170.4) if "Tekapo" in loc_choice else (69.6, 18.9)
        sky_url = f"https://virtualsky.lco.global/embed/index.html?longitude={lon}&latitude={lat}&projection=stereo&constellations=true&constellationlabels=true&meteorshowers=true&showstarlabels=true&live=true&az=180&color=dark"
        components.iframe(sky_url, height=600)

# ==============================================================================
# SAYFA 6: KARA DELİK FİZİK MOTORU
# ==============================================================================
elif menu_secimi in ["KARA DELİK SİM.", "BLACK HOLE SIM."]:
    st.markdown("<h2>Kara Delik & Kütleçekim Simülatörü</h2>", unsafe_allow_html=True)
    st.write("---")
    bh_html = """
    <div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; background: rgba(5,16,36,0.6); backdrop-filter: blur(10px); padding: 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.5);">
        <div style="color: #D4AF37; font-family: 'Cinzel', serif; font-size:1.5rem; margin-bottom: 20px; text-align: center; letter-spacing: 2px;">GRAVITY ENGINE v1.0</div>
        <div style="display: flex; justify-content: center; gap: 30px; margin-bottom: 30px;">
            <label style="color: #E0E0E0; font-family: 'Montserrat', sans-serif;">Kütle (Mass): <input type="range" id="massSlider" min="50" max="300" value="150" style="accent-color: #B8860B;"></label>
            <label style="color: #E0E0E0; font-family: 'Montserrat', sans-serif;">Hız (Velocity): <input type="range" id="speedSlider" min="1" max="10" value="5" style="accent-color: #B8860B;"></label>
        </div>
        <canvas id="bhCanvas" width="800" height="500" style="display: block; margin: 0 auto; background: radial-gradient(circle at center, #0a1930 0%, #000 100%); border-radius: 8px; border: 1px solid rgba(184,134,11,0.2);"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('bhCanvas'); const ctx = canvas.getContext('2d');
        const massSlider = document.getElementById('massSlider'); const speedSlider = document.getElementById('speedSlider');
        let particles = [];
        for(let i=0; i<350; i++) { particles.push({x: Math.random() * canvas.width, y: Math.random() * canvas.height, vx: (Math.random() - 0.5) * 3, vy: (Math.random() - 0.5) * 3, color: `hsl(${Math.random() * 50 + 15}, 100%, 65%)`}); }
        function animate() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.15)'; ctx.fillRect(0, 0, canvas.width, canvas.height);
            const cx = canvas.width / 2; const cy = canvas.height / 2; const mass = parseInt(massSlider.value); const speedMult = parseInt(speedSlider.value) / 5;
            ctx.beginPath(); ctx.arc(cx, cy, mass / 3, 0, Math.PI * 2); ctx.fillStyle = '#000'; ctx.fill(); ctx.lineWidth = 2; ctx.strokeStyle = 'rgba(212, 175, 55, 0.8)'; ctx.stroke(); ctx.shadowBlur = Math.random() * 20 + 30; ctx.shadowColor = '#D4AF37';
            ctx.shadowBlur = 0;
            particles.forEach(p => {
                const dx = cx - p.x; const dy = cy - p.y; const dist = Math.sqrt(dx*dx + dy*dy);
                const force = (mass * 6) / (dist * dist); p.vx += (dx / dist) * force; p.vy += (dy / dist) * force;
                p.x += p.vx * speedMult; p.y += p.vy * speedMult;
                if(dist < mass / 3) { p.x = Math.random() * canvas.width; p.y = 0; p.vx = (Math.random() - 0.5) * 3; p.vy = Math.random() * 2; }
                ctx.beginPath(); ctx.arc(p.x, p.y, 1.5, 0, Math.PI * 2); ctx.fillStyle = p.color; ctx.fill();
            });
            requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(bh_html, height=750)

# ==============================================================================
# YENİ SAYFA 7: UZAY SESLERİ (VİDEO EMBED İLE HATASIZ HALE GETİRİLDİ)
# ==============================================================================
elif menu_secimi in ["UZAY SESLERİ", "SPACE SOUNDS"]:
    st.markdown("<h2>Uzay Sesleri Laboratuvarı</h2>", unsafe_allow_html=True)
    st.markdown("<p>NASA'nın kaydettiği elektromanyetik dalgaların sese dönüştürüldüğü resmi kayıtlar.</p>", unsafe_allow_html=True)
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="service-card" style="height:auto; border: none; box-shadow: none;"><div class="service-content"><h3 class="service-title">Jüpiter'in Elektromanyetik Sesi</h3><p class="service-desc">Juno aracının Jüpiter manyetik alanından geçerken kaydettiği plazma dalgaları.</p></div></div>""", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=e3fqE01YYWs")
    with col2:
        st.markdown("""<div class="service-card" style="height:auto; border: none; box-shadow: none;"><div class="service-content"><h3 class="service-title">Perseus Kara Deliği</h3><p class="service-desc">Bir kara deliğin etrafındaki gaz dalgalanmalarının sese dönüştürülmüş hali.</p></div></div>""", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=ioR54X7idHU")

# ==============================================================================
# YENİ SAYFA 8: KOZMİK BUTİK (KIRIK RESİMLER ONARILDI)
# ==============================================================================
elif menu_secimi in ["KOZMİK BUTİK", "COSMIC BOUTIQUE"]:
    st.markdown("<h2>Kozmik Butik & Koleksiyon</h2>", unsafe_allow_html=True)
    st.markdown("<p>VIP müşterilerimiz için tasarlanmış sertifikalı uzay objeleri ve premium gözlem ekipmanları.</p>", unsafe_allow_html=True)
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1614729939124-03290b56c9ce?q=80&w=600"><div class="service-content"><h3 class="service-title">Pallasite Meteorit</h3><p class="service-desc">4.5 milyar yaşında, sertifikalı zeytuni kristalli demir-nikel göktaşı parçası.</p><div class="price-tag" style="font-size: 2rem;">$5,400</div></div></div>""", unsafe_allow_html=True)
        st.button("Sepete Ekle", key="m1")
    with c2:
        st.markdown("""<div class="service-card" style="border-color: #D4AF37 !important; box-shadow: 0 0 20px rgba(212,175,55,0.3) !important;"><div style="background: #D4AF37; color: #000; padding: 5px; font-weight: bold; text-align:center;">LİMİTLİ ÜRETİM</div><img class="service-img" src="https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?q=80&w=600"><div class="service-content"><h3 class="service-title">EVA Astronot Kostümü</h3><p class="service-desc">Giyilebilir NASA replikası. Kask içi iletişim sistemi entegreli.</p><div class="price-tag" style="font-size: 2rem;">$12,000</div></div></div>""", unsafe_allow_html=True)
        st.button("Sepete Ekle", key="m2")
    with c3:
        st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1517976487492-5750f3195933?q=80&w=600"><div class="service-content"><h3 class="service-title">Altın Kaplama Teleskop</h3><p class="service-desc">Kişiye özel işlenmiş 18 ayar altın kaplama masaüstü gözlem aracı.</p><div class="price-tag" style="font-size: 2rem;">$8,500</div></div></div>""", unsafe_allow_html=True)
        st.button("Sepete Ekle", key="m3")

# ==============================================================================
# SAYFA 9: STELLARIS AI
# ==============================================================================
elif menu_secimi in ["STELLARIS AI"]:
    st.markdown("<h2>Stellaris Kozmik Rehber (AI Asistan)</h2>", unsafe_allow_html=True)
    st.write("---")
    if "messages" not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "Stellaris VIP Kontrol Paneline hoş geldiniz. Ben Stellaris AI. Size nasıl yardımcı olabilirim?"}]
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])
    if prompt := st.chat_input("Mesajınızı yazın..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Kozmik veritabanı taranıyor..."):
                time.sleep(1)
                lower_prompt = prompt.lower()
                if "atacama" in lower_prompt: response = "Şili'deki Atacama Çölü, yılda 300'den fazla bulutsuz gecesi ile dünyanın en iyi gözlem noktasıdır."
                elif "tekapo" in lower_prompt: response = "Yeni Zelanda'daki Tekapo Gölü, Uluslararası Karanlık Gökyüzü Rezervidir."
                else: response = "Uzman astronomlarımız size en iyi deneyimi sunmak için 'Uzay Pasaportu' oluşturmanızı öneriyor."
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

# ==============================================================================
# SAYFA 10: UZAY PASAPORTU
# ==============================================================================
elif menu_secimi in ["UZAY PASAPORTU", "SPACE PASSPORT"]:
    st.markdown("<h2>Kişisel Uzay Biniş Kartı</h2>", unsafe_allow_html=True)
    st.write("---")
    col_form, col_pass = st.columns([1, 2])
    with col_form:
        pass_name = st.text_input("Yolcu Adı / Name:", "Yusuf Sezer Korkmaz")
        pass_dest = st.selectbox("Hedef / Destination:", ["Atacama Çölü", "Tekapo Gölü", "TRAPPIST-1e", "Kepler-186f"])
        pass_class = st.selectbox("Sınıf / Class:", ["VIP Astro-Turist", "Uzay Komutanı"])
        pass_date = st.date_input("Tarih / Date:", datetime.date.today())
        generate_btn = st.button("Kartı Oluştur")
    with col_pass:
        random_barcode = "".join([str(random.randint(0, 9)) for _ in range(12)])
        pass_html = f"""
        <div class="boarding-pass"><div class="pass-left"><div class="pass-title">STELLARIS ASTRO-LINES</div><br>
        <div style="display: flex; justify-content: space-between;"><div><div class="pass-label">PASSENGER NAME</div><div class="pass-value">{pass_name.upper()}</div></div>
        <div><div class="pass-label">FLIGHT CLASS</div><div class="pass-value">{pass_class.upper()}</div></div></div>
        <div style="display: flex; justify-content: space-between;"><div><div class="pass-label">DESTINATION</div><div class="pass-value">{pass_dest.upper()}</div></div>
        <div><div class="pass-label">DATE</div><div class="pass-value">{pass_date.strftime('%d %b %Y')}</div></div></div>
        <div class="pass-barcode">||| | || ||| | ||| || {random_barcode}</div></div><div class="pass-right"><div class="pass-logo">STELLARIS</div></div></div>
        """
        st.markdown(pass_html, unsafe_allow_html=True)

# ==============================================================================
# SAYFA 11: VİDEOLAR GALERİSİ
# ==============================================================================
elif menu_secimi in ["VİDEOLAR GALERİSİ", "VIDEO GALLERY"]:
    st.markdown("<h2>Stellaris Uzay ve Bilim Sineması</h2>", unsafe_allow_html=True); st.write("---")
    v_col1, v_col2 = st.columns(2)
    with v_col1: st.markdown("<h3>James Webb Teleskobu</h3>", unsafe_allow_html=True); st.video("https://www.youtube.com/watch?v=uD4izuDMUQA"); st.markdown("<br><h3>SpaceX Starship Fırlatması</h3>", unsafe_allow_html=True); st.video("https://www.youtube.com/watch?v=-1wcilQ58hI")
    with v_col2: st.markdown("<h3>Mars Yüzeyi 4K</h3>", unsafe_allow_html=True); st.video("https://www.youtube.com/watch?v=ZEyAs3NWH4A"); st.markdown("<br><h3>Dünya 4K Manzaralar</h3>", unsafe_allow_html=True); st.video("https://www.youtube.com/watch?v=Un5SEJ8MyPc")

# ==============================================================================
# SAYFA 12: KOZMİK TAKVİM (KIRIK RESİM ONARILDI)
# ==============================================================================
elif menu_secimi in ["KOZMİK TAKVİM", "COSMIC CALENDAR"]:
    st.markdown("<h2>Kozmik Takvim & Nadir Fenomenler</h2>", unsafe_allow_html=True); st.write("---")
    selected_event = st.selectbox("Seçiniz / Select:", ["Perseid Göktaşı Yağmuru", "Satürn Karşı Konumu", "Tam Güneş Tutulması"])
    col_info, col_metrics = st.columns([2, 1])
    with col_info:
        img_url = "https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?q=80&w=800" if "Perseid" in selected_event else "https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=800" if "Sat" in selected_event else "https://images.unsplash.com/photo-1485795959911-ea5ebf41b6ae?q=80&w=800"
        st.markdown(f"""<div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; padding: 25px; background: rgba(5,16,36,0.5); backdrop-filter: blur(10px);"><img src="{img_url}" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;"></div>""", unsafe_allow_html=True)
    with col_metrics: st.metric("Görüş / Visibility", "Ultra HD", "99%"); st.progress(60 if "Perseid" in selected_event else 85 if "Sat" in selected_event else 98); st.button("Rezervasyon / Book")

# ==============================================================================
# SAYFA 13: UZAY HAVADURUMU
# ==============================================================================
elif menu_secimi in ["UZAY HAVADURUMU", "SPACE WEATHER"]:
    st.markdown("<h2>Canlı Uzay Hava Durumu</h2>", unsafe_allow_html=True); st.write("---")
    c1, c2, c3 = st.columns(3); c1.metric("Kp İndeksi", "6.33", "+1.2"); c2.metric("Güneş Rüzgarı", "540 km/s", "+45"); c3.metric("Bz (Manyetik)", "-5.2 nT", "Güney")
    st.write("---"); st.area_chart(pd.DataFrame({"Kp": [2.3, 4.0, 6.3, 5.1, 3.2, 2.0, 4.5, 7.1, 5.0]}), color="#B8860B")

# ==============================================================================
# SAYFA 14: IŞIK KİRLİLİĞİ
# ==============================================================================
elif menu_secimi in ["IŞIK KİRLİLİĞİ", "LIGHT POLLUTION"]:
    st.markdown("<h2>Bortle Scale: Işık Kirliliği Simülatörü</h2>", unsafe_allow_html=True); st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl: bortle_val = st.slider("Gökyüzü Kalitesi", 1, 9, 9, step=2)
    with col_view: st.markdown(f"""<div style="position: relative; width: 100%; height: 400px; border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);"><img src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200" style="width: 100%; height: 100%; object-fit: cover; filter: brightness({1.2 - ((bortle_val - 1) / 8.0)}) contrast(1.2);"><div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(200,100,50,0.9), rgba(50,70,100,0.8)); opacity: {(bortle_val - 1) / 8.0}; pointer-events: none;"></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 15: EKİPMANLAR (AÇIKLAMALAR GERİ GETİRİLDİ)
# ==============================================================================
elif menu_secimi in ["EKİPMANLAR", "EQUIPMENT"]:
    st.markdown("<h2>VIP Gözlem Ekipmanları</h2>", unsafe_allow_html=True)
    st.markdown("<p>Gözlemlerimiz sırasında misafirlerimize sunulan en üst düzey teknolojik optik ekipmanlar.</p>", unsafe_allow_html=True)
    st.write("---")
    e1, e2, e3 = st.columns(3)
    with e1: st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1517976487492-5750f3195933?q=80&w=800"><div class="service-content"><h3 class="service-title">Celestron CPC 1100</h3><p class="service-desc">Derin uzay nesneleri (Galaksiler ve Bulutsular) için tasarlanmış ultra HD teleskop.</p></div></div>""", unsafe_allow_html=True)
    with e2: st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1506443432602-ac2fcd6f54e0?q=80&w=800"><div class="service-content"><h3 class="service-title">Meade LX200 14''</h3><p class="service-desc">Gezegenlerin ince detaylarını yakalamak için devasa diyaframlı profesyonel araç.</p></div></div>""", unsafe_allow_html=True)
    with e3: st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800"><div class="service-content"><h3 class="service-title">Lunt Solar Systems</h3><p class="service-desc">Gündüz aktiviteleri için güneş patlamalarını güvenle izlemenizi sağlayan teleskop.</p></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 16: ASTRO-FOTOĞRAF
# ==============================================================================
elif menu_secimi in ["ASTRO-FOTOĞRAF", "ASTRO-PHOTO"]:
    st.markdown("<h2>Astro-Fotoğrafçılık Simülatörü</h2>", unsafe_allow_html=True); st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl: iso_val = st.slider("ISO Değeri", 100, 6400, 800, step=100); exp_val = st.slider("Pozlama Süresi (s)", 1, 30, 10, step=1)
    with col_view: st.markdown(f"""<div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);"><img src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200" style="width: 100%; filter: brightness({0.15 + (exp_val / 30.0) * 0.6 + (iso_val / 6400.0) * 0.5});"></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 17: REZERVASYON (TAM FORM GERİ GETİRİLDİ)
# ==============================================================================
elif menu_secimi in ["REZERVASYON", "BOOKING"]:
    st.markdown("<h2>Online Rezervasyon & Biletleme</h2>", unsafe_allow_html=True)
    st.markdown("<p>Mükemmel karanlığa olan yolculuğunuzu seçin ve yerinizi ayırtın.</p>", unsafe_allow_html=True)
    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    with col_center:
        deneyim_turu = st.radio("Astro-Deneyiminizi Seçin", ["Gece Gözlem Turu ve Mitoloji ($150)", "Astro-Fotoğrafçılık Workshop'u ($250)", "VIP Premium Çöl Konaklaması ($800)"])
        st.write("---")
        col_form1, col_form2 = st.columns(2)
        with col_form1: secilen_tarih = st.date_input("Tarih / Date", min_value=datetime.date.today())
        with col_form2: kisi_sayisi = st.slider("Misafir Sayısı", 1, 8, 2)
        fiyat = 150 if "150" in deneyim_turu else 250 if "250" in deneyim_turu else 800
        st.markdown(f"<div class='price-tag'>${(fiyat * kisi_sayisi):,} <span style='font-size: 1rem; color: #C5A059;'>USD Toplam</span></div>", unsafe_allow_html=True)
        if st.button("Rezervasyon Gönder"): st.success("Talebiniz başarıyla alınmıştır. Dijital ekibimiz iletişim kuracaktır.")

# ==============================================================================
# SAYFA 18: SÜRDÜRÜLEBİLİRLİK (AKORDEONLAR GERİ GETİRİLDİ)
# ==============================================================================
elif menu_secimi in ["SÜRDÜRÜLEBİLİRLİK", "SUSTAINABILITY"]:
    st.markdown("<h2>Sürdürülebilir Bilimsel Turizm</h2>", unsafe_allow_html=True)
    st.markdown("<p>Doğaya ve Gökyüzüne Saygı. Evrenin güzelliklerini keşfederken dünyamızı koruyoruz.</p>", unsafe_allow_html=True)
    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    with col_center:
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh;" src="https://images.unsplash.com/photo-1502481851512-e9e2529bfbf9?q=80&w=1200"></div>', unsafe_allow_html=True)
        with st.expander("Işık Kirliliği Azaltımı"): st.write("Tesislerimizde gökyüzü gözlemini engellememesi için yalnızca kırmızı bazlı, düşük lümenli zemin aydınlatmaları ve harekete duyarlı sensörler kullanılmaktadır.")
        with st.expander("Sıfır Karbon Ayak İzi"): st.write("Gözlem noktalarına ulaşım sağlayan turlarımızda tamamen sıfır emisyonlu elektrikli araçlar ve güneş paneli destekli üniteler kullanılmaktadır.")
        with st.expander("Yerel İş Birliği ve Tasarım"): st.write("Bölge halkı istihdam edilmekte, tesis mimarisinde doğanın silüetini bozmayan minimal yaklaşım tercih edilmektedir.")

# ==============================================================================
# SAYFA 19: YATIRIMCI PORTALI
# ==============================================================================
elif menu_secimi in ["YATIRIMCI PORTALI", "INVESTOR PORTAL"]:
    st.markdown("<h2>Yatırımcı Portalı</h2>", unsafe_allow_html=True); st.write("---")
    if st.text_input("Şifre (stellaris2026):", type="password") == "stellaris2026": st.area_chart(pd.DataFrame({"Şili": [1000, 2500, 4800, 7500], "Yeni Zelanda": [800, 1900, 3500, 6000]}), color=["#B8860B", "#C5A059"])
