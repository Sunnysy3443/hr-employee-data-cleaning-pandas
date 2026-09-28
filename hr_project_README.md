# HR Employee Data Cleaning & Analysis (Python/Pandas)

Cleaning and analyzing a realistically messy HR dataset using pandas — demonstrating real-world data wrangling, not just clean-data querying.

(I have cleaned and analyze a real messy HR dataset using pandas and demonstated real-world data wrangling for analysis and present it on clean format.)

## The Problem

Raw HR exports are rarely clean. This dataset (30 employees) intentionally includes:

Raw HR data includes 30 employee with multiple missiung values, duplicate employees entered under two different ID with mixed date formates.
- Inconsistent text casing (`Sales`, `sales`, `SALES`)
- Missing values (Salary, Designation)
- Duplicate employees entered under two different IDs
- Mixed date formats (`2021-03-15`, `15/06/2020`, `Jan 5 2020`)
- Extra whitespace in names

## Cleaning Steps

| Issue | Fix | Reasoning |
|---|---|---|
| Inconsistent casing | `.str.lower()` | Standardize Department/Status values |
| Extra whitespace | `.str.strip()` | Prevent silent mismatches in grouping |
| Missing Salary | `groupby().transform('mean')` + `fillna()` | Filled with **department** average, not company-wide — salaries genuinely differ by department |
| Missing Designation | `fillna('Unknown')` | Transparent placeholder rather than guessing a job title |
| Duplicate employees | `duplicated(subset=[...])` + `drop_duplicates()` | Matched on Name/Department/Salary/Join_Date (not ID) — caught the same person entered under two different Employee_IDs |
| Mixed date formats | `pd.to_datetime(..., format='mixed')` | Lets pandas infer each date's format individually instead of assuming one format for the whole column |

Result: 30 raw rows → 27 cleaned rows.


## Cleaning Steps

Inconsistent text casing | .str.lower() | fixed the casing for each department
- Missing values .mean()) and .fillna ] | used two functions to find mean of the data and fillna to fillup that mean at the place of missing values
- Duplicate employees entered under two different IDs | df.duplicated() and df.drop_duplicates(subset=['Employee_Name', 'Department', 'Salary', 'Join_Date'], keep='first')
print(df.shape)| to find the duplicate and keep the first data from duplicate and remove the same duplicate rows.  
- Mixed date formats (`2021-03-15`, `15/06/2020`, `Jan 5 2020`) | pd.to_datetime and format='mixed' | used pd.to_datetime function to check the formate and used format='mixed' to check the formate individually rather then assuming the all date formate could be same to avoid any misunderstanding
- Extra whitespace in names | .str.strip() | used .strip method to cut the white space to avoid the count of unused and unrequired space in dataset

## Analysis

- Attrition rate by department (Finance highest at 40%, Marketing 0%)
- Average tenure by department
- Company-wide attrition: 22 active / 5 resigned

* The number of days employees have worked and working from the date of joining in year and days format.
* Number of eployees are currently working and resigned which is currently working=22 and resigned=5
* Department wise mean of salary.

## Files

- `employee_data_raw.csv` — original messy data
- `employee_data_cleaned.csv` — cleaned output
- `hr_data_cleaning_analysis.py` — full cleaning + analysis script
- `attrition_by_department.png` — visualization
- `pandas_cheat_sheet.md` — reference of every pandas method used, in plain English

- `employee_data_raw.csv` — Original file of messy data
- `employee_data_cleaned.csv` — Cleaned and filtered file using pandas
- `hr_data_cleaning_analysis.py` — Full file of codes to clean the data and output
- `attrition_by_department.png` — image of showing the attration of employee department vise
- `pandas_cheat_sheet.md` — Whole summary and explaination of my code and workflow from scratch to end of the project including methods used in pandas.

## Key Takeaway

In a real job, a missing or ambiguous value is a judgment call, not a default to fill blindly. This project deliberately uses **different fixes for different situations**: a calculated estimate where a smart default exists (Salary), a transparent placeholder where guessing would be misleading (Designation), and a note that in a live production scenario, either gap should ideally be verified against the source system before finalizing.

In this project Pandas library have been used to clean and filter out the data as well using filling up the missing values, removing extra spaces to avoid the unnecessary count and making file size bigger then its actual size, removing the dublicate entries of employees data with different employee ID to avoid any confusion and for the conslusion using matplotlib library to make a graph visual of attration of employees by department.