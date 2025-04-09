import streamlit as st
import pandas as pd
import joblib

model = joblib.load("mobile_price_model.pkl")

st.title("📱 Prédiction de la gamme de prix d'un téléphone")

# Sliders / Inputs pour les 20 features
battery_power = st.slider("🔋 Batterie (mAh)", 500, 2000)
blue = st.radio("🔵 Bluetooth", [0, 1])
clock_speed = st.slider("⏱️ Vitesse CPU (GHz)", 0.5, 3.0, step=0.1)
dual_sim = st.radio("📶 Dual SIM", [0, 1])
fc = st.slider("📷 Caméra frontale (Mpx)", 0, 20)
four_g = st.radio("📡 4G", [0, 1])
int_memory = st.slider("💾 Mémoire interne (Go)", 2, 64)
m_dep = st.slider("📏 Épaisseur mobile (cm)", 0.1, 1.0, step=0.1)
mobile_wt = st.slider("⚖️ Poids du mobile (g)", 80, 250)
n_cores = st.slider("🧠 Nombre de cœurs CPU", 1, 8)
pc = st.slider("📸 Caméra principale (Mpx)", 0, 20)
px_height = st.slider("📐 Hauteur écran (px)", 0, 2000)
px_width = st.slider("📏 Largeur écran (px)", 0, 2000)
ram = st.slider("🧠 RAM (Mo)", 256, 4000, step=128)
sc_h = st.slider("📲 Hauteur écran (cm)", 5, 20)
sc_w = st.slider("📲 Largeur écran (cm)", 0, 20)
talk_time = st.slider("🔋 Autonomie appel (h)", 2, 20)
three_g = st.radio("📶 3G", [0, 1])
touch_screen = st.radio("👆 Écran tactile", [0, 1])
wifi = st.radio("📶 WiFi", [0, 1])

# Mettre toutes les données dans un DataFrame
input_data = pd.DataFrame([{
    'battery_power': battery_power,
    'blue': blue,
    'clock_speed': clock_speed,
    'dual_sim': dual_sim,
    'fc': fc,
    'four_g': four_g,
    'int_memory': int_memory,
    'm_dep': m_dep,
    'mobile_wt': mobile_wt,
    'n_cores': n_cores,
    'pc': pc,
    'px_height': px_height,
    'px_width': px_width,
    'ram': ram,
    'sc_h': sc_h,
    'sc_w': sc_w,
    'talk_time': talk_time,
    'three_g': three_g,
    'touch_screen': touch_screen,
    'wifi': wifi
}])

# Prédiction
if st.button("🎯 Prédire la gamme de prix"):
    prediction = model.predict(input_data)[0]
    gammes = ["📉 Bas de gamme", "📈 Moyenne gamme", "📊 Haut de gamme", "💎 Premium"]
    st.success(f"Résultat : {gammes[prediction]}")
