# HexSoftware_Geolocation_Tracker
This is a geolocation tracker which uses IP Addresses from the user and it can also track multiple IP Addresses  at the same time and display all of them on map. 

# 🌍 Geolocation Tracker

A Python-based geolocation tracker that uses IP addresses to pinpoint locations on an interactive map. Built step by step as a learning project.

---

## 📋 Table of Contents

- [What is Geolocation?](#what-is-geolocation)
- [Features](#features)
- [Project Structure](#project-structure)
- [Libraries Used](#libraries-used)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [How It Works](#how-it-works)
- [Output](#output)
- [What I Learned](#what-i-learned)
- [Future Features](#future-features)

---

## 🧠 What is Geolocation?

Geolocation is the process of identifying the real-world geographic location of a device connected to the internet using its **IP address**. It returns data such as:

- Country, Region, City
- Latitude & Longitude coordinates
- Timezone
- ISP (Internet Service Provider)

---

## ✅ Features

- 🌐 Automatically fetches your **public IP address**
- 🔍 Tracks **any IP address** entered by the user
- 🗺️ Plots **multiple IP addresses** on a single interactive map
- 📍 Displays a **marker pin** with location details (city, region, country, ISP)
- 💾 **Saves results** to a CSV file automatically
- 🚀 **Auto opens** the map in your browser

---

## 📁 Project Structure

```
geolocation-tracker/
│
├── geo_tracker.py       # Main Python script
├── geo_map.html         # Generated interactive map (auto created)
├── geo_results.csv      # Saved location results (auto created)
└── README.md            # Project documentation
```

---

## 🛠️ Libraries Used

| Library | Purpose | Install |
|---|---|---|
| `requests` | Makes HTTP calls to geolocation APIs | `pip install requests` |
| `folium` | Generates interactive HTML maps | `pip install folium` |
| `csv` | Saves location data to CSV files | Built-in |
| `webbrowser` | Auto opens the map in browser | Built-in |

---

## ⚙️ Installation

1. Make sure you have **Python 3** installed
2. Install the required libraries:

```bash
pip install requests folium
```

3. Clone or download the project files into a folder

---

## ▶️ How to Run

```bash
python geo_tracker.py
```

You will be prompted to enter one or more IP addresses separated by commas:

```
Enter IP addresses separated by a comma: 8.8.8.8, 1.1.1.1
```

The map will automatically open in your browser!

---

## ⚙️ How It Works

### Step 1 — Fetch Public IP
```python
response = requests.get("https://api.ipify.org?format=json")
ip = response.json()["ip"]
```

### Step 2 — Call Geolocation API
```python
geo_url = f"http://ip-api.com/json/{ip}"
geo_data = requests.get(geo_url).json()
```

### Step 3 — Extract Location Fields
```python
city    = geo_data["city"]
region  = geo_data["regionName"]
country = geo_data["country"]
lat     = geo_data["lat"]
lon     = geo_data["lon"]
isp     = geo_data["isp"]
```

### Step 4 — Build the Map
```python
my_map = folium.Map(location=[lat, lon], zoom_start=12)
```

### Step 5 — Add Marker Pin
```python
folium.Marker(
    location=[lat, lon],
    popup=popup_text,
    tooltip="Click to see location info",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(my_map)
```

### Step 6 — Save and Open
```python
my_map.save("geo_map.html")
webbrowser.open("geo_map.html")
```

---

## 📊 Output

### Interactive Map (`geo_map.html`)
- Opens automatically in your browser
- Shows red marker pins for each tracked IP
- Click a pin to see city, region, country and ISP info

### CSV File (`geo_results.csv`)
| IP | City | Region | Country | Latitude | Longitude | ISP |
|---|---|---|---|---|---|---|
| 8.8.8.8 | Mountain View | California | United States | 37.386 | -122.0838 | Google LLC |

---

## 🧠 What I Learned

- Making **API calls** with `requests`
- Parsing **JSON responses**
- Building **dynamic URLs** with f-strings
- Working with **Python dictionaries**
- Using **for loops** to process multiple items
- Creating **interactive maps** with `folium`
- Saving data to **CSV files**
- Using **built-in Python modules** like `webbrowser` and `csv`
- **Debugging** real errors by reading tracebacks

---

## 🚀 Future Features

- 🤖 AI-powered **Predictive Location Services**
- 🎨 Different **pin colors** per country
- 🗺️ **Lines connecting** all pins on the map
- 🖥️ Simple **GUI** using `tkinter`
- 📄 Export report as **PDF**

---

## 👨‍💻 Built By

Built step by step as a Python learning project — from understanding APIs to plotting interactive maps!
