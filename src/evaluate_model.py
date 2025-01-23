# src/evaluate_model.py
import pandas as pd
import matplotlib.pyplot as plt

def plot_predictions(model, data_path):
    data = pd.read_csv(data_path)
    X = data[['SMA_5', 'SMA_20', 'Daily_Return']]
    y = data['Close'].shift(-1).dropna()
    X = X.iloc[:-1, :]

    predictions = model.predict(X)
    
    plt.figure(figsize=(14, 7))
    plt.plot(data.index[-len(predictions):], y[-len(predictions):], label='Actual')
    plt.plot(data.index[-len(predictions):], predictions, label='Predicted')
    plt.legend()
    plt.title("Stock Price Prediction")
    plt.show()

if __name__ == "__main__":
    from train_model import train_model
    model = train_model("../data/processed_data.csv")
    plot_predictions(model, "../data/processed_data.csv")
