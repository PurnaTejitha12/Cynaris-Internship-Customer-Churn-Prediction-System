# Cynaris Internship - Customer Churn Prediction System

## Project Overview

This project focuses on building a Machine Learning based Customer Churn Prediction System.

The goal is to predict whether a customer is likely to leave (Churn) or continue using the service (No Churn) based on customer subscription details, service usage, and account information.

The trained Machine Learning model is integrated with a Flask web application where users can enter customer details and receive a churn prediction along with the probability of churn.

---

## Problem Statement

Customer churn is a major challenge for businesses because losing customers can directly affect revenue.

Instead of waiting for customers to leave, businesses can use Machine Learning to identify customers who are at high risk of churn and take preventive actions such as:

- Personalized offers
- Discounts
- Customer support
- Service improvements
- Retention campaigns

This project predicts whether a customer is likely to churn based on their available customer information.

---

## Dataset

**Dataset Used:** IBM Telco Customer Churn Dataset

**Target Variable:** Churn

The dataset contains customer information related to:

- Customer account details
- Subscription information
- Service usage
- Contract information
- Payment information
- Customer support interactions

---

## Data Preparation

The following preprocessing steps were performed:

- Explored the dataset using `head()`, `info()`, `describe()`, and `shape`
- Removed the unnecessary `customerID` column
- Converted `TotalCharges` from text format to numeric format
- Handled missing values using median imputation
- Removed duplicate records
- Converted the target variable `Churn` from Yes/No into numerical values:
  - `1` = Churn
  - `0` = No Churn

---

## Feature Engineering

Feature engineering was performed to convert the raw customer information into features that could be used by Machine Learning algorithms.

The following techniques were used:

- Feature and target separation
- Identification of numerical and categorical features
- One-Hot Encoding for categorical variables
- Numerical feature scaling using StandardScaler

The final model uses the following 12 features:

1. `tenure`
2. `monthly_charges`
3. `total_charges`
4. `support_calls`
5. `contract_One year`
6. `contract_Two year`
7. `payment_method_Credit`
8. `payment_method_Debit`
9. `payment_method_UPI`
10. `internet_service_Fiber`
11. `tech_support_Yes`
12. `online_security_Yes`

---

## Machine Learning Models

Three classification algorithms were implemented and compared:

### 1. Logistic Regression

Used as a baseline classification model to predict whether a customer will churn or not.

### 2. Random Forest Classifier

An ensemble learning algorithm that combines multiple decision trees to improve prediction performance.

### 3. Gradient Boosting Classifier

An ensemble learning technique that builds models sequentially to improve prediction accuracy.

---

## Model Evaluation

The models were evaluated using several performance metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report
- ROC Curve
- ROC-AUC Score

These metrics were used to compare the performance of the different classification algorithms.

---

## Cross Validation

5-Fold Cross Validation was used to obtain a more reliable estimate of model performance.

The dataset was divided into five parts.

The model was trained and tested multiple times using different combinations of training and validation sets.

This helps reduce the possibility of evaluating the model based on only one train-test split.

---

## Hyperparameter Tuning

Hyperparameter tuning was performed using `GridSearchCV`.

GridSearchCV tests different combinations of model parameters and identifies the combination that provides the best performance based on the selected evaluation metric.

This helped improve the performance of the selected Machine Learning model.

---

## Feature Importance

Feature importance analysis was performed using the Random Forest model.

This helped identify which customer attributes contribute more strongly to the churn prediction.

Examples include:

- Tenure
- Monthly Charges
- Total Charges
- Support Calls
- Contract Type
- Payment Method
- Internet Service
- Technical Support
- Online Security

---

## Model Saving

The trained Machine Learning model was saved using Joblib.

The following files were created:

```text
best_churn_model.pkl
scaler.pkl