from django.shortcuts import render
import requests
from .models import Suggested_Places, Hotels, Booking

# Create your views here.

API_KEY = "YOUR_API_KEY"

def calculate_distance(hotels, pickup):
    Distance=[]
    Hotel=[]
    pickup = pickup.replace(' ', "%20")
    pickup = pickup.replace(',', "%2C")
    url1 = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="
    url2 = pickup
    url3 = "&destinations="
    url4=""
    for hotel in hotels:
        Hotel.append(hotel)     
        address = hotel.address.replace(' ', "%20")
        address = address.replace(',', "%2C")
        url4 = url4 + address + "|"
    url4=url4.rstrip(url4[-1])
    url5 = "&units=imperial&key="
    url=url1+url2+url3+url4+url5+API_KEY
    print(url)
    output=requests.get(url).json()
    for data in output['rows'][0]['elements']:
        Distance.append(data['distance']['text'])
    return tuple(zip(Distance, Hotel))
    

def home(request):
    suggested = Suggested_Places.objects.all()
    return render(request, 'home.html', {'suggested': suggested})

def places(request):
    pickup = request.GET['Pickup']
    pickup_city = request.GET['static']
    hotels = Hotels.objects.filter(located=pickup_city).all()
    print(pickup)
    params = {
        'key': API_KEY,
        'address': pickup
    }
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params).json()
    response.keys()
    if response['status']=='OK':
        geometry = response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']
        print(lat, lon)
    Dis_Hotel = calculate_distance(hotels, pickup)
    return render(request, 'places.html', {'lat': lat, 'lon':lon, 'hotels':hotels, 'first':hotels[0], 'dis_hotel': Dis_Hotel})

def pickup(request):
    name=request.GET['place']
    image=request.GET['image']
    return render(request, 'pickup.html', {'name':name, 'image': image})