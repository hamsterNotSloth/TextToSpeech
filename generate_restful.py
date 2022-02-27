from argparse import Namespace
from flask import Flask,jsonify
from generate import initializeTextPRompt, runBotArtist


app = Flask(__name__)

@app.route('/abc')
def index():
    args = Namespace()
    textPrompt = "Painting of an apple"
    initializeTextPRompt(textPrompt)
    generateObj = runBotArtist()
    return "leaning python"

if __name__ == "__main__":
    app.run(debug=True)