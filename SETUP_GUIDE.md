# 🚀 Quick Setup Guide

## Prerequisites Installation

### 1. Install Python

#### Windows:
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. ✅ **IMPORTANT**: Check "Add Python to PATH" during installation
4. Verify installation:
   ```bash
   python --version
   ```

#### macOS:
```bash
# Using Homebrew
brew install python3

# Verify
python3 --version
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip

# Verify
python3 --version
```

### 2. Install Power BI Desktop

1. Download from [Microsoft Power BI](https://powerbi.microsoft.com/desktop/)
2. Run the installer
3. Launch Power BI Desktop

---

## Project Setup

### Step 1: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Verify Installation

```bash
python -c "import pandas, numpy, matplotlib, seaborn; print('✓ All libraries installed successfully!')"
```

---

## Running the Project

### Option 1: Run Full Pipeline

```bash
# 1. Clean the data
python scripts/data_cleaning.py

# 2. Open Jupyter notebook for analysis
jupyter notebook notebooks/data_analysis.ipynb

# 3. Create Power BI dashboard (manual step)
# Open Power BI Desktop → Load cleaned_sales_data.csv → Create visualizations
```

### Option 2: Step-by-Step Execution

#### Step A: Data Cleaning
```bash
cd "c:\Users\asus\Downloads\Power Data"
python scripts\data_cleaning.py
```

**Expected Output:**
- Creates `data/cleaned_sales_data.csv`
- Prints data quality report
- Shows cleaning statistics

#### Step B: Data Analysis
```bash
jupyter notebook notebooks/data_analysis.ipynb
```

**What to do:**
1. Jupyter will open in your browser
2. Click on `data_analysis.ipynb`
3. Run all cells (Cell → Run All)
4. Explore the visualizations

#### Step C: Power BI Dashboard
1. Open Power BI Desktop
2. Get Data → Text/CSV → Select `data/cleaned_sales_data.csv`
3. Create visualizations using the guide in `dashboard/README_DASHBOARD.md`

---

## Troubleshooting

### Issue: Python not found

**Solution:**
```bash
# Verify Python installation
where python

# If not found, reinstall Python with "Add to PATH" option
```

### Issue: Module not found (e.g., pandas, numpy)

**Solution:**
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Issue: Permission denied

**Solution:**
```bash
# Windows: Run as Administrator
# macOS/Linux: Use sudo (for system-wide installation)
pip install --user -r requirements.txt
```

### Issue: Jupyter notebook won't open

**Solution:**
```bash
# Install/reinstall Jupyter
pip install --upgrade jupyter notebook

# Try running with full command
python -m jupyter notebook
```

### Issue: Can't find cleaned_sales_data.csv

**Solution:**
```bash
# Make sure you ran the cleaning script first
python scripts/data_cleaning.py

# Check if file exists
dir data
```

---

## Project Directory After Setup

```
Sales-Data-Analytics-Dashboard/
│
├── data/
│   ├── raw_sales_data.csv          ✓ Created
│   └── cleaned_sales_data.csv       ✓ Generated after running cleaning script
│
├── notebooks/
│   └── data_analysis.ipynb          ✓ Created
│
├── scripts/
│   └── data_cleaning.py             ✓ Created
│
├── dashboard/
│   ├── sales_dashboard.pbix         ⚠ Create manually in Power BI
│   └── README_DASHBOARD.md          ✓ Created (guide)
│
├── images/
│   ├── dashboard_preview.png        ⚠ Add after creating dashboard
│   └── README.md                    ✓ Created (instructions)
│
├── venv/                            ✓ Created after virtual env setup
├── requirements.txt                 ✓ Created
├── README.md                        ✓ Created
├── .gitignore                       ✓ Created
└── SETUP_GUIDE.md                   ✓ This file
```

---

## Quick Command Reference

### Python/Pip Commands
```bash
# Install package
pip install package_name

# Install from requirements
pip install -r requirements.txt

# List installed packages
pip list

# Upgrade package
pip install --upgrade package_name
```

### Jupyter Commands
```bash
# Start Jupyter Notebook
jupyter notebook

# Start JupyterLab
jupyter lab

# List running notebooks
jupyter notebook list

# Stop Jupyter server
# Press Ctrl+C in terminal
```

### Virtual Environment
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Deactivate
deactivate
```

---

## Testing Your Setup

Run this test script to verify everything works:

```bash
python -c "
import sys
print(f'Python version: {sys.version}')

try:
    import pandas as pd
    print('✓ Pandas installed')
    
    import numpy as np
    print('✓ NumPy installed')
    
    import matplotlib.pyplot as plt
    print('✓ Matplotlib installed')
    
    import seaborn as sns
    print('✓ Seaborn installed')
    
    print('\n✓✓✓ All requirements satisfied! You can proceed with the project.')
except ImportError as e:
    print(f'\n❌ Error: {e}')
    print('Run: pip install -r requirements.txt')
"
```

---

## Next Steps

After setup is complete:

1. ✅ Run `python scripts/data_cleaning.py`
2. ✅ Open and explore `notebooks/data_analysis.ipynb`
3. ✅ Review the generated insights
4. ✅ Create Power BI dashboard following the guide
5. ✅ Take screenshots and add to `images/` folder
6. ✅ Update README.md with your contact info

---

## Getting Help

- **Python Issues**: [Python Documentation](https://docs.python.org/)
- **Pandas Help**: [Pandas Documentation](https://pandas.pydata.org/docs/)
- **Power BI Help**: [Power BI Documentation](https://docs.microsoft.com/power-bi/)
- **Jupyter Issues**: [Jupyter Documentation](https://jupyter-notebook.readthedocs.io/)

---

## Contact & Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Review error messages carefully
3. Search for error messages online
4. Check project issues on GitHub
5. Reach out to the project maintainer

---

**Ready to start? Run:**

```bash
pip install -r requirements.txt
python scripts/data_cleaning.py
jupyter notebook notebooks/data_analysis.ipynb
```

Good luck with your data analytics project! 🚀📊
