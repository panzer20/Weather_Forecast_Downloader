## Project name: Weather Forecast Downloader

A simple command-line Python program that fetches and displays the current weather forecast for a given location. This project is an improved version of an example from the book *Automate the Boring Stuff with Python* (Polish Edition, 2017) by Albert Sweigart.

## About

The program demonstrates how to:
- Read user input from command-line arguments
- Send HTTP requests to a public API
- Parse JSON data
- Display selected weather information in a user-friendly format

This repository was created as part of my learning journey in Python programming. It shows that I understand how the original solution works and how to enhance it. Publishing this project is part of building a portfolio to demonstrate my progress and understanding of real-world Python applications.

## Features

- Accepts a city name as a command-line argument
- Connects to the [OpenWeatherMap](https://openweathermap.org/) API
- Retrieves current weather data in JSON format
- Displays the weather conditions and temperature for the selected location

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)
- An API key from [OpenWeatherMap](https://openweathermap.org/)

## Getting Started

1. Clone this repository or download the `weather.py` script.
2. Install required Python packages if you haven't already:

   ```
   pip install requests
   ```

3. Create an account at [OpenWeatherMap](https://openweathermap.org/) and generate your free API key.
4. Open the `weather.py` file and replace the `api_key` variable with your personal key:

   ```
   api_key = 'YOUR_API_KEY'
   ```

5. Run the program from the command line, providing the city as an argument:

   ```
   python weather.py Warsaw
   ```
   
## Example Output

```
Weather for: Warsaw
Clear - clear sky
Temperature: 18.5°C
```

## Notes

- Make sure you enter a valid city name when calling the script.
- This program only retrieves weather data for the current day.
- Error handling is basic; future improvements could include better user feedback and input validation.

## License

This project is released under the MIT License.
