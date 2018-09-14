import folium
import pandas as pd
import os

os.chdir('/home/dmonty/PycharmProjects/udemy/webmap')

map = folium.Map(location=[28.228137, -82.716516], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="Dave's Map!")
fg.add_child(folium.Marker([28.228137, -82.716516], popup="I live here!", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker([29.928102, -81.435126], popup="Creta Massenge"))
fg.add_child(folium.Marker([27.7902203, -82.722427], popup="Carol Hixon"))
fg.add_child(folium.Marker([27.7902171, -82.7228409], popup="Robert White"))

data = pd.read_csv("Volcanoes_USA.txt")

lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])
print(elev)

def elev_clr(el):
    if el < 1000:
        return 'green'
    elif el < 3000:
        return 'orange'
    else:
        return 'red'

vols = folium.FeatureGroup(name="Volcanoes")
for lt, ln, elev in zip(lat, lon, elev):
    vols.add_child(folium.CircleMarker([lt, ln], popup=str(elev), radius=6, fill_color=elev_clr(elev),\
                                       color='grey', fill_opacity=0.7))
    # vols.add_child(folium.Marker([lt, ln], popup=str(elev), icon=folium.Icon(color=elev_clr(elev))))
#  use this to put strings in markers:  popup=folium.Popup(name, parse_html=True)

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 100000000
                            else 'orange' if 100000000 <= x['properties']['POP2005'] < 500000000 else 'red'}))

map.add_child((fg))
map.add_child(vols)
map.save("map1.html")

