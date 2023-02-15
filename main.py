import streamlit as st


st.title('Penjumlahan')

bil1 = st.number_input('Masukkan angka pertama')
bil2 = st.number_input('Masukkan angka kedua')

hitung = st.button('Hitung')

if hitung:
    hasil = bil1 + bil2
    st.success(f'Hasil: {hasil}')
