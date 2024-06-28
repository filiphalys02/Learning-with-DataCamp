import pandas as pd
import pingouin


# Perform an appropriate hypothesis test to determine the p-value, and hence result,
# of whether to reject or fail to reject the null hypothesis that
# the mean number of goals scored in women's international soccer matches is the same as men's.
# Use a 10% significance level.

# For this analysis, you'll use Official FIFA World Cup matches since 2002-01-01,
# and you'll also assume that each match is fully independent, i.e., team form is ignored.

# The p-value and the result of the test must be stored in a dictionary called result_dict in the form:
# result_dict = {"p_val": p_val, "result": result}
# where p_val is the p-value and result is either the string "fail to reject" or "reject",
# depending on the result of the test.

alpha = 0.01

men = pd.read_csv("men_results.csv")
women = pd.read_csv("women_results.csv")

men["sex"] = "men"
women["sex"] = "women"

men["date"] = pd.to_datetime(men["date"])
women["date"] = pd.to_datetime(women["date"])

men = men[men["date"] > "2002-01-01"]
women = women[women["date"] > "2002-01-01"]

men = men[men["tournament"] == "FIFA World Cup"]
women = women[women["tournament"] == "FIFA World Cup"]

men["full_score"] = men["home_score"] + men["away_score"]
women["full_score"] = women["home_score"] + women["away_score"]

group = pd.concat([men, women], axis=0, ignore_index=True)
sex_vs_goals = group[["sex", "full_score"]]
sex_vs_goals_wide = sex_vs_goals.pivot(columns="sex", values="full_score")

mwu = pingouin.mwu(x=sex_vs_goals_wide["women"], y=sex_vs_goals_wide["men"], alternative="greater")
p_val = mwu["p-val"].values[0]


if p_val <= alpha:
    result = "reject"
else:
    result = "fail to reject"


result = result
result_dict = {"p_val": p_val, "result": result}

print(result_dict)
