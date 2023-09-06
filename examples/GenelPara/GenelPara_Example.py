# This code is written to show use case of GenelPara API. When the code runs it will print the prices and changes with color.
# Bu kod GenelPara API kullanımını göstermek için yazılmıştır. Kod çalıştığında fiyatları ve değişimleri renkli olarak basacaktır

# Import necessary libraries. Gerekli kütüphaneleri içe aktarın.
import requests # Used for HTTP requests. HTTP istekleri için kullanılır.

# Define the URL. URL'yi belirle.
url = "https://api.genelpara.com/embed/altin.json"

# Make the GET request. GET isteğini gerçekleştir.
response = requests.get(url)

# If the request is successful do this. Sonuç başarılıysa bunu yap.
try:
    # Parse the JSON response. JSON yanıtını ayrıştır.
    data = response.json()

    # Define colors for positive and negative values. Pozitif ve negatif değerler için renkleri tanımla.
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m' 

    # Loop through the currency data. Para birimi verileri arasında dolaş.
    for currency, info in data.items():
        alis = info["alis"]
        satis = info["satis"]
        degisim = float(info["degisim"])

        # Determine the color for degisim (change). Değişim için rengi ayarla.
        color = GREEN if degisim >= 0 else RED

        # Print the info with color. Bilgileri renkli olarak bastır
        print(f"{currency} alış: {alis}")
        print(f"{currency} satiş: {satis}")
        print(f"{currency} değişim: {color}{degisim}{RESET}\n")

# If the request fails then return an error message. İstek başarısız olursa hata mesajı döndür.
except Exception as e:
    print("Hata:",e,"\n","Lütfen daha sonra tekrar deneyiniz.")
