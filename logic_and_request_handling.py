import requests

username = input('Enter your username: ')
url = f"https://api.chess.com/pub/player/{username}/stats"

headers = {"User-Agent": "my-chess-app/1.0"}
response = requests.get(url, headers=headers)

data = response.json()

rapid = data.get("chess_rapid")
if rapid:
    rating = rapid["last"]["rating"]
    print("Rapid rating in chess.com:", rating)
    rapid_lichess = rating + 250
    print(f'Lichess rating: {rapid_lichess}')
    rapid_FIDE = rating + 150
    print(f'FIDE rating: {rapid_FIDE}')
    rapid_USCF = rapid_FIDE
    print(f'USCF rating: {rapid_USCF}')
else:
    print("No rapid games found for this user.")
