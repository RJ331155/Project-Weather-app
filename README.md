# 🌦️ Weather Monitoring System (Class 12 CS Project)

A professional desktop application developed for the Class 12 Computer Science (083) practical examination. This project integrates real-time weather data fetching, database management, and standalone software distribution.

## 📝 Project Details
**Title:** Weather Monitoring System with Python-MySQL Connectivity and API Integration  
**Subject:** Computer Science (Class XII)  
**Developer:** R JAYAM  

---

## 🚀 Overview
This application provides a real-time weather dashboard. It bridges the gap between a Python-based Graphical User Interface (GUI) and a MySQL backend, demonstrating how modern software handles live data from the internet and stores it locally.

## 🛠️ Key Features
* **Live API Data:** Connects to OpenWeatherMap API to fetch temperature, humidity, and wind speed via the `requests` module.
* **Database Persistence:** Uses `mysql.connector` to manage backend data (search history and logs) for permanent storage.
* **Automated Geocoding:** Converts city names to precise coordinates using `geopy`.
* **Global Time Tracking:** Detects local time for any city worldwide using `timezonefinder` and `pytz`.
* **Standalone Executable:** Packaged into a portable `.exe` file using `auto-py-to-exe` for easy deployment on Windows machines.

## 📚 Technical Stack
| Category | Technology Used |
| :--- | :--- |
| **Language** | Python 3.x |
| **GUI Library** | Tkinter |
| **Database** | MySQL (Relational Database) |
| **APIs** | OpenWeatherMap REST API |
| **Distribution** | Auto-py-to-exe |

## 📦 Python Modules Used
* `mysql.connector`: To establish Python-MySQL connectivity.
* `requests`: To fetch and parse JSON data from the weather API.
* `geopy.geocoders`: To perform reverse geocoding for city coordinates.
* `timezonefinder`: To find the timezone of a specific location.
* `pytz`: To handle world clock conversions.
* `datetime`: To process and display system and local time.
* `auto-py-to-exe`: To convert scripts into a standalone application.

## ⚙️ Setup and Installation

### 1. Prerequisites
* Python 3.x installed.
* MySQL Server installed and running.

### 2. Database Configuration
Create the database and update the credentials in your script:
```sql
CREATE DATABASE weather_db;
-- Note: Ensure your table structure matches the code logic
