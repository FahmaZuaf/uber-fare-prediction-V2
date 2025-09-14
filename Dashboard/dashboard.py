import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os
import requests

# === BASE DIR & LOGO ===
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
logo_path = os.path.join(BASE_DIR, "Images", "logo.jpg")

# === PAGE CONFIG ===
st.set_page_config(
    page_title="Uber Fare Predictor",
    page_icon=logo_path,
    layout="centered"
)

# === TITLE & DESCRIPTION ===
st.title("Uber Fare Predictor")
st.markdown(
    "Prediksi biaya perjalanan Uber berdasarkan **jarak, jumlah penumpang, jam, hari, dan bulan**."
)

# === LOAD MODEL & SCALER ===
model_path = os.path.join(BASE_DIR, "models", "uber_fare_model.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")

# Jika ingin sepenuhnya aman, re-train model di versi scikit-learn saat ini
# model = train_model() -> joblib.dump(model, model_path)
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# === AMBIL KURS REAL-TIME ===
@st.cache_data(ttl=3600)
def get_currency_rates(base="USD"):
    url = f"https://open.er-api.com/v6/latest/{base}"
    try:
        response = requests.get(url)
        data = response.json()
        if data["result"] == "success":
            rates = {
                "IDR (Rp)": data["rates"]["IDR"],
                "JPY (¥)": data["rates"]["JPY"],
                "KRW (₩)": data["rates"]["KRW"],
                "SGD ($)": data["rates"]["SGD"],
                "CNY (¥)": data["rates"]["CNY"]
            }
            return rates
        else:
            st.warning("Gagal mengambil kurs, gunakan default statis.")
            return {
                "IDR (Rp)": 16000,
                "JPY (¥)": 145,
                "KRW (₩)": 1300,
                "SGD ($)": 1.35,
                "CNY (¥)": 7.3
            }
    except Exception as e:
        st.warning(f"Error saat mengambil kurs: {e}. Gunakan default statis.")
        return {
            "IDR (Rp)": 16000,
            "JPY (¥)": 145,
            "KRW (₩)": 1300,
            "SGD ($)": 1.35,
            "CNY (¥)": 7.3
        }

currency_rates = get_currency_rates()

# === FORM SINGLE TRIP ===
st.subheader("🔹 Prediksi Single Trip")
with st.form("fare_form"):
    col1, col2 = st.columns(2)
    with col1:
        distance = st.number_input("📏 Jarak (km)", min_value=0.0, step=0.1, format="%.2f")
        passenger = st.number_input("👥 Jumlah Penumpang", min_value=1, max_value=6, value=1)
    with col2:
        hour = st.slider("⏰ Jam Keberangkatan", 0, 23, 12)
        day = st.selectbox(
            "📅 Hari (0=Senin ... 6=Minggu)",
            options=[0, 1, 2, 3, 4, 5, 6],
            format_func=lambda x: ["Sen","Sel","Rab","Kam","Jum","Sab","Min"][x]
        )
        month = st.slider("🗓️ Bulan", 1, 12, 6)

    selected_currency = st.selectbox("💱 Pilih Mata Uang", options=list(currency_rates.keys()))
    submitted = st.form_submit_button("🔮 Prediksi Tarif")

if submitted:
    try:
        # Buat DataFrame agar sesuai feature names
        features = pd.DataFrame(
            [[distance, passenger, hour, day, month]],
            columns=["distance", "passenger_count", "hour", "day", "month"]
        )
        scaled = scaler.transform(features)
        fare_usd = model.predict(scaled)[0]

        rate = currency_rates[selected_currency]
        fare_converted = fare_usd * rate

        st.success(f"💰 Estimasi Tarif: **${fare_usd:.2f} USD** → **{fare_converted:,.2f} {selected_currency}**")
        st.balloons()
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")

# === BATCH PREDICTION ===
st.subheader("📂 Batch Prediction (Upload CSV)")
uploaded_file = st.file_uploader(
    "Upload file CSV dengan kolom: distance, passenger_count, hour, day, month",
    type="csv"
)

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        required_cols = ["distance", "passenger_count", "hour", "day", "month"]
        if all(col in data.columns for col in required_cols):
            df_input = data[required_cols].copy()  # pastikan DataFrame
            scaled = scaler.transform(df_input)
            data["Fare_USD"] = model.predict(scaled)

            rate = currency_rates[selected_currency]
            data[f"Fare_{selected_currency}"] = data["Fare_USD"] * rate

            st.success("✅ Prediksi berhasil dilakukan!")
            st.dataframe(data)

            csv_download = data.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download Hasil Prediksi", csv_download, "predictions.csv", "text/csv")
        else:
            st.error(f"⚠️ CSV harus memiliki kolom: {required_cols}")
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")

# === FOOTER ===
st.markdown("---")
st.caption("© 2025 Fahma Zuaf Zarir - All Rights Reserved.")
st.markdown(
    "Project ini dibuat untuk tujuan edukasi dan demonstrasi. "
    "Data dan model yang digunakan mungkin tidak mencerminkan kondisi nyata.")