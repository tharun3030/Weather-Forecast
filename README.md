# Weather Forecast App

This is a simple and visually appealing *Weather Forecast App* built using Python and the Tkinter library. The app fetches real-time weather data from the *OpenWeatherMap API* and displays the current weather conditions, temperature, humidity, wind speed, and other details for a specified city. Users can switch between Celsius and Fahrenheit units and see a weather icon representing the current condition.

# Features

- *Real-time Weather Data*: Fetches live weather data for any city in the world using the OpenWeatherMap API.
- *Temperature Unit Toggle*: Users can switch between Celsius and Fahrenheit with a single button click.
- *Weather Icons*: Displays an appropriate weather icon based on the current weather condition (e.g., sunny, rainy, cloudy).
- *Sunrise and Sunset Times*: Shows the local time for sunrise and sunset in a human-readable format.
- *Attractive UI*: Includes a customizable background image, styled text, and buttons for a clean and modern look.

# Installation

# Prerequisites
- Python 3.x
- requests library
- Pillow library (for image handling)
- OpenWeatherMap API key (free to obtain at https://openweathermap.org/api)

# Libraries
Install the required Python libraries using pip:

bash
pip install requests pillow


# Setup

1. Clone this repository:

   bash
   git clone https://github.com/your-username/weather-forecast-app.git
   

2. Navigate to the project directory:

   bash
   cd weather-forecast-app
   

3. Place your background image file (e.g., background.jpg) in the project directory. You can either use your own image or comment out the background section in the code if you prefer a simple background.

4. Replace the placeholder with your OpenWeatherMap API key:

   python
   api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=YOUR_API_KEY"
   

# Usage

Run the weather_forecast.py script:

bash
python weather_forecast.py


1. Enter the name of the city in the input field.
2. Press Enter or click on *Get Weather* to fetch weather data.
3. View the current weather, temperature, and other details.
4. Click *Switch to Fahrenheit* to toggle between Celsius and Fahrenheit.

# Technologies Used

- *Python*: Core language used for building the app.
- *Tkinter*: Python's built-in library for creating the GUI.
- *Pillow*: Used for handling and displaying images such as weather icons and backgrounds.
- *OpenWeatherMap API*: Provides real-time weather data.

# Customization

You can customize the following parts of the app:
- *Background Image*: Replace the background image (background.jpg) with your own.
- *Fonts and Colors*: Modify the font styles and colors in the code to match your aesthetic preferences.
- *Icons*: You can further enhance the app by displaying more icons or adding animations.

