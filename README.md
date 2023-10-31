# CSV Merge and Deduplication

This Python script merges two CSV files and performs deduplication based on 'First Name' and 'Last Name' columns.

## How to Use

### Prerequisites
- Python 3.x
- Pandas library (`pip install pandas`)

### Usage
1. Clone the repository or download the `csvdedupe.py` file.
2. Open a terminal.
3. Run the script with the following command:
   ```bash
   python3 csvdedupe.py -f1 file1.csv -f2 file2.csv -o output.csv

Replace file1.csv and file2.csv with the names of your CSV files.
-o specifies the output file after deduplication.

Arguments
-f1, --file1: First CSV file path.
-f2, --file2: Second CSV file path.
-o, --output: Output file path after deduplication.
File Descriptions

### Checking dupes in output file
```bash
python3 check_dupes.py -f output.csv

Description
The script uses Pandas to read the CSV file specified by the user and checks for duplicate rows within the DataFrame. It identifies and displays duplicate rows based on their content.

Arguments
-f or --file: Specifies the path to the input CSV file.
Example
```
python check_duplicates.py -f data.csv
```
