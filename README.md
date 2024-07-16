# Weather API Python Program
This Python program allows you to check weather information via the command line interface (CLI) using the OpenWeatherMap API.

### Installation
1. Clone the repository:
  ```python
    cd your_repository 
    git clone https://github.com/sylviezhang37/weather-api.git
  ```
  
2. Get your personal API from [OpenWeatherMap](https://openweathermap.org/api). You'll need it for
  ```python
    // in api.py, replace "config.API_KEY" with your API key or create a config.py to store it securely.
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{country}&appid={config.API_KEY}&mode=xml'

    // rest of the program
  ```
  
3. Run the program in the CLI
  ```python
    python3 your_repository/main.py
  ```

4. Follow the prompt to get weather data!

   ![Screenshot 2024-07-15 at 9 38 27 PM](https://github.com/user-attachments/assets/23905046-7752-4c61-8312-0641ccf02e4d)
