from setup import MTKIPA
from setup import KIMIPA
from setup import FISIPA
from setup import MTKIPS
from setup import INDOIPS
from setup import ENGIPS
from setup import EKOIPS
import pickle
import pandas as pd 
import streamlit as st

# ------------------Prepocessing Data IPA ---------------------
model = pickle.load(open('model_ipa.pkl', 'rb'))
df_rec = pd.read_csv("D:\magangaku\Project_Rekomendasi_SNBP\stream\datafiks.csv")
df_rec = df_rec[['ProgramStudi','TipeStudi']]
df_rec.drop_duplicates(inplace=True)
def Recommender(X):
    a = df_rec[df_rec['TipeStudi']==X].values
    b = a[:,0]
    st.write(f'Rekomendasi Jurusan: {b}', end='')

# ------------------Prepocessing Data IPS ---------------------
model_IPS = pickle.load(open('model_ips.pkl', 'rb'))
df_rec_IPS = pd.read_csv("D:\magangaku\Project_Rekomendasi_SNBP\stream\datafiks.csv")
df_rec_IPS = df_rec[['ProgramStudi','TipeStudi']]
df_rec_IPS.drop_duplicates(inplace=True)
def Recommender_IPS(X):
    a_ips = df_rec[df_rec_IPS['TipeStudi']==X].values
    b_ips = a_ips[:,0]
    st.write(f'Rekomendasi Jurusan: {b_ips}', end='')

#-------------------Interface Streamlit-----------------"""
side = st.sidebar.radio("Menu",["Sistem Rekomendasi IPA", "Sistem Rekomendasi IPS"])

if side == "Sistem Rekomendasi IPA":     
    st.title('Selamat Datang di Laman Sistem Rekomendasi Program Studi Untuk IPA')
    mtk = st.number_input('Masukkan Nilai Rata-Rata Matematika Wajib Kamu')
    ind = st.number_input('Masukkan Nilai Rata-Rata Bahasa Indonesia Kamu')
    eng = st.number_input('Masukkan Nilai Rata-Rata Bahasa Inggris Kamu')
    bio = st.number_input('Masukkan Nilai Rata-Rata Biologi Kamu')
    kim = st.number_input('Masukkan Nilai Rata-Rata Kimia Kamu')
    fis = st.number_input('Masukkan Nilai Rata-Rata Fisika Kamu')
    MTK_IPA = MTKIPA(mtk)
    Indo_IPA = MTKIPA(ind)
    Eng_IPA = MTKIPA(eng)
    Biologi_IPA = MTKIPA(bio)
    Kimia_IPA = KIMIPA(kim)
    Fisika_IPA = FISIPA(fis)

    # initialize list of lists
    data = [[MTK_IPA,Indo_IPA,Eng_IPA,Biologi_IPA,Kimia_IPA,Fisika_IPA]]
  
    # Create the pandas DataFrame
    New_Data = pd.DataFrame(data, columns=['MTK_IPA','Indo_IPA','Eng_IPA','Biologi_IPA','Kimia_IPA','Fisika_IPA'])

    if st.button('Rekomendasi Program Studi'):
        Prediction = model.predict(New_Data)
        pred = Prediction
        rec_str = pred.item()[:]
        st.write('Program Studi Yang Direkomendasikan: ')
        st.write(rec_str)
        print("\n")
        rec = Recommender(rec_str)

if side == "Sistem Rekomendasi IPS":     
    st.title('Selamat Datang di Laman Sistem Rekomendasi Program Studi Untuk IPS')
    mtk = st.number_input('Masukkan Nilai Rata-Rata Matematika Wajib Kamu')
    ind = st.number_input('Masukkan Nilai Rata-Rata Bahasa Indonesia Kamu')
    eng = st.number_input('Masukkan Nilai Rata-Rata Bahasa Inggris Kamu')
    sos = st.number_input('Masukkan Nilai Rata-Rata Sosiologi Kamu')
    geo = st.number_input('Masukkan Nilai Rata-Rata Geografi Kamu')
    eko = st.number_input('Masukkan Nilai Rata-Rata Ekonomi Kamu')
    MTK_IPS = MTKIPS(mtk)
    Indo_IPS = INDOIPS(ind)
    Eng_IPS = ENGIPS(eng)
    Sosiologi_IPS = ENGIPS(sos)
    Geografi_IPS = ENGIPS(geo)
    Ekonomi_IPS = EKOIPS(eko)

    # initialize list of lists
    data = [[MTK_IPS,Indo_IPS,Eng_IPS,Sosiologi_IPS,Geografi_IPS,Ekonomi_IPS]]
  
    # Create the pandas DataFrame
    New_Data = pd.DataFrame(data, columns=['MTK_IPA','Indo_IPA','Eng_IPA','Sosiologi_IPS','Geografi_IPS','Ekonomi_IPS'])

    if st.button('Rekomendasi Program Studi'):
        Prediction_IPS = model_IPS.predict(New_Data)
        pred_IPS = Prediction_IPS
        rec_str_IPS = pred_IPS.item()[:]
        st.write('Program Studi Yang Direkomendasikan: ')
        st.write(rec_str_IPS)
        print("\n")
        rec = Recommender_IPS(rec_str_IPS)




