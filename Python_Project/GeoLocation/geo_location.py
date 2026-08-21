import geocoder,folium

ip = geocoder.ip("me")  # Here "me" takes the current ip address
address = ip.latlng # here latlng is latitude and longitude
mymap = folium.Map(location=address,zoom_start=12)
folium.Circle(address,radius=500).add_to(mymap)
mymap.save("mymap1.html")



