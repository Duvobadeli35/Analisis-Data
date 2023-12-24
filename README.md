## Analisis Data Rental Sepeda
# Setup Environment 

Upload data ke google drive
Buka Google Colab

masukkan kodingan dan sesuaikan dengan lokasi data di google drive :
from google.colab import drive #google colab mengimpor dari drive
drive.mount('/content/drive', force_remount=True)  #menghubungkan google colab ke drive
%cd /content/drive/My Drive/ColabNotebooks/AnalisisData/Bike-sharing-dataset
!ls #menampilkan daftar file dan direktori

# install streamlit
!pip install streamlit 


# Run Streamlit app
%%writefile dashboard.py
!streamlit run dashboard.py & npx localtunnel --port 8501
copy angka di external url selain port 8501
klik local tunnel 
masukkan endpoint dengan angka yang di copy
submit
