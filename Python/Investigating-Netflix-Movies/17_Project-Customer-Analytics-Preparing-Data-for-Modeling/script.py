import pandas as pd

ds_jobs = pd.read_csv("customer_train.csv")

ds_jobs_clean = ds_jobs.copy()

# Convert int64 to int32
ds_jobs_clean["student_id"] = ds_jobs_clean["student_id"].astype("int32")
ds_jobs_clean["training_hours"] = ds_jobs_clean["training_hours"].astype("int32")
ds_jobs_clean["job_change"] = ds_jobs_clean["job_change"].astype("int32")

# Convert float64 to float16
ds_jobs_clean["city_development_index"] = ds_jobs_clean["city_development_index"].astype("float16")

# Convert nominal categorical data to category type
ds_jobs_clean["city"] = ds_jobs_clean["city"].astype("category")
ds_jobs_clean["gender"] = ds_jobs_clean["gender"].astype("category")
ds_jobs_clean["major_discipline"] = ds_jobs_clean["major_discipline"].astype("category")
ds_jobs_clean["company_type"] = ds_jobs_clean["company_type"].astype("category")

# Convert ordinal categorical data to ordered categories
ordered_cats = {
    'relevant_experience': ['No relevant experience', 'Has relevant experience'],
    'enrolled_university': ['no_enrollment', 'Part time course', 'Full time course'],
    'education_level': ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'],
    'experience': ['<1'] + list(map(str, range(1, 21))) + ['>20'],
    'company_size': ['<10', '10-49', '50-99', '100-499', '500-999', '1000-4999', '5000-9999', '10000+'],
    'last_new_job': ['never', '1', '2', '3', '4', '>4']
}

ds_jobs_clean["relevant_experience"] = ds_jobs_clean["relevant_experience"]\
    .astype(pd.CategoricalDtype(ordered_cats["relevant_experience"], ordered=True))
ds_jobs_clean["enrolled_university"] = ds_jobs_clean["enrolled_university"]\
    .astype(pd.CategoricalDtype(ordered_cats["enrolled_university"], ordered=True))
ds_jobs_clean["education_level"] = ds_jobs_clean["education_level"]\
    .astype(pd.CategoricalDtype(ordered_cats["education_level"], ordered=True))
ds_jobs_clean["experience"] = ds_jobs_clean["experience"]\
    .astype(pd.CategoricalDtype(ordered_cats["experience"], ordered=True))
ds_jobs_clean["company_size"] = ds_jobs_clean["company_size"]\
    .astype(pd.CategoricalDtype(ordered_cats["company_size"], ordered=True))
ds_jobs_clean["last_new_job"] = ds_jobs_clean["last_new_job"]\
    .astype(pd.CategoricalDtype(ordered_cats["last_new_job"], ordered=True))

# Filter
ds_jobs_clean = ds_jobs_clean[(ds_jobs_clean['experience'] >= '10') & (ds_jobs_clean['company_size'] >= '1000-4999')]
