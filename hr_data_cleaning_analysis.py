import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('employee_data_raw.csv')

print(df.info())
print(df.describe())
print(df.isnull().sum())

df['Department'] = df['Department'].str.lower()
print(df['Department'])

df['Status'] = df['Status'].str.lower()
print(df['Status'])

df['Employee_Name'] = df['Employee_Name'].str.strip()
print(df['Employee_Name'].apply(len))

print(df.groupby('Department')['Salary'].mean())

df['Salary'] = df['Salary'].fillna(df.groupby('Department')['Salary'].transform('mean'))
df['Salary'] = df['Salary'].round(2)
print(df.isnull().sum())

df['Designation'] = df['Designation'].fillna('Unknown')
print(df.isnull().sum())

print(df[df.duplicated()])

print(df[df.duplicated(subset=['Employee_Name', 'Department', 'Salary', 'Join_Date'], keep=False)])

df = df.drop_duplicates(subset=['Employee_Name', 'Department', 'Salary', 'Join_Date'], keep='first')
print(df.shape)

print(df[df.duplicated(subset=['Employee_Name', 'Department', 'Salary', 'Join_Date'], keep=False)])

df['Join_Date'] = pd.to_datetime(df['Join_Date'], format='mixed')
print(df['Join_Date'])

df.to_csv('employee_data_cleaned.csv', index=False)

print(df.shape)

print(df.groupby('Department')['Status'].value_counts())

df['Tenure_Days'] = (pd.Timestamp.now() - df['Join_Date']).dt.days
df['Tenure_Years'] = round(df['Tenure_Days'] / 365, 1)
print(df.groupby('Department')['Tenure_Years'].mean())

df.groupby('Department')['Status'].value_counts().unstack().plot(kind='bar')
plt.title('Attrition by Department')
plt.ylabel('Number of Employees')
plt.savefig('attrition_by_department.png')
plt.show()