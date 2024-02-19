from django.shortcuts import render
import folium
# Create your views here.
def index(request):
 m = folium.Map(location=[10.97797,  76.18307], zoom_start=13)

# Add a marker to the map
 folium.Marker([10.97797,  76.18307], popup='Your Location').add_to(m)

# Save the map to an HTML file
 m.save('index.html')
 return render(request, 'index.html')

def map_view(request):
     map_width = 800
     map_height = 700
     m = folium.Map(location=[11.1112,  76.1784], zoom_start=13,width=map_width, height=map_height)
     folium.Marker([11.1112,  76.1784], popup='Malapuram').add_to(m)

     map_html = m._repr_html_()

     return render(request, 'map.html', {'map_html': map_html})