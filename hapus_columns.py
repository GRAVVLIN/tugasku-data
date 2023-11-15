import streamlit as st
import pandas as pd

# Menambahkan widget untuk memilih file CSV
uploaded_file = st.file_uploader("Pilih File CSV", type=["csv"])

if uploaded_file is not None:
    # Membaca data dari file CSV yang diunggah
    df = pd.read_csv(uploaded_file)

    # Menampilkan DataFrame sebelum penghapusan kolom
    st.write("DataFrame Sebelum Penghapusan Kolom:")
    st.write(df)

    # Memilih kolom yang akan dihapus
    kolom_yang_dihapus = st.multiselect('Pilih Kolom yang Akan Dihapus', df.columns)

    # Menghapus kolom yang dipilih jika ada yang dipilih
    if kolom_yang_dihapus:
        df = df.drop(kolom_yang_dihapus, axis=1)

    # Menampilkan DataFrame setelah penghapusan kolom
    st.write("\nDataFrame Setelah Penghapusan Kolom:")
    st.write(df)
else:
    st.warning("Silakan pilih file CSV untuk melanjutkan.")
