# src/strategy_backtest.py
def backtest_strategy(model, data_path):
    data = pd.read_csv(data_path)
    X = data[['SMA_5', 'SMA_20', 'Daily_Return']]
    y = data['Close'].shift(-1).dropna()
    X = X.iloc[:-1, :]
    
    predictions = model.predict(X)
    initial_capital = 10000
    cash = initial_capital
    shares_held = 0

    for i, price in enumerate(data['Close'][-len(predictions):]):
        if predictions[i] > price:
            shares_held += cash // price
            cash -= shares_held * price
        elif shares_held > 0:
            cash += shares_held * price
            shares_held = 0

    portfolio_value = cash + shares_held * data['Close'].iloc[-1]
    print(f"Final Portfolio Value: ${portfolio_value:.2f}")

if __name__ == "__main__":
    from train_model import train_model
    model = train_model("../data/processed_data.csv")
    backtest_strategy(model, "../data/processed_data.csv")
