from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def draw_map():
    return "Hello World"