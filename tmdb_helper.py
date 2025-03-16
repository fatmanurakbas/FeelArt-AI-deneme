import requests

API_KEY = "8b4971cb8bd025e788420cabfc29ef"
BASE_URL = "https://api.themoviedb.org/3"

def get_popular_movies():
    """Popüler filmleri TMDB API'den çeker."""
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Hata:", response.status_code, response.text)
        return None

