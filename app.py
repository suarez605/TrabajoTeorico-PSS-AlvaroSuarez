from flask import Flask
from flask import render_template
import pandas as pd 
import os
import folium
from folium.plugins import HeatMap

app = Flask(__name__)


@app.route('/hello')
def draw_map():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)