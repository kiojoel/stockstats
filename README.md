# Stock Analyzer Web App

A simple web application built with Python and Flask that allows users to analyze historical stock data. The app fetches data for a given ticker symbol and date range, calculates key statistics, and displays a price chart.

### [View Live App](https://stockstats.onrender.com/)

## Features

- Enter any valid US stock ticker symbol.
- Select a custom date range for analysis.
- View key statistics: highest price, average closing price, and total volume.
- See a visual line chart of the stock's closing price over the selected period.
- Handles invalid ticker symbols and network errors gracefully.
- Live and publicly accessible via Render.

## Technologies Used

- **Backend:** Python, Flask
- **Data Retrieval:** `yfinance` library
- **Plotting:** `matplotlib`
- **Frontend:** HTML, CSS
- **WSGI Server:** Gunicorn
- **Deployment:** Render

## How to Run Locally

To run this project on your own machine:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**

    ```bash
    python app.py
    ```

5.  Open your web browser and navigate to `http://127.0.0.1:5000`.
