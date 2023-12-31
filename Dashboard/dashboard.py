# -*- coding: utf-8 -*-
"""dashboard

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1526rN_j_uPwUVQEcwM8sJc6ltuACRJam

# Proyek Analisis Data: Bike-sharing-dataset
- **Nama:** Muhammad David Ubaidillah
- **Email:** mdavidulearning@gmail.com
- **ID Dicoding:** muhammad_david_ubaid

## Menentukan Pertanyaan Bisnis

- bagaimana tingkat kelembapan udara mempengaruhi penyewa pada saat rentang hari kerja?
- Season berapa rental sepeda yang paling banyak dan paling sedikit tersewa pada rentang hari kerja?

## Import Semua Packages/Library yang Digunakan
"""

# Commented out IPython magic to ensure Python compatibility.

from google.colab import drive #google colab mengimpor dari drive
drive.mount('/content/drive', force_remount=True) #menghubungkan google colab ke drive
# %cd /content/drive/My Drive/ColabNotebooks/AnalisisData/Bike-sharing-dataset
!ls#menampilkan daftar file dan direktori

#install streamlit
!pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
#impor future
from __future__ import print_function, division

#menggunakan matplotlip untuk bisa menampilkan visual kedalam ennvironment jupyter notebook dan python
# %matplotlib inline
import numpy as np #mengimpor lib numpy
import pandas as pd #impor lib panda
import seaborn as sns #impor lib seaborn
import matplotlib.pyplot as plt #impor lib matplotlib.pyplot
import streamlit as st #impor lib streamlit
from babel.numbers import format_currency #impor lib babel.numbers

"""## Data Wrangling

### Gathering Data
"""

#membaca file menggunakan pandas as pd dan disimpan pada day
day = pd.read_csv('day.csv')
day

#memilih kolom yang ingin ditampilkan
d = day[['weekday']]
f = day[['hum']]
s = day[['season']]

"""### Assessing Data"""

#menampilkan informasi tentang DataFrame
d.info()

#menampilkan informasi tentang DataFrame
f.info()

#menampilkan informasi tentang DataFrame
s.info()

day.isnull().sum()

day.isna().sum()

print("Jumlah duplikasi: ", day.duplicated().sum())

d.describe()

f.describe()

s.describe()

"""### Cleaning Data"""

day.drop_duplicates(inplace=True)

print("Jumlah duplikasi: ", day.duplicated().sum())

"""## Exploratory Data Analysis (EDA)

### Explore ...
"""

d.hist()

f.hist()

s.hist()

d.corr()

f.corr()

s.corr()

"""## Visualization & Explanatory Analysis

### Pertanyaan 1:
"""

plt.scatter(x=d, y=f)

sum_hum_items_df = day.groupby("weekday").hum.sum().sort_values(ascending=False).reset_index()
sum_hum_items_df

"""### Pertanyaan 2:"""

day.groupby("season").weekday.sum().sort_values(ascending=False).reset_index()

