# Python Weather API

A Python application that fetches real-time weather information using public APIs.

## Project Overview

This project demonstrates API integration using Python and the `requests` module. 
The user enters a city name, and the application searches for the city and retrieves current weather information.

## Features

- Search weather by city name
- Uses the Python `requests` module
- Parses JSON API responses
- Displays temperature, humidity, and wind speed
- Handles invalid city names
- Handles API and network errors
- Uses a virtual environment for project dependencies

## Technologies Used

- Python 3
- Requests
- Open-Meteo Geocoding API
- Open-Meteo Weather API

## How It Works

```text
User enters city
       ↓
Geocoding API
       ↓
Latitude & Longitude
       ↓
Weather API
       ↓
JSON Response
       ↓
Extract weather data
       ↓
Display result


Save with **Ctrl + S**.

---

# Step 2 — Check your project

You should now have:

```text
Python-Weather-API/
│
├── .gitignore
├── README.md
├── requirements.txt
└── weather_app.py