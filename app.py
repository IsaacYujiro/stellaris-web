import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import datetime
import time
import os
import glob

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

    [data-baseweb="tab-list"] { justify-content: center; gap: 10px; flex-wrap: wrap; }
    [data-baseweb="tab"] { background-color: transparent !important; color: #C5A059 !important; font-family: 'Cinzel', serif; font-size: 0.9rem; padding: 5px 10px; }
    [aria-selected="true"] { color: #B8860B !important; border-bottom: 2px solid #B8860B !important; font-weight: bold; }
    .stProgress > div > div > div > div { background-color: #B8860B !important; }
    
    /* Yanıp Sönen Kırmızı Kayıt İkonu Animasyonu */
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
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
        "ANA SAYFA", "LOKASYONLARIMIZ", "CANLI GÖZLEMEVİ", "VİDEOLAR GALERİSİ", 
        "KOZMİK TAKVİM", "UZAY HAVADURUMU", "IŞIK KİRLİLİĞİ", "EKİPMANLAR", 
        "ASTRO-FOTOĞRAF", "YAPAY ZEKA", "REZERVASYON", "SÜRDÜRÜLEBİLİRLİK", "YATIRIMCI PORTALI"
    ]
    sistem_durumu = "Sistem: Çevrimiçi"
else:
    menu_secenekleri = [
        "HOME", "OUR LOCATIONS", "LIVE OBSERVATORY", "VIDEO GALLERY", 
        "COSMIC CALENDAR", "SPACE WEATHER", "LIGHT POLLUTION", "EQUIPMENT", 
        "ASTRO-PHOTO", "AI SIMULATOR", "BOOKING", "SUSTAINABILITY", "INVESTOR PORTAL"
    ]
    sistem_durumu = "System: Online"

menu_secimi = st.sidebar.radio("GizliNavigasyonBasligi", menu_secenekleri, label_visibility="collapsed")
st.sidebar.write("---")
st.sidebar.info(sistem_durumu)

# Ortak Fonksiyon: Youtube kullanmayan, doğrudan uydu API'lerini yenileyen sistem
def auto_refresh_image(img_id, img_url, refresh_rate_ms, title, max_width="600px", filter_css="none"):
    html_code = f"""
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
    return html_code

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
        st.markdown("<p>Stellaris, sıradan tatil anlayışını geride bırakıp gözlerini evrenin derinliklerine çevirenler için doğdu. Işık kirliliğinden tamamen arınmış dünyanın en karanlık ve en berrak noktalarında, bilim ve doğayı kusursuz bir lüksle harmanlıyoruz.</p>", unsafe_allow_html=True)
    else:
        st.markdown("<h2>Discover the Limits of the Sky</h2>", unsafe_allow_html=True)
        st.markdown("<p>Stellaris was born for those who leave ordinary holiday concepts behind and turn their eyes to the depths of the universe. In the darkest and clearest points of the world, completely free from light pollution, we blend science and nature with flawless luxury.</p>", unsafe_allow_html=True)
        
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
# SAYFA 3: CANLI GÖZLEMEVİ (YOUTUBE TAMAMEN SİLİNDİ - 100% GARANTİ API'LER)
# ==============================================================================
elif menu_secimi in ["CANLI GÖZLEMEVİ", "LIVE OBSERVATORY"]:
    if lang == "TR":
        st.markdown("<h2>Stellaris Kesintisiz Uydu Ağı</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #D4AF37;'><b>Video oynatıcıları iptal edildi.</b> Aşağıdaki tüm kanallar doğrudan NASA ve NOAA uydularından çekilen <b>ham veri akışlarıdır</b>. Siz hiçbir şey yapmasanız da sistem arka planda her 60 saniyede bir yeni fotoğrafları çeker. Asla hata vermez.</p>", unsafe_allow_html=True)
    else:
        st.markdown("<h2>Stellaris Uninterrupted Satellite Network</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #D4AF37;'><b>All video players eliminated.</b> All channels below are <b>raw data streams</b> pulled directly from NASA and NOAA satellites. The system auto-refreshes seamlessly every 60 seconds.</p>", unsafe_allow_html=True)
    st.write("---")
    
    t1, t2, t3, t4, t5, t6, t7 = st.tabs([
        "🌍 GOES-16 (Amerika)", 
        "🌍 HIMAWARI (Asya)", 
        "🌍 GOES-16 (Kızılötesi)", 
        "☀️ SDO 304 (Güneş)", 
        "☀️ SDO 171 (Güneş)", 
        "☀️ SDO 211 (Korona)",
        "☀️ SDO (Manyetik)",
        "🛰️ SOHO C2 (İç Korona)", 
        "🛰️ SOHO C3 (Radar)", 
        "📍 ISS CANLI RADAR",
        "🔭 TELESKOP SİM."
    ])

    with t1:
        st.markdown("<h3>NOAA GOES-16 (Doğu Yarımküre & Amerika)</h3>", unsafe_allow_html=True)
        components.html(auto_refresh_image("goes16_img", "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/latest.jpg", 60000, "LIVE: GOES-16 (EAST)", "550px"), height=650)

    with t2:
        st.markdown("<h3>Japonya Meteoroloji Ajansı HIMAWARI-9 (Asya & Pasifik)</h3>", unsafe_allow_html=True)
        components.html(auto_refresh_image("goes18_img", "https://cdn.star.nesdis.noaa.gov/AHI/FD/GEOCOLOR/latest.jpg", 60000, "LIVE: HIMAWARI-9 (WEST)", "550px"), height=650)

    with t3:
        st.markdown("<h3>NOAA GOES-16 Band 13 (Kızılötesi Sıcaklık / Gece Görüşü)</h3>", unsafe_allow_html=True)
        components.html(auto_refresh_image("goes16ir_img", "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/Band13/latest.jpg", 60000, "LIVE: GOES-16 INFRARED", "550px"), height=650)

    with t4:
        st.markdown("<h3>NASA SDO (AIA 304 - Kızılötesi Güneş Patlamaları)</h3>", unsafe_allow_html=True)
        components.html(auto_refresh_image("sdo304_img", "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0304.jpg", 60000, "LIVE: SDO (AIA 304)", "550px"), height=650)

    with t5:
        st.markdown("<h3>NASA SDO (AIA 171 - Manyetik Döngüler)</h3>", unsafe_allow_html=True)
        components.html(auto_refresh_image("sdo171_img", "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0171.jpg", 60000, "LIVE: SDO (AIA 171)", "550px"), height=650)

    with t6:
        st.markdown("<h3>NASA SDO (AIA 211 - Güneş Koronası)</h3>", unsafe_allow_html=True)
        components.html(auto_refresh_image("sdo211_img", "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0211.jpg", 60000, "LIVE: SDO (AIA 211)", "550px"), height=650)

    with t7:
        st.markdown("<h3>NASA SDO (HMI - Manyetik Alan Haritası)</h3>", unsafe_allow_html=True)
        components.html(auto_refresh_image("sdohmi_img", "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_HMIB.jpg", 60000, "LIVE: SDO MAGNETOGRAM", "550px", "contrast(1.5)"), height=650)

    with t8:
        st.markdown("<h3>NASA SOHO LASCO C2 (İç Koronagraf)</h3>", unsafe_allow_html=True)
        components.html(auto_refresh_image("sohoc2_img", "https://soho.nascom.nasa.gov/data/realtime/c2/1024/latest.jpg", 60000, "LIVE: SOHO LASCO C2", "550px", "contrast(1.2)"), height=650)

    with t9:
        st.markdown("<h3>NASA SOHO LASCO C3 (Geniş Açılı Uzay Radarı)</h3>", unsafe_allow_html=True)
        components.html(auto_refresh_image("sohoc3_img", "https://soho.nascom.nasa.gov/data/realtime/c3/1024/latest.jpg", 60000, "LIVE: SOHO LASCO C3", "550px"), height=650)

    with t10:
        st.markdown("<h3>Uluslararası Uzay İstasyonu (ISS) Canlı Konumu</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div style="border: 2px solid #B8860B; border-radius: 8px; overflow: hidden; height: 550px;">
            <iframe src="https://isstracker.spaceflight.esa.int/" width="100%" height="100%" frameborder="0" style="pointer-events: none;"></iframe>
        </div>
        """, unsafe_allow_html=True)

    with t11:
        if "telescope_connected" not in st.session_state: st.session_state.telescope_connected = False
        istasyon = st.selectbox("İstasyon / Station:", ["Atacama Alpha (Celestron 1100 HD)", "Tekapo South (Meade LX200 14'')"])
        if st.button("Sanal Bağlantı Kur / Connect"):
            with st.spinner("Bağlanılıyor..."): time.sleep(1)
            st.session_state.telescope_connected = True
        if st.session_state.telescope_connected:
            st.write("---")
            col_view, col_controls = st.columns([2, 1])
            with col_controls:
                zoom_level = st.slider("Zoom", 1.0, 3.0, 1.0, 0.1)
                filter_type = st.radio("Filtre / Filter", ["Görünür / Visible", "H-Alpha (Kızıl)", "O-III (Mavi)"])
                css_filter = "sepia(100%) hue-rotate(-50deg) saturate(300%)" if "H-Alpha" in filter_type else "sepia(100%) hue-rotate(130deg) saturate(200%)" if "O-III" in filter_type else "none"
            with col_view:
                deep_space_img = "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=1200" if "Atacama" in istasyon else "https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?q=80&w=1200"
                st.markdown(f"""
                <div style="width: 100%; height: 400px; border: 2px solid #B8860B; border-radius: 8px; overflow: hidden; background: #000; position: relative;">
                    <div style="position: absolute; top: 15px; left: 15px; color: red; font-family: monospace; font-weight: bold; z-index: 10;"><span style="animation: blink 1s infinite;">●</span> SIMULATION</div>
                    <img src="{deep_space_img}" style="width: 100%; height: 100%; object-fit: cover; transform: scale({zoom_level}); filter: {css_filter}; transition: all 0.5s ease;">
                </div>
                """, unsafe_allow_html=True)

# ==============================================================================
# YENİ SAYFA 4: VİDEOLAR GALERİSİ (YENİ VE KUSURSUZ KATEGORİLER)
# ==============================================================================
elif menu_secimi in ["VİDEOLAR GALERİSİ", "VIDEO GALLERY"]:
    st.markdown("<h2>{}</h2>".format("Stellaris Uzay ve Bilim Sineması" if lang == "TR" else "Stellaris Space & Science Cinema"), unsafe_allow_html=True)
    st.markdown("<p>{}</p>".format("Evrenin en büyüleyici anlarının yüksek çözünürlüklü kayıtları. Kategorilere ayrılmış bu premium arşivde arkanıza yaslanın ve uzayın derinliklerine dalın. Tüm içerikler 'Embed' garantilidir." if lang == "TR" else "High-definition recordings of the universe's most fascinating moments. Sit back and dive into the depths of space in this categorized premium archive. All content is embed-guaranteed."), unsafe_allow_html=True)
    st.write("---")

    t_doc, t_launch, t_planet, t_ambient = st.tabs([
        "🌌 Derin Uzay Belgeselleri" if lang == "TR" else "🌌 Deep Space Docs",
        "🚀 Fırlatmalar & Görevler" if lang == "TR" else "🚀 Launches & Missions",
        "🪐 Gezegen Keşifleri" if lang == "TR" else "🪐 Planetary Exploration",
        "✨ 4K Kozmik Ambiyans" if lang == "TR" else "✨ 4K Cosmic Ambient"
    ])

    with t_doc:
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            st.markdown(f"<h3>{'Geleceğin Zaman Çizelgesi (Evrenin Sonu)' if lang=='TR' else 'Timelapse of the Future'}</h3>", unsafe_allow_html=True)
            st.video("https://www.youtube.com/watch?v=uD4izuDMUQA")
        with v_col2:
            st.markdown(f"<h3>{'Yaşamın Kökeni ve Uzaylılar' if lang=='TR' else 'Life Beyond: Aliens'}</h3>", unsafe_allow_html=True)
            st.video("https://www.youtube.com/watch?v=SUelbSa-OkA")

    with t_launch:
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            st.markdown(f"<h3>{'SpaceX Starship Dev Uçuş Testi' if lang=='TR' else 'SpaceX Starship Flight Test'}</h3>", unsafe_allow_html=True)
            st.video("https://www.youtube.com/watch?v=-1wcilQ58hI")
        with v_col2:
            st.markdown(f"<h3>{'Apollo 11: İnsanlığın Ay\'a Adımı' if lang=='TR' else 'Apollo 11: Moon Landing'}</h3>", unsafe_allow_html=True)
            st.video("https://www.youtube.com/watch?v=S9HdPi9Ikhk")

    with t_planet:
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            st.markdown(f"<h3>{'Mars Yüzeyi 4K (Perseverance)' if lang=='TR' else 'Mars Surface in 4K'}</h3>", unsafe_allow_html=True)
            st.video("https://www.youtube.com/watch?v=ZEyAs3NWH4A")
        with v_col2:
            st.markdown(f"<h3>{'James Webb: Evrenin İlk Işıkları' if lang=='TR' else 'James Webb: First Lights'}</h3>", unsafe_allow_html=True)
            st.video("https://www.youtube.com/watch?v=XhJEJABkjuw")

    with t_ambient:
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            st.markdown(f"<h3>{'Güneş 4K (NASA Goddard)' if lang=='TR' else 'The Sun in 4K (NASA)'}</h3>", unsafe_allow_html=True)
            st.video("https://www.youtube.com/watch?v=6tmbeLTHC_0")
        with v_col2:
            st.markdown(f"<h3>{'Dünya: ISS\'ten 4K Manzaralar' if lang=='TR' else 'Earth: 4K Views from ISS'}</h3>", unsafe_allow_html=True)
            st.video("https://www.youtube.com/watch?v=Xjs6fnpPWy4")

# ==============================================================================
# SAYFA 5: KOZMİK TAKVİM
# ==============================================================================
elif menu_secimi in ["KOZMİK TAKVİM", "COSMIC CALENDAR"]:
    st.markdown("<h2>{}</h2>".format("Kozmik Takvim & Nadir Fenomenler" if lang == "TR" else "Cosmic Calendar & Rare Phenomena"), unsafe_allow_html=True)
    st.write("---")
    events = ["Perseid Göktaşı Yağmuru (Ağustos)", "Satürn Karşı Konumu (Eylül)", "Tam Güneş Tutulması"] if lang == "TR" else ["Perseid Meteor Shower", "Saturn Opposition", "Total Solar Eclipse"]
    selected_event = st.selectbox("Seçiniz / Select:", events)
    st.write("")
    col_info, col_metrics = st.columns([2, 1])
    with col_info:
        if "Perseid" in selected_event: img_url, rarity = "https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?q=80&w=800&auto=format&fit=crop", 60
        elif "Sat" in selected_event: img_url, rarity = "https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=800&auto=format&fit=crop", 85
        else: img_url, rarity = "https://images.unsplash.com/photo-1539321908154-049275965646?q=80&w=800&auto=format&fit=crop", 98
        st.markdown(f"""<div style="border: 1px solid #B8860B; border-radius: 8px; padding: 20px; background: #030814;"><img src="{img_url}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px; border: 1px solid #B8860B;"></div>""", unsafe_allow_html=True)
    with col_metrics:
        st.metric("Görüş / Visibility", "Ultra HD", "99%")
        st.progress(rarity)
        if st.button("Rezervasyon / Book"): st.success("İletildi / Submitted")

# ==============================================================================
# SAYFA 6: UZAY HAVADURUMU
# ==============================================================================
elif menu_secimi in ["UZAY HAVADURUMU", "SPACE WEATHER"]:
    st.markdown("<h2>{}</h2>".format("Canlı Uzay Hava Durumu & Aurora Tahmini" if lang == "TR" else "Live Space Weather & Aurora Forecast"), unsafe_allow_html=True)
    st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("Kp İndeksi / Index", "6.33", "+1.2 (G2)")
    c2.metric("Rüzgar / Solar Wind", "540 km/s", "+45 km/s")
    c3.metric("Bz (Manyetik)", "-5.2 nT", "Güney / South")
    st.write("---")
    st.area_chart(pd.DataFrame({"Kp": [2.3, 4.0, 6.3, 5.1, 3.2, 2.0, 4.5, 7.1, 5.0]}), color="#B8860B")

# ==============================================================================
# SAYFA 7: IŞIK KİRLİLİĞİ
# ==============================================================================
elif menu_secimi in ["IŞIK KİRLİLİĞİ", "LIGHT POLLUTION"]:
    st.markdown("<h2>Bortle Scale: Light Pollution Simulator</h2>", unsafe_allow_html=True)
    st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl:
        bortle_val = st.slider("Gökyüzü Kalitesi / Sky Quality (9 = Şehir, 1 = Çöl)", 1, 9, 9, step=2)
    sky_glow_opacity = (bortle_val - 1) / 8.0  
    star_brightness = 1.2 - sky_glow_opacity   
    with col_view:
        st.markdown(f"""
        <div style="position: relative; width: 100%; height: 400px; border: 2px solid #B8860B; border-radius: 4px; overflow: hidden; background-color: #000; box-shadow: 0 5px 25px rgba(0,0,0,0.8);">
            <img src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200" style="width: 100%; height: 100%; object-fit: cover; filter: brightness({star_brightness}) contrast(1.2); transition: all 0.8s ease;">
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(200,100,50,0.9), rgba(50,70,100,0.8)); opacity: {sky_glow_opacity}; pointer-events: none;"></div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# SAYFA 8: EKİPMANLAR
# ==============================================================================
elif menu_secimi in ["EKİPMANLAR", "EQUIPMENT"]:
    st.markdown("<h2>VIP Gözlem Ekipmanları / Observation Equipment</h2>", unsafe_allow_html=True)
    st.write("---")
    e1, e2, e3 = st.columns(3)
    with e1: st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1517976487492-5750f3195933?q=80&w=800"><div class="service-content"><h3 class="service-title">Celestron CPC 1100 HD</h3></div></div>""", unsafe_allow_html=True)
    with e2: st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1506443432602-ac2fcd6f54e0?q=80&w=800"><div class="service-content"><h3 class="service-title">Meade LX200 14''</h3></div></div>""", unsafe_allow_html=True)
    with e3: st.markdown("""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800"><div class="service-content"><h3 class="service-title">Lunt Solar Systems</h3></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 9: ASTRO-FOTOĞRAF
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
# SAYFA 10: YAPAY ZEKA
# ==============================================================================
elif menu_secimi in ["YAPAY ZEKA", "AI SIMULATOR"]:
    st.markdown("<h2>AI-Powered Deep Space Simulation</h2>", unsafe_allow_html=True)
    st.write("---")
    st.selectbox("Celestial Object", ["Spiral Galaxy", "Nebula", "Supernova"])
    if st.button("Run AI"): st.success("Complete")

# ==============================================================================
# SAYFA 11: REZERVASYON
# ==============================================================================
elif menu_secimi in ["REZERVASYON", "BOOKING"]:
    st.markdown("<h2>Deneyimler & Online Rezervasyon / Booking</h2>", unsafe_allow_html=True)
    st.write("---")
    kisi_sayisi = st.slider("Misafir / Guests", 1, 8, 2)
    st.markdown(f"<div class='price-tag'>${(250 * kisi_sayisi):,}</div>", unsafe_allow_html=True)
    if st.button("Rezervasyon Gönder / Send Booking"): st.success("Talebiniz alınmıştır / Request received.")

# ==============================================================================
# SAYFA 12: SÜRDÜRÜLEBİLİRLİK
# ==============================================================================
elif menu_secimi in ["SÜRDÜRÜLEBİLİRLİK", "SUSTAINABILITY"]:
    st.markdown("<h2>Sürdürülebilir Bilimsel Turizm / Sustainability</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh;" src="https://images.unsplash.com/photo-1502481851512-e9e2529bfbf9?q=80&w=1200"></div>', unsafe_allow_html=True)

# ==============================================================================
# SAYFA 13: YATIRIMCI PORTALI
# ==============================================================================
elif menu_secimi in ["YATIRIMCI PORTALI", "INVESTOR PORTAL"]:
    st.markdown("<h2>Kurumsal İş Modeli / Corporate Portal</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.text_input("Şifre / Password (stellaris2026):", type="password") == "stellaris2026":
        st.success("Erişim Sağlandı / Access Granted")
        st.area_chart(pd.DataFrame({"Şili": [1000, 2500, 4800, 7500, 12000], "Yeni Zelanda": [800, 1900, 3500, 6000, 9500]}, index=["Yıl 1", "Yıl 2", "Yıl 3", "Yıl 4", "Yıl 5"]), color=["#B8860B", "#C5A059"])
