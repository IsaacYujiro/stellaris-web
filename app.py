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
# SİTE YAPILANDIRMASI VE AGRESİF LÜKS CSS
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

    .stButton { display: flex; justify-content: center; margin-top: 20px; }
    div.stButton > button:first-child { background-color: #030814 !important; color: #B8860B !important; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 1.1rem; padding: 15px 50px; border: 1px solid #B8860B !important; border-radius: 2px; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); letter-spacing: 2px; text-transform: uppercase; }
    div.stButton > button:first-child:hover { background-color: #B8860B !important; color: #051024 !important; transform: scale(1.05); box-shadow: 0 0 20px rgba(184, 134, 11, 0.4); }

    [data-baseweb="tab-list"] { justify-content: center; gap: 10px; flex-wrap: wrap; }
    [data-baseweb="tab"] { background-color: transparent !important; color: #C5A059 !important; font-family: 'Cinzel', serif; font-size: 0.9rem; padding: 5px 10px; }
    [aria-selected="true"] { color: #B8860B !important; border-bottom: 2px solid #B8860B !important; font-weight: bold; }
    .stProgress > div > div > div > div { background-color: #B8860B !important; }
    
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    
    /* Pasaport Kartı CSS */
    .boarding-pass { background: linear-gradient(135deg, #030814 0%, #0a1930 100%); border: 2px solid #B8860B; border-radius: 12px; padding: 30px; box-shadow: 0 10px 40px rgba(184, 134, 11, 0.3); text-align: left; position: relative; overflow: hidden; max-width: 800px; margin: 0 auto; display: flex; justify-content: space-between; }
    .pass-left { width: 70%; border-right: 2px dashed #B8860B; padding-right: 20px; }
    .pass-right { width: 25%; display: flex; flex-direction: column; align-items: center; justify-content: center; }
    .pass-title { color: #D4AF37; font-family: 'Cinzel', serif; font-size: 1.8rem; margin-bottom: 5px; text-align: left !important; }
    .pass-label { color: #888; font-size: 0.8rem; text-transform: uppercase; margin-bottom: 2px; text-align: left !important; }
    .pass-value { color: #fff; font-size: 1.2rem; font-weight: bold; margin-bottom: 15px; text-align: left !important; }
    .pass-barcode { margin-top: 20px; letter-spacing: 5px; font-family: monospace; color: #B8860B; font-size: 1.5rem; text-align: center !important; }
    .pass-logo { font-family: 'Cinzel', serif; color: #B8860B; font-size: 1.5rem; writing-mode: vertical-rl; text-orientation: mixed; transform: rotate(180deg); }
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
        "ANA SAYFA", "LOKASYONLARIMIZ", "CANLI GÖZLEMEVİ", "3D SİMÜLASYONLAR", "UZAY PASAPORTU",
        "VİDEOLAR GALERİSİ", "KOZMİK TAKVİM", "UZAY HAVADURUMU", "IŞIK KİRLİLİĞİ", "EKİPMANLAR", 
        "ASTRO-FOTOĞRAF", "REZERVASYON", "SÜRDÜRÜLEBİLİRLİK", "YATIRIMCI PORTALI"
    ]
    sistem_durumu = "Sistem: Çevrimiçi"
else:
    menu_secenekleri = [
        "HOME", "OUR LOCATIONS", "LIVE OBSERVATORY", "3D SIMULATIONS", "SPACE PASSPORT",
        "VIDEO GALLERY", "COSMIC CALENDAR", "SPACE WEATHER", "LIGHT POLLUTION", "EQUIPMENT", 
        "ASTRO-PHOTO", "BOOKING", "SUSTAINABILITY", "INVESTOR PORTAL"
    ]
    sistem_durumu = "System: Online"

menu_secimi = st.sidebar.radio("GizliNavigasyonBasligi", menu_secenekleri, label_visibility="collapsed")
st.sidebar.write("---")
st.sidebar.info(sistem_durumu)

def auto_refresh_image(img_id, img_url, refresh_rate_ms, title, max_width="600px", filter_css="none"):
    return f"""
    <div style="border: 2px solid #B8860B; border-radius: 8px; position: relative; overflow: hidden; text-align: center; background: #000; padding: 20px;">
        <div style="position: absolute; top: 15px; left: 15px; background: rgba(0,0,0,0.8); padding: 5px 15px; color: #00ff00; font-family: monospace; font-weight: bold; border: 1px solid #00ff00; z-index: 10; border-radius: 4px; font-size:12px;">
            <span style="animation: blink 1s infinite;">●</span> {title}
        </div>
        <img id="{img_id}" src="{img_url}" style="width: 100%; max-width: {max_width}; border-radius: 4px; box-shadow: 0 0 40px rgba(184, 134, 11, 0.4); filter: {filter_css};">
    </div>
    <script>
        setInterval(function() {{
            document.getElementById('{img_id}').src = '{img_url}?time=' + new Date().getTime();
        }}, {refresh_rate_ms});
    </script>
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
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:45vh; filter: brightness(60%);" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=2000&auto=format&fit=crop"></div>', unsafe_allow_html=True)

# ==============================================================================
# SAYFA 2: LOKASYONLARIMIZ
# ==============================================================================
elif menu_secimi in ["LOKASYONLARIMIZ", "OUR LOCATIONS"]:
    st.markdown("<h2>Hedef Ülkeler ve Küresel Pazar</h2>", unsafe_allow_html=True)
    st.write("---")
    col_space1, col_chile, col_nz, col_space2 = st.columns([1, 4, 4, 1])
    with col_chile:
        st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?q=80&w=800&auto=format&fit=crop"><div class="service-content"><h3 class="service-title">Atacama Çölü, Şili</h3><p class="service-desc">Yılda 300 günden fazla bulutsuz gece.</p></div></div>""", unsafe_allow_html=True)
    with col_nz:
        st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=800&auto=format&fit=crop"><div class="service-content"><h3 class="service-title">Tekapo Gölü, Yeni Zelanda</h3><p class="service-desc">Uluslararası karanlık gökyüzü rezervi.</p></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 3: CANLI GÖZLEMEVİ
# ==============================================================================
elif menu_secimi in ["CANLI GÖZLEMEVİ", "LIVE OBSERVATORY"]:
    st.markdown("<h2>Stellaris Kesintisiz Uydu Ağı</h2>", unsafe_allow_html=True)
    st.write("---")
    t1, t2, t3, t4, t5, t6 = st.tabs(["🌍 GOES-16 (Amerika)", "🌍 HIMAWARI (Asya)", "☀️ SDO 304 (Güneş)", "☀️ SDO 171 (Güneş)", "🛰️ SOHO C3 (Radar)", "📍 ISS CANLI RADAR"])

    with t1: components.html(auto_refresh_image("goes16_img", "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/latest.jpg", 60000, "LIVE: GOES-16", "550px"), height=650)
    with t2: components.html(auto_refresh_image("himawari_img", "https://cdn.star.nesdis.noaa.gov/AHI/FD/GEOCOLOR/latest.jpg", 60000, "LIVE: HIMAWARI-9", "550px"), height=650)
    with t3: components.html(auto_refresh_image("sdo304_img", "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0304.jpg", 60000, "LIVE: SDO (AIA 304)", "550px"), height=650)
    with t4: components.html(auto_refresh_image("sdo171_img", "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0171.jpg", 60000, "LIVE: SDO (AIA 171)", "550px"), height=650)
    with t5: components.html(auto_refresh_image("sohoc3_img", "https://soho.nascom.nasa.gov/data/realtime/c3/1024/latest.jpg", 60000, "LIVE: SOHO LASCO C3", "550px"), height=650)
    with t6: st.markdown("""<div style="border: 2px solid #B8860B; border-radius: 8px; overflow: hidden; height: 550px;"><iframe src="https://isstracker.spaceflight.esa.int/" width="100%" height="100%" frameborder="0" style="pointer-events: none;"></iframe></div>""", unsafe_allow_html=True)

# ==============================================================================
# YENİ SAYFA 4: 3D SİMÜLASYONLAR (GENİŞLETİLMİŞ NASA API'LERİ)
# ==============================================================================
elif menu_secimi in ["3D SİMÜLASYONLAR", "3D SIMULATIONS"]:
    st.markdown("<h2>{}</h2>".format("İnteraktif 3D Uzay Simülatörleri" if lang == "TR" else "Interactive 3D Space Simulators"), unsafe_allow_html=True)
    st.markdown("<p style='color: #D4AF37;'><b>Sanal Keşif:</b> NASA'nın resmi 3D motorlarıyla Güneş Sistemini, dış gezegenleri ve meteorları farenizle kontrol ederek keşfedin.</p>", unsafe_allow_html=True)
    st.write("---")

    t_solar, t_exo, t_ast, t_sky = st.tabs([
        "🌍 GÜNEŞ SİSTEMİ" if lang == "TR" else "🌍 SOLAR SYSTEM",
        "🪐 ÖTEGEZEGENLER" if lang == "TR" else "🪐 EXOPLANETS",
        "☄️ ASTEROİT TAKİBİ" if lang == "TR" else "☄️ ASTEROID WATCH",
        "🌌 CANLI GÖKYÜZÜ" if lang == "TR" else "🌌 LIVE SKY MAP"
    ])

    with t_solar:
        st.markdown("<h3>NASA Eyes on the Solar System</h3>", unsafe_allow_html=True)
        st.markdown("""<div style="border: 2px solid #B8860B; border-radius: 8px; overflow: hidden; box-shadow: 0 0 30px rgba(184, 134, 11, 0.3);"><iframe src="https://eyes.nasa.gov/apps/solar-system/#/home?embed=true" width="100%" height="600" frameborder="0"></iframe></div>""", unsafe_allow_html=True)

    with t_exo:
        st.markdown("<h3>NASA Eyes on Exoplanets (Güneş Sistemi Dışı Gezegenler)</h3>", unsafe_allow_html=True)
        st.markdown("""<div style="border: 2px solid #B8860B; border-radius: 8px; overflow: hidden; box-shadow: 0 0 30px rgba(184, 134, 11, 0.3);"><iframe src="https://eyes.nasa.gov/apps/exo/#/?embed=true" width="100%" height="600" frameborder="0"></iframe></div>""", unsafe_allow_html=True)

    with t_ast:
        st.markdown("<h3>NASA Asteroid Watch (Dünyaya Yaklaşan Cisimler)</h3>", unsafe_allow_html=True)
        st.markdown("""<div style="border: 2px solid #B8860B; border-radius: 8px; overflow: hidden; box-shadow: 0 0 30px rgba(184, 134, 11, 0.3);"><iframe src="https://eyes.nasa.gov/apps/asteroids/#/?embed=true" width="100%" height="600" frameborder="0"></iframe></div>""", unsafe_allow_html=True)

    with t_sky:
        st.markdown("<h3>İnteraktif Yıldız Haritası</h3>", unsafe_allow_html=True)
        loc_choice = st.selectbox("Gözlem Noktası Seçin:", ["Atacama Çölü, Şili", "Tekapo Gölü, Yeni Zelanda", "Kuzey Kutbu"])
        if "Atacama" in loc_choice: lat, lon = -23.0, -67.7
        elif "Tekapo" in loc_choice: lat, lon = -44.0, 170.4
        else: lat, lon = 69.6, 18.9 

        sky_js_html = f"""
        <div id="starmap" style="width:100%;height:600px;border-radius:8px;border:2px solid #B8860B;background:#000;box-shadow: 0 0 30px rgba(184, 134, 11, 0.3);"></div>
        <script src="https://virtualsky.lco.global/embed/stuquery.min.js"></script>
        <script src="https://virtualsky.lco.global/embed/virtualsky.min.js"></script>
        <script>
        S.ready(function() {{
            var planetarium = S.virtualsky({{
                id: 'starmap',
                projection: 'stereo',
                latitude: {lat},
                longitude: {lon},
                constellations: true,
                constellationlabels: true,
                showstarlabels: true,
                showplanets: true,
                meteorshowers: true,
                live: true,
                mouse: true,
                color: 'dark'
            }});
        }});
        </script>
        """
        components.html(sky_js_html, height=650)

# ==============================================================================
# SAYFA 5: DİJİTAL UZAY PASAPORTU
# ==============================================================================
elif menu_secimi in ["UZAY PASAPORTU", "SPACE PASSPORT"]:
    st.markdown("<h2>{}</h2>".format("Kişisel Uzay Biniş Kartı" if lang == "TR" else "Personal Space Boarding Pass"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Stellaris ile yıldızlara yolculuğunuz başlıyor. Kendi dijital biniş kartınızı oluşturun." if lang == "TR" else "Your journey to the stars begins. Create your digital boarding pass."), unsafe_allow_html=True)
    st.write("---")

    col_form, col_pass = st.columns([1, 2])
    
    with col_form:
        st.markdown("<h3>Yolcu Bilgileri</h3>", unsafe_allow_html=True)
        pass_name = st.text_input("Yolcu Adı / Passenger Name:", "Yusuf Sezer Korkmaz")
        pass_dest = st.selectbox("Hedef / Destination:", ["Atacama Çölü (ALMA)", "Tekapo Gölü (Mount John)", "Uluslararası Uzay İstasyonu (ISS)", "Ay Yüzeyi (Artemis Base)"])
        pass_class = st.selectbox("Sınıf / Class:", ["VIP Astro-Turist", "Araştırmacı / Bilim İnsanı", "Uzay Komutanı"])
        pass_date = st.date_input("Kalkış Tarihi / Departure Date:", datetime.date.today())
        generate_btn = st.button("Biniş Kartı Oluştur")

    with col_pass:
        st.markdown("<h3>Dijital Pasaportunuz</h3>", unsafe_allow_html=True)
        random_barcode = "".join([str(random.randint(0, 9)) for _ in range(12)])
        pass_html = f"""
        <div class="boarding-pass">
            <div class="pass-left">
                <div class="pass-title">STELLARIS ASTRO-LINES</div>
                <br>
                <div style="display: flex; justify-content: space-between;">
                    <div>
                        <div class="pass-label">PASSENGER NAME</div>
                        <div class="pass-value">{pass_name.upper()}</div>
                    </div>
                    <div>
                        <div class="pass-label">FLIGHT CLASS</div>
                        <div class="pass-value">{pass_class.upper()}</div>
                    </div>
                </div>
                <div style="display: flex; justify-content: space-between;">
                    <div>
                        <div class="pass-label">DESTINATION</div>
                        <div class="pass-value">{pass_dest.upper()}</div>
                    </div>
                    <div>
                        <div class="pass-label">DATE</div>
                        <div class="pass-value">{pass_date.strftime('%d %b %Y')}</div>
                    </div>
                </div>
                <div style="display: flex; justify-content: space-between;">
                    <div>
                        <div class="pass-label">GATE</div>
                        <div class="pass-value">A-01 (EARTH)</div>
                    </div>
                    <div>
                        <div class="pass-label">BOARDING TIME</div>
                        <div class="pass-value">22:00 UTC</div>
                    </div>
                </div>
                <div class="pass-barcode">||| | || ||| | ||| || {random_barcode}</div>
            </div>
            <div class="pass-right">
                <div class="pass-logo">STELLARIS</div>
            </div>
        </div>
        """
        st.markdown(pass_html, unsafe_allow_html=True)
        if generate_btn: st.success("Biniş Kartınız sisteme kaydedildi! Uçuşa hazırsınız." if lang == "TR" else "Boarding Pass registered! You are ready for flight.")

# ==============================================================================
# SAYFA 6: VİDEOLAR GALERİSİ
# ==============================================================================
elif menu_secimi in ["VİDEOLAR GALERİSİ", "VIDEO GALLERY"]:
    st.markdown("<h2>Stellaris Uzay ve Bilim Sineması</h2>", unsafe_allow_html=True)
    st.write("---")
    v_col1, v_col2 = st.columns(2)
    with v_col1:
        st.markdown(f"<h3>James Webb Teleskobu</h3>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=uD4izuDMUQA")
        st.markdown(f"<br><h3>SpaceX Starship Fırlatması</h3>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=-1wcilQ58hI")
    with v_col2:
        st.markdown(f"<h3>Mars Yüzeyi 4K</h3>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=ZEyAs3NWH4A")
        st.markdown(f"<br><h3>Dünya 4K Manzaralar</h3>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=Un5SEJ8MyPc")

# ==============================================================================
# SAYFA 7: KOZMİK TAKVİM
# ==============================================================================
elif menu_secimi in ["KOZMİK TAKVİM", "COSMIC CALENDAR"]:
    st.markdown("<h2>Kozmik Takvim & Nadir Fenomenler</h2>", unsafe_allow_html=True)
    st.write("---")
    selected_event = st.selectbox("Seçiniz / Select:", ["Perseid Göktaşı Yağmuru", "Satürn Karşı Konumu", "Tam Güneş Tutulması"])
    st.write("")
    col_info, col_metrics = st.columns([2, 1])
    with col_info:
        if "Perseid" in selected_event: img_url, rarity = "https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?q=80&w=800", 60
        elif "Sat" in selected_event: img_url, rarity = "https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=800", 85
        else: img_url, rarity = "https://images.unsplash.com/photo-1539321908154-049275965646?q=80&w=800", 98
        st.markdown(f"""<div style="border: 1px solid #B8860B; border-radius: 8px; padding: 20px; background: #030814;"><img src="{img_url}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px; border: 1px solid #B8860B;"></div>""", unsafe_allow_html=True)
    with col_metrics:
        st.metric("Görüş / Visibility", "Ultra HD", "99%")
        st.progress(rarity)
        if st.button("Rezervasyon / Book"): st.success("İletildi / Submitted")

# ==============================================================================
# SAYFA 8: UZAY HAVADURUMU
# ==============================================================================
elif menu_secimi in ["UZAY HAVADURUMU", "SPACE WEATHER"]:
    st.markdown("<h2>Canlı Uzay Hava Durumu & Aurora Tahmini</h2>", unsafe_allow_html=True)
    st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("Kp İndeksi / Index", "6.33", "+1.2 (G2)")
    c2.metric("Rüzgar / Solar Wind", "540 km/s", "+45 km/s")
    c3.metric("Bz (Manyetik)", "-5.2 nT", "Güney / South")
    st.write("---")
    st.area_chart(pd.DataFrame({"Kp": [2.3, 4.0, 6.3, 5.1, 3.2, 2.0, 4.5, 7.1, 5.0]}), color="#B8860B")

# ==============================================================================
# SAYFA 9: IŞIK KİRLİLİĞİ
# ==============================================================================
elif menu_secimi in ["IŞIK KİRLİLİĞİ", "LIGHT POLLUTION"]:
    st.markdown("<h2>Bortle Scale: Light Pollution Simulator</h2>", unsafe_allow_html=True)
    st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl: bortle_val = st.slider("Gökyüzü Kalitesi / Sky Quality (9 = Şehir, 1 = Çöl)", 1, 9, 9, step=2)
    sky_glow_opacity = (bortle_val - 1) / 8.0  
    star_brightness = 1.2 - sky_glow_opacity   
    with col_view:
        st.markdown(f"""
        <div style="position: relative; width: 100%; height: 400px; border: 2px solid #B8860B; border-radius: 4px; overflow: hidden; background-color: #000; box-shadow: 0 5px 25px rgba(0,0,0,0.8);">
            <img src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200" style="width: 100%; height: 100%; object-fit: cover; filter: brightness({star_brightness}) contrast(1.2);">
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(200,100,50,0.9), rgba(50,70,100,0.8)); opacity: {sky_glow_opacity}; pointer-events: none;"></div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# SAYFA 10: EKİPMANLAR
# ==============================================================================
elif menu_secimi in ["EKİPMANLAR", "EQUIPMENT"]:
    st.markdown("<h2>VIP Gözlem Ekipmanları / Observation Equipment</h2>", unsafe_allow_html=True)
    st.write("---")
    e1, e2, e3 = st.columns(3)
    with e1: st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1517976487492-5750f3195933?q=80&w=800"><div class="service-content"><h3 class="service-title">Celestron CPC 1100 HD</h3></div></div>""", unsafe_allow_html=True)
    with e2: st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1506443432602-ac2fcd6f54e0?q=80&w=800"><div class="service-content"><h3 class="service-title">Meade LX200 14''</h3></div></div>""", unsafe_allow_html=True)
    with e3: st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800"><div class="service-content"><h3 class="service-title">Lunt Solar Systems</h3></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 11: ASTRO-FOTOĞRAF
# ==============================================================================
elif menu_secimi in ["ASTRO-FOTOĞRAF", "ASTRO-PHOTO"]:
    st.markdown("<h2>Astro-Photography Simulator</h2>", unsafe_allow_html=True)
    st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl:
        iso_val = st.slider("ISO Değeri / ISO Value", 100, 6400, 800, step=100)
        exp_val = st.slider("Pozlama Süresi / Exposure (s)", 1, 30, 10, step=1)
    with col_view:
        brightness = 0.15 + (exp_val / 30.0) * 0.6 + (iso_val / 6400.0) * 0.5
        st.markdown(f"""<div style="position: relative; width: 100%; border: 2px solid #B8860B; border-radius: 4px; overflow: hidden;"><img src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200" style="width: 100%; filter: brightness({brightness});"></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 12: REZERVASYON
# ==============================================================================
elif menu_secimi in ["REZERVASYON", "BOOKING"]:
    st.markdown("<h2>Deneyimler & Online Rezervasyon / Booking</h2>", unsafe_allow_html=True)
    st.write("---")
    kisi_sayisi = st.slider("Misafir / Guests", 1, 8, 2)
    st.markdown(f"<div class='price-tag'>${(250 * kisi_sayisi):,}</div>", unsafe_allow_html=True)
    if st.button("Rezervasyon Gönder / Send Booking"): st.success("Talebiniz alınmıştır / Request received.")

# ==============================================================================
# SAYFA 13: SÜRDÜRÜLEBİLİRLİK
# ==============================================================================
elif menu_secimi in ["SÜRDÜRÜLEBİLİRLİK", "SUSTAINABILITY"]:
    st.markdown("<h2>Sürdürülebilir Bilimsel Turizm / Sustainability</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh;" src="https://images.unsplash.com/photo-1502481851512-e9e2529bfbf9?q=80&w=1200"></div>', unsafe_allow_html=True)

# ==============================================================================
# SAYFA 14: YATIRIMCI PORTALI
# ==============================================================================
elif menu_secimi in ["YATIRIMCI PORTALI", "INVESTOR PORTAL"]:
    st.markdown("<h2>Kurumsal İş Modeli / Corporate Portal</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.text_input("Şifre / Password (stellaris2026):", type="password") == "stellaris2026":
        st.success("Erişim Sağlandı / Access Granted")
        st.area_chart(pd.DataFrame({"Şili": [1000, 2500, 4800, 7500, 12000], "Yeni Zelanda": [800, 1900, 3500, 6000, 9500]}, index=["Yıl 1", "Yıl 2", "Yıl 3", "Yıl 4", "Yıl 5"]), color=["#B8860B", "#C5A059"])
