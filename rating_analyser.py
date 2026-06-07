from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ratings = None
    error = None

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        if username:
            url = f"https://api.chess.com/pub/player/{username}/stats"
            headers = {"User-Agent": "my-chess-app/1.0"}
            try:
                response = requests.get(url, headers=headers, timeout=10)
                data = response.json()
                rapid = data.get("chess_rapid")
                if rapid:
                    chesscom = rapid["last"]["rating"]
                    ratings = {
                        "username": username,
                        "chesscom": chesscom,
                        "lichess": chesscom + 250,
                        "fide": chesscom + 150,
                        "uscf": chesscom + 150,
                    }
                else:
                    error = f"No rapid games found for '{username}'."
            except Exception:
                error = "Could not reach Chess.com. Check the username and try again."
        else:
            error = "Please enter a username."

    return render_template('index.html', ratings=ratings, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
