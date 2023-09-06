# This code is written to show use case of NVI KPS API. When the code runs it will get necessary citizenship input then authenticate the details. 
# Bu kod NVI KPS API kullanımını göstermek için yazılmıştır. Kod çalıştığında vatandaşlıkla ilgili gerekli girdileri alıp, detayları doğrulatacaktır.

# Import necessary libraries. Gerekli kütüphaneleri içe aktarın.
import requests # Used for HTTP requests. HTTP istekleri için kullanılır.
import xml.etree.ElementTree as ET # Used for XML parsing. XML ayrıştırması için kullanılır.

# Input data. Verileri gir.
tc_no = input("TC Kimlik No: ")
ad = input("Ad: ")
soyad = input("Soyad: ")
yil = input("Dogum Yili: ")

# Define the SOAP request. SOAP isteğini tanımla.
soap_request = f"""<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
      <TCKimlikNo>{tc_no}</TCKimlikNo>
      <Ad>{ad}</Ad>
      <Soyad>{soyad}</Soyad>
      <DogumYili>{yil}</DogumYili>
    </TCKimlikNoDogrula>
  </soap12:Body>
</soap12:Envelope>"""

# Set the headers for the request. İsteğin header'larını tanımla.
headers = {
    "Content-Type": "application/soap+xml; charset=utf-8",
}

# URL of the SOAP service. SOAP hizmetinin URL'si.
url = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx"

# Send the SOAP request. SOAP isteğini gönder
response = requests.post(url, data=soap_request, headers=headers)

# Parse the SOAP response. SOAP yanıtını ayrıştır.
root = ET.fromstring(response.content)

# Find and extract the value of TCKimlikNoDogrulaResult. TCKimlikNoDogrulaResult değerini bul ve çıkart.
result_element = root.find(".//{http://tckimlik.nvi.gov.tr/WS}TCKimlikNoDogrulaResult")
result = result_element.text if result_element is not None else None

# Check the result and print an appropriate message. Sonucu kontrol et ve uygun bir mesaj yazdır
if result == "true":
    print("Girilen bilgiler doğrudur.")
else:
    print("Girilen bilgiler yanlıştır")
