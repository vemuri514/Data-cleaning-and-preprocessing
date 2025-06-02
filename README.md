
# 📊 Netflix Data Cleaning - Task 1

## 🧩 Project Overview

This project is part of a data preprocessing task focused on cleaning and preparing a raw dataset for analysis. The dataset used is the **Netflix Movies and TV Shows** dataset from Kaggle, which contains metadata about titles available on the Netflix platform.

---

## 🎯 Objective

The goal was to:
- Identify and handle missing values
- Remove duplicate records
- Standardize inconsistent formats (e.g., text fields and dates)
- Ensure clean, analysis-ready data

---

## 🛠️ Tools Used

- Python 3
- Pandas Library

---

## 🔧 Data Cleaning Steps

1. **Handled Missing Values**
   - Replaced `NaN` values in `director`, `cast`, and `country` with `"Unknown"`
   - Dropped rows where critical fields like `date_added`, `rating`, or `duration` were missing

2. **Removed Duplicates**
   - Applied `.drop_duplicates()` to remove any duplicate records

3. **Standardized Formats**
   - Cleaned and standardized text in columns like `type` and `rating`
   - Converted `date_added` to `datetime` format for consistency

4. **Cleaned Column Names**
   - Renamed columns to lowercase and replaced spaces with underscores for uniformity

5. **Checked and Fixed Data Types**
   - Ensured correct data types for all columns (e.g., `release_year` as integer, `date_added` as datetime)

---

## 📁 Files Included

| File Name                  | Description                                |
|---------------------------|--------------------------------------------|
| `netflix_titles.csv`      | Original dataset from Kaggle               |
| `netflix_titles_cleaned.csv` | Cleaned and preprocessed dataset         |
| `netflix_data_cleaning.py`| Python script used for data cleaning       |
| `README.md`               | This project documentation file            |

---

## 📌 Notes

This project demonstrates a typical data cleaning workflow using Python and Pandas, suitable for real-world data preprocessing tasks in analytics or machine learning pipelines.

---

## 🧠 Author

*Your Name Here*  
*Your Contact (optional)*
