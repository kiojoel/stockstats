from flask import Flask, render_template, request
import yfinance as yf
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime, timedelta

import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

def get_stock_data(ticker, start_date, end_date):
    """Fetches stock data, calculates stats, and generates a plot for a given date range."""
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date, progress=False)

        if stock_data.empty:
            return {"error": f"No data found for '{ticker}' in the specified date range."}

        #  Calculate Statistics
        stats = {
            'highest': stock_data['High'].max().iloc[0],
            'average': stock_data['Close'].mean().iloc[0],
            'volume': stock_data['Volume'].sum().iloc[0]
        }

        # Generate Plot in Memory
        plt.figure(figsize=(12, 6))
        stock_data['Close'].plot(grid=True)
        plt.title(f'{ticker.upper()} Closing Price ({start_date} to {end_date})')
        plt.ylabel('Price (USD)')
        plt.xlabel('Date')

        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', bbox_inches='tight')
        plt.close()
        img_buffer.seek(0)

        # Encode the buffer's content to a base64 string
        plot_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return {"stats": stats, "plot": plot_base64}

    except Exception as e:
        return {"error": f"An error occurred: {e}"}


@app.route('/')
def home():
    """Renders the homepage and provides default dates for the form."""
    end_date_default = datetime.now().strftime('%Y-%m-%d')
    start_date_default = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

    return render_template('index.html',
                           default_start=start_date_default,
                           default_end=end_date_default)


@app.route('/results', methods=['POST'])
def results():
    """Handles form submission, gets data, and renders the results page."""
    ticker = request.form.get('ticker', '').strip().upper()
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    # Add validation for inputs
    if not all([ticker, start_date, end_date]):
        return render_template('index.html', error="All fields are required.",
                               default_start=(datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d'),
                               default_end=datetime.now().strftime('%Y-%m-%d'))

    if start_date >= end_date:
        return render_template('index.html', error="Start date must be before end date.",
                               last_ticker=ticker,
                               default_start=start_date,
                               default_end=end_date)

    # Pass the dates to our analysis function
    data = get_stock_data(ticker, start_date, end_date)

    if "error" in data:
        return render_template('index.html', error=data["error"], last_ticker=ticker,
                               default_start=start_date, default_end=end_date)

    # Pass the dates to the results template for display
    return render_template('results.html',
                           ticker=ticker,
                           stats=data["stats"],
                           plot_url=data["plot"],
                           start_date=start_date,
                           end_date=end_date)


if __name__ == '__main__':
    app.run(debug=True)