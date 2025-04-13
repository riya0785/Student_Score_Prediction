import os
import pandas as pd
import joblib
import logging
from sklearn.linear_model import LogisticRegression

# Setup logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/train.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    logging.info("Loading training data...")
    X_train = pd.read_csv('data/X_train.csv')
    y_train = pd.read_csv('data/y_train.csv')

    # Ensure y is a 1D array
    if y_train.shape[1] == 1:
        y_train = y_train.values.ravel()

    logging.info("Training Logistic Regression model...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    logging.info("Saving model...")
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/student_model.pkl')

    logging.info("Model training complete.")

except Exception as e:
    logging.error(f"Error during training: {e}")
    print("[ERROR] Check logs/train.log for details.")
