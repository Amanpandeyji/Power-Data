# Scripts Folder

This folder contains Python scripts for data processing and analysis.

## Available Scripts

### 1. data_cleaning.py
**Purpose:** Clean and preprocess raw sales data

**What it does:**
- Loads raw_sales_data.csv
- Removes duplicate records
- Handles missing values
- Formats dates properly
- Removes invalid records
- Adds derived features (Year, Month, Profit Margin, etc.)
- Generates cleaned_sales_data.csv
- Prints comprehensive data quality report

**How to run:**
```bash
python scripts/data_cleaning.py
```

**Expected output:**
```
==============================================================
RETAIL SALES DATA CLEANING PIPELINE
==============================================================
Loading data...
Data loaded successfully. Shape: (121, 10)

==================================================
DATA QUALITY REPORT
==================================================

Total Records: 121
Total Columns: 10

[... cleaning process ...]

✓ Cleaned data saved to: ../data/cleaned_sales_data.csv
Final dataset shape: (119, 17)

==============================================================
DATA CLEANING COMPLETED SUCCESSFULLY!
==============================================================
```

**Input:** `data/raw_sales_data.csv`  
**Output:** `data/cleaned_sales_data.csv`

---

### 2. quick_analysis.py
**Purpose:** Generate quick visualizations without running the full notebook

**What it does:**
- Loads cleaned sales data
- Creates 4 key visualizations:
  1. Revenue by Region (Bar chart)
  2. Category Distribution (Pie chart)
  3. Monthly Revenue Trend (Line chart)
  4. Top 10 Products (Horizontal bar chart)
- Displays summary metrics
- Saves dashboard image

**How to run:**
```bash
python scripts/quick_analysis.py
```

**Prerequisites:**
- Must run data_cleaning.py first
- Requires matplotlib and seaborn

**Expected output:**
```
✓ Data loaded successfully!
Records: 119

[Shows visualization window]

✓ Visualization saved as 'images/quick_analysis.png'

============================================================
QUICK SUMMARY
============================================================
Total Revenue: $XX,XXX.XX
Total Profit: $X,XXX.XX
Average Order: $XXX.XX
Total Orders: XXX
============================================================
```

**Input:** `data/cleaned_sales_data.csv`  
**Output:** 
- `images/quick_analysis.png` (saved chart)
- Display window with visualizations
- Console summary statistics

---

## Usage Workflow

### Complete Analysis Pipeline:

```bash
# Step 1: Clean the data
python scripts/data_cleaning.py

# Step 2: Quick visualization
python scripts/quick_analysis.py

# Step 3: Full analysis (optional)
jupyter notebook notebooks/data_analysis.ipynb
```

---

## Script Dependencies

Both scripts require:
```
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## Troubleshooting

### Error: "No module named 'pandas'"
**Solution:**
```bash
pip install pandas numpy matplotlib seaborn
```

### Error: "File not found: raw_sales_data.csv"
**Solution:**
- Ensure you're in the project root directory
- Check that data/raw_sales_data.csv exists
- Try running with full path

### Error: "Permission denied"
**Solution:**
- Close any programs using the CSV files
- Run terminal as administrator (Windows)
- Check file permissions

---

## Adding New Scripts

To add your own scripts:

1. Create a new .py file in this folder
2. Add appropriate imports
3. Include error handling
4. Add documentation
5. Update this README

Example template:
```python
"""
Script Name
Brief description of what it does
"""

import pandas as pd

def main():
    """Main function"""
    try:
        # Your code here
        pass
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

---

## Future Script Ideas

- `generate_report.py` - Create PDF reports
- `data_validation.py` - Validate data quality
- `export_to_excel.py` - Export analysis to Excel
- `update_dashboard.py` - Refresh Power BI data
- `send_email_report.py` - Email automated reports

---

Last Updated: March 11, 2026
