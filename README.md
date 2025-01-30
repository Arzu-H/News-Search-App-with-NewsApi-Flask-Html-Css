# News Search API Project

This is a simple project that uses the [News API](https://newsapi.org/) to fetch and display news articles based on user-provided keywords. The project allows users to search for news articles, view relevant news, and interact with a basic web interface built with **Flask**.

## Features

- Search for news articles by keyword.
- Display up to 10 articles per search (based on the News API's response).
- Built using **Flask** for the web server and **HTML/CSS** for the front-end.
  
## Requirements

To run the project locally, you need to have the following installed:

- Python 3.x
- Flask
- Requests

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

You will also need to create a News API account to get an API key.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/news-search-api.git
   cd news-search-api
   ```

2. **Create a `config.py` file**:
   Create a file named `config.py` in the project root directory and add your **News API key**:

   ```python
   NEWS_API_KEY = 'your_api_key_here'
   ```

3. **Run the app**:
   Start the Flask application by running the following command:

   ```bash
   python app.py
   ```

   This will start the web server locally, and you can visit `http://127.0.0.1:5000/` in your web browser.

## How it works

- **User Input**: The user enters a keyword in the search bar on the webpage.
- **API Request**: The app sends a request to the News API with the provided keyword.
- **Results**: The app displays the top 10 articles related to the keyword (if available).
  
## Project Structure

```
news-search-api/
├── app.py             # Flask web server and route handling
├── config.py          # Contains the API key for News API
├── templates/
│   └── index.html     # HTML page for displaying the search form and news results
└── static/
    └── styles.css     # Simple styling for the frontend
```

### Notes

- This is a **simple project** to demonstrate using News API with Flask.
- The project only shows up to 10 results per search due to API restrictions.
- It is possible to expand this project by adding more features like pagination, advanced filters, etc.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
