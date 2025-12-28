# 🌦️ Weather Application (Class 12 CS Project)

A comprehensive Python desktop application developed as a Computer Science project. The app fetches real-time weather data and utilizes MySQL for backend data management, demonstrating Python-MySQL connectivity.

## 📝 Project Overview
This project aims to provide users with accurate weather information including temperature, humidity, and wind speed for any location worldwide. It integrates external APIs with a graphical user interface and a relational database.

## 🛠️ Key Features
* **Live API Integration:** Uses `requests` to fetch data from OpenWeatherMap.
* **Database Management:** Uses `mysql.connector` to store and retrieve data (e.g., search logs/user data).
* **Automatic Geocoding:** Uses `geopy` to convert city names into coordinates.
* **Timezone Handling:** Automatically detects the local time of the searched city using `timezonefinder`.
* **User-Friendly GUI:** Built using Python's `tkinter` library.

## 📚 Modules Used
| Module | Purpose |
| :--- | :--- |
| **Tkinter** | Creating the Graphical User Interface. |
| **MySQL Connector** | Connecting Python with the MySQL database. |
| **Requests** | Fetching data from the Weather API. |
| **Geopy** | Converting location names to Lat/Long coordinates. |
| **Pytz / Timezonefinder** | Managing and displaying local time zones. |

## ⚙️ Prerequisites & Setup
1. **MySQL Server:** Ensure you have MySQL installed and running.
2. **Table Setup:** Create the database and tables as specified in the project documentation.
3. **Libraries:** Install required libraries using:
   ```bash
   pip install requests mysql-connector-python pytz timezonefinder geopy
