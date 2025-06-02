
# netflix_data_cleaning.py

import pandas as pd
import os  # Import the os module to interact with the operating system

# Check the current working directory to see where the script is looking for the file
print("Current working directory:", os.getcwd())

# List files in the current directory to see if 'netflix_titles.csv' is present
print("Files in current directory:", os.listdir())

# Load the dataset
# Ensure 'netflix_titles.csv' is in the same directory as this script
# or provide the full path, e.g., df = pd.read_csv("/path/to/your/file/netflix_titles.csv")
df = pd.read_csv("/content/netflix_titles_cleaned.csv")

# Display initial info
print("Initial dataset shape:", df.shape)
print("Missing values:\n", df.isnull().sum())

# 1. Fill missing values with 'Unknown'
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)

# 2. Drop rows with missing critical fields
df.dropna(subset=['date_added', 'rating', 'duration'], inplace=True)

# 3. Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'])

# 4. Standardize text values
df['type'] = df['type'].str.strip().str.title()
df['rating'] = df['rating'].str.strip().str.upper()

# 5. Rename columns to lowercase with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 6. Remove duplicates
df.drop_duplicates(inplace=True)

# 7. Check and fix data types
df['release_year'] = df['release_year'].astype(int)

# Display cleaned dataset info
print("\nCleaned dataset shape:", df.shape)
print("Remaining missing values:\n", df.isnull().sum())

# Save cleaned data to CSV
df.to_csv("netflix_titles_cleaned.csv", index=False)
print("\nCleaned dataset saved as 'netflix_titles_cleaned.csv'")
