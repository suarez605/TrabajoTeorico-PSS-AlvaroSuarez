from flask import Flask
from flask import render_template
import pandas as pd 
import os
import folium
from folium.plugins import HeatMap

app = Flask(__name__)


@app.route('/Bye')
def draw_map():
    return "Bye"


@app.route('/drawMap')
def draw_map():
    map_data = pd.read_csv("./Data/data_01.csv", sep=';')
    lat = map_data['LATITUD'].mean()
    lom = map_data['LONGITUD'].mean()
    startingLocation = [lat, lom]#[39.47, -0.37]
    hmap = folium.Map(location=startingLocation, zoom_start=15)
    max_amount = map_data['RelacionPrecioTamanio'].max()
    hm_wide = HeatMap( list(zip(map_data.LATITUD.values, map_data.LONGITUD.values, map_data.RelacionPrecioTamanio.values)),
                        min_opacity=0.2,
                        max_val=max_amount,
                        radius=17, blur=15,
                        max_zoom=1)

    # Adds the heatmap element to the map
    hmap.add_child(hm_wide)
    # Saves the map to heatmap.hmtl
    hmap.save(os.path.join('./templates', 'heatmap.html'))
    #Render the heatmap
    return render_template('heatmap.html')

if __name__ == "__main__":
    app.run(debug=True)