# Bank Marketing Decision Tree Classifier

Decision Tree classification project using the UCI Bank Marketing dataset.

The main goal is to predict whether a customer will subscribe to a term deposit (`yes` or `no`) based on demographic and behavioral information. The project includes data preprocessing, exploratory data analysis (EDA), model building, and performance evaluation.

## Project Summary

- Loaded and inspected the Bank Marketing dataset.
- Analyzed dataset structure, variable types, and target distribution.
- Performed preprocessing by encoding categorical features into numerical values.
- Conducted exploratory data analysis using charts and statistical summaries.
- Built a Decision Tree Classifier to predict customer subscription.
- Evaluated model performance using accuracy score, confusion matrix, and classification metrics.

## Dataset Details

- Dataset: UCI Bank Marketing Dataset
- Total Records: 45,211 customers
- Features: 16 input features and 1 target variable
- Target Variable: `y`
  - `yes` → Customer subscribed to a term deposit
  - `no` → Customer did not subscribe

The dataset contains customer demographic information, financial details, and previous marketing campaign data, including features such as `age`, `job`, `marital`, `education`, `balance`, `housing`, `loan`, `contact`, `campaign`, `pdays`, and `poutcome`.

## Exploratory Data Analysis

- Analyzed the distribution of the target variable.
- Studied customer age and balance distributions.
- Examined job and marital status distributions.
- Compared customer characteristics with subscription outcomes.
- Used count plots, histograms, box plots, and correlation heatmaps to identify patterns and insights in the dataset.

## Model Building

- Encoded categorical variables using Label Encoding.
- Split the dataset into training and testing sets using an 80:20 ratio.
- Trained a Decision Tree Classifier using the entropy criterion.
- Generated predictions on unseen test data.

## Evaluation Metrics

- Accuracy Score
- Confusion Matrix
- Precision
- Recall
- F1 Score

## Conclusion

This project demonstrates how a Decision Tree Classifier can be used to predict customer subscription behavior using demographic and campaign-related information. The model helps identify potential customers and can assist banks in improving marketing efficiency and decision-making.