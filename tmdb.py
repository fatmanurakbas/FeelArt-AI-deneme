import requests

API_KEY = "8b4971cb8bd025e788420cabcfc29efb"
url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1"

response = requests.get(url)

if response.status_code == 200:
    print(response.json())  # API'den gelen veriyi yazdır
else:
    print("Hata:", response.status_code, response.text)

