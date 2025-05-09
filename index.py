from flask import Flask, send_from_directory, redirect
import os

app = Flask(__name__)

# Directory where the HTML files are located (same as this script)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def root():
    # Redirect to /starting
    return redirect('/starting')

@app.route('/starting')
def starting():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/lobby')
def lobby():
    return send_from_directory(BASE_DIR, 'lobby.html')

@app.route('/training')
def training():
    return send_from_directory(BASE_DIR, 'train.html')

@app.route('/play')
def play():
    return send_from_directory(BASE_DIR, 'game.html')

@app.route('/share')
def share():
    return send_from_directory(BASE_DIR, 'share.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

