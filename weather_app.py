import requests


# API endpoints
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(city):
    try:
        # Step 1: Search for the city
        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            GEOCODING_URL,
            params=geo_params,
            timeout=10
        )

        geo_response.raise_for_status()

        geo_data = geo_response.json()

        # Check whether the city was found
        if "results" not in geo_data or not geo_data["results"]:
            print("\nCity not found. Please try another city.")
            return

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        country = location.get("country", "Unknown")

        # Step 2: Request weather data
        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "timezone": "auto"
        }

        weather_response = requests.get(
            WEATHER_URL,
            params=weather_params,
            timeout=10
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()

        # Step 3: Parse JSON response
        current = weather_data["current"]

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]

        # Step 4: Display filtered information
        print("\n" + "=" * 45)
        print("           WEATHER INFORMATION")
        print("=" * 45)

        print(f"Location     : {city_name}, {country}")
        print(f"Temperature  : {temperature} °C")
        print(f"Humidity     : {humidity}%")
        print(f"Wind Speed   : {wind_speed} km/h")

        print("=" * 45)

    except requests.exceptions.Timeout:
        print("\nError: The API request timed out.")

    except requests.exceptions.RequestException as error:
        print(f"\nAPI request failed: {error}")

    except (KeyError, TypeError, ValueError):
        print("\nError: Unexpected data received from the API.")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


def main():
    print("=" * 45)
    print("        PYTHON WEATHER APPLICATION")
    print("=" * 45)

    city = input("Enter city name: ").strip()

    if not city:
        print("Please enter a city name.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()