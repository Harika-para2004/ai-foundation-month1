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


