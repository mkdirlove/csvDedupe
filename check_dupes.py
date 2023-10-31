import pandas as pd
import argparse

def check_duplicates(file_path):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Check for duplicate rows in the DataFrame
    duplicate_rows = df[df.duplicated(keep=False)]

    # If there are duplicates, display the duplicate rows
    if not duplicate_rows.empty:
        print("Duplicate Rows:")
        print(duplicate_rows)
    else:
        print("No duplicate rows found.")

# Argparse configuration
parser = argparse.ArgumentParser(description='Check for duplicates in a CSV file')
parser.add_argument('-f', '--file', help='Input CSV file', required=True)
args = parser.parse_args()

# Replace 'file.csv' with the actual CSV file you want to check for duplicates
check_duplicates(args.file)
