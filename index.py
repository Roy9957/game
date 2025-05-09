from flask import Flask, send_from_directory, redirect

app = Flask(__name__, static_folder='../public')

@app.route('/')
def root():
    # Redirect to /starting
    return redirect('/starting')

@app.route('/starting')
def starting():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/lobby')
def lobby():
    return send_from_directory(app.static_folder, 'lobby.html')

@app.route('/training')
def training():
    return send_from_directory(app.static_folder, 'train.html')

@app.route('/play')
def play():
    return send_from_directory(app.static_folder, 'game.html')

@app.route('/share')
def share():
    return send_from_directory(app.static_folder, 'share.html')

