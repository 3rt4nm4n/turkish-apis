# This code is written to show use case of Tuzla Municipality API. When the code runs it will print a table about annual water consumption in Tuzla for the last 5 years.
# Bu kod Tuzla Belediyesi'nin API kullanımını göstermek için yazılmıştır. Kod çalıştığında Tuzla'da son 5 yıldaki yıllık su tüketimini bir tablo halinde basacaktır.

# Import necessary libraries. Gerekli kütüphaneleri içe aktarın.
import requests # Used for HTTP requests. HTTP istekleri için kullanılır.
import pandas as pd # Used to work with datasets. Veri setleri ile çalışmak için kullanılır.

# Assign the url as Tuzla Municipality API's endpoint. url'yi Tuzla Belediyesi'nin API bağlantı ucu olarak ata.
url = 'https://veri.tuzla.bel.tr/api/3/action/datastore_search?resource_id=39667e59-7874-455e-9c19-c9acb605b0b1&limit=5'  

# Send a GET request to the specified URL. Belirlenen URL'ye GET isteği gönder.
response = requests.get(url)

# Parse the JSON response. JSON yanıtını ayrıştır.
data = response.json()

# Extract the 'records' part of the response. Yanıtın 'records' (kayıtlar) kısmını çıkar.
records = data.get('result').get('records')

# Create a DataFrame from the extracted records. Çıkarılan kayıtlardan bir DataFrame oluştur.
df = pd.DataFrame(records)

# Print the DataFrame. DataFrame'i yazdır.
print(df)

# Expected Output/Beklenen Çıktı:
#   _id   YIL TUKETIM MIKTARI
#0    1  2022      24.758.012
#1    2  2021      32.598.699
#2    3  2020      20.495.275
#3    4  2019      16.936.290
#4    5  2018      14.956.036

# For further details visit: https://veri.tuzla.bel.tr/dataset/
# Daha fazla bilgi için: https://veri.tuzla.bel.tr/dataset/