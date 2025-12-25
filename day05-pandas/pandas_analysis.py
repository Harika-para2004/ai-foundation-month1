import pandas as pd

df = pd.read_csv("./data.csv")
print(df)
print(df.isna().sum())
print(df.info())

df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].median())

# Average salary per department
avg_salary = df.groupby("department")["salary"].mean()
print(avg_salary)

# Count of employees in each department
dept_count = df.groupby("department")["name"].count()
print(dept_count)

# Employees older than 30
older_than_30 = df[df["age"] > 30]
print(older_than_30)

# Adding a new column for salary after 10% tax deduction
df["salary_after_tax"] = df["salary"] * 0.9
print(df)

# Maximum salary in each department
max_salary = df.groupby("department")["salary"].max()
print(max_salary)

# Sorting employees by age
sorted_by_age = df.sort_values(by="age")
print(sorted_by_age)

# Top 5 highest paid employees
top_5_paid = df.nlargest(5, "salary")
print(top_5_paid)

# Employees with salary above average
average_salary = df["salary"].mean()
above_average_salary = df[df["salary"] > average_salary]
print(above_average_salary)

# Correlation between age and salary
correlation = df["age"].corr(df["salary"])
print("Correlation between age and salary:", correlation)

# Applying a function to categorize employees based on age
def seniority(age):
    if age >= 35:
        return "Senior"
    else:
        return "Junior"

df["seniority"] = df["age"].apply(seniority)
print(df)

# Exporting the cleaned DataFrame to a new CSV file
df.to_csv("cleaned_data.csv", index=False)

