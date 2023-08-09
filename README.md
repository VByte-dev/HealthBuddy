# HealthBuddy

HealthBuddy is a web application built using Flask that allows users to retrieve nutrition information for various food items using an external API. Users can enter a food item's name as a query, and the application will display its nutritional details.

## Getting Started

To run this application on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/VByte-dev/your-repo.git
   ```

2. Install the required dependencies:
   ```bash
   pip install Flask requests
   ```

3. Replace the `api_key` in the `app.py` file with your actual API key.

4. Start the Flask application:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Features

- Enter a food item's name in the search box to retrieve its nutrition information.
- Displays nutritional details such as calories, serving size, fat content, protein, sodium, potassium, cholesterol, carbohydrates, fiber, and sugar.

## Technologies Used

- Flask: A micro web framework for Python.
- Requests: A Python library for making HTTP requests to external APIs.

## API Usage

This application uses the Nutrition API provided by API Ninjas to retrieve nutrition information for food items. You can find more information about their API [here](https://api.api-ninjas.com/docs/nutrition).
