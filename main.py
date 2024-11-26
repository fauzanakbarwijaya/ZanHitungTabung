# IMPORT EXPORT
from functions import function

# MAIN PROGRAM
jari_jari = int(input("Masukkan Jari Jari Tabung: "))
tinggi = int(input("Masukkan Tinggi Tabung: "))
print(function.hitungVolumeTabung(jari_jari,tinggi))

# # IMPORT STREAMLIT
# import streamlit as st
# from functions import function  

# # JUDUL APLIKASI
# st.title("Kalkulator Volume Tabung")

# # INPUT DATA
# jari_jari = st.number_input("Masukkan Jari-jari Tabung:", min_value=0.0, format="%.2f")
# tinggi = st.number_input("Masukkan Tinggi Tabung:", min_value=0.0, format="%.2f")

# # TOMBOL HITUNG
# if st.button("Hitung Volume"):
#     if jari_jari > 0 and tinggi > 0:
#         # Menghitung volume tabung
#         volume = function.hitungVolumeTabung(jari_jari, tinggi)
#         st.success(f"Volume Tabung: {volume:.2f} satuan kubik")
#     else:
#         st.error("Jari-jari dan tinggi harus lebih besar dari nol!")
