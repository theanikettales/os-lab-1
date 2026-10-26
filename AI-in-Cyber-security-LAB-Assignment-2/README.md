# Assignment 2 – Decision Tree Classification

**Student Name:** Aniket Singh 
**Roll Number:** 2501012308 
**Assignment:** 2  
**Language:** Python  
**Environment:** Google Colab / Jupyter Notebook

## 📌 Overview

This assignment demonstrates a basic machine learning classification workflow using a **Decision Tree Classifier**.

The model analyzes login activity data and classifies each login record as either:

- **Normal**
- **Suspicious**

The assignment covers dataset inspection, data cleaning, feature and target selection, train-test splitting, Decision Tree training, model evaluation, confusion matrix visualization, and prediction on new login activity.

## 🎯 Objectives

- Inspect and understand the given dataset.
- Identify input features and the target label.
- Handle missing values in numerical columns.
- Remove duplicate records.
- Split the dataset into training and testing sets.
- Train a Decision Tree classification model.
- Evaluate the model using accuracy and a confusion matrix.
- Predict whether new login activities are Normal or Suspicious.

## 📊 Dataset

The dataset contains login activity information with the following attributes:

| Feature | Description |
|---|---|
| `record_id` | Unique identifier for each record |
| `failed_logins` | Number of failed login attempts |
| `login_hour` | Hour at which the login occurred |
| `new_device` | Indicates whether the login was from a new device |
| `download_mb` | Amount of data downloaded in MB |
| `label` | Target class: Normal or Suspicious |

The model uses the following four features:

```text
failed_logins
login_hour
new_device
download_mb
```

The target variable is:

```text
label
```

## 🧹 Data Cleaning

The original dataset contained:

- **101 records**
- **1 duplicate row**
- Missing values in `failed_logins`
- Missing values in `download_mb`

The missing numerical values were replaced using the **median**, and duplicate rows were removed.

After cleaning:

```text
Final rows: 100
Missing values: 0
Duplicate rows: 0
```

## 🔀 Train-Test Split

The cleaned dataset was divided into:

- **75% training data**
- **25% testing data**

A `random_state` of `42` was used for reproducibility, and stratified splitting was applied to preserve the class distribution.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
```

### Dataset Split

```text
Training rows: 75
Testing rows: 25
```

## 🌳 Decision Tree Model

A Decision Tree Classifier was trained using:

```python
DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)
```

The model was trained on the four login-activity features and used to predict the class of unseen test records.

## 📈 Model Performance

The Decision Tree achieved:

**Accuracy: 88.00%**

A confusion matrix was also generated to visualize the model's classification performance for the **Normal** and **Suspicious** classes.

## 🔍 Sample Predictions

The notebook tests the trained model on new login activity examples.

| Failed Logins | Login Hour | New Device | Download (MB) | Prediction |
|---:|---:|---:|---:|---|
| 0 | 10 | 0 | 45 | Normal |
| 8 | 2 | 1 | 180 | Suspicious |
| 2 | 23 | 1 | 900 | Suspicious |

These examples demonstrate how the model can identify potentially suspicious login behavior based on the provided activity features.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Google Colab / Jupyter Notebook

## 📁 Project Structure

```text
Assignment-2/
│
├── Assignment 2 Ritik Sharma (2401010058).ipynb
├── simple_login_activity.csv
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the notebook

Open:

```text
Assignment 2 Ritik Sharma (2401010058).ipynb
```

using either **Google Colab** or **Jupyter Notebook**.

### 3. Keep the dataset in the same directory

Make sure:

```text
simple_login_activity.csv
```

is available in the same working directory as the notebook.

### 4. Run the cells

Execute the notebook cells sequentially to:

1. Load the dataset
2. Inspect the data
3. Clean the dataset
4. Split the data
5. Train the Decision Tree
6. Evaluate the model
7. Generate predictions

## 📌 Key Learning Outcomes

Through this assignment, the following concepts were implemented:

- Data inspection using Pandas
- Missing-value handling
- Duplicate removal
- Feature and target selection
- Train-test splitting
- Decision Tree classification
- Model prediction
- Accuracy evaluation
- Confusion matrix visualization

## 🏁 Conclusion

This assignment successfully demonstrates the complete workflow of a basic supervised machine learning classification problem. The Decision Tree model achieved **88% accuracy** on the test dataset and was able to classify login activities as Normal or Suspicious.

The experiment provides practical understanding of how raw data can be cleaned, transformed into model-ready features, used to train a classification algorithm, and evaluated using standard machine learning metrics.

---

**Author:** Ritik Sharma  
**Roll No.:** 2401010058  
**Assignment:** 2
