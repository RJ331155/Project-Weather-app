# 🌦️ SkyCast: Weather Intelligence System
### Class 12 Computer Science Project (083)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Database](https://img.shields.io/badge/Database-MySQL-orange.svg)](https://www.mysql.com/)
[![Framework](https://img.shields.io/badge/Framework-Tkinter-red.svg)](https://docs.python.org/3/library/tkinter.html)
[![Distribution](https://img.shields.io/badge/Build-Executable-green.svg)](https://pypi.org/project/auto-py-to-exe/)

---

## 📝 Project Details
- **Title:** Weather Monitoring System with Python-MySQL Connectivity
- **Developer:** R JAYAM
- **Subject:** Computer Science (Class XII)
- **Status:** Stable / Deployment Ready

---

## 🚀 Overview
**SkyCast** is a professional desktop application developed for the Class 12 Computer Science practical examination. It bridges the gap between a Python-based Graphical User Interface (GUI) and a MySQL backend, demonstrating how modern software handles live data from the internet and stores it locally for persistent record-keeping.



## ✨ Key Features
- 🌐 **Global Search:** Fetches real-time weather data (temperature, humidity, wind) via OpenWeatherMap API.
- 🗄️ **Data Persistence:** Automated search logging and history tracking using **MySQL Connector**.
- 📍 **Smart Geocoding:** Instant coordinate translation for any city using `geopy`.
- 🕒 **Timezone Aware:** Dynamic clock synchronization using `pytz` and `timezonefinder`.
- 📦 **Standalone App:** Packaged into a portable `.exe` file using `auto-py-to-exe` for zero-install deployment.

## 📦 Python Modules Used
| Module | Purpose |
| :--- | :--- |
| **mysql.connector** | Establishing Python-MySQL database connectivity. |
| **requests** | Fetching and parsing JSON data from REST APIs. |
| **geopy** | Performing geocoding for city coordinates. |
| **timezonefinder** | Finding local timezones based on coordinates. |
| **pytz** | Handling global time conversions. |
| **auto-py-to-exe** | Converting the Python script into a Windows Executable (.exe). |

## ⚙️ Setup and Installation

### 1. Prerequisites
* Python 3.x installed.
* MySQL Server installed and running.

### 2. Database Configuration
Ensure MySQL is running and create the necessary database. Update your connection credentials (host, user, password) in the Python script.
``` sql
CREATE DATABASE weather_db;
-- Create your tables as per the project documentation
```


###3. Installation
Clone the repository and install the required dependencies:
git clone [https://github.com/RJ331155/Project-Weather-app.git](https://github.com/RJ331155/Project-Weather-app.git)
`pip install <module_name>`


###4. Execution
To launch the application from the source code:
python 
`"WEATHER APP.py"`

The EXE 
`[🚀 Download Standalone EXE](https://github.com/RJ331155/Project-Weather-app/raw/main/WEATHER2APP/WEATHER%20APP.exe)`

##🖥️ Distribution
A standalone Windows version is provided in the repository. This allows the application to run as a .exe on any machine without requiring a Python installation, provided a MySQL server is accessible to the application.

Declaration: This project is original work developed for the fulfillment of the Class 12 Computer Science Practical curriculum.
