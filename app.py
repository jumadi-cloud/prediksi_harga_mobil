import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="App Prediksi Harga Mobil",
    page_icon="👋",
)

# Navigasi
with st.sidebar:
        selected = option_menu(
             menu_title="Pilih Menu", 
             options=["Prediksi", "test"], 
             icons=['house', "list-task"], 
             menu_icon="cast", 
             default_index=0,
             )
if selected == "Prediksi":
    # Judul Aplikasi
    st.title('Prediksi Harga Mobil Bekas')      

    # Load model
    model = pickle.load(open('model harga mobil.sav', 'rb'))

    # Input Fitur
    tahun = st.number_input('Input Tahun Mobil', min_value=2005, max_value=2025, step=1)
    km_clean = st.number_input('Input Kilometer Mobil (km)', min_value=0)   
    brand = st.number_input('Input Kode Brand Mobil', min_value=0, max_value=26, step=1)
    with st.expander("**klik untuk melihat daftar kode Brand Mobil**"):
        st.write(""" Audi: 0, BMW: 1, BYD: 2, Chery: 3, Chevrolet: 4, Daihatsu: 5, Datsun: 6,
        Ferrari: 7, Ford: 8, GWM: 9, Honda: 10, Hyundai: 11, Jeep: 12, KIA: 13,
        Land: 14, Lexus: 15, MG: 16, MINI: 17, Mazda: 18, Mercedes-Benz: 19,
        Mitsubishi: 20, Nissan: 21, Peugeot: 22, Porsche: 23, Suzuki: 24,
        Toyota: 25, Wuling: 26
        """)
    trans = st.number_input('Input Transmisi (Automatic: 0 Manual: 1)', min_value=0, max_value=1, step=1 )

    # Tombol Prediksi

    if st.button('Prediksi Harga'):
        input_data = np.array([[tahun, km_clean, brand, trans]])
        prediction = model.predict(input_data)

        # Konversi ke Rupiah
        kurs_eur_to_idr = 10  # Bisa disesuaikan
        harga_rupiah = prediction[0] * kurs_eur_to_idr
        st.success(f'Prediksi harga mobil bekas: Rp {harga_rupiah:,.0f}')


if selected == "test":
     st.title('Pengembangan')
