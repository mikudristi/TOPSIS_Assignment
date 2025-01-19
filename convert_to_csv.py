import pandas as pd
import sys

# Replace 'YourRollNumber' with your actual roll number
roll_number = "102217188"

# Input and output file names
input_file = "data.xlsx"  # Make sure this file is in the same directory as the script
output_file = f"{roll_number}-data.csv"

try:
    # Load the Excel file
    df = pd.read_excel(input_file)
    
    # Save it as a CSV file
    df.to_csv(output_file, index=False)
    
    print(f"File converted successfully: {output_file}")
except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
