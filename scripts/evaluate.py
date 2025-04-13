import os
import pandas as pd
import joblib
import logging
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# Setup logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/evaluation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    logging.info("Loading test data...")
    X_test = pd.read_csv('data/X_test.csv')
    y_test = pd.read_csv('data/y_test.csv')

    # Ensure y_test is 1D
    if y_test.shape[1] == 1:
        y_test = y_test.values.ravel()

    logging.info("Loading model...")
    model = joblib.load('models/student_model.pkl')

    logging.info("Making predictions and evaluating...")
    y_pred = model.predict(X_test)

    report = classification_report(y_test, y_pred)
    print(report)
    logging.info("Classification Report:\n" + report)

    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()

    os.makedirs('visuals', exist_ok=True)
    plt.savefig('visuals/confusion_matrix.png')
    logging.info("Confusion matrix saved to visuals/confusion_matrix.png")

    logging.info("Evaluation complete.")

except Exception as e:
    logging.error(f"Error during evaluation: {e}")
    print("[ERROR] Check logs/evaluation.log for details.")
