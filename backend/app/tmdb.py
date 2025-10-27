import requests, os

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def get_movie_details(tmdb_id: int):
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={TMDB_API_KEY}&language=de-DE"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    return {
        "title": data["title"],
        "year": data["release_date"].split("-")[0],
        "description": data["overview"],
        "poster_url": f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    }
