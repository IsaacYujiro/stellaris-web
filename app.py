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
    div[role="radiogroup"] p { color: #B8860B !important; font-family: 'Cinzel', serif !important; font-size: 1.1rem !important; font-weight: 600 !important; text-align: center !important; visibility: visible !important; display: block !important; width: 100%; margin-top: 5px; transition: all 0.3s ease; }
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
    
    /* İlerleme Çubuğu (Progress Bar) Altın Rengi Yapma */
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
        "ANA SAYFA", "LOKASYONLARIMIZ", "KOZMİK TAKVİM", "IŞIK KİRLİLİĞİ", 
        "EKİPMANLAR", "REZERVASYON", "YAPAY ZEKA", "SÜRDÜRÜLEBİLİRLİK", "YATIRIMCI PORTALI"
    ]
    sistem_durumu = "Sistem: Çevrimiçi"
else:
    menu_secenekleri = [
        "HOME", "OUR LOCATIONS", "COSMIC CALENDAR", "LIGHT POLLUTION", 
        "EQUIPMENT", "BOOKING", "AI SIMULATOR", "SUSTAINABILITY", "INVESTOR PORTAL"
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
        st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?q=80&w=800&auto=format&fit=crop"><div class="service-content"><h3 class="service-title">{t_chile_title}</h3><p class="service-desc">{t_chile_desc}</p></div></div>""", unsafe_allow_html=True)
    with col_nz:
        st.markdown(f"""<div class="service-card"><img class="service-img" src="https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=800&auto=format&fit=crop"><div class="service-content"><h3 class="service-title">{t_nz_title}</h3><p class="service-desc">{t_nz_desc}</p></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# YENİ SAYFA 3: KOZMİK TAKVİM VE NADİR FENOMENLER
# ==============================================================================
elif menu_secimi in ["KOZMİK TAKVİM", "COSMIC CALENDAR"]:
    if lang == "TR":
        st.markdown("<h2>Kozmik Takvim & Nadir Fenomenler</h2>", unsafe_allow_html=True)
        st.markdown("<p>Astro-turizmde zamanlama her şeydir. Dünyanın en karanlık noktalarında, yaklaşan en nadir doğa ve uzay olaylarına tanıklık etmek için yerinizi ayırtın.</p>", unsafe_allow_html=True)
        ev_label = "Keşfetmek İstediğiniz Etkinliği Seçin:"
        events = [
            "Perseid Göktaşı Yağmuru (Ağustos)",
            "Satürn Karşı Konumu - Halka Gözlemi (Eylül)",
            "Tam Güneş Tutulması Özel Turu (Kış Dönemi)"
        ]
        btn_label = "Bu Tarih İçin VIP Rezervasyon Başlat"
    else:
        st.markdown("<h2>Cosmic Calendar & Rare Phenomena</h2>", unsafe_allow_html=True)
        st.markdown("<p>Timing is everything in astro-tourism. Secure your spot to witness the rarest upcoming natural and space events from the darkest points on Earth.</p>", unsafe_allow_html=True)
        ev_label = "Select the Event You Want to Explore:"
        events = [
            "Perseid Meteor Shower (August)",
            "Saturn Opposition - Ring Observation (September)",
            "Total Solar Eclipse Exclusive Tour (Winter Season)"
        ]
        btn_label = "Start VIP Booking for This Date"

    st.write("---")
    
    selected_event = st.selectbox(ev_label, events)
    st.write("")
    
    col_info, col_metrics = st.columns([2, 1])
    
    with col_info:
        if "Perseid" in selected_event:
            img_url = "https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?q=80&w=800&auto=format&fit=crop"
            e_title = "Perseid Göktaşı Şöleni" if lang == "TR" else "Perseid Meteor Spectacle"
            e_desc = "Saatte ortalama 100'den fazla ateş topunun atmosfere girdiği yılın en görkemli meteor yağmuru. Atacama'nın zifiri karanlığında her saniye gökyüzünde bir çizgi göreceksiniz." if lang == "TR" else "The most spectacular meteor shower of the year where over 100 fireballs enter the atmosphere per hour. In the pitch black of Atacama, you will see a streak across the sky every second."
            e_equip = "Ekipman: Çıplak Göz & Geniş Açılı Lensler" if lang == "TR" else "Equipment: Naked Eye & Wide Angle Lenses"
            rarity = 60
            
        elif "Sat" in selected_event:
            img_url = "https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=800&auto=format&fit=crop"
            e_title = "Satürn Karşı Konumu" if lang == "TR" else "Saturn Opposition"
            e_desc = "Satürn'ün Dünya'ya en yakın ve en parlak olduğu dönem. Gezegenin buzlu halkaları ve uydusu Titan, VIP teleskoplarımızla adeta elinizi uzatıp dokunabileceğiniz kadar net." if lang == "TR" else "The period when Saturn is closest and brightest to Earth. The planet's icy rings and its moon Titan are so clear through our VIP telescopes that you feel you could reach out and touch them."
            e_equip = "Ekipman: Meade LX200 14'' Advanced" if lang == "TR" else "Equipment: Meade LX200 14'' Advanced"
            rarity = 85
            
        else:
            img_url = "https://images.unsplash.com/photo-1539321908154-049275965646?q=80&w=800&auto=format&fit=crop"
            e_title = "Tam Güneş Tutulması" if lang == "TR" else "Total Solar Eclipse"
            e_desc = "Gündüzün geceye döndüğü o efsanevi an. Korona (Güneş Tacı) gözlemi ve özel filtreli ekipmanlarla ömür boyu unutulmayacak, çok nadir bir bilimsel macera." if lang == "TR" else "That legendary moment when day turns into night. A once-in-a-lifetime scientific adventure with Corona observation and special filtered equipment."
            e_equip = "Ekipman: Lunt Solar Systems H-Alpha" if lang == "TR" else "Equipment: Lunt Solar Systems H-Alpha"
            rarity = 98

        st.markdown(f"""
        <div style="border: 1px solid #B8860B; border-radius: 8px; padding: 20px; background: #030814;">
            <h3 style="text-align: left !important; color: #D4AF37 !important;">{e_title}</h3>
            <img src="{img_url}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px; margin-bottom: 15px; border: 1px solid #B8860B;">
            <p style="text-align: left !important;">{e_desc}</p>
            <p style="text-align: left !important; font-weight: bold; color: #B8860B !important;">{e_equip}</p>
        </div>
        """, unsafe_allow_html=True)

    with col_metrics:
        st.markdown("<br>", unsafe_allow_html=True)
        met1 = "Görüş Kalitesi" if lang == "TR" else "Visibility Quality"
        met2 = "Atmosferik Denge" if lang == "TR" else "Atmospheric Stability"
        met3 = "Nadirlik (Rarity)" if lang == "TR" else "Event Rarity"
        
        st.metric(label=met1, value="Ultra HD", delta="Bulutsuzluk %99")
        st.metric(label=met2, value="5/5", delta="Kusursuz")
        
        st.markdown(f"<p style='text-align: left !important; margin-bottom: 5px !important; color: #C5A059;'>{met3}</p>", unsafe_allow_html=True)
        st.progress(rarity)
        
        st.write("")
        st.write("")
        if st.button(btn_label):
            st.success("Talebiniz VIP Müşteri Temsilcimize İletildi." if lang == "TR" else "Your request has been sent to our VIP Representative.")

# ==============================================================================
# SAYFA 4: IŞIK KİRLİLİĞİ (BORTLE) SİMÜLATÖRÜ
# ==============================================================================
elif menu_secimi in ["IŞIK KİRLİLİĞİ", "LIGHT POLLUTION"]:
    if lang == "TR":
        st.markdown("<h2>Bortle Ölçeği: Işık Kirliliği Simülatörü</h2>", unsafe_allow_html=True)
        st.markdown("<p>Atacama Çölü'nün neden eşsiz olduğunu kendi gözlerinizle görün. Şehir hayatının ışıklarından yavaşça kurtularak gerçek bir gece gökyüzüne ulaşmak için aşağıdaki kaydırıcıyı kullanın.</p>", unsafe_allow_html=True)
        slider_label = "Gökyüzü Kalitesi (9 = Şehir Merkezi, 1 = Mükemmel Karanlık)"
        bortle_texts = {
            9: "Bortle 9: İç Şehir. Gökyüzü tamamen parlak turuncu/beyazdır. Sadece Ay ve birkaç parlak gezegen görülebilir.",
            7: "Bortle 7: Banliyö. Işık kubbeleri ufku kaplar. Samanyolu tamamen görünmezdir.",
            5: "Bortle 5: Kırsal Alan. Gökyüzünde sönük bir Samanyolu izi seçilebilir ancak detay yoktur.",
            3: "Bortle 3: Karanlık Gökyüzü. Samanyolu yapısal detaylarıyla görünmeye başlar. Ufukta hafif ışık kirliliği vardır.",
            1: "Bortle 1: Atacama/Tekapo. Kusursuz Karanlık. Samanyolu o kadar parlaktır ki yere gölge düşürür. Binlerce yıldız çıplak gözle seçilir."
        }
    else:
        st.markdown("<h2>Bortle Scale: Light Pollution Simulator</h2>", unsafe_allow_html=True)
        st.markdown("<p>See for yourself why the Atacama Desert is unique. Use the slider below to slowly escape the city lights and reach a true night sky.</p>", unsafe_allow_html=True)
        slider_label = "Sky Quality (9 = Inner City, 1 = Perfect Dark Sky)"
        bortle_texts = {
            9: "Bortle 9: Inner City. The sky is brilliantly lit orange/white. Only the Moon and a few planets are visible.",
            7: "Bortle 7: Suburban. Light domes cover the horizon. The Milky Way is totally invisible.",
            5: "Bortle 5: Rural. A faint washed-out Milky Way is visible, but lacks any detail.",
            3: "Bortle 3: Dark Sky. The Milky Way appears with complex structure. Minor light pollution on the horizon.",
            1: "Bortle 1: Atacama/Tekapo. Perfect Darkness. The Milky Way is so bright it casts shadows. Thousands of stars visible to the naked eye."
        }

    st.write("---")
    col_ctrl, col_view = st.columns([1, 2])
    with col_ctrl:
        bortle_val = st.slider(slider_label, min_value=1, max_value=9, value=9, step=2)
        st.write("")
        st.info(bortle_texts[bortle_val])

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
# SAYFA 5: GÖZLEM KOŞULLARI & EKİPMAN
# ==============================================================================
elif menu_secimi in ["EKİPMANLAR", "EQUIPMENT"]:
    if lang == "TR":
        st.markdown("<h2>Gözlem Koşulları ve VIP Ekipmanlar</h2>", unsafe_allow_html=True)
        st.markdown("<p>Kusursuz bir deneyim için anlık gökyüzü berraklık oranları ve teknoloji harikası teleskoplarımız.</p>", unsafe_allow_html=True)
        m1, m2, m3 = "Atacama Berraklık", "Tekapo Berraklık", "Ay Evresi"
        m1_v, m2_v, m3_v = "%98", "%92", "Yeni Ay"
        m1_d, m2_d, m3_d = "+2% (Mükemmel)", "-1% (Çok İyi)", "Gözlem İçin Kusursuz"
        t_eq = "VIP Gözlem Ekipmanlarımız"
        eq1_t, eq1_d = "Celestron CPC 1100 HD", "Derin uzay nesneleri (Galaksiler ve Bulutsular) için ultra yüksek çözünürlüklü bilgisayarlı teleskop."
        eq2_t, eq2_d = "Meade LX200 14''", "Gezegenlerin ve ay kraterlerinin en ince detaylarını yakalamak için devasa diyaframlı profesyonel gözlem aracı."
        eq3_t, eq3_d = "Lunt Solar Systems", "Gündüz aktiviteleri için güneş patlamalarını ve taçküreyi güvenle izlemenizi sağlayan özel H-Alpha teleskobu."
    else:
        st.markdown("<h2>Observation Conditions and VIP Equipment</h2>", unsafe_allow_html=True)
        st.markdown("<p>Real-time sky clarity rates and our state-of-the-art telescopes for a flawless experience.</p>", unsafe_allow_html=True)
        m1, m2, m3 = "Atacama Clarity", "Tekapo Clarity", "Moon Phase"
        m1_v, m2_v, m3_v = "98%", "92%", "New Moon"
        m1_d, m2_d, m3_d = "+2% (Perfect)", "-1% (Excellent)", "Flawless for Observation"
        t_eq = "Our VIP Observation Equipment"
        eq1_t, eq1_d = "Celestron CPC 1100 HD", "Ultra-high-definition computerized telescope designed specifically for deep space objects."
        eq2_t, eq2_d = "Meade LX200 14''", "A massive aperture professional observation tool for capturing the finest details of planets."
        eq3_t, eq3_d = "Lunt Solar Systems", "Specialized H-Alpha telescope allowing you to safely observe solar flares during daytime."

    st.write("---")
    col1, col2, col3 = st.columns(3)
    col1.metric(label=m1, value=m1_v, delta=m1_d)
    col2.metric(label=m2, value=m2_v, delta=m2_d)
    col3.metric(label=m3, value=m3_v, delta=m3_d, delta_color="off")
    st.write("---")
    st.markdown(f"<h3>{t_eq}</h3>", unsafe_allow_html=True)
    st.write("")
    
    e1, e2, e3 = st.columns(3)
    with e1: st.markdown(f"""<div class="service-card" style="box-shadow:none; border:none;"><img class="service-img" src="https://images.unsplash.com/photo-1517976487492-5750f3195933?q=80&w=800&auto=format&fit=crop" style="border-radius:8px; border: 1px solid #B8860B;"><div class="service-content" style="padding:15px;"><h3 class="service-title" style="font-size:1.1rem;">{eq1_t}</h3><p class="service-desc">{eq1_d}</p></div></div>""", unsafe_allow_html=True)
    with e2: st.markdown(f"""<div class="service-card" style="box-shadow:none; border:none;"><img class="service-img" src="https://images.unsplash.com/photo-1506443432602-ac2fcd6f54e0?q=80&w=800&auto=format&fit=crop" style="border-radius:8px; border: 1px solid #B8860B;"><div class="service-content" style="padding:15px;"><h3 class="service-title" style="font-size:1.1rem;">{eq2_t}</h3><p class="service-desc">{eq2_d}</p></div></div>""", unsafe_allow_html=True)
    with e3: st.markdown(f"""<div class="service-card" style="box-shadow:none; border:none;"><img class="service-img" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop" style="border-radius:8px; border: 1px solid #B8860B;"><div class="service-content" style="padding:15px;"><h3 class="service-title" style="font-size:1.1rem;">{eq3_t}</h3><p class="service-desc">{eq3_d}</p></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# SAYFA 6: DENEYİMLER & REZERVASYON
# ==============================================================================
elif menu_secimi in ["REZERVASYON", "BOOKING"]:
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
# SAYFA 7: DİJİTAL UZAY & YAPAY ZEKA SİMÜLASYONU
# ==============================================================================
elif menu_secimi in ["YAPAY ZEKA", "AI SIMULATOR"]:
    if lang == "TR":
        st.markdown("<h2>Yapay Zeka Destekli Derin Uzay Simülasyonu</h2>", unsafe_allow_html=True)
        st.markdown("<p>Gözlem saati gelene kadar kendi dijital galaksinizi tasarlayın. Simülasyon motorumuz parametrelerinizi işleyerek size özel kozmik yapıları görselleştirir.</p>", unsafe_allow_html=True)
        s_title, s_obj, s_color = "Simülasyon Parametreleri", "Gök Cismi Tipi", "Ana Renk Paleti"
        s_opts = ["Sarmal Galaksi", "Yıldız Doğumhanesi (Nebula)", "Süpernova Kalıntısı"]
        s_color_opts = ["Mistik Mor & Elektrik Mavisi", "Derin Kızıl & Altın", "Zümrüt Yeşili & Siyah"]
        s_btn, s_loading, s_success = "Simülasyonu Başlat (AI Engine)", "Sinir ağları üzerinden piksel verileri işleniyor...", "Simülasyon başarıyla tamamlandı."
    else:
        st.markdown("<h2>AI-Powered Deep Space Simulation</h2>", unsafe_allow_html=True)
        st.markdown("<p>Design your own digital galaxy while waiting for observation hours. Our simulation engine processes your parameters to visualize custom cosmic structures.</p>", unsafe_allow_html=True)
        s_title, s_obj, s_color = "Simulation Parameters", "Celestial Object Type", "Primary Color Palette"
        s_opts = ["Spiral Galaxy", "Stellar Nursery (Nebula)", "Supernova Remnant"]
        s_color_opts = ["Mystic Purple & Electric Blue", "Deep Crimson & Gold", "Emerald Green & Black"]
        s_btn, s_loading, s_success = "Run Simulation (AI Engine)", "Processing pixel data through neural networks...", "Simulation successfully completed."

    st.write("---")
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown(f"<h3>{s_title}</h3>", unsafe_allow_html=True)
        secilen_cisim = st.selectbox(s_obj, s_opts)
        secilen_renk = st.selectbox(s_color, s_color_opts)
        st.write("")
        if st.button(s_btn):
            with st.spinner(s_loading): time.sleep(3)
            st.success(s_success)
            st.write("---")
            if "Galaksi" in secilen_cisim or "Galaxy" in secilen_cisim: gen_img = "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=1200&auto=format&fit=crop"
            elif "Nebula" in secilen_cisim or "Doğumhanesi" in secilen_cisim: gen_img = "https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?q=80&w=1200&auto=format&fit=crop"
            else: gen_img = "https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?q=80&w=1200&auto=format&fit=crop"
            st.markdown(f'<div class="hero-container"><img class="hero-image" style="height:auto; filter: brightness(80%); border: 3px solid #D4AF37;" src="{gen_img}"></div>', unsafe_allow_html=True)

# ==============================================================================
# SAYFA 8: SÜRDÜRÜLEBİLİRLİK
# ==============================================================================
elif menu_secimi in ["SÜRDÜRÜLEBİLİRLİK", "SUSTAINABILITY"]:
    if lang == "TR":
        st.markdown("<h2>Sürdürülebilir Bilimsel Turizm</h2>", unsafe_allow_html=True)
        title, desc = "Doğaya ve Gökyüzüne Saygı", "Sürdürülebilirlik ilkelerimiz çevresel ve kültürel uyumu kapsar."
        ex1 = ("Işık Kirliliği Azaltımı", "Tesislerimizde yalnızca kırmızı bazlı, düşük lümenli zemin aydınlatmaları kullanılır.")
        ex2 = ("Sıfır Karbon Ayak İzi", "Turlarımızda tamamen sıfır emisyonlu elektrikli araçlar kullanılır.")
    else:
        st.markdown("<h2>Sustainable Scientific Tourism</h2>", unsafe_allow_html=True)
        title, desc = "Respect for Nature and the Sky", "Our sustainability principles cover environmental and cultural harmony."
        ex1 = ("Light Pollution Reduction", "Only red-based, low-lumen floor lighting is used in our facilities.")
        ex2 = ("Zero Carbon Footprint", "Our tours use completely zero-emission electric vehicles.")

    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 6, 1])
    with col_center:
        st.markdown('<div class="hero-container"><img class="hero-image" style="height:35vh;" src="https://images.unsplash.com/photo-1502481851512-e9e2529bfbf9?q=80&w=1200&auto=format&fit=crop"></div>', unsafe_allow_html=True)
        st.markdown(f"<h3>{title}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p>{desc}</p>", unsafe_allow_html=True)
        st.write("")
        with st.expander(ex1[0]): st.write(ex1[1])
        with st.expander(ex2[0]): st.write(ex2[1])

