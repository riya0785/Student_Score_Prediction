# 📊 Student Performance Prediction using Machine Learning

This project builds a machine learning pipeline to predict student performance based on academic and demographic features. It includes data preprocessing, model training, evaluation, logging, and visualizations.

---

## 🗂️ Project Structure
```
StudentPerformanceML/
├── data/                   # Raw and processed student data
│   ├── student_data.csv
│   └── processed_student_data.csv
├── scripts/                # Python scripts for each stage of the pipeline
│   ├── preprocess.py
│   ├── train_model.py
│   └── evaluate.py
├── models/                 # Saved machine learning models
│   └── student_model.pkl
├── visuals/                # Output visualizations (e.g., confusion matrix)
│   └── confusion_matrix.png
├── run_pipeline.bat        # Windows batch script to run the full pipeline
├── README.md               # Project overview and instructions
└── requirements.txt        # Python dependencies
```
## ⚙️ Setup Instructions

1. **Clone or Download** this repository.
2. **Install Python 3.7+** if not already installed.
3. (Optional but recommended) Create and activate a virtual environment:
    ```
    python -m venv venv
    .\venv\Scripts\activate      # Windows
    ```
4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ How to Run the Project

From PowerShell or Command Prompt in the project root:

```bash
.\run_pipeline.bat
```

This will:
- Preprocess the dataset
- Train a logistic regression model
- Evaluate the model and save a confusion matrix

---

## 📌 Key Files

- `scripts/preprocess.py`: Cleans and prepares data
- `scripts/train_model.py`: Trains and saves the model
- `scripts/evaluate.py`: Evaluates model performance and saves confusion matrix
- `run_pipeline.bat`: Automates the full ML pipeline for Windows

---

## 📈 Output

- ✅ Model saved in: `models/student_model.pkl`
- 📊 Confusion Matrix: `visuals/confusion_matrix.png`

---

## 🧠 ML Model Used

- **Logistic Regression** (from `scikit-learn`)
- Feature-target split from `processed_student_data.csv`

---

## 📦 Requirements

```
pandas
scikit-learn
matplotlib
```

> Add more if needed in `requirements.txt`

---

## 🙌 Acknowledgements

- Built using Python and Scikit-Learn
- Inspired by real-world educational data analysis tasks

---

## 📬 Contact

Feel free to reach out if you have questions or suggestions!
```
