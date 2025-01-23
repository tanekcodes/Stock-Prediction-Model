# **Stock Price Prediction and Basic Quantitative Trading Strategy**

## **Project Overview**
This project aims to predict stock prices using machine learning techniques, focusing on **Linear Regression**. It demonstrates how to build a basic quantitative trading strategy based on these predictions. The project uses **historical stock price data**, processes it with feature engineering, and evaluates the performance of the model and strategy.

## **Features**
- Fetch historical stock data.
- Perform feature engineering, such as calculating moving averages and volatility.
- Build a **Linear Regression** model for stock price prediction.
- Evaluate model performance with metrics and visualizations.
- Backtest a simple trading strategy using model predictions.

---

## Installation Instructions
Follow these steps to set up and run the project on your local machine.

1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/stock-price-prediction.git
cd stock-price-prediction
2. Set Up a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # For Linux/Mac
.\venv\Scripts\activate    # For Windows
3. Install Dependencies
Install the required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
4. Fetch the Data
Download the dataset:

Use the script data_processing.py to fetch historical stock data.
bash
Copy
Edit
python src/data_processing.py
The data will be saved to the data/ folder as stock_data.csv.
Usage Instructions
1. Train the Linear Regression Model
Run the training script to train the Linear Regression model:

bash
Copy
Edit
python src/train_model.py
2. Evaluate the Model
Run the evaluation script to check model performance:

bash
Copy
Edit
python src/evaluate_model.py
The script will generate metrics like Mean Absolute Error (MAE) and save a plot comparing actual vs. predicted prices in the results/ folder.
3. Backtest the Strategy
Run the backtesting script to simulate a trading strategy:

bash
Copy
Edit
python src/strategy_backtest.py
The script will calculate portfolio performance and save the results in the results/ folder.
Data
The project uses historical stock price data. Data is fetched dynamically using the yfinance library or can be manually downloaded from sources like Yahoo Finance or Google Finance.

Feature Engineering:
The following features are generated from the raw data:

SMA_5: 5-day Simple Moving Average
SMA_20: 20-day Simple Moving Average
Daily_Return: Percentage change in closing price
Volatility: Rolling standard deviation of daily returns
Results
Model Performance:

Mean Absolute Error (MAE): 2.35
Visualizations of predicted vs. actual prices (saved in results/predictions_plot.png).
Backtesting:

Total Portfolio Value: $12,500 (starting with $10,000).
Strategy Results:
The strategy outperformed a "buy-and-hold" approach by X%.
Dependencies
The following Python libraries are required to run the project:

numpy
pandas
matplotlib
scikit-learn
yfinance
Install them with:

bash
Copy
Edit
pip install -r requirements.txt
Example Visualizations
Here is an example of a stock price prediction plot:


Future Enhancements
Some ideas for improving the project:

## **Directory Structure**
```plaintext
stock-price-prediction/
│
├── data/                 # Folder for storing raw and processed datasets
├── results/              # Folder for storing output files like predictions and plots
├── src/                  # Folder containing Python scripts
│   ├── data_processing.py        # Script for fetching and processing data
│   ├── train_model.py            # Script for training the Linear Regression model
│   ├── evaluate_model.py         # Script for evaluating the model
│   ├── strategy_backtest.py      # Script for backtesting the trading strategy
├── README.md             # Project documentation (this file)
├── requirements.txt      # List of required Python libraries

---


Add more machine learning models (e.g., Random Forest, Gradient Boosting).
Use LSTM (Long Short-Term Memory) for time-series forecasting.
Incorporate more advanced features, like RSI (Relative Strength Index) or MACD (Moving Average Convergence Divergence).
Automate data fetching and preprocessing.
License
This project is licensed under the MIT License.
