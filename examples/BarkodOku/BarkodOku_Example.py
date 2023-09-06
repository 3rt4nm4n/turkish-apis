# This code is written to show use case of BarkodOku API. In this example BarkodGetir function is used. When the code runs it will check the barcode and print name of the product. 
# Bu kod BarkodOku API kullanımını göstermek için yazılmıştır. Bu örnekte BarkodGetir fonksiyonu kullanılmıştır. Kod çalıştığında barkodu kontrol edip ürünün adını yazacaktır.

# Import necessary libraries. Gerekli kütüphaneleri içe aktarın.
import requests # Used for HTTP requests. HTTP istekleri için kullanılır.
import xml.etree.ElementTree as ET # Used for XML parsing. XML ayrıştırması için kullanılır.

# Define the URL and API key. URL ve API anahtarını belirle.
url = "https://www.barkodoku.com/ws/BarkodServis.asmx"
api_key = "API_KEY_HERE"

# Define the barcode you want to query. Aratmak istediğin barkodu tanımla.
barcode_example = "8690565100530"

# Create the SOAP request. SOAP isteğini yarat.
soap_request = f"""<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <BarkodGetir xmlns="http://barkodoku.com/">
      <apiKey>{api_key}</apiKey>
      <barkod>{barcode_example}</barkod>
    </BarkodGetir>
  </soap12:Body>
</soap12:Envelope>"""

# Define the headers. Header'ları tanımla
headers = {
    "Content-Type": "application/soap+xml; charset=utf-8",
}

# Make the SOAP request. SOAP isteğini gerçekleştir.
response = requests.post(url=url, data=soap_request, headers=headers)
# If the request is successful do this. Sonuç başarılıysa bunu yap.
try:
  # Parse the SOAP response. SOAP yanıtını ayrıştır
  root = ET.fromstring(response.content)

  # Extract the relevant data from the response. Yanıtta istediğin verileri çıkart.
  urun_barkod = root.find(".//{http://barkodoku.com/}UrunBarkod/{http://barkodoku.com/}UrunBarkod").text
  urun_ad = root.find(".//{http://barkodoku.com/}UrunBarkod/{http://barkodoku.com/}UrunAd").text

  # Print product barcode and name. Ürün barkodu ve adını bastır.
  print(f"UrunBarkod: {urun_barkod}")
  print(f"UrunAd: {urun_ad}")

# If the request was not successful return an error message. Eğer istek başarılı değilse hata mesajı döndür
except Exception as e:
  print(f"Request failed: {e}")
