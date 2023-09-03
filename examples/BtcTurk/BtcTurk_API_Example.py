# This code is written to show use case of BTC Turk's API. When the code runs it will print the price of USD TRY every second. 
# Bu kod BTC Turk'ün API kullanımını göstermek için yazılmıştır. Kod çalıştığında her saniye USD TRY fiyatını basacaktır.

# Import necessary libraries. Gerekli kütüphaneleri içe aktarın.
import requests # Used for HTTP requests. HTTP istekleri için kullanılır.
import time # Used for time related functions. Zamanla ilgili fonksiyonlarda kullanılır.

# Assign the url as BTC Turk's API. url'yi BTC Turk'ün API'si olarak ata.
url="https://api.btcturk.com/api/v2/ticker"

# Set an infinite loop. Sonsuz bir döngü oluştur.
while (1):
    # Send a GET request to the url. url'ye GET isteği ata.
    response=requests.get(url)

    # Parse the JSON response into a Python dict. JSON yanıtını bir Python sözlüğüne ayrıştır.
    dt=response.json()

    # Create an empty dictionary. Boş bir sözlük oluştur.
    data={}

    # Specify currency pair that we are interested in. İlgimizi çeken para çiftimizi ayarla.
    data['pair']='USDTTRY'

    # Iterate through received data. Gelen veri içerisinde dolaş.
    for i in range(0,len(dt['data'])):
        if dt['data'][i]['pair']==data['pair']:
                dataindex=i
          
    # Extract and store relevant information. İlgili bilgileri çıkar ve depola.
    data['denominatorSymbol']=dt["data"][dataindex]["denominatorSymbol"]     
    data['numeratorSymbol']=dt["data"][dataindex]["numeratorSymbol"]
    data['last']=dt["data"][dataindex]["last"]

    # Print the currency pair name and latest price. Para çiftinin adını ve son fiyatı bastır.
    print(""+data['numeratorSymbol']+" / "+data['denominatorSymbol']+" = "+str(data['last'])+"\n")

   # Wait 1 second. 1 saniye bekle.
    time.sleep(1)

# For further details visit: https://docs.btcturk.com/
# Daha fazla bilgi için: https://docs.btcturk.com/
 
