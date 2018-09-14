# Kidney_Disease_Detection
This is a classification problem to predict kidney disease.

The chronic kidney disease dataset contains both categorical and numeric features, but contains lots of missing values. The goal here is to predict who has chronic kidney disease given various blood indicators as features.

The dataset can be download from UCI Machine Learning Repository.
There are 3 self defined package:
  1. missing_values_table: check the percetage of missing values and turn it into a table
  2. Categorical_Imputer: imputing categorical missing values using the most frequent
  3. roc_auc: plot self defined roc curve