# ==============================================================================
# SAYFA 9: YATIRIMCI PORTALI
# ==============================================================================
elif menu_secimi in ["YATIRIMCI PORTALI", "INVESTOR PORTAL"]:
    if lang == "TR":
        st.markdown("<h2>Kurumsal İş Modeli & Gelecek Vizyonu</h2>", unsafe_allow_html=True)
        st.markdown("<p>Sadece yetkili erişim. (İpucu: stellaris2026)</p>", unsafe_allow_html=True)
        pw_label, msg_success, msg_error = "Kurumsal Şifre:", "Yönetici Paneline Erişim Sağlandı.", "Hatalı Şifre."
        t_vision, t_phases, t_chart = "5 Yıllık Büyüme Vizyonu", "Faz 2: İzlanda | Faz 3: Namibya", "Büyüme Projeksiyonu"
        d_cols = {"Şili": [1000, 2500, 4800, 7500, 12000], "Yeni Zelanda": [800, 1900, 3500, 6000, 9500]}
    else:
        st.markdown("<h2>Corporate Business Model & Future Vision</h2>", unsafe_allow_html=True)
        st.markdown("<p>Authorized access only. (Hint: stellaris2026)</p>", unsafe_allow_html=True)
        pw_label, msg_success, msg_error = "Corporate Password:", "Access Granted to Admin Panel.", "Incorrect Password."
        t_vision, t_phases, t_chart = "5-Year Growth Vision", "Phase 2: Iceland | Phase 3: Namibia", "Growth Projection"
        d_cols = {"Chile": [1000, 2500, 4800, 7500, 12000], "New Zealand": [800, 1900, 3500, 6000, 9500]}

    st.write("---")
    col_space1, col_center, col_space2 = st.columns([1, 4, 1])
    with col_center:
        sifre = st.text_input(pw_label, type="password")
        if sifre == "stellaris2026":
            st.success(msg_success)
            st.write("---")
            st.markdown(f"<h3>{t_vision}</h3>", unsafe_allow_html=True)
            st.info(t_phases)
            st.write("---")
            st.markdown(f"<h3>{t_chart}</h3>", unsafe_allow_html=True)
            st.area_chart(pd.DataFrame(d_cols, index=["Yıl 1", "Yıl 2", "Yıl 3", "Yıl 4", "Yıl 5"]), color=["#B8860B", "#C5A059"])
        elif sifre != "":
            st.error(msg_error)
