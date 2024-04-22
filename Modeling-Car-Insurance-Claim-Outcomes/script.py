# Import required modules
import pandas as pd
import numpy as np
from statsmodels.formula.api import logit

# Start coding!

data = pd.read_csv("car_insurance.csv")

data["credit_score"].fillna(data["credit_score"].mean(), inplace=True)
data["annual_mileage"].fillna(data["annual_mileage"].mean(), inplace=True)

accurancy_dict = {}
for col in data:
    if col != "id" and col != "outcome":
        outcomes = pd.DataFrame()
        model = logit(f"outcome ~ {col}", data=data).fit()

        actual_response = data[f"{col}"]
        predicted_response = np.round(model.predict())

        outcomes["actual_response"] = actual_response
        outcomes["predicted_response"] = predicted_response

        conf_matrix = model.pred_table()
        TN = conf_matrix[0, 0]
        TP = conf_matrix[1, 1]
        FN = conf_matrix[1, 0]
        FP = conf_matrix[0, 1]

        accurancy = (TN + TP) / (TN + TP + FN + FP)

        accurancy_dict[f"{col}"] = accurancy

# max accurancy value
max_accurancy_value = max(accurancy_dict.values())

# max accurancy key name
for key, value in accurancy_dict.items():
    if value == max_accurancy_value:
        max_accurancy_key = key

print("Max accurancy value is for column:", max_accurancy_key, "| Value is equal to:", max_accurancy_value)

best_feature_df = pd.DataFrame({"best_feature": [max_accurancy_key], "best_accuracy": [max_accurancy_value]})

print(best_feature_df)
