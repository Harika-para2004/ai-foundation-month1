import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

mydataset2 = {
    'cars': ["BMW", "Volvo", "Mazda"],
    'passings': [4, 5, 6]
}

df = pd.DataFrame(mydataset2)
print("Dataframe: \n", df)

#Pandas Series is like a column in a table.

arr = ["harika", 7.5, 2]
myVar = pd.Series(arr)
print("Pandas Series:\n",myVar)
print("First element of the Series: ", myVar[1])

b = pd.Series(arr, index=["name", "GPA", "sem"])
print("Pandas Series with custom index:\n", b)
print("Element with index 'GPA': ", b["GPA"])
# 2. Data selection & filtering
print("\n--- Data selection & filtering ---\n")
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 23, 22],
    'Salary': [50000, 60000, 55000]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
# Selecting a single column
print("Name column:\n", df["Name"])
# Selecting multiple columns
print("Name and salary :\n", df[["Name", "Salary"]])
# Filtering rows based on a condition
filtered_df = df[df["Salary"] > 50000]
print("\n Filtered DataFrame (Salary > 50000):\n", filtered_df)

# 3. Data cleaning & manipulation
print("\n--- Data cleaning & manipulation ---\n")
data  = {
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [24, None, 22, 32],
    'Salary': [50000, 60000, None, 65000]
}
df = pd.DataFrame(data)
print("Original DataFrame with missing values:\n", df)
# Handling missing values by filling with mean (for numerical columns) or 'Unknown' (for categorical columns)
# fillna() method is used to fill the missing values in the DataFrame.
df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print("\nDataFrame after handling missing values:\n", df)

# Renaming columns
df = df.rename(columns={'Name': 'Full name', 'Salary': 'Annual salary', 'Age':'Age(yrs)'})
df = df.rename(columns = {'Annual salary':'Salary(USD)'})
print("\nDataFrame after renaming columns:\n", df)

# Changing data types
df['Age(yrs)'] = df['Age(yrs)'].astype(int)
print("\nDataFrame after changing data types:\n", df)

# 4. Data aggregation & grouping
print("\n--- Data aggregation & grouping ---\n")
data = {
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [50000, 60000, 55000, 65000, 52000]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# Grouping by department and calculating mean salary
grouped_df = df.groupby('Department')['Salary'].mean()
print("\nMean Salary by Department:\n", grouped_df)
# Aggregating data: total and average salary by department'
agg_df = df.groupby('Department')['Salary'].agg(['sum','mean','count','max','min','std','var'])
print("\nTotal and Average Salary by Department:\n", agg_df)
# Resetting index after grouping
reset_df = agg_df.reset_index()
print("\nReset Index DataFrame:\n", reset_df)
# Merging two DataFrames
data2 = {
    'Department': ['HR', 'IT', 'Finance'],
    'Location': ['New York', 'San Francisco', 'Chicago']
}
df2 = pd.DataFrame(data2)
print("\nSecond DataFrame:\n", df2)
# Merging two DataFrames
merged_df = pd.merge(df, df2, on='Department')
print("\nMerged DataFrame:\n", merged_df)




