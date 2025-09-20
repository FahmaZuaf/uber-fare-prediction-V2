# 🚖 Uber Fare Predictor

Prediksi biaya perjalanan Uber secara cepat dan interaktif menggunakan **Python**, **Streamlit**, dan **Machine Learning**.  
Project ini memungkinkan prediksi **tarif tunggal (single trip)** maupun **batch prediction** dari file CSV. Selain itu, hasil prediksi dapat dikonversi ke berbagai mata uang real-time (IDR, JPY, KRW, SGD, CNY).

---

## 🛠️ Fitur

- Prediksi tarif Uber berdasarkan:
  - Jarak perjalanan (km)
  - Jumlah penumpang
  - Jam keberangkatan
  - Hari dalam minggu
  - Bulan
- Batch prediction: upload CSV untuk prediksi banyak perjalanan sekaligus
- Konversi tarif ke berbagai mata uang secara real-time
- UI interaktif menggunakan Streamlit
- Export hasil prediksi ke CSV
- Responsif dan ramah untuk semua perangkat

---

## 🌐 Sumber Dataset

Dataset diambil dari [Kaggle: Uber Fares Dataset](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)

Dataset ini berisi informasi tentang perjalanan Uber termasuk lokasi penjemputan, timestamp, dan jumlah tarif. Fitur-fitur yang ada meliputi:

- `fare_amount`: Variabel target (kontinu) yang menunjukkan tarif dalam USD
- `pickup_datetime`: Timestamp penjemputan
- `pickup_longitude`: Koordinat bujur lokasi penjemputan
- `pickup_latitude`: Koordinat lintang lokasi penjemputan
- `dropoff_longitude`: Koordinat bujur lokasi pengantaran
- `dropoff_latitude`: Koordinat lintang lokasi pengantaran
- `passenger_count`: Jumlah penumpang dalam kendaraan

> Catatan: Dalam aplikasi Streamlit ini, **latitude dan longitude tidak digunakan**, hanya jarak, jumlah penumpang, waktu, hari, dan bulan.

---

## 📂 Struktur Project

Uber Fare Prediction/

├─ Dashboard/

│ └─ dashboard.py # Streamlit app

├─ models/

│ ├─ uber_fare_model.pkl

│ └─ scaler.pkl

├─ Images/

│ └─ logo.jpg

├─ data/

│ └─ uber.csv

├─ notebooks/

│ └─ uber-fare-predict.ipynb

├─ requirements.txt

└─ README.md

---

## ⚙️ Instalasi

1. Clone repository:

```bash
git clone https://github.com/FahmaZuaf/uber-fare-prediction-V2.git
cd "Uber Fare Prediction"
```

2. Buat virtual environment (opsional tapi direkomendasikan):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependency:

```bash
pip install -r requirements.txt
```

---

🚀 Menjalankan Aplikasi

```bash
streamlit run Dashboard/dashboard.py
```

Aplikasi akan terbuka di browser default atau menggunakan URL yang ditampilkan di terminal.

---

💻 Contoh Penggunaan

- Single Trip Prediction

Masukkan jarak, jumlah penumpang, jam, hari, dan bulan → klik Prediksi Tarif → hasil muncul dalam USD atau mata uang pilihan.

- Batch Prediction

Upload CSV dengan kolom: distance, passenger, hour, day, month → klik Prediksi → hasil ditampilkan dan bisa di-download.

---

🌐 Konversi Mata Uang

Aplikasi mendukung konversi ke:

- IDR (Rupiah)

- JPY (Yen Jepang)

- KRW (Won Korea)

- SGD (Dollar Singapura)

- CNY (Yuan Tiongkok)

Kurs diambil secara real-time menggunakan API.

---

⚡ Lisensi

© 2025 Fahma Zuaf Zarir - All Rights Reserved.


Selamat Mencoba >_<
