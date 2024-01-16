# import semua library yg dibutuhin
import streamlit as st
import pickle
import numpy as np

# coba load model yg suda dibuat
with open('model_uas.pkl', 'rb') as file:
    model = pickle.load(file)

# coba bukin fungsi untuk predict-nya
def predict_charges(age, bmi, children, smoker, region):
    input_data = np.array([[age, bmi, children, smoker, region]])
    prediction = model.predict(input_data)
    return prediction

# ini UI
def main():
    st.title("Prediksi Biaya Asuransi")

    # Input dari pengguna
    age = st.slider("Usia", min_value=18, max_value=64, value=25)
    bmi = st.number_input("BMI", min_value=15.0, max_value=50.0, value=25.0)
    children = st.slider("Jumlah Anak", min_value=0, max_value=5, value=0)
    smoker = st.selectbox("Perokok", ["Tidak", "Ya"])
    region = st.selectbox("Wilayah", ["Southeast", "Northwest", "Southwest", "Northeast"])

    # change inout jadi form yg bisa diterima model
    smoker = 1 if smoker == "Ya" else 0
    region_mapping = {"Southeast": 0, "Northwest": 1, "Southwest": 2, "Northeast": 3}
    region = region_mapping[region]

    # button submit for predict
    if st.button("Submit"):
        prediction = predict_charges(age, bmi, children, smoker, region)
        st.success(f"Prediksi Biaya Asuransi: ${prediction[0]:,.2f}")

    st.title("by Arya Adhari Prasetyo - 2020230001")

# Jalankan aplikasi
if __name__ == '__main__':
    main()



# UAS ini dibantu oleh ChatGPT dalam menggunakan model_uas.pkl ke dalam streamlitnya
# Arya Adhari Prasetyo - 2020230001