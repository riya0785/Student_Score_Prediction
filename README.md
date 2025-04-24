#  Student Performance Prediction using Machine Learning

This project builds a machine learning pipeline to predict student performance based on academic and demographic features. It includes data preprocessing, model training, evaluation, logging, and visualizations.

---
Presented By : 

* Riya Shukla
* Simrann Dabrai
* Shhreyash Pandey
     
##  Project Structure
```
StudentPerformanceML/
├── data/                      # Dataset and train-test splits
│   ├── student_performance_prediction.csv
│   ├── X_train.csv
│   ├── X_test.csv
│   ├── y_train.csv
│   └── y_test.csv
├── scripts/                   # Python scripts for pipeline stages
│   ├── preprocess.py
│   ├── train_model.py
│   └── evaluate.py
├── models/                    # Trained model
│   └── student_model.pkl
├── visuals/                   # Evaluation visuals
│   └── confusion_matrix.png
├── logs/                      # Logs for each step
│   ├── preprocess.log
│   ├── train.log
│   └── evaluation.log
├── run_pipeline.bat           # Batch script to run full pipeline (Windows)
├── requirements.txt           # Required Python packages
└── README.md                  # Project documentation
```
##  Setup Instructions

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

##  How to Run the Project

From PowerShell or Command Prompt in the project root:

```bash
.\run_pipeline.bat
```

This will:
- Preprocess the dataset
- Train a logistic regression model
- Evaluate the model and save a confusion matrix

---
Using Linux

git clone https://github.com/yourusername/StudentPerformanceML.git
cd StudentPerformanceML
----setup the environment----
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
chmod +x run_all.sh
./run_all.sh
---The script will:----

Activate the virtual environment

Run the preprocess.ipynb notebook

Run the training.ipynb notebook

Run the evaluate.ipynb notebook


##  Key Files

- `scripts/preprocess.py`: Cleans and prepares data
- `scripts/train_model.py`: Trains and saves the model
- `scripts/evaluate.py`: Evaluates model performance and saves confusion matrix
- `run_pipeline.bat`: Automates the full ML pipeline for Windows

---

##  Output

-  Model saved in: `models/student_model.pkl`
-  Confusion Matrix: `visuals/confusion_matrix.png`(will be saved once the code for evaluate.ipynb is executed)

---

##  ML Model Used

- **Logistic Regression** (from `scikit-learn`)
- Feature-target split from `processed_student_data.csv`

---

##  Requirements

```
pandas
scikit-learn
matplotlib
```

> Add more if needed in `requirements.txt`

---

##  Acknowledgements

- Built using Python and Scikit-Learn
- Inspired by real-world educational data analysis tasks

