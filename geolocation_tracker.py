import requests
import folium
import webbrowser
import csv

#Making a GET request to the ipify API
#response = requests.get("https://api.ipify.org?format=json")

#Parse the JSON and extract the IP
#data = response.json()
#ip = data["ip"]
ip_list = input("Enter your IP Addresses separated with a comma(,): ").split(",")
ip_list = [ip.strip() for ip in ip_list]
print("Your public IP Addresses are: ", ip_list)

#Create an empty list to store the IP Addresses from the user
locations = []

#Building an API URL by inserting my IP Address
for ip in ip_list:
    geo_url = f"http://ip-api.com/json/{ip}"
    #make another GET requests to that URL
    geo_response = requests.get(geo_url)
    #Parse the JSON response
    geo_data = geo_response.json()
    #Extract city, regionName, country, lat, lon, isp
    location = {
        "ip": ip,
        "city": geo_data["city"],
        "regionName": geo_data["regionName"],
        "country": geo_data["country"],
        "latitude": float(geo_data["lat"]),
        "longitude": geo_data["lon"],
        "isp": geo_data["isp"]
        }
    locations.append(location)
    
    print(f"Located: {ip} -> {geo_data['city']}, {geo_data['country']}")


first = locations[0]
my_map = folium.Map(location=[first["latitude"], first["longitude"]], zoom_start=4)

#Loop to loop on all locations and create a mark with a different colour for all of them
for loc in locations:
    popup_text = f"IP: {loc['ip']}\nCity: {loc['city']}\nRegion: {loc['regionName']}\nCountry: {loc['country']}\nISP: {loc['isp']}"
    folium.Marker(
    location=[loc["latitude"], loc["longitude"]],
    popup=popup_text,
    tooltip=loc["city"],
    icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(my_map)
    with open("heo_results.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "City", "Region", "Country", "Latitude", "Longitude", "ISP"])
        writer.writerow([loc["ip"], loc["city"], loc["regionName"], loc["country"], loc["latitude"], loc["longitude"], loc["isp"]])
#Save and auto open the map
my_map.save("geo_map.html")
webbrowser.open("geo_map.html")
print("map saved and opened!")

''''
print("\nCity: ", city)
print("Region: ", regionName)
print("Country: ", country)
print("Latitude: ", latitude)
print("Longitude: ", longitude)
print("ISP: ", isp)

#Create a Map


#Save the map as an HTML
my_map.save("geo_map.html")


#Build a popup message from the extracted fields


#Create marker and add it on the map


#Save the map
my_map.save("geo_map.html")
print("Saved to geo_map.html you can open!!!")
webbrowser.open("geo_map.html")
'''
