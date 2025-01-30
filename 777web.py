import streamlit as st
st.title("web data diri")
name = st.text_input("Masukkan nama anda: ")
age = st.slider("Masukkan usia anda: ", 0, 100, 19)
st.write(f"Usia anda adalah {age} tahun.")
occupation = st.selectbox("Pilih pekerjaan anda: ", ["Pelajar", "Pekerja", "Wirausaha", "Lainnya"])
st.write(f"Pekerjaan anda adalah {occupation}.")
if st.button("Submit"):
    st.write(f"Selamat datang, {name}!")
    
