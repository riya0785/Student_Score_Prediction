import os
import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Setup logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/preprocess.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    logging.info('Loading dataset...')
    df = pd.read_csv('data\student_performance_prediction.csv')

    logging.info('Dropping missing values...')
    df.dropna(inplace=True)

    # Encode categorical columns
    logging.info('Encoding categorical columns...')
    label_encoder = LabelEncoder()
    categorical_cols = ['Passed', 'Participation in Extracurricular Activities', 'Parent Education Level']

    for col in categorical_cols:
        if col in df.columns:
            df[col] = label_encoder.fit_transform(df[col])
        else:
            logging.warning(f"Column '{col}' not found in dataset.")

    # Split features and target
    logging.info('Splitting features and target...')
    X = df.drop(['Passed', 'Student ID'], axis=1)
    y = df['Passed']

    # Train-test split
    logging.info('Splitting data into train and test sets...')
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Save to CSV
    os.makedirs('data', exist_ok=True)
    X_train.to_csv('data/X_train.csv', index=False)
    X_test.to_csv('data/X_test.csv', index=False)
    y_train.to_csv('data/y_train.csv', index=False)
    y_test.to_csv('data/y_test.csv', index=False)

    logging.info('Preprocessing complete.')

except Exception as e:
    logging.error(f'Error during preprocessing: {e}')
    print(f'[ERROR] Check logs/preprocess.log for details.')
