import pandas as pd
import chardet
# 'Employee Sample Data - Copy.csv'
file_path='C:\\Users\\User\\Downloads\\Employee Sample Data - 1.csv'
# df = pd.read_csv(file_path)
# print(df)
with open(file_path, 'rb') as f:
    result = chardet.detect(f.read())
    print(result) # Use the detected encoding

df = pd.read_csv(file_path, encoding=result['encoding'])
print("The original dataset")
print(df.head())
print(df.describe())
print(df.info())
print("Now i will clean the data ")
new_df=df.dropna()
print(new_df.to_string())
#removing the duplicates
dup=df.drop_duplicates(inplace=True)
print(dup)
#After cleaning
print(df.head())
print(df.describe())
print(df.info())
new_inputs={
    'EEID':['E01234', 'E04321', 'E01798', 'E02222', 'E09988'],
    'Full Name': ['Saif Attieh', 'Ahmad Mustafa', 'Mohammad Ahmad', 'Ahmad Mohammad', 'Sara Ahmad'],
    'Job Title': ['Data Analys', 'Software Engineer', 'Accountant', 'Coordinator', 'Director'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales'],
    'Business Unit': ['BU1', 'BU2', 'BU3', 'BU1', 'BU4'],
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Female'],
    'Ethnicity': ['White', 'Asian', 'Black', 'Hispanic', 'White'],
    'Age': [35, 25, 42, 33, 45],
    'Hire Date': ['15-01-2020', '15-05-2018', '11-11-2015', '09-08-2017', '25-03-2014'],
    'Annual Salary': [12000, 6000, 15000, 10000, 160000],
    'Bonus %': [6.0, 2.5, 3.0, 1.5, 6.5],
    'Country': ['Jordan', 'Lebanon', 'Saudi Arabia', 'Egypt', 'Jordan'],
    'City': ['Amman', 'Beirut', 'Jeddah', 'Cario', 'Amman'],
    'Exit Date': ['10-5-2022', '19-9-2023', '31-12-2019', '16-6-2021', '25-5-2016'],
}
df_new=pd.DataFrame(new_inputs)
df.loc[:4]=df_new
df.to_csv(file_path, index=False)
print("--------Now i will display the first 5 modified rows--------")
print(df.head())
#Largest salary
temp_column = pd.to_numeric(df['Annual Salary'], errors='coerce')
max_salary_row = temp_column.max()
print("the largest salary:")
print(max_salary_row)
