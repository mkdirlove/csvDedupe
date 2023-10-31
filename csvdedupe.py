import pandas as pd
import argparse
import os

banner = """
  __________   __       __       __
 / ___/ __/ | / /______/ /__ ___/ /_ _____  ___
/ /___\ \ | |/ /___/ _  / -_) _  / // / _ \/ -_)
\___/___/ |___/    \_,_/\__/\_,_/\_,_/ .__/\__/
                                    /_/
"""

# Function to merge two CSV files
def merge_csv(file1, file2, merge_output):
    # Read CSV files into Pandas DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Merge data from both DataFrames
    merged_df = pd.concat([df1, df2])

    # Save the merged data to a new CSV file
    merged_df.to_csv(merge_output, index=False)

# Function to deduplicate CSV files based on 'First Name' and 'Last Name' columns
def deduplicate_csv(file_path):
    # Read CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Identify and remove duplicate rows based on 'First Name' and 'Last Name' columns
    deduplicated_df = df.drop_duplicates(subset=['First Name', 'Last Name'])

    # Save the deduplicated data back to a new CSV file
    deduplicated_df.to_csv('deduplicated_' + file_path, index=False)

# Function to merge and deduplicate
def merge_and_dedupe(file1, file2, output):
    # Merge CSV files
    merge_csv(file1, file2, 'merged_temp.csv')

    # Deduplicate the merged file
    deduplicate_csv('merged_temp.csv')

    # Rename the deduplicated file to the output filename
    import os
    os.rename('deduplicated_merged_temp.csv', output)

    # Clean up temporary merged file
    os.remove('merged_temp.csv')

# Argparse configuration
os.system("clear")
print(banner)
parser = argparse.ArgumentParser(description='Merge and deduplicate CSV files')
parser.add_argument('-f1', '--file1', help='First CSV file', required=True)
parser.add_argument('-f2', '--file2', help='Second CSV file', required=True)
parser.add_argument('-o', '--output', help='Output file')
args = parser.parse_args()

# Replace 'file1.csv' and 'file2.csv' with your CSV file names for merging and deduplication
merge_and_dedupe(args.file1, args.file2, args.output)