from matplotlib import pyplot as plt
_df_2.plot(kind='scatter', x='season', y='weekday', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

"""## Conclusion

- Kelembapan udara sangat mempengaruhi orang untuk melakukan aktivitas bersepeda dengan menyewa sepeda. Keadaan kelembapan udara berkisar antara 0.4 - 0.8 di rentang hari kerja orang seringkali menyewa sepeda untuk melakukan aktivitas bersepeda.
- Keadaan musim mempengaruhi orang untuk melakukan aktivitas bersepeda. Musim ke-3 adalah musim yang paling ramai orang menyewa sepeda untuk melakukan aktivitas bersepeda, sedangkan musim ke-4 adalah musim yang paling sepi orang menyewa sepeda.

##Dashboard di streamlit
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile dashboard.py
# #import library
# import streamlit as st
# 
# import numpy as np #mengimpor lib numpy
# import pandas as pd #impor lib panda
# import seaborn as sns
# import matplotlib.pyplot as plt
# import streamlit as st
# from babel.numbers import format_currency
# 
# #membaca file dengan pandas
# day = pd.read_csv('day.csv')
# 
# #memberikan judul
# st.header('Analisis Data rental sepeda')
# st.header('link gdrive [disini](https://drive.google.com/drive/folders/1kwyj_Joqy2J4278ZbzssHbAyUqGw79Gg?usp=sharing)')
# st.subheader('Pertanyaan bisnis rental sepeda')
# st.text('1. bagaimana tingkat kelembapan udara mempengaruhi penyewa pada saat rentang hari kerja?')
# st.text('2. Season berapa rental sepeda yang paling banyak dan paling sedikit tersewa pada rentang hari kerja?')
# 
# #membuat sidebar untuk registrasi penyewaan
# with st.sidebar:
# 
#     st.text('Registrasi Sewa Sepeda')
#     st.write('silahkan masukkan data diri anda')
#     st.text_input('Nama Anda')
#     st.number_input('umur anda')
#     st.text_area('Alamat anda')
#     st.date_input('tanggal lahir anda')
#     st.time_input('waktu anda sekarang')
#     st.file_uploader('foto wajah anda')
# 
# #definisikan order by hum
# def create_sum_hum_items_df(df):
#     sum_hum_items_df = day.groupby("weekday").hum.sum().sort_values(ascending=False).reset_index()
#     sum_hum_items_df
#     return sum_hum_items_df
# 
# #definisikan order by season
# def create_sum_order_items_df(df):
#     sum_order_items_df = day.groupby("season").weekday.sum().sort_values(ascending=False).reset_index()
#     sum_order_items_df
#     return sum_order_items_df
# 
# #definisi variabel
# main_df = day.groupby("season").weekday.sum().sort_values(ascending=False).reset_index()
# hum_df = day.groupby("weekday").hum.sum().sort_values(ascending=False).reset_index()
# sum_order_items_df = create_sum_order_items_df(main_df)
# sum_hum_items_df = create_sum_hum_items_df(hum_df)
# 
# 
# #membuat sebuah gambar dan sumbu
# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
# 
# #definisikan colors yang digunakan
# colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
# 
# #membuat tabs:
# tab1, tab2 = st.tabs(["kelembapan udara", "musim"])
# tab1.write("Tabel data kelembapan udara di hari kerja")
# tab2.write("Tabel data penyewa rentang hari kerja di berbagai musim")
# 
# # mengisi tabs 1:
# with tab1:
# 
#   def create_sum_hum_items_df(df):
#     sum_hum_items_df = day.groupby("weekday").hum.sum().sort_values(ascending=False).reset_index()
#     sum_hum_items_df
#     return sum_hum_items_df
# 
#   #menampilkan tabel penyewaan dengan kelembapan udara
#   st.text('tabel kelembapan udara dan penyewaan sepeda pada saat rentang hari kerja')
#   st.table(sum_hum_items_df.iloc[0:10])
# 
#   sns.barplot(x="weekday", y="hum", data=sum_hum_items_df.sort_values(by="hum", ascending=True).head(10), palette=colors, ax=ax[1])
#   ax[1].set_ylabel(None)
#   ax[1].set_xlabel("kelembapan udara", fontsize=30)
#   ax[1].invert_xaxis()
#   ax[1].yaxis.set_label_position("right")
#   ax[1].yaxis.tick_right()
#   ax[1].set_title("Jumlah penyewa dengan kelembapan udara pada hari kerja", loc="center", fontsize=50)
#   ax[1].tick_params(axis='y', labelsize=35)
#   ax[1].tick_params(axis='x', labelsize=30)
# 
#   st.pyplot(fig)
# 
# #mengisi tabs 2
# with tab2:
# 
#   def create_sum_order_items_df(df):
#     sum_order_items_df = day.groupby("season").weekday.sum().sort_values(ascending=False).reset_index()
#     sum_order_items_df
#     return sum_order_items_df
# 
# 
#   #menampilkan tabel penyewaan dengan season
#   st.text('Tabel Season dan penyewaan sepeda pada rentang hari kerja')
#   st.table(sum_order_items_df.iloc[0:10])
# 
#   #membuat barplot penyewaan dengan season
#   sns.barplot(x="season", y="weekday", data=sum_order_items_df.sort_values(by="weekday", ascending=True).head(5), palette=colors, ax=ax[1])
#   ax[1].set_ylabel(None)
#   ax[1].set_xlabel("musim", fontsize=30)
#   ax[1].invert_xaxis()
#   ax[1].yaxis.set_label_position("right")
#   ax[1].yaxis.tick_right()
#   ax[1].set_title("Jumlah penyewa di setiap musim pada hari kerja", loc="center", fontsize=50)
#   ax[1].tick_params(axis='y', labelsize=35)
#   ax[1].tick_params(axis='x', labelsize=30)
# 
#   st.pyplot(fig)
# 
# st.header(' Kesimpulan :  ')
# st.subheader('1. Kelembapan udara sangat mempengaruhi orang untuk melakukan aktivitas bersepeda dengan menyewa sepeda. Keadaan kelembapan udara berkisar antara 0.4 - 0.8 di rentang hari kerja orang seringkali menyewa sepeda untuk melakukan aktivitas bersepeda. ')
# st.subheader('2. Keadaan musim mempengaruhi orang untuk melakukan aktivitas bersepeda. Musim ke-3 adalah musim yang paling ramai orang menyewa sepeda untuk melakukan aktivitas bersepeda, sedangkan musim ke-4 adalah musim yang paling sepi orang menyewa sepeda.')
#

!streamlit run dashboard.py & npx localtunnel --port 8501