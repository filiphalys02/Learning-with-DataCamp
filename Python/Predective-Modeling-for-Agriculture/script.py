# All required libraries are imported here for you.
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the dataset
crops = pd.read_csv("soil_measures.csv")
# Identify the single feature that has the strongest predictive performance for classifying crop types.
# Find the feature in the dataset that produces the best score for predicting "crop".
# From this information, create a variable called best_predictive_feature, which:
# Should be a dictionary containing the best predictive feature name as a key and the evaluation score
# (for the metric you chose) as the value.

X = crops[["N", "P", "K", "ph"]]
y = crops["crop"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

f1_dict = {}

for feature in ["N", "P", "K", "ph"]:
    logreg = LogisticRegression(multi_class="multinomial")
    logreg.fit(X_train[[feature]], y_train)
    y_pred = logreg.predict(X_test[[feature]])
    f1 = metrics.f1_score(y_test, y_pred, average="weighted")
    f1_dict[feature] = f1

# print(f1_dict)

best_predictive_feature = {"K": f1_dict["K"]}
print(best_predictive_feature)