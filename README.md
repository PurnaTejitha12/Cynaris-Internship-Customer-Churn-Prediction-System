# Cynaris Internship - Customer Churn Prediction System

## Project Overview

This project focuses on building a Machine Learning based Customer Churn Prediction System. The goal is to predict whether a customer is likely to leave (churn) or continue using the service based on customer demographics, subscription details, and service usage information.

## Problem Statement

Customer churn is a major challenge for businesses. This project develops a classification model that identifies customers who are likely to churn, helping organizations take preventive actions and improve customer retention.

## Dataset

- Dataset Used: IBM Telco Customer Churn Dataset
- Target Variable: Churn

The dataset contains customer information such as:
- Demographics
- Account information
- Subscription details
- Service usage details

## Data Preparation

Performed the following preprocessing steps:

- Explored dataset using `head()`, `info()`, `describe()`, and `shape`
- Removed unnecessary `customerID` column
- Converted `TotalCharges` from text format to numeric format
- Handled missing values using median imputation
- Removed duplicate records
- Converted target variable (Yes/No) into numerical format (1/0)

## Feature Engineering

Applied:

- Feature and target separation
- Identification of numerical and categorical features
- One-Hot Encoding for categorical variables
- StandardScaler for numerical feature normalization

## Model Building

Implemented and compared multiple classification algorithms:

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

## Model Evaluation

Evaluated models using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report
- ROC Curve
- ROC-AUC Score

## Model Improvement

Applied:

- 5-Fold Cross Validation for reliable model evaluation
- Hyperparameter tuning using GridSearchCV

## Feature Importance Analysis

Analyzed important customer attributes influencing churn prediction using the Random Forest model.

## Model Saving

Saved the trained machine learning model and preprocessing objects using Joblib for future deployment.

## Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

## Project Workflow

1. Data Loading
2. Data Exploration
3. Data Cleaning
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Hyperparameter Tuning
8. Model Saving

## Conclusion

Developed an end-to-end Customer Churn Prediction System using Machine Learning techniques. The project includes complete data preprocessing, model comparison, performance evaluation, optimization, and model persistence for future usage.