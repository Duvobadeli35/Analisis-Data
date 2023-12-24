## Analisis Data Rental Sepeda
# Setup Environment 
```
Upload data ke google drive
Buka Google Colab

masukkan kodingan dan sesuaikan dengan lokasi data di google drive :
from google.colab import drive #google colab mengimpor dari drive
drive.mount('/content/drive', force_remount=True)  #menghubungkan google colab ke drive
%cd /content/drive/My Drive/ColabNotebooks/AnalisisData/Bike-sharing-dataset
!ls #menampilkan daftar file dan direktori

link gooogle drive ('https://drive.google.com/drive/folders/1kwyj_Joqy2J4278ZbzssHbAyUqGw79Gg?usp=sharing')
atau
bisa lihat di dashboard.py bagian streamlit
```
# install streamlit
```
!pip install streamlit 
#import library
import streamlit as st

import numpy as np #mengimpor lib numpy
import pandas as pd #impor lib panda
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from babel.numbers import format_currency
```
# Run Streamlit app
```
%%writefile dashboard.py
!streamlit run dashboard.py & npx localtunnel --port 8501
copy angka di external url selain port 8501
klik URL
masukkan endpoint IP dengan angka yang di copy
submit
```
