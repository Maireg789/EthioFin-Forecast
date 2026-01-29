import pandas as pd
import os

def load_unified_data(filepath):
    try:
        # Load the Excel file object to check sheet names
        xl = pd.ExcelFile(filepath)
        sheet_names = xl.sheet_names
        print(f"📂 Available sheets: {sheet_names}")

        # Try to find 'data' or 'Sheet1', otherwise take the first sheet
        target_sheet = 'data' if 'data' in sheet_names else sheet_names[0]
        
        df = pd.read_excel(filepath, sheet_name=target_sheet)
        print(f"✅ Successfully loaded {len(df)} records from sheet: '{target_sheet}'")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

if __name__ == "__main__":
    path = "data/raw/ethiopia_fi_unified_data.xlsx"
    data = load_unified_data(path)