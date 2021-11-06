import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 2000:
        return 'green'
    elif 2000 <= elevation < 3000:
        return 'blue'
    else:
        return 'red'
m=folium.Map(location=[38.58, -99.09],zoom_start = 7)
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius= 6, popup=str(el)+"m",
   fill_color=color_producer(el), color = 'gray', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'green' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


m.add_child(fgv)
m.add_child(fgp)
m.add_child(folium.LayerControl())
m.save("Maps1.html")





