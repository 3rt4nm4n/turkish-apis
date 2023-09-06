# This code is written to show use case of SPK (Capital Markets Board) API. When the code runs it will return the list of publicly traded companies and their locations. 
# Bu kod SPK (Sermaye Piyasası Kurulu) API kullanımını göstermek için yazılmıştır. Kod çalıştığında halka açık borsada işlem gören şirket listesini ve adreslerini döndürür.

# Import necessary libraries. Gerekli kütüphaneleri içe aktarın.
import requests # Used for HTTP requests. HTTP istekleri için kullanılır.

# Define the URL. URL'yi belirle.
url = "https://ws.spk.gov.tr/HalkaAcikSirket/api/Sirketler/Borsa"

# Make the GET request. GET isteğini gerçekleştir.
response = requests.get(url)

# Parse the JSON response. JSON yanıtını ayrıştır.
data = response.json()

# Loop through the publicly traded companies data. Halka Açık borsada işlem gören şirket verileri arasında dolaş.
for info in data:
    # Print company name and city address. Şirket adı ve il adresini yazdır.
    print(info["unvani"])
    print(info["adresIl"])
    print("\n") 
