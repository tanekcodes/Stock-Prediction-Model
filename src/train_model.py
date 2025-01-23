# src/train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def train_model(data_path):
    data = pd.read_csv(data_path)
    X = data[['SMA_5', 'SMA_20', 'Daily_Return']]
    y = data['Close'].shift(-1).dropna()
    X = X.iloc[:-1, :]  # Align features with target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    print(f"Mean Absolute Error: {mae:.2f}")

    return model

if __name__ == "__main__":
    model = train_model("../data/processed_data.csv")
