"""
=========================================================================================
STELLARIS INTERNATIONAL ASTRO-TOURISM HOLDING - VIP PORTAL
Versiyon: 7.0.0 (Corporate Production-Ready Master Build)
Açıklama: Ultra Yüksek Net Değere Sahip Bireyler (UHNWI) için tasarlanmış, 
tamamen duyarlı, yasal/kurumsal sayfaları eklenmiş, optimize edilmiş final sürümü.
=========================================================================================
"""

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import datetime
import time
import os
import glob
import random

# =======================================================================================
# 1. SİTE YAPILANDIRMASI VE ULTRA-LÜKS ANİMASYONLU CSS MİMARİSİ
# =======================================================================================
st.set_page_config(page_title="Stellaris | Premium Astro-Tourism", page_icon="🌌", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&family=Cinzel:wght@400;600;700&display=swap');

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
        animation: starBackground 200s linear infinite;
    }
    @keyframes starBackground { 
        0% { background-position: 0 0, 40px 60px, 130px 270px; } 
        100% { background-position: -550px -550px, -310px -290px, 380px 520px; } 
    }

    header { background-color: transparent !important; }
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; color: #E0E0E0; text-align: center; }
    
    [data-testid="stSidebar"] { background: rgba(3, 8, 20, 0.85) !important; backdrop-filter: blur(20px) !important; border-right: 1px solid rgba(184, 134, 11, 0.4) !important; }
    [data-testid="stSidebar"] * { color: #B8860B !important; }

    div[role="radiogroup"] > label > div:first-of-type { display: none !important; }
    div[role="radiogroup"] p { color: #B8860B !important; font-family: 'Cinzel', serif !important; font-size: 1.05rem !important; font-weight: 600 !important; text-align: center !important; visibility: visible !important; display: block !important; width: 100%; margin-top: 5px; transition: all 0.4s ease; padding: 10px 0; border-radius: 6px; letter-spacing: 1px;}
    div[role="radiogroup"] label:hover p { color: #D4AF37 !important; text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.5); background: rgba(184, 134, 11, 0.1); transform: translateX(8px);}
    div[role="radiogroup"] label[aria-checked="true"] p { color: #FFD700 !important; text-shadow: 0px 0px 15px rgba(255, 215, 0, 0.8); border-bottom: 2px solid #B8860B; background: rgba(184, 134, 11, 0.2); transform: scale(1.02);}

    [data-baseweb="select"], input[type="text"], input[type="password"], textarea { background-color: rgba(3, 8, 20, 0.6) !important; border: 1px solid #B8860B !important; border-radius: 6px; backdrop-filter: blur(5px); color: #FFF !important;}
    [data-baseweb="select"] * { color: #C5A059 !important; font-family: 'Montserrat', sans-serif !important; }
    
    div[data-testid="stMetricValue"] { color: #D4AF37 !important; font-family: 'Cinzel', serif !important; font-size: 2.8rem !important; text-shadow: 0px 0px 20px rgba(212, 175, 55, 0.6); transition: transform 0.4s ease; display: inline-block;}
    div[data-testid="stMetricValue"]:hover { transform: scale(1.1); color: #FFD700 !important; }
    div[data-testid="stMetricLabel"] { color: #B8860B !important; font-family: 'Montserrat', sans-serif !important; font-size: 1.2rem !important; font-weight: 500; }
    
    h1, h2, h3, h4, h5, h6 { font-family: 'Cinzel', serif; font-weight: 700; text-align: center !important; width: 100%; background: linear-gradient(45deg, #C5A059, #F3E5AB, #D4AF37, #B8860B); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: shine 6s linear infinite; padding-bottom: 10px;}
    @keyframes shine { to { background-position: 200% center; } }
    
    .hero-title { font-size: 5.5rem; letter-spacing: 12px; margin-bottom: 10px; animation: pulseGlow 4s infinite alternate; }
    @keyframes pulseGlow { from { text-shadow: 0 0 10px rgba(212,175,55,0.2); } to { text-shadow: 0 0 30px rgba(212,175,55,0.7); } }

    p { text-align: center !important; margin: 0 auto 15px auto !important; max-width: 950px; line-height: 1.9; color: #a8b2d1 !important; font-weight: 300; font-size: 1.05rem;}
    hr { border-top: 1px solid rgba(184, 134, 11, 0.3) !important; width: 70%; margin: 45px auto !important; }

    .block-container { animation: fadeSlideUp 1.2s cubic-bezier(0.165, 0.84, 0.44, 1); }
    @keyframes fadeSlideUp { from { opacity: 0; transform: translateY(50px); } to { opacity: 1; transform: translateY(0); } }

    .hero-image { width: 100%; max-width: 1400px; height: 60vh; object-fit: cover; border-radius: 12px; filter: brightness(65%); border: 1px solid rgba(184, 134, 11, 0.5); animation: slowZoom 40s infinite alternate cubic-bezier(0.455, 0.03, 0.515, 0.955); }
    @keyframes slowZoom { from { transform: scale(1); } to { transform: scale(1.1); } }
    .hero-container { position: relative; text-align: center; margin-bottom: 50px; display: flex; justify-content: center; overflow: hidden; border-radius: 12px; box-shadow: 0 20px 50px rgba(0,0,0,0.8);}

    .service-card, .planet-card, .stat-box, .info-panel { background: rgba(5, 16, 36, 0.45) !important; backdrop-filter: blur(15px) !important; border-radius: 16px !important; border: 1px solid rgba(184, 134, 11, 0.3) !important; box-shadow: 0 10px 40px 0 rgba(0, 0, 0, 0.6) !important; transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; overflow: hidden; }
    .service-card:hover, .planet-card:hover, .stat-box:hover, .info-panel:hover { transform: translateY(-8px) scale(1.02) !important; border-color: rgba(212, 175, 55, 0.9) !important; box-shadow: 0 20px 50px rgba(184, 134, 11, 0.25) !important; }
    
    .stat-box { padding: 30px; text-align: center; margin-top: 20px; }
    .stat-number { font-family: 'Cinzel', serif; font-size: 3rem; color: #D4AF37; font-weight: bold; margin-bottom: 10px; text-shadow: 0 0 15px rgba(212, 175, 55, 0.5);}
    .stat-label { font-size: 1rem; text-transform: uppercase; color: #8892b0; letter-spacing: 2px; font-weight: 500;}

    .service-img { width: 100%; height: 260px; object-fit: cover; border-bottom: 1px solid rgba(184, 134, 11, 0.3); transition: transform 0.7s ease; }
    .service-card:hover .service-img { transform: scale(1.08); }
    .service-content { padding: 30px; }
    .price-tag { font-family: 'Cinzel', serif; font-size: 3.5rem; color: #D4AF37; font-weight: 700; margin: 30px 0; text-align: center; text-shadow: 0px 0px 25px rgba(184, 134, 11, 0.5); }
    
    .stButton { display: flex; justify-content: center; margin-top: 25px; }
    div.stButton > button:first-child { background: linear-gradient(135deg, rgba(3,8,20,0.95) 0%, rgba(17,34,64,0.95) 100%) !important; color: #D4AF37 !important; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 1.2rem; padding: 18px 60px; border: 1px solid rgba(184, 134, 11, 0.6) !important; border-radius: 40px; transition: all 0.4s ease; letter-spacing: 3px; text-transform: uppercase; box-shadow: 0 5px 20px rgba(0,0,0,0.6);}
    div.stButton > button:first-child:hover { background: linear-gradient(135deg, rgba(184, 134, 11, 0.25) 0%, rgba(212, 175, 55, 0.4) 100%) !important; color: #FFF !important; border-color: #D4AF37 !important; transform: translateY(-4px) scale(1.03); box-shadow: 0 0 25px rgba(212, 175, 55, 0.7) !important; }

    [data-baseweb="tab-list"] { justify-content: center; gap: 12px; flex-wrap: wrap; margin-bottom: 25px;}
    [data-baseweb="tab"] { background: rgba(5, 16, 36, 0.7) !important; color: #8892b0 !important; font-family: 'Cinzel', serif; font-size: 1rem; padding: 12px 25px; border-radius: 30px; border: 1px solid rgba(184,134,11,0.2) !important; transition: all 0.3s ease;}
    [aria-selected="true"] { background: rgba(184, 134, 11, 0.2) !important; color: #FFD700 !important; border-color: #D4AF37 !important; box-shadow: 0 0 20px rgba(184,134,11,0.3); transform: scale(1.05); }
    
    .stProgress > div > div > div > div { background: linear-gradient(90deg, #8B6508, #D4AF37, #F3E5AB) !important; }
    
    .spinning-planet { width: 280px; height: 280px; border-radius: 50%; display: block; margin: 0 auto 25px auto; box-shadow: inset -30px -30px 50px rgba(0,0,0,0.95), 0 0 40px rgba(184, 134, 11, 0.4); animation: spin 45s linear infinite; object-fit: cover;}
    @keyframes spin { 100% { transform: rotate(360deg); } }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    
    .mission-box { background: rgba(3, 8, 20, 0.75); border-left: 5px solid #D4AF37; padding: 35px; margin-bottom: 30px; border-radius: 0 12px 12px 0; text-align: left !important; box-shadow: 0 8px 20px rgba(0,0,0,0.5); transition: transform 0.3s ease;}
    .mission-box:hover { transform: translateX(10px); }
    .mission-box h3 { text-align: left !important; margin-bottom: 18px; color: #D4AF37; font-size: 1.8rem;}
    .mission-box p { text-align: left !important; font-size: 1.1rem; color: #E0E0E0 !important; line-height: 1.9;}
    
    th { background-color: rgba(184, 134, 11, 0.2) !important; color: #D4AF37 !important; font-family: 'Cinzel', serif; font-size: 1.1rem; }
    td { background-color: rgba(5, 16, 36, 0.4) !important; color: #E0E0E0 !important; border-bottom: 1px solid rgba(184, 134, 11, 0.2) !important;}
    
    .sidebar-footer { position: absolute; bottom: 10px; width: 100%; text-align: center; color: #8892b0; font-size: 0.75rem; font-family: 'Montserrat', sans-serif;}
    </style>
    """, unsafe_allow_html=True)

# =======================================================================================
# 2. OTURUM YÖNETİMİ (SESSION STATE)
# =======================================================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = ""

# =======================================================================================
# 3. YAN MENÜ (SIDEBAR) VE NAVİGASYON
# =======================================================================================
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
st.sidebar.write("---")

menu_secenekleri = [
    "ANA SAYFA", "LOKASYONLARIMIZ", "CANLI GÖZLEMEVİ", "3D SİMÜLASYONLAR", "KARA DELİK SİM.",
    "VİDEOLAR GALERİSİ", "KOZMİK TAKVİM", "UZAY HAVADURUMU", "IŞIK KİRLİLİĞİ", 
    "EKİPMAN KATALOĞU", "ASTRO-FOTOĞRAF", "VIP REZERVASYON", "VİZYON & SÜRDÜRÜLEBİLİRLİK",
    "DESTEK & SSS", "YASAL & ÇEREZLER", "YATIRIMCI PORTALI"
] if lang == "TR" else [
    "HOME", "OUR LOCATIONS", "LIVE OBSERVATORY", "3D SIMULATIONS", "BLACK HOLE SIM.",
    "VIDEO GALLERY", "COSMIC CALENDAR", "SPACE WEATHER", "LIGHT POLLUTION", 
    "EQUIPMENT CATALOG", "ASTRO-PHOTO", "VIP BOOKING", "VISION & SUSTAINABILITY",
    "SUPPORT & FAQ", "LEGAL & COOKIES", "INVESTOR PORTAL"
]

menu_secimi = st.sidebar.radio("Nav", menu_secenekleri, label_visibility="collapsed")
st.sidebar.write("---")

st.sidebar.markdown(f"<p style='color:#B8860B; font-size:0.85rem; font-weight:bold; margin-bottom:8px !important; letter-spacing:1px;'>{'Kozmik Ambiyans' if lang == 'TR' else 'Cosmic Ambient'}</p>", unsafe_allow_html=True)
st.sidebar.markdown("""
<audio controls autoplay loop style="width: 100%; height: 35px; outline: none; border-radius: 6px; opacity: 0.85; box-shadow: 0 2px 10px rgba(0,0,0,0.5);">
    <source src="https://cdn.pixabay.com/audio/2022/11/22/audio_febc508520.mp3" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

st.sidebar.write("---")
st.sidebar.info("Sistem: Çevrimiçi / Şifreli Bağlantı" if lang == "TR" else "System: Online / Secured")
st.sidebar.markdown("<div class='sidebar-footer'>Stellaris Corp. © 2026 | v7.0.0</div>", unsafe_allow_html=True)

def auto_refresh_image(img_id, img_url, refresh_rate_ms, title, max_width="600px", filter_css="none"):
    return f"""
    <div style="border: 1px solid rgba(184, 134, 11, 0.3); border-radius: 12px; position: relative; overflow: hidden; text-align: center; background: rgba(5,16,36,0.5); backdrop-filter: blur(10px); padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        <div style="position: absolute; top: 15px; left: 15px; background: rgba(0,0,0,0.8); padding: 6px 15px; color: #00e676; font-family: monospace; font-weight: bold; border: 1px solid rgba(0,230,118,0.5); z-index: 10; border-radius: 30px; font-size:12px; box-shadow: 0 0 12px rgba(0,230,118,0.3); letter-spacing:1px;">
            <span style="animation: blink 1s infinite;">●</span> {title}
        </div>
        <img id="{img_id}" src="{img_url}" style="width: 100%; max-width: {max_width}; border-radius: 8px; filter: {filter_css}; transition: all 0.3s ease;">
    </div>
    <script>
        setInterval(function() {{ 
            var img = document.getElementById('{img_id}');
            if (img) {{ img.src = '{img_url}?time=' + new Date().getTime(); }}
        }}, {refresh_rate_ms});
    </script>
    """

# =======================================================================================
# 4. SAYFA İÇERİKLERİ VE İŞ MANTIKLARI
# =======================================================================================

# ---------------------------------------------------------------------------------------
# SAYFA 1: ANA SAYFA 
# ---------------------------------------------------------------------------------------
if menu_secimi in ["ANA SAYFA", "HOME"]:
    col_logo, col_hero, col_empty = st.columns([1, 2, 1])
    with col_hero:
        if bulunan_logo: st.image(bulunan_logo, use_container_width=True)
        else:
            st.markdown("<h1 class='hero-title'>STELLARIS</h1>", unsafe_allow_html=True)
            st.markdown(f"<p class='hero-subtitle' style='color:#D4AF37; letter-spacing:5px; font-weight:bold; font-size:1.1rem;'>{'ULUSLARARASI ASTRO-TURİZM HOLDİNGİ' if lang == 'TR' else 'INTERNATIONAL ASTRO-TOURISM HOLDING'}</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("<h2>{}</h2>".format("Sınırların Ötesinde Bir Lüks" if lang == "TR" else "Luxury Beyond Borders"), unsafe_allow_html=True)
    home_desc = "Stellaris, sıradan tatil anlayışını geride bırakıp gözlerini evrenin derinliklerine çeviren seçkin bireyler için tasarlanmıştır. Işık kirliliğinden %100 arındırılmış dünyanın en karanlık noktalarında, kişiye özel cam fanus (Glass Dome) konaklamaları, Michelin yıldızlı gastronomi deneyimi ve özel jet transferleri ile bilim ve ultra-lüksü kusursuz bir uyumla harmanlıyoruz." if lang == "TR" else "Stellaris is designed for distinguished individuals who leave ordinary holidays behind and turn their eyes to the depths of the universe. In the darkest points of the world, 100% free from light pollution, we blend science and ultra-luxury flawlessly with personalized Glass Dome accommodations, Michelin-starred gastronomy, and private jet transfers."
    st.markdown(f"<p>{home_desc}</p>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown(f"<div class='stat-box'><div class='stat-number'>500+</div><div class='stat-label'>{'Bulutsuz Gece' if lang=='TR' else 'Clear Nights'}</div></div>", unsafe_allow_html=True)
    with c2: st.markdown(f"<div class='stat-box'><div class='stat-number'>$120M</div><div class='stat-label'>{'Yatırım Hacmi' if lang=='TR' else 'Investment Volume'}</div></div>", unsafe_allow_html=True)
    with c3: st.markdown(f"<div class='stat-box'><div class='stat-number'>3</div><div class='stat-label'>{'Özel Rezerv' if lang=='TR' else 'Exclusive Reserves'}</div></div>", unsafe_allow_html=True)
    with c4: st.markdown(f"<div class='stat-box'><div class='stat-number'>%100</div><div class='stat-label'>{'VIP Gizlilik' if lang=='TR' else 'VIP Privacy'}</div></div>", unsafe_allow_html=True)
    
    st.write("---")
    col_space1, col_image, col_space2 = st.columns([1, 10, 1])
    with col_image:
        st.markdown('<div class="hero-container"><img class="hero-image" src="https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=2000&auto=format&fit=crop"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------
# SAYFA 2: LOKASYONLARIMIZ
# ---------------------------------------------------------------------------------------
elif menu_secimi in ["LOKASYONLARIMIZ", "OUR LOCATIONS"]:
    st.markdown("<h2>{}</h2>".format("Hedef Ülkeler ve Küresel Pazar" if lang == "TR" else "Target Locations & Global Market"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Sıfır ışık kirliliğine sahip, uluslararası koruma altındaki stratejik karanlık gökyüzü rezervleri." if lang == "TR" else "Strategic dark sky reserves under international protection with zero light pollution."), unsafe_allow_html=True)
    st.write("---")
    
    locations = [
        {
            "img": "https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?q=80&w=800",
            "title_tr": "Atacama Çölü, Şili", "title_en": "Atacama Desert, Chile",
            "desc_tr": "Dünyanın en kurak çölü olan Atacama'da, 4.000 metre rakımda yer alan tesisimiz, yılda 300 günden fazla bulutsuz gece garantisi sunar. Ünlü ALMA gözlemevine komşudur.",
            "desc_en": "Located at 4,000m in the driest desert globally, our facility guarantees 300+ clear nights. It neighbors the famous ALMA observatory."
        },
        {
            "img": "https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=800",
            "title_tr": "Tekapo Gölü, Yeni Zelanda", "title_en": "Lake Tekapo, New Zealand",
            "desc_tr": "UNESCO tarafından 'Uluslararası Karanlık Gökyüzü Rezervi' ilan edilmiştir. Güney Haçı takımyıldızını ve Aurora Australis'i VIP olanaklarla deneyimleyin.",
            "desc_en": "Declared an 'International Dark Sky Reserve' by UNESCO. Experience the Southern Cross and Aurora Australis with VIP amenities."
        },
        {
            "img": "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=800&q=80",
            "title_tr": "NamibRand Doğa Koruma Alanı, Namibya", "title_en": "NamibRand Nature Reserve, Namibia",
            "desc_tr": "Afrika'nın en prestijli Gold Tier karanlık gökyüzü parkı. Çöl kumulları üzerinde vahşi yaşam safarisi ve olağanüstü derin uzay gözlemini bir arada sunar.",
            "desc_en": "Africa's most prestigious Gold Tier dark sky park. Offers a combination of wildlife safari over desert dunes and extraordinary deep space observation."
        }
    ]

    cols = st.columns(3)
    for idx, loc in enumerate(locations):
        with cols[idx]:
            title = loc["title_tr"] if lang == "TR" else loc["title_en"]
            desc = loc["desc_tr"] if lang == "TR" else loc["desc_en"]
            st.markdown(f"""
            <div class="service-card">
                <img class="service-img" src="{loc['img']}">
                <div class="service-content">
                    <h3 class="service-title" style="font-size:1.4rem;">{title}</h3>
                    <p class="service-desc" style="font-size:0.95rem;">{desc}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------
# SAYFA 3: CANLI GÖZLEMEVİ
# ---------------------------------------------------------------------------------------
elif menu_secimi in ["CANLI GÖZLEMEVİ", "LIVE OBSERVATORY"]:
    st.markdown("<h2>{}</h2>".format("Stellaris Kesintisiz Uydu Ağı" if lang == "TR" else "Stellaris Live Satellite Network"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Tüm kanallar doğrudan NASA ve NOAA uydularından alınan, askeri sınıf ham veri akışlarıdır." if lang == "TR" else "All channels are military-grade raw data streams pulled directly from NASA and NOAA satellites."), unsafe_allow_html=True)
    st.write("---")
    
    t_labels = ["🌍 GOES-16", "🌍 HIMAWARI", "☀️ SDO 304", "☀️ SDO 171", "🛰️ SOHO C3", "📍 ISS RADAR", "🔭 TELESKOP SİM." if lang == "TR" else "🔭 TELESCOPE SIM"]
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(t_labels)
    
    with tab1: 
        st.markdown(f"<p style='color:#D4AF37;'><b>{'GOES-16 Uydusu (Kuzey ve Güney Amerika)' if lang=='TR' else 'GOES-16 Satellite (Americas)'}</b></p>", unsafe_allow_html=True)
        components.html(auto_refresh_image("goes16_img", "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/latest.jpg", 60000, "LIVE: GOES-16", "600px"), height=650)
    with tab2: 
        st.markdown(f"<p style='color:#D4AF37;'><b>{'Himawari-9 Uydusu (Asya ve Pasifik)' if lang=='TR' else 'Himawari-9 Satellite (Asia & Pacific)'}</b></p>", unsafe_allow_html=True)
        components.html(auto_refresh_image("himawari_img", "https://cdn.star.nesdis.noaa.gov/AHI/FD/GEOCOLOR/latest.jpg", 60000, "LIVE: HIMAWARI-9", "600px"), height=650)
    with tab3: 
        st.markdown(f"<p style='color:#D4AF37;'><b>{'Solar Dynamics Observatory - 304 Ångström (Güneş Plazması)' if lang=='TR' else 'SDO - 304 Ångström (Solar Plasma)'}</b></p>", unsafe_allow_html=True)
        components.html(auto_refresh_image("sdo304_img", "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0304.jpg", 60000, "LIVE: SDO 304", "600px"), height=650)
    with tab4: 
        st.markdown(f"<p style='color:#D4AF37;'><b>{'Solar Dynamics Observatory - 171 Ångström (Manyetik Döngüler)' if lang=='TR' else 'SDO - 171 Ångström (Magnetic Loops)'}</b></p>", unsafe_allow_html=True)
        components.html(auto_refresh_image("sdo171_img", "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0171.jpg", 60000, "LIVE: SDO 171", "600px"), height=650)
    with tab5: 
        st.markdown(f"<p style='color:#D4AF37;'><b>{'SOHO LASCO C3 (Güneş Fırtınası Radarı)' if lang=='TR' else 'SOHO LASCO C3 (Coronagraph)'}</b></p>", unsafe_allow_html=True)
        components.html(auto_refresh_image("sohoc3_img", "https://soho.nascom.nasa.gov/data/realtime/c3/1024/latest.jpg", 60000, "LIVE: SOHO C3", "600px"), height=650)
    with tab6: 
        st.markdown(f"<p style='color:#D4AF37;'><b>{'Uluslararası Uzay İstasyonu (ISS) Canlı Takip' if lang=='TR' else 'International Space Station (ISS) Live Tracker'}</b></p>", unsafe_allow_html=True)
        st.markdown("""<div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; height: 550px; background: rgba(5,16,36,0.5);"><iframe src="https://isstracker.spaceflight.esa.int/" width="100%" height="100%" frameborder="0" style="pointer-events: none;"></iframe></div>""", unsafe_allow_html=True)
    with tab7:
        st.markdown(f"<p style='color:#D4AF37;'><b>{'Teleskop Kontrol Arayüzü Simülasyonu' if lang=='TR' else 'Telescope Control Interface Simulation'}</b></p>", unsafe_allow_html=True)
        col_view, col_controls = st.columns([5, 2])
        with col_controls:
            st.markdown(f"<div class='info-panel' style='padding:20px; height:100%;'>", unsafe_allow_html=True)
            zoom_level = st.slider("Zoom / Yakınlaştırma" if lang=="TR" else "Zoom Level", 1.0, 4.0, 1.0, 0.1)
            filter_options = ["Görünür", "H-Alpha (Kızılötesi)", "O-III (Mavi-Yeşil)"] if lang == "TR" else ["Visible", "H-Alpha (Infrared)", "O-III (Blue-Green)"]
            filter_type = st.radio("Optik Filtre / Optical Filter" if lang=="TR" else "Optical Filter", filter_options)
            css_filter = "sepia(100%) hue-rotate(-50deg) saturate(300%)" if "H-Alpha" in filter_type else "sepia(100%) hue-rotate(130deg) saturate(200%)" if "O-III" in filter_type else "none"
            st.markdown("</div>", unsafe_allow_html=True)
        with col_view:
            st.markdown(f"""
            <div style="width: 100%; height: 500px; border: 1px solid rgba(184, 134, 11, 0.5); border-radius: 12px; overflow: hidden; background: #000; position: relative; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                <div style="position: absolute; top: 20px; left: 20px; color: #ff3333; font-family: monospace; font-weight: bold; z-index: 10; font-size:14px; background:rgba(0,0,0,0.6); padding:5px 10px; border-radius:4px; border:1px solid #ff3333;">
                    <span style="animation: blink 1s infinite;">●</span> SENSOR ACTIVE
                </div>
                <div style="position: absolute; bottom: 20px; right: 20px; color: #D4AF37; font-family: monospace; z-index: 10; font-size:12px; background:rgba(0,0,0,0.6); padding:5px 10px; border-radius:4px;">
                    RA: 05h 35m 17s | DEC: -05° 23′ 28″
                </div>
                <img src="https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=1600" style="width: 100%; height: 100%; object-fit: cover; transform: scale({zoom_level}); filter: {css_filter}; transition: all 0.5s ease;">
            </div>
            """, unsafe_allow_html=True)

# =======================================================================================
# SAYFA 4: 3D SİMÜLASYONLAR
# =======================================================================================
elif menu_secimi in ["3D SİMÜLASYONLAR", "3D SIMULATIONS"]:
    st.markdown("<h2>{}</h2>".format("İnteraktif 3D Uzay Simülatörleri" if lang == "TR" else "Interactive 3D Space Simulators"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Tam ekran moduna geçerek uzayın derinliklerinde serbestçe gezinebilirsiniz." if lang == "TR" else "Enter full-screen mode to freely navigate the depths of space."), unsafe_allow_html=True)
    st.write("---")
    
    t_labels = ["🌍 3D DÜNYA", "🪐 GÜNEŞ SİSTEMİ", "☄️ ASTEROİT AVI", "👽 ÖTEGEZEGENLER", "🌌 CANLI GÖKYÜZÜ"] if lang == "TR" else ["🌍 3D EARTH", "🪐 SOLAR SYSTEM", "☄️ ASTEROIDS", "👽 EXOPLANETS", "🌌 LIVE SKY"]
    tab1, tab2, tab3, tab4, tab5 = st.tabs(t_labels)
    
    style_str = "border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.6); background: rgba(5,16,36,0.5);"
    
    with tab1: st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/earth/#/" width="100%" height="700" frameborder="0" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
    with tab2: st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/solar-system/#/home?embed=true" width="100%" height="700" frameborder="0" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
    with tab3: st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/asteroids/#/?embed=true" width="100%" height="700" frameborder="0" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
    with tab4: st.markdown(f"""<div style="{style_str}"><iframe src="https://eyes.nasa.gov/apps/exo/#/?embed=true" width="100%" height="700" frameborder="0" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
    with tab5:
        loc_options = ["Atacama Çölü, Şili", "Tekapo Gölü, Yeni Zelanda", "NamibRand, Namibya"] if lang == "TR" else ["Atacama Desert, Chile", "Lake Tekapo, New Zealand", "NamibRand, Namibia"]
        loc_choice = st.selectbox("Gözlem Noktası Seçimi / Select Observation Point:" if lang=="TR" else "Select Observation Point:", loc_options)
        if "Atacama" in loc_choice: lat, lon = -23.0, -67.7
        elif "Tekapo" in loc_choice: lat, lon = -44.0, 170.4
        else: lat, lon = -25.2, 15.9 
        
        sky_url = f"https://virtualsky.lco.global/embed/index.html?longitude={lon}&latitude={lat}&projection=stereo&constellations=true&constellationlabels=true&meteorshowers=true&showstarlabels=true&live=true&az=180&color=dark"
        st.markdown(f"""<div style="{style_str}"><iframe src="{sky_url}" width="100%" height="700" frameborder="0" allowfullscreen="true" scrolling="no"></iframe></div>""", unsafe_allow_html=True)

# =======================================================================================
# SAYFA 5: KARA DELİK FİZİK MOTORU 
# =======================================================================================
elif menu_secimi in ["KARA DELİK SİM.", "BLACK HOLE SIM."]:
    st.markdown("<h2>{}</h2>".format("Kütleçekim ve Kara Delik Simülatörü" if lang == "TR" else "Gravity & Black Hole Simulator"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Aşağıdaki parametrelerle oynayarak uzay-zamanın nasıl büküldüğünü ve olay ufkunu (Event Horizon) analiz edin." if lang == "TR" else "Analyze how space-time bends and the Event Horizon behaves by tweaking the parameters below."), unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown(f"""
        <div class="info-panel" style="padding: 20px; text-align: left; height:100%;">
            <h4 style="color:#D4AF37; text-align:left !important; font-size:1.2rem;">{'Teorik Altyapı' if lang=='TR' else 'Theoretical Basis'}</h4>
            <p style="text-align:left !important; font-size:0.9rem;">{'Kara delikler, kütlesi o kadar büyük ve yoğun olan kozmik cisimlerdir ki, ışık dahil hiçbir şey kütleçekiminden (Gravity) kaçamaz. Etrafındaki dönen yıldız tozu halkasına <b>Yığılma Diski (Accretion Disk)</b> denir.' if lang=='TR' else 'Black holes are cosmic bodies with mass so large and dense that nothing, not even light, can escape their gravity. The rotating ring of stardust around them is called the <b>Accretion Disk</b>.'}</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        bh_html = f"""
        <div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; overflow: hidden; background: rgba(5,16,36,0.6); backdrop-filter: blur(10px); padding: 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.5);">
            <div style="color: #D4AF37; font-family: 'Cinzel', serif; font-size:1.5rem; margin-bottom: 20px; text-align: center; letter-spacing: 2px;">STELLARIS GRAVITY ENGINE</div>
            <div style="display: flex; justify-content: center; gap: 40px; margin-bottom: 30px; flex-wrap: wrap;">
                <label style="color: #E0E0E0; font-family: 'Montserrat', sans-serif; font-weight:bold;">{"Tekillik Kütlesi" if lang=="TR" else "Singularity Mass"}: <br><input type="range" id="massSlider" min="50" max="350" value="180" style="accent-color: #B8860B; width:200px; margin-top:10px;"></label>
                <label style="color: #E0E0E0; font-family: 'Montserrat', sans-serif; font-weight:bold;">{"Disk Hızı" if lang=="TR" else "Disk Velocity"}: <br><input type="range" id="speedSlider" min="1" max="15" value="6" style="accent-color: #B8860B; width:200px; margin-top:10px;"></label>
            </div>
            <div style="max-width:100%; overflow-x:auto; text-align:center;">
                <canvas id="bhCanvas" width="800" height="450" style="background: radial-gradient(circle at center, #0a1930 0%, #000 100%); border-radius: 8px; border: 1px solid rgba(184,134,11,0.2); box-shadow: 0 0 30px rgba(0,0,0,0.8) inset;"></canvas>
            </div>
        </div>
        <script>
            const canvas = document.getElementById('bhCanvas'); const ctx = canvas.getContext('2d');
            const massSlider = document.getElementById('massSlider'); const speedSlider = document.getElementById('speedSlider');
            let particles = [];
            for(let i=0; i<450; i++) {{ 
                particles.push({{
                    x: Math.random() * canvas.width, 
                    y: Math.random() * canvas.height, 
                    vx: (Math.random() - 0.5) * 4, 
                    vy: (Math.random() - 0.5) * 4, 
                    color: `hsl(${{Math.random() * 60 + 10}}, 100%, 70%)`,
                    size: Math.random() * 2 + 0.5
                }}); 
            }}
            function animate() {{
                ctx.fillStyle = 'rgba(0, 0, 0, 0.2)'; ctx.fillRect(0, 0, canvas.width, canvas.height);
                const cx = canvas.width / 2; const cy = canvas.height / 2; 
                const mass = parseInt(massSlider.value); const speedMult = parseInt(speedSlider.value) / 5;
                
                ctx.beginPath(); ctx.arc(cx, cy, mass / 3, 0, Math.PI * 2); 
                ctx.fillStyle = '#000'; ctx.fill(); 
                ctx.lineWidth = 3; ctx.strokeStyle = 'rgba(212, 175, 55, 0.9)'; ctx.stroke(); 
                ctx.shadowBlur = Math.random() * 20 + 40; ctx.shadowColor = '#D4AF37';
                ctx.shadowBlur = 0; 
                
                particles.forEach(p => {{
                    const dx = cx - p.x; const dy = cy - p.y; const dist = Math.sqrt(dx*dx + dy*dy);
                    const force = (mass * 7) / (dist * dist); 
                    p.vx += (dx / dist) * force; p.vy += (dy / dist) * force;
                    p.x += p.vx * speedMult; p.y += p.vy * speedMult;
                    
                    if(dist < mass / 3) {{ 
                        p.x = Math.random() * canvas.width; p.y = (Math.random() > 0.5 ? 0 : canvas.height); 
                        p.vx = (Math.random() - 0.5) * 4; p.vy = (Math.random() - 0.5) * 4; 
                    }}
                    ctx.beginPath(); ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2); ctx.fillStyle = p.color; ctx.fill();
                }});
                requestAnimationFrame(animate);
            }}
            animate();
        </script>
        """
        components.html(bh_html, height=720)

# =======================================================================================
# SAYFA 6: VİDEOLAR GALERİSİ
# =======================================================================================
elif menu_secimi in ["VİDEOLAR GALERİSİ", "VIDEO GALLERY"]:
    st.markdown("<h2>{}</h2>".format("Stellaris Uzay ve Bilim Sineması" if lang == "TR" else "Stellaris Space Cinema"), unsafe_allow_html=True); st.write("---")
    v_col1, v_col2 = st.columns(2)
    with v_col1: 
        st.markdown(f"<h3>{'James Webb Uzay Teleskobu' if lang=='TR' else 'James Webb Space Telescope'}</h3>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=uD4izuDMUQA")
        st.markdown(f"<br><h3>{'SpaceX Starship Fırlatması' if lang=='TR' else 'SpaceX Starship Launch'}</h3>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=-1wcilQ58hI")
    with v_col2: 
        st.markdown(f"<h3>{'Mars Yüzeyi 4K Simülasyon' if lang=='TR' else 'Mars Surface in 4K'}</h3>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=ZEyAs3NWH4A")
        st.markdown(f"<br><h3>{'ISS Üzerinden Dünya (4K)' if lang=='TR' else 'Earth from ISS (4K)'}</h3>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=Un5SEJ8MyPc")

# =======================================================================================
# SAYFA 7: KOZMİK TAKVİM 
# =======================================================================================
elif menu_secimi in ["KOZMİK TAKVİM", "COSMIC CALENDAR"]:
    st.markdown("<h2>{}</h2>".format("Kozmik Takvim & Nadir Fenomenler" if lang == "TR" else "Cosmic Calendar & Phenomena"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Gözlem turlarınızı gökyüzünün en aktif olduğu dönemlere göre planlayın." if lang == "TR" else "Plan your observation tours according to the most active periods of the sky."), unsafe_allow_html=True)
    st.write("---")
    
    events = ["Perseid Göktaşı Yağmuru", "Satürn Karşı Konumu", "Tam Güneş Tutulması"] if lang == "TR" else ["Perseid Meteor Shower", "Saturn Opposition", "Total Solar Eclipse"]
    selected_event = st.selectbox("Astronomik Olay Seçiniz / Select Astronomical Event:" if lang=="TR" else "Select Astronomical Event:", events)
    
    col_info, col_metrics = st.columns([2, 1])
    with col_info:
        if "Perseid" in selected_event:
            img_url = "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?q=80&w=800"
            desc = "Yılın en görkemli meteor yağmuru. Saatte 100'e yakın kayan yıldız izleme fırsatı." if lang == "TR" else "The most spectacular meteor shower of the year. Opportunity to watch nearly 100 shooting stars per hour."
        elif "Sat" in selected_event:
            img_url = "https://images.unsplash.com/photo-1614728263610-18fb23c7b505?auto=format&fit=crop&w=800"
            desc = "Satürn'ün Dünya'ya en yakın ve en parlak olduğu dönem. Halkalar kusursuz görünür." if lang == "TR" else "The period when Saturn is closest and brightest to Earth. The rings are perfectly visible."
        else:
            img_url = "https://images.unsplash.com/photo-1539321908154-049275965646?q=80&w=800"
            desc = "Ay'ın Güneş'i tamamen örtmesiyle oluşan muazzam taçküre (korona) parlaması." if lang == "TR" else "The magnificent coronal flare formed by the Moon completely covering the Sun."
            
        st.markdown(f"""
        <div style="border: 1px solid rgba(184,134,11,0.3); border-radius: 12px; padding: 20px; background: rgba(5,16,36,0.6); backdrop-filter: blur(10px); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            <img src="{img_url}" style="width: 100%; height: 380px; object-fit: cover; border-radius: 8px; margin-bottom:15px;">
            <p style="text-align:left !important; font-size:1.05rem; color:#E0E0E0;"><b>{'Bilgi' if lang=='TR' else 'Info'}:</b> {desc}</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_metrics: 
        st.markdown(f"<div class='info-panel' style='padding:30px; height:100%;'>", unsafe_allow_html=True)
        st.metric("Görüş / Visibility" if lang=="TR" else "Visibility", "Ultra HD", "99%")
        st.write("---")
        st.metric("Aktivite Seviyesi / Activity Level" if lang=="TR" else "Activity Level", "Yüksek / High" if lang=="TR" else "High", "Max")
        st.progress(60 if "Perseid" in selected_event else 85 if "Sat" in selected_event else 98)
        st.write("")
        if st.button("Hemen Yer Ayırt" if lang=="TR" else "Book Now", use_container_width=True): 
            st.toast("VIP Temsilcilerimiz Sizinle İletişime Geçecektir." if lang=="TR" else "Our VIP Reps Will Contact You.", icon="🎫")
        st.markdown("</div>", unsafe_allow_html=True)

# =======================================================================================
# SAYFA 8: UZAY HAVADURUMU 
# =======================================================================================
elif menu_secimi in ["UZAY HAVADURUMU", "SPACE WEATHER"]:
    st.markdown("<h2>{}</h2>".format("Jeomanyetik Fırtına & Uzay Hava Durumu" if lang == "TR" else "Geomagnetic Storm & Space Weather"), unsafe_allow_html=True)
    warn_text = "Jeomanyetik fırtınalar (Kp Index) muazzam kutup ışıkları yaratsa da, hassas astrofotografi sensörleri için parazit oluşturabilir. Profesyonel çekimlerinizi bu endekse göre planlayın." if lang == "TR" else "While geomagnetic storms create magnificent auroras, they can cause noise for sensitive astrophotography sensors. Plan your professional shoots according to this index."
    st.markdown(f"<p>{warn_text}</p>", unsafe_allow_html=True)
    st.write("---")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Kp Index", "6.33", "+1.2 (Storm)" if lang=="EN" else "+1.2 (Fırtına)")
    c2.metric("Solar Wind" if lang=="EN" else "Güneş Rüzgarı", "540 km/s", "+45")
    c3.metric("Aurora Prob." if lang=="EN" else "Aurora Olasılığı", "%85", "+%15")
    c4.metric("Solar Flare" if lang=="EN" else "Parlama Sınıfı", "M1.2", "Moderate" if lang=="EN" else "Orta")
    st.write("---")
    
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.markdown("<h3>{}</h3>".format("5 Günlük Kp İndeksi Tahmini" if lang == "TR" else "5-Day Kp Index Forecast"), unsafe_allow_html=True)
        days = ["Pzt", "Sal", "Çar", "Per", "Cum"] if lang == "TR" else ["Mon", "Tue", "Wed", "Thu", "Fri"]
        col_name = "Fırtına Gücü (Kp)" if lang == "TR" else "Storm Intensity (Kp)"
        df_kp = pd.DataFrame({col_name: [2.3, 4.0, 6.3, 5.1, 3.2]}, index=days)
        st.bar_chart(df_kp, color="#D4AF37")
        
    with col_chart2:
        st.markdown("<h3>{}</h3>".format("Güneş Rüzgarı Hızı (km/s)" if lang == "TR" else "Solar Wind Speed (km/s)"), unsafe_allow_html=True)
        df_wind = pd.DataFrame({"Hız / Speed" if lang=="TR" else "Speed (km/s)": [350, 420, 540, 490, 400]}, index=days)
        st.line_chart(df_wind, color="#B8860B")

# =======================================================================================
# SAYFA 9: IŞIK KİRLİLİĞİ 
# =======================================================================================
elif menu_secimi in ["IŞIK KİRLİLİĞİ", "LIGHT POLLUTION"]:
    st.markdown("<h2>{}</h2>".format("Bortle Scale: Işık Kirliliği Simülatörü" if lang == "TR" else "Light Pollution Simulator"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Işık kirliliğinin derin uzay gözlemine olan yıkıcı etkisini kaydırıcı (slider) ile test edin." if lang == "TR" else "Test the devastating effect of light pollution on deep space observation using the slider."), unsafe_allow_html=True)
    st.write("---")
    
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl: 
        st.markdown(f"<div class='info-panel' style='padding:30px; height:100%;'>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:left !important;'><b>Bortle 1:</b> {'Kusursuz Karanlık (Stellaris Tesisleri)' if lang=='TR' else 'Perfect Darkness (Stellaris Facilities)'} <br><br><b>Bortle 9:</b> {'Şehir Merkezi (Yıldızlar Görünmez)' if lang=='TR' else 'City Center (Stars Invisible)'}</p>", unsafe_allow_html=True)
        bortle_val = st.slider("Gökyüzü Kalitesi / Sky Quality" if lang=="TR" else "Sky Quality", 1, 9, 1, step=1)
        st.markdown("</div>", unsafe_allow_html=True)
    
    glow_opacity = (bortle_val - 1) / 8.0  
    blur_amount = (bortle_val - 1) * 0.6
    brightness = 1.0 - (glow_opacity * 0.4)
    
    with col_view: st.markdown(f"""
        <div style="position: relative; width: 100%; height: 450px; border: 1px solid rgba(184,134,11,0.5); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.8);">
            <img src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1600" style="width: 100%; height: 100%; object-fit: cover; filter: brightness({brightness}) blur({blur_amount}px); transition: all 0.3s ease;">
            <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(255, 120, 0, {glow_opacity}), transparent); pointer-events: none; transition: all 0.3s ease;"></div>
            <div style="position: absolute; top: 20px; left: 20px; color: #FFF; font-family: monospace; background:rgba(0,0,0,0.7); padding:5px 15px; border-radius:4px; border:1px solid #B8860B;">
                BORTLE CLASS: {bortle_val}
            </div>
        </div>
        """, unsafe_allow_html=True)

# =======================================================================================
# SAYFA 10: EKİPMAN KATALOĞU 
# =======================================================================================
elif menu_secimi in ["EKİPMAN KATALOĞU", "EQUIPMENT CATALOG", "EKİPMANLAR", "EQUIPMENT"]:
    st.markdown("<h2>{}</h2>".format("VIP Gözlem Envanteri" if lang == "TR" else "VIP Observation Inventory"), unsafe_allow_html=True)
    desc_text = "Tesislerimizde misafirlerimizin kullanımına sunulan askeri sınıf ve profesyonel araştırma düzeyindeki optik, takip ve görüntüleme ekipmanlarının teknik özellikleridir." if lang == "TR" else "Technical specifications of the military-grade and professional research-level optical, tracking, and imaging equipment available to our guests at our facilities."
    st.markdown(f"<p>{desc_text}</p>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    type_str = "Tasarım Türü" if lang == "TR" else "Design Type"
    aper_str = "Diyafram Çapı" if lang == "TR" else "Aperture Diameter"
    foc_str = "Odak Uzunluğu" if lang == "TR" else "Focal Length"
    use_str = "Kapasite & Özellik" if lang == "TR" else "Capacity & Feature"

    with col1:
        st.markdown(f"""
        <div class="service-card" style="padding:30px; text-align:left; height:auto; margin-bottom:25px;">
            <h3 style="color:#D4AF37; margin-bottom:15px; text-align:left !important; border-bottom: 1px solid rgba(184,134,11,0.3); padding-bottom:10px;">🔭 Celestron CPC 1100 GPS (XLT)</h3>
            <p style="text-align:left !important; color:#E0E0E0; line-height:2;">
            <b style="color:#B8860B;">{type_str}:</b> Schmidt-Cassegrain<br>
            <b style="color:#B8860B;">{aper_str}:</b> 280mm (11 inç)<br>
            <b style="color:#B8860B;">{foc_str}:</b> 2800mm (f/10)<br>
            <b style="color:#B8860B;">{use_str}:</b> {"Tam otomatik 16 kanallı GPS hizalama sistemi ve StarBright XLT kaplaması ile %97 maksimum ışık geçirgenliği sağlar. Derin uzay (Deep-Sky) galaksi analizleri içindir." if lang=='TR' else "Provides 97% maximum light transmission with fully automated 16-channel GPS alignment and StarBright XLT coating."}</p>
        </div>
        <div class="service-card" style="padding:30px; text-align:left; height:auto; margin-bottom:25px;">
            <h3 style="color:#D4AF37; margin-bottom:15px; text-align:left !important; border-bottom: 1px solid rgba(184,134,11,0.3); padding-bottom:10px;">☀️ Lunt LS100MT Solar Observatory</h3>
            <p style="text-align:left !important; color:#E0E0E0; line-height:2;">
            <b style="color:#B8860B;">{type_str}:</b> Dedicated H-alpha Solar<br>
            <b style="color:#B8860B;">{aper_str}:</b> 100mm (Double Stacked)<br>
            <b style="color:#B8860B;">{use_str}:</b> {"Güneş rüzgarlarını, C-sınıfı patlamaları ve taçküreyi (corona) gerçek zamanlı ve %100 güvenli izlemek için endüstri standardı filtreleme mekanizması kullanır." if lang=='TR' else "Utilizes double-stacked industry standard filtering mechanisms to view solar winds, C-class flares, and the corona in real-time."}</p>
        </div>
        <div class="service-card" style="padding:30px; text-align:left; height:auto; margin-bottom:25px;">
            <h3 style="color:#D4AF37; margin-bottom:15px; text-align:left !important; border-bottom: 1px solid rgba(184,134,11,0.3); padding-bottom:10px;">🔭 Takahashi FSQ-130ED</h3>
            <p style="text-align:left !important; color:#E0E0E0; line-height:2;">
            <b style="color:#B8860B;">{type_str}:</b> Flat-Field Super Quadruplet Refractor<br>
            <b style="color:#B8860B;">{aper_str}:</b> 130mm<br>
            <b style="color:#B8860B;">{use_str}:</b> {"Geniş alan astrofotografi için renk sapmalarını (chromatic aberration) tamamen yok eden Japon yapımı, en üst düzey optik mühendislik harikası." if lang=='TR' else "A Japanese marvel of optical engineering that completely eliminates chromatic aberration for wide-field astrophotography."}</p>
        </div>
        <div class="service-card" style="padding:30px; text-align:left; height:auto;">
            <h3 style="color:#D4AF37; margin-bottom:15px; text-align:left !important; border-bottom: 1px solid rgba(184,134,11,0.3); padding-bottom:10px;">👁️ Tele Vue Ethos Eyepiece Set</h3>
            <p style="text-align:left !important; color:#E0E0E0; line-height:2;">
            <b style="color:#B8860B;">{"Görüş Alanı" if lang=="TR" else "FOV"}:</b> 100° (Hyper-Wide)<br>
            <b style="color:#B8860B;">{"Odak Aralıkları" if lang=="TR" else "Focal Lengths"}:</b> 21mm, 13mm, 8mm, 6mm<br>
            <b style="color:#B8860B;">{use_str}:</b> {"Teleskopta adeta uzay yürüyüşü (spacewalk) hissi yaratan dünyanın en geniş açılı mercek seti." if lang=='TR' else "The widest angle eyepiece set in the world, creating a &#39;spacewalk&#39; feeling when looking through the scope."}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="service-card" style="padding:30px; text-align:left; height:auto; margin-bottom:25px;">
            <h3 style="color:#D4AF37; margin-bottom:15px; text-align:left !important; border-bottom: 1px solid rgba(184,134,11,0.3); padding-bottom:10px;">🔭 Planewave CDK20 Observatory</h3>
            <p style="text-align:left !important; color:#E0E0E0; line-height:2;">
            <b style="color:#B8860B;">{type_str}:</b> Corrected Dall-Kirkham (CDK)<br>
            <b style="color:#B8860B;">{aper_str}:</b> 508mm (20 inç)<br>
            <b style="color:#B8860B;">{use_str}:</b> {"Üniversite araştırmaları için kullanılan, mükemmel düz bir odak düzlemi sunan devasa karbon fiber gövdeli profesyonel sistem." if lang=='TR' else "Massive carbon-fiber professional system offering a perfectly flat focal plane, used for university-level research."}</p>
        </div>
        <div class="service-card" style="padding:30px; text-align:left; height:auto; margin-bottom:25px;">
            <h3 style="color:#D4AF37; margin-bottom:15px; text-align:left !important; border-bottom: 1px solid rgba(184,134,11,0.3); padding-bottom:10px;">📸 FLI ProLine 16803 (Kamera)</h3>
            <p style="text-align:left !important; color:#E0E0E0; line-height:2;">
            <b style="color:#B8860B;">{"Sensör Mimarisi" if lang=="TR" else "Sensor Arch"}:</b> KAF-16803 CCD (Monochrome)<br>
            <b style="color:#B8860B;">{"Çözünürlük" if lang=="TR" else "Resolution"}:</b> 16 Megapixels (9um pixel size)<br>
            <b style="color:#B8860B;">{use_str}:</b> {"Dünyanın en elit uzay fotoğrafçılarının tercih ettiği, bilimsel seviyede sıvı soğutmalı (-55°C) derin uzay kamerası." if lang=='TR' else "Scientific-grade liquid-cooled (-55°C) deep space camera preferred by the world&#39;s most elite space photographers."}</p>
        </div>
        <div class="service-card" style="padding:30px; text-align:left; height:auto; margin-bottom:25px;">
            <h3 style="color:#D4AF37; margin-bottom:15px; text-align:left !important; border-bottom: 1px solid rgba(184,134,11,0.3); padding-bottom:10px;">⚙️ Software Bisque Paramount ME II</h3>
            <p style="text-align:left !important; color:#E0E0E0; line-height:2;">
            <b style="color:#B8860B;">{type_str}:</b> Robotic Equatorial Mount<br>
            <b style="color:#B8860B;">{"Taşıma Kapasitesi" if lang=="TR" else "Payload"}:</b> 109 kg (240 lbs)<br>
            <b style="color:#B8860B;">{use_str}:</b> {"Devasa teleskop dizilerini titreşimsiz ve Dünya&#39;nın dönüş hızıyla milimetrik düzeyde senkronize hareket ettiren endüstriyel taşıyıcı ayak." if lang=='TR' else "An industrial mount that moves massive telescope arrays smoothly and in millimeter synchronization with the Earth&#39;s rotation."}</p>
        </div>
        <div class="service-card" style="padding:30px; text-align:left; height:auto;">
            <h3 style="color:#D4AF37; margin-bottom:15px; text-align:left !important; border-bottom: 1px solid rgba(184,134,11,0.3); padding-bottom:10px;">🏢 Baader Planetarium 3.5m Dome</h3>
            <p style="text-align:left !important; color:#E0E0E0; line-height:2;">
            <b style="color:#B8860B;">{type_str}:</b> Fiberglass Observatory Dome<br>
            <b style="color:#B8860B;">{"Rotasyon" if lang=="TR" else "Rotation"}:</b> 360° Motorized<br>
            <b style="color:#B8860B;">{use_str}:</b> {"İklimlendirmeli, teleskop hareketiyle otonom senkronize olan rüzgar ve ısı kalkanlı profesyonel gözlem kubbesi." if lang=='TR' else "Air-conditioned professional observatory dome with wind and heat shield, autonomously synchronized with telescope movement."}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------
# SAYFA 11: ASTRO-FOTOĞRAF
# ---------------------------------------------------------------------------------------
elif menu_secimi in ["ASTRO-FOTOĞRAF", "ASTRO-PHOTO"]:
    st.markdown("<h2>{}</h2>".format("Astro-Fotoğrafçılık Simülatörü" if lang == "TR" else "Astro-Photography Simulator"), unsafe_allow_html=True); st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl: 
        st.markdown(f"<div class='info-panel' style='padding:20px; height:100%;'>", unsafe_allow_html=True)
        iso_val = st.slider("ISO Değeri / ISO Value", 100, 6400, 800, step=100)
        exp_val = st.slider("Pozlama Süresi / Exposure (s)", 1, 30, 10, step=1)
        st.markdown("</div>", unsafe_allow_html=True)
    with col_view: 
        brightness = 0.15 + (exp_val / 30.0) * 0.6 + (iso_val / 6400.0) * 0.5
        st.markdown(f"""<div style="border: 1px solid rgba(184,134,11,0.5); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.6);"><img src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200" style="width: 100%; filter: brightness({brightness}) contrast({1.0 + (iso_val/10000.0)}); transition:all 0.2s ease;"></div>""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------
# SAYFA 12: VIP REZERVASYON 
# ---------------------------------------------------------------------------------------
elif menu_secimi in ["VIP REZERVASYON", "VIP BOOKING"]:
    st.markdown("<h2>{}</h2>".format("Premium Rezervasyon & VIP Planlama" if lang == "TR" else "Premium Booking & VIP Planning"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("UHNWI (Ultra Yüksek Net Değere Sahip Bireyler) standartlarındaki tesislerimizde eşsiz bir deneyim yaşamak için seyahatinizi kişiselleştirin." if lang == "TR" else "Personalize your journey to experience unique facilities at UHNWI standards."), unsafe_allow_html=True)
    st.write("---")
    
    if lang == "TR":
        pkg_options = [
            "Tekapo Explorer (3 Gece, Villa & Özel Astronom) - $35,000",
            "Atacama Stratosphere (5 Gece, Glass Dome & ALMA VIP) - $85,000",
            "NamibRand Ultimate Expedition (7 Gece, Sıfır-G Uçuş & Safari) - $150,000"
        ]
    else:
        pkg_options = [
            "Tekapo Explorer (3 Nights, Villa & Private Astronomer) - $35,000",
            "Atacama Stratosphere (5 Nights, Glass Dome & ALMA VIP) - $85,000",
            "NamibRand Ultimate Expedition (7 Nights, Zero-G Flight & Safari) - $150,000"
        ]
    
    col_comp, col_center, col_space2 = st.columns([2, 5, 1])
    
    with col_comp:
        if lang == "TR":
            st.markdown("### Stellaris Değer Önerisi")
            st.markdown("""<div class="info-panel" style="padding:20px;">
            <b style="color:#D4AF37;">Standart Lüks Tatiller ($15K - $25K)</b><br>
            <span style="font-size:0.85rem; color:#E0E0E0;">- 5 Yıldızlı Otel (Işık Kirliliği)<br>- Standart Fine-Dining<br>- Ticari Uçuş (First Class)</span><br><br>
            <b style="color:#D4AF37;">Stellaris Deneyimi ($35K - $150K)</b><br>
            <span style="font-size:0.85rem; color:#E0E0E0;">- Özel Cam Fanus (Bortle 1 Gökyüzü)<br>- Planewave 20'' & Kişisel Astronom<br>- Michelin Yıldızlı Şef & Sınırsız Havyar<br>- Helikopter & Özel Jet Transferleri<br>- Sıfır Yerçekimi (Zero-G) Simülasyon Uçuşu</span>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("### Stellaris Value Proposition")
            st.markdown("""<div class="info-panel" style="padding:20px;">
            <b style="color:#D4AF37;">Standard Luxury Vacations ($15K - $25K)</b><br>
            <span style="font-size:0.85rem; color:#E0E0E0;">- 5 Star Hotel (Light Pollution)<br>- Standard Fine-Dining<br>- Commercial Flight (First Class)</span><br><br>
            <b style="color:#D4AF37;">The Stellaris Experience ($35K - $150K)</b><br>
            <span style="font-size:0.85rem; color:#E0E0E0;">- Private Glass Dome (Bortle 1 Sky)<br>- Planewave 20'' & Personal Astronomer<br>- Michelin Star Chef & Unlimited Caviar<br>- Helicopter & Private Jet Transfers<br>- Zero-Gravity Simulation Flight</span>
            </div>""", unsafe_allow_html=True)

    with col_center:
        st.markdown(f"<div class='info-panel' style='padding:40px;'>", unsafe_allow_html=True)
        
        deneyim_turu = st.radio("Ana Paket Seçimi / Select Main Package:" if lang == "TR" else "Select Main Package:", pkg_options)
        
        st.write("---")
        st.markdown(f"<p style='text-align:left !important; color:#D4AF37; font-size:1.2rem;'><b>{'Lüks Eklentiler / Luxury Add-ons:' if lang == 'TR' else 'Luxury Add-ons:'}</b></p>", unsafe_allow_html=True)
        
        ekstra1 = st.checkbox("Kişisel Astrofotografçı & Belgesel Ekibi / Personal Astrophotographer & Doc Team (+$12,500)" if lang == "TR" else "Personal Astrophotographer & Doc Team (+$12,500)")
        ekstra2 = st.checkbox("Özel Helikopter ile Havalimanı Transferi / Private Heli-Transfer (+$8,000)" if lang == "TR" else "Private Heli-Transfer (+$8,000)")
        ekstra3 = st.checkbox("Tam Zamanlı Michelin Yıldızlı Şef / Full-time Michelin Star Chef (+$15,000)" if lang == "TR" else "Full-time Michelin Star Chef (+$15,000)")
        
        st.write("---")
        col_form1, col_form2 = st.columns(2)
        with col_form1: secilen_tarih = st.date_input("Tahmini Geliş Tarihi / Estimated Date" if lang == "TR" else "Estimated Date", min_value=datetime.date.today())
        with col_form2: kisi_sayisi = st.slider("VIP Konuk Sayısı / VIP Guests" if lang == "TR" else "VIP Guests", 1, 6, 2)
        
        # Privacy Agreement Checkbox
        agree = st.checkbox("VIP Gizlilik ve Uçuş Şartlarını Kabul Ediyorum." if lang == "TR" else "I agree to the VIP Confidentiality & Flight Terms.")
        
        # Fiyat Hesaplama
        taban_fiyat = 35000 if "35" in deneyim_turu else 85000 if "85" in deneyim_turu else 150000
        ekstra_toplam = (12500 if ekstra1 else 0) + (8000 if ekstra2 else 0) + (15000 if ekstra3 else 0)
        toplam_fiyat = (taban_fiyat * kisi_sayisi) + ekstra_toplam
        
        st.markdown(f"<div class='price-tag' style='font-size:4rem;'>${(toplam_fiyat):,} <span style='font-size: 1.2rem; color: #C5A059;'>USD Toplam / Total</span></div>", unsafe_allow_html=True)
        
        if st.button("Ödeme ve Uçuş Ekranına Geç / Proceed to Payment & Flight" if lang == "TR" else "Proceed to Payment", use_container_width=True): 
            if agree:
                with st.spinner("Güvenli ağ üzerinden şifreli işlem yapılıyor..." if lang == "TR" else "Processing via secure network..."):
                    time.sleep(2)
                st.toast("VIP Temsilciniz jetinizi koordine ediyor..." if lang == "TR" else "Your VIP Rep is coordinating your jet...", icon="✈️")
                st.balloons()
            else:
                st.error("Lütfen VIP sözleşmeyi onaylayın." if lang == "TR" else "Please agree to the VIP terms.")
            
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------
# SAYFA 13: VİZYON & SÜRDÜRÜLEBİLİRLİK
# ---------------------------------------------------------------------------------------
elif menu_secimi in ["VİZYON & SÜRDÜRÜLEBİLİRLİK", "VISION & SUSTAINABILITY"]:
    st.markdown("<h2>{}</h2>".format("Kurumsal Vizyon & Gelecek Planlarımız" if lang == "TR" else "Corporate Vision & Future Plans"), unsafe_allow_html=True)
    st.write("---")
    
    t_vis, t_sus, t_exo = st.tabs([
        "🌟 Vizyon & Misyon" if lang == "TR" else "🌟 Vision & Mission", 
        "🍃 Sürdürülebilirlik" if lang == "TR" else "🍃 Sustainability", 
        "🚀 Uzay Biletlemesi (2040)" if lang == "TR" else "🚀 Space Ticketing (2040)"
    ])
    
    with t_vis:
        col_space1, col_center, col_space2 = st.columns([1, 8, 1])
        with col_center:
            mission_title = "Kurumsal Misyonumuz" if lang=="TR" else "Corporate Mission"
            mission_text = "Evrenin gizemlerini ve uzayın derinliklerini, akademik düzeyde bilimsel bir ciddiyet ve ultra-premium hizmet anlayışıyla misafirlerimize sunmak. Dünyanın ışık kirliliğinden %100 arındırılmış benzersiz lokasyonlarında, uzay keşfini modern, yüksek teknolojili ve ilham verici elit bir seyahat deneyimine dönüştürüyoruz." if lang=="TR" else "To present the mysteries of the universe to our guests with academic scientific rigor and an ultra-premium service approach. In unique locations 100% free from light pollution, we transform space exploration into a high-tech, modern, and inspiring elite travel experience."
            
            vision_title = "Gelecek Vizyonumuz" if lang=="TR" else "Our Vision"
            vision_text = "Astro-Turizm kavramını küresel finans ve teknoloji standartlarında yeniden tanımlayarak, insanlığın uzay yolculuğu vizyonuna ticari bir zemin hazırlamak. Amacımız sadece Dünya'dan yıldızları izletmek değil, 2040 yılına kadar ticari yıldızlararası seyahatler için ilham veren ve altyapı sağlayan küresel bir endüstri öncüsü olmaktır." if lang=="TR" else "To redefine Astro-Tourism at global finance and tech standards, preparing a commercial ground for humanity's space travel. Our goal is to be a global industry pioneer providing infrastructure for commercial interstellar travel by 2040."

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
            st.markdown('<div class="hero-container" style="height:45vh;"><img class="hero-image" src="https://images.unsplash.com/photo-1502481851512-e9e2529bfbf9?q=80&w=1200"></div>', unsafe_allow_html=True)
            with st.expander("Optik Çevre Koruma (Zero-Glow Protocol)" if lang == "TR" else "Optical Environment Protection"): 
                st.write("Tesislerimizde gökyüzü silüetini ve astronomik ölçümleri bozmamak adına yalnızca yere dönük, hareket sensörlü ve tam kırmızı bazlı (600nm dalga boyu) aydınlatmalar kullanılır. Tesislerimizin 50 km yarıçapında radyo sinyali ve drone uçuşu yasaktır." if lang == "TR" else "To preserve the sky silhouette, we only use downward-facing, motion-sensored, red-based (600nm) lighting. Radio signals and drone flights are banned within a 50 km radius of our reserves.")
            with st.expander("Sıfır Karbon ve Otonom Enerji" if lang == "TR" else "Zero Carbon & Autonomous Energy"): 
                st.write("Cam fanus (Glass Dome) konaklamalarımız %100 otonom güneş enerjisi ve Tesla Powerwall batarya üniteleriyle çalışır. VIP transferlerimizde yalnızca yüksek menzilli zırhlı elektrikli SUV'ler kullanılmaktadır." if lang == "TR" else "Our Glass Domes operate on 100% solar energy and Tesla Powerwall units. We strictly use armored electric SUVs for VIP transfers.")
            
    with t_exo:
        exo_intro = "Holdingimizin 2040 vizyonu, galaksinin derinliklerindeki yaşanabilir ötegezegenlere (Exoplanet) ilk ticari sivil uçuş biletlemelerini başlatmaktır. Projelendirilen rotalarımız için ön talep toplanmaktadır." if lang == "TR" else "Our holding's 2040 vision is to launch the first commercial civilian flight ticketing to habitable exoplanets in the depths of the galaxy. Pre-requests are being collected."
        st.markdown(f"<p style='margin-top:20px !important;'>{exo_intro}</p>", unsafe_allow_html=True)
        
        dist_str = "Dünyaya Uzaklık" if lang=="TR" else "Distance"
        stat_str = "Gezegen Sınıfı" if lang=="TR" else "Planet Class"
        tick_str = "PROJE BÜTÇESİ" if lang=="TR" else "PROJECT BUDGET"
        btn_str = "Yatırımcı Ön Talep Listesi" if lang=="TR" else "Investor Waitlist"
        succ_str = "VIP Bekleme Listesine Kaydedildi!" if lang=="TR" else "Saved to VIP Waitlist!"
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""<div class="planet-card" style="padding: 30px; text-align: center;"><h3 style="color: #D4AF37; margin-bottom: 20px;">TRAPPIST-1e</h3><img class="spinning-planet" src="https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=400" style="filter: hue-rotate(150deg) saturate(200%);"><p style="color: #E0E0E0; font-size: 0.95rem; text-align: left !important; line-height:1.8;"><b>{dist_str}:</b> 39 Işık Yılı<br><b>{stat_str}:</b> {"Karasal Okyanus Gezegeni" if lang=="TR" else "Terrestrial Ocean Planet"}</p><div style="color: #B8860B; font-weight: bold; margin-top: 15px;">{tick_str}: $4.5 Milyar</div></div>""", unsafe_allow_html=True)
            if st.button(btn_str, key="b1", use_container_width=True): 
                st.toast(succ_str, icon="🚀")
                st.snow()
        with c2:
            st.markdown(f"""<div class="planet-card" style="padding: 30px; text-align: center; border-color: #D4AF37 !important; box-shadow: 0 0 30px rgba(212,175,55,0.2) !important;"><h3 style="color: #D4AF37; margin-bottom: 20px;">Kepler-186f</h3><img class="spinning-planet" src="https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=400" style="filter: hue-rotate(240deg) saturate(150%);"><p style="color: #E0E0E0; font-size: 0.95rem; text-align: left !important; line-height:1.8;"><b>{dist_str}:</b> 582 Işık Yılı<br><b>{stat_str}:</b> {"Kızıl Yıldız / Dünya Benzeri" if lang=="TR" else "Red Dwarf / Earth-like"}</p><div style="color: #B8860B; font-weight: bold; margin-top: 15px;">{tick_str}: $8.2 Milyar</div></div>""", unsafe_allow_html=True)
            if st.button(btn_str, key="b2", use_container_width=True): 
                st.toast(succ_str, icon="🚀")
                st.snow()
        with c3:
            st.markdown(f"""<div class="planet-card" style="padding: 30px; text-align: center;"><h3 style="color: #D4AF37; margin-bottom: 20px;">Proxima b</h3><img class="spinning-planet" src="https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=400" style="filter: hue-rotate(60deg) saturate(80%);"><p style="color: #E0E0E0; font-size: 0.95rem; text-align: left !important; line-height:1.8;"><b>{dist_str}:</b> 4.2 Işık Yılı<br><b>{stat_str}:</b> {"Yüksek Radyasyonlu Kayaç" if lang=="TR" else "High-Rad Rocky Planet"}</p><div style="color: #B8860B; font-weight: bold; margin-top: 15px;">{tick_str}: $1.2 Milyar</div></div>""", unsafe_allow_html=True)
            if st.button(btn_str, key="b3", use_container_width=True): 
                st.toast(succ_str, icon="🚀")
                st.snow()

# ---------------------------------------------------------------------------------------
# SAYFA 15: DESTEK & SSS (YENİ KURUMSAL SAYFA)
# ---------------------------------------------------------------------------------------
elif menu_secimi in ["DESTEK & SSS", "SUPPORT & FAQ"]:
    st.markdown("<h2>{}</h2>".format("Destek Merkezi & İletişim" if lang == "TR" else "Support Center & Contact"), unsafe_allow_html=True)
    st.write("---")
    
    t_faq, t_contact = st.tabs(["❓ S.S.S. / FAQ", "📩 İletişim / Contact"])
    
    with t_faq:
        st.markdown("<h3>{}</h3>".format("Sıkça Sorulan Sorular" if lang == "TR" else "Frequently Asked Questions"), unsafe_allow_html=True)
        with st.expander("VIP Rezervasyon iptal politikası nedir?" if lang == "TR" else "What is the VIP Booking cancellation policy?"):
            st.write("Rezervasyonunuzu uçuştan 30 gün öncesine kadar ücretsiz iptal edebilirsiniz. Özel jet transferi içeren paketlerde jet tahsis bedeli kesilmektedir." if lang == "TR" else "You can cancel your booking free of charge up to 30 days before the flight. For packages including private jet transfers, the jet allocation fee is deducted.")
        with st.expander("Gözlem turları için önceden astronomi bilgisi gerekiyor mu?" if lang == "TR" else "Is prior astronomy knowledge required for observation tours?"):
            st.write("Hayır. Her turumuzda size özel tahsis edilmiş profesyonel bir astronom ve rehber eşlik etmektedir." if lang == "TR" else "No. A dedicated professional astronomer and guide will accompany you on every tour.")
        with st.expander("Konaklama alanlarında sağlık ve güvenlik önlemleri nelerdir?" if lang == "TR" else "What are the health and safety measures in the accommodation areas?"):
            st.write("Tüm tesislerimizde 7/24 tam donanımlı sağlık ekibi ve acil durum tahliye helikopteri hazır bekletilmektedir." if lang == "TR" else "A fully equipped medical team and emergency evacuation helicopter are on standby 24/7 at all our facilities.")
            
    with t_contact:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f"""
            <div class='info-panel' style='padding:30px;'>
                <h3 style='color:#D4AF37;'>{'Bize Ulaşın' if lang=='TR' else 'Contact Us'}</h3>
                <p style='text-align:left !important;'>
                <b>Email:</b> vip@stellaris-holding.com<br>
                <b>{'Telefon' if lang=='TR' else 'Phone'}:</b> +1 (800) 555-0199<br>
                <b>Merkez / HQ:</b> Geneva, Switzerland</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='info-panel' style='padding:30px;'>", unsafe_allow_html=True)
            c_name = st.text_input("İsim / Name")
            c_email = st.text_input("E-Mail")
            c_msg = st.text_area("Mesajınız / Your Message", height=100)
            if st.button("Gönder / Send", use_container_width=True):
                st.toast("Mesajınız VIP masamıza iletildi." if lang == "TR" else "Your message has been sent to our VIP desk.", icon="✅")
            st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------
# SAYFA 16: YASAL & ÇEREZLER (YENİ KURUMSAL SAYFA)
# ---------------------------------------------------------------------------------------
elif menu_secimi in ["YASAL & ÇEREZLER", "LEGAL & COOKIES"]:
    st.markdown("<h2>{}</h2>".format("Kurumsal Politikalar" if lang == "TR" else "Corporate Policies"), unsafe_allow_html=True)
    st.write("---")
    
    t_cookie, t_privacy, t_terms = st.tabs(["🍪 Çerez Politikası / Cookie Policy", "🔒 Gizlilik / Privacy", "⚖️ Şartlar / Terms"])
    
    with t_cookie:
        st.markdown(f"""
        <div class='info-panel' style='padding:40px; text-align:left;'>
            <h3 style='color:#D4AF37; margin-bottom:20px;'>{'Çerez Kullanımı' if lang=='TR' else 'Cookie Usage'}</h3>
            <p style='text-align:left !important;'>{'Stellaris Holding, dijital platformlarında ultra-premium kullanıcı deneyimi sunmak, tercihlerinizi hatırlamak ve güvenliğinizi sağlamak amacıyla zorunlu ve analitik çerezler kullanmaktadır. Gizliliğiniz bizim için en üst düzey bir önceliktir. Çerez verileriniz asla üçüncü şahıslara satılmaz.' if lang=='TR' else 'Stellaris Holding uses essential and analytical cookies on its digital platforms to provide an ultra-premium user experience, remember your preferences, and ensure your security. Your privacy is a top priority for us. Your cookie data is never sold to third parties.'}</p>
        </div>
        """, unsafe_allow_html=True)
        
    with t_privacy:
        st.markdown(f"""
        <div class='info-panel' style='padding:40px; text-align:left;'>
            <h3 style='color:#D4AF37; margin-bottom:20px;'>{'VIP Gizlilik Sözleşmesi' if lang=='TR' else 'VIP Privacy Policy'}</h3>
            <p style='text-align:left !important;'>{'UHNWI misafirlerimizin kimlikleri, seyahat planları ve finansal verileri askeri düzeyde (AES-256) şifreleme ile korunmaktadır. Uçuş ve konaklama bilgileriniz, kişisel izniniz olmadan herhangi bir basın veya medya kuruluşu ile paylaşılamaz.' if lang=='TR' else 'The identities, travel plans, and financial data of our UHNWI guests are protected with military-grade (AES-256) encryption. Your flight and accommodation information cannot be shared with any press or media organization without your personal consent.'}</p>
        </div>
        """, unsafe_allow_html=True)
        
    with t_terms:
        st.markdown(f"""
        <div class='info-panel' style='padding:40px; text-align:left;'>
            <h3 style='color:#D4AF37; margin-bottom:20px;'>{'Hizmet Şartları' if lang=='TR' else 'Terms of Service'}</h3>
            <p style='text-align:left !important;'>{'Stellaris platformunu kullanan tüm ziyaretçiler, uluslararası sivil havacılık ve uzay turizmi ön şartlarını kabul etmiş sayılır. Tesislerimize girişler ön güvenlik taramasına ve davet/onay esasına tabidir.' if lang=='TR' else 'All visitors using the Stellaris platform are deemed to have accepted the preconditions of international civil aviation and space tourism. Entry to our facilities is subject to pre-security screening and invitation/approval basis.'}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------
# SAYFA 17: YATIRIMCI PORTALI
# ---------------------------------------------------------------------------------------
elif menu_secimi in ["YATIRIMCI PORTALI", "INVESTOR PORTAL"]:
    st.markdown("<h2>{}</h2>".format("Stellaris Holding Yatırımcı Portalı" if lang == "TR" else "Stellaris Holding Investor Portal"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Sadece yetkili yönetim kurulu üyeleri ve hissedarlar içindir." if lang == "TR" else "Strictly for authorized board members and shareholders only."), unsafe_allow_html=True)
    st.write("---")
    
    if st.text_input("Yetkilendirme Şifresi / Authorization Key (stellaris2026):", type="password") == "stellaris2026": 
        st.success("Güvenli Bağlantı Kuruldu. / Secure Connection Established." if lang == "TR" else "Secure Connection Established.")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("2025 YTD Gelir (USD)" if lang=="TR" else "2025 YTD Revenue", "$24.5M", "+18.2% YoY")
        c2.metric("EBITDA Marjı" if lang=="TR" else "EBITDA Margin", "%42.8", "+3.5%")
        c3.metric("VIP Üye Sayısı (Kümülatif)" if lang=="TR" else "VIP Members (Cum.)", "1,240", "+120 Yeni/New")
        
        st.write("---")
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.markdown("<h3>{}</h3>".format("Bölgesel Büyüme Projeksiyonu (USD Bin)" if lang == "TR" else "Regional Growth Projection (USD Thousands)"), unsafe_allow_html=True)
            df_growth = pd.DataFrame({
                "Şili (Atacama)" if lang=="TR" else "Chile (Atacama)": [1000, 2500, 4800, 7500, 12000], 
                "Yeni Zelanda" if lang=="TR" else "New Zealand": [800, 1900, 3500, 6000, 9500],
                "Namibya (Yeni)" if lang=="TR" else "Namibia (New)": [0, 0, 0, 2500, 7800]
            }, index=["2022", "2023", "2024", "2025", "2026 (Tahmin/Est)"])
            st.area_chart(df_growth, color=["#B8860B", "#C5A059", "#ffffff"])
            
        with col_c2:
            st.markdown("<h3>{}</h3>".format("Tesis Doluluk Oranları (%)" if lang == "TR" else "Facility Occupancy Rates (%)"), unsafe_allow_html=True)
            df_occ = pd.DataFrame({
                "Atacama Glass Domes": [45, 60, 85, 92, 98],
                "Tekapo Observatory": [50, 70, 80, 88, 95]
            }, index=["Q1", "Q2", "Q3", "Q4", "Q1 '26"])
            st.line_chart(df_occ, color=["#FFD700", "#B8860B"])
            
        st.write("---")
        note_tr = "Gelecek yıl Afrika kıtasında, Namibya Çölü (NamibRand) bölgesinde inşasına başlanacak 3. faz VIP rezervasyon ve konaklama alanı ile küresel astro-turizm pazar payımızın %65 oranında artması öngörülmektedir. Elon Musk ve SpaceX yöneticileriyle yapılan ön görüşmeler, gelecekteki Mars simülasyon eğitimlerinin doğrudan tesislerimizde yapılması üzerine yoğunlaşmıştır."
        note_en = "With the 3rd phase VIP booking and accommodation area to be built in the Namib Desert (NamibRand) on the African continent next year, our global astro-tourism market share is projected to increase by 65%. Preliminary talks with Elon Musk and SpaceX executives have focused on conducting future Mars simulation trainings directly at our facilities."
        
        st.markdown(f"""
        <div class="info-panel" style='text-align:left !important; padding:30px;'>
            <h4 style="color:#D4AF37; margin-bottom:15px;">{'CEO Stratejik Notu:' if lang=='TR' else 'CEO Strategic Note:'}</h4>
            <p style="text-align:left !important; font-size:1.1rem; line-height:1.8;">
            {note_tr if lang == 'TR' else note_en}
            </p>
        </div>
        """, unsafe_allow_html=True)
