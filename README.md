# 📊 Retail Sales Data Analytics Dashboard

A comprehensive data analytics project that analyzes retail sales data using **Python (Pandas)** and visualizes insights through interactive **Power BI dashboards**. The project focuses on extracting meaningful business insights such as revenue trends, customer behavior, and regional performance.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)](https://pandas.pydata.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Latest-yellow.svg)](https://powerbi.microsoft.com/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

---

## 🚀 Project Overview

Retail businesses generate large amounts of transactional data, but raw data alone does not provide actionable insights.

This project builds a **complete analytics pipeline** that:

✅ Cleans and preprocesses retail sales data using Python  
✅ Performs Exploratory Data Analysis (EDA)  
✅ Transforms datasets for analytics  
✅ Builds interactive dashboards in Power BI  
✅ Generates insights to support data-driven business decisions

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Data processing and analysis |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) | Data manipulation and transformation |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) | Numerical computations |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat&logo=python&logoColor=white) | Data visualization |
| ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat&logo=python&logoColor=white) | Statistical visualizations |
| ![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black) | Interactive dashboards |

---

## 📂 Project Structure

```
Sales-Data-Analytics-Dashboard/
│
├── data/
│   ├── raw_sales_data.csv          # Original raw dataset
│   └── cleaned_sales_data.csv       # Cleaned and processed dataset
│
├── notebooks/
│   └── data_analysis.ipynb          # Jupyter notebook with EDA
│
├── scripts/
│   └── data_cleaning.py             # Python script for data cleaning
│
├── dashboard/
│   └── sales_dashboard.pbix         # Power BI dashboard file
│
├── images/
│   └── dashboard_preview.png        # Dashboard screenshot
│
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## 📊 Dataset Description

The retail sales dataset contains the following fields:

| Column | Description |
|--------|-------------|
| **Order ID** | Unique order identifier |
| **Order Date** | Date of purchase |
| **Product Category** | Category of product (Electronics, Furniture, Office Supplies) |
| **Product Name** | Name of product |
| **Sales** | Revenue generated |
| **Quantity** | Number of items sold |
| **Region** | Sales region (North, South, East, West) |
| **Customer Segment** | Customer type (Corporate, Consumer, Home Office) |
| **Profit** | Profit generated |
| **Discount** | Discount applied |

**Dataset Size**: 120+ transactions across 2023

---

## ⚙️ Data Processing Pipeline

### 1️⃣ Data Collection

Load dataset using Pandas:

```python
import pandas as pd

df = pd.read_csv("data/raw_sales_data.csv")
print(df.head())
```

### 2️⃣ Data Cleaning

Cleaning steps include:
- ✅ Removing duplicates
- ✅ Handling missing values
- ✅ Formatting dates
- ✅ Removing invalid records

```python
# Remove duplicates
df.drop_duplicates(inplace=True)

# Format dates
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Handle missing values
df.fillna({'Product Category': 'Unknown', 'Sales': 0}, inplace=True)
```

### 3️⃣ Data Transformation

Create additional features for analysis:

```python
# Extract date components
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Quarter'] = df['Order Date'].dt.quarter
df['Month Name'] = df['Order Date'].dt.month_name()

# Calculate metrics
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100
df['Revenue Per Unit'] = df['Sales'] / df['Quantity']
```

### 4️⃣ Exploratory Data Analysis

Key analyses performed:
- 📈 Monthly revenue trends
- 🌍 Sales by region
- 📦 Top performing product categories
- 👥 Customer segment performance

Example analysis:

```python
# Regional sales analysis
regional_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(regional_sales)

# Monthly trend analysis
monthly_trend = df.groupby('Month Name')['Sales'].sum()
monthly_trend.plot(kind='line', marker='o')
```

---

## 📈 Power BI Dashboard

An interactive **Power BI dashboard** was created to visualize key insights.

### Dashboard Features

📌 **Revenue KPI indicators**  
📌 **Monthly sales trends**  
📌 **Regional performance maps**  
📌 **Product category analysis**  
📌 **Customer segmentation**  
📌 **Interactive filters and drilldowns**

### How to Use the Dashboard

1. Open `dashboard/sales_dashboard.pbix` in Power BI Desktop
2. Connect to the cleaned dataset in `data/cleaned_sales_data.csv`
3. Refresh data to load latest information
4. Explore interactive visualizations and filters

---

## 💡 Key Business Insights

The analytics dashboard helps identify:

✅ **High revenue generating product categories**  
   - Electronics leads with highest revenue contribution
   - Furniture shows strong profit margins

✅ **Regions contributing the most to sales**  
   - Regional performance varies significantly
   - Opportunity to optimize underperforming regions

✅ **Seasonal patterns in customer purchasing**  
   - Q4 shows peak sales activity
   - Monthly trends reveal seasonal opportunities

✅ **Customer segments with highest profitability**  
   - Corporate segment has highest average order value
   - Consumer segment drives volume

### Strategic Recommendations

1. 🎯 **Focus marketing efforts** on best-performing regions
2. 📦 **Increase inventory** for high-revenue product categories
3. 👥 **Develop targeted campaigns** for high-value customer segments
4. 📅 **Leverage seasonal trends** for promotional planning
5. 💰 **Optimize discount strategies** to improve profit margins

---

## 📸 Dashboard Preview

![Dashboard Preview](images/dashboard_preview.png)

*Note: Add your Power BI dashboard screenshot to the `images/` folder*

---

## 🔮 Future Improvements

Possible extensions for the project:

- [ ] **Real-time sales analytics** using APIs
- [ ] **Integration with SQL databases** for automated data pipeline
- [ ] **Sales forecasting** using Machine Learning (ARIMA, Prophet)
- [ ] **Automated ETL pipelines** with Apache Airflow
- [ ] **Customer Lifetime Value (CLV)** analysis
- [ ] **Market basket analysis** for product recommendations
- [ ] **Predictive analytics** for inventory optimization
- [ ] **Web-based dashboard** using Plotly Dash or Streamlit

---

## 📌 How to Run the Project

### Prerequisites

- Python 3.8 or higher
- Power BI Desktop (for viewing dashboards)
- Jupyter Notebook or JupyterLab

### Installation Steps

1️⃣ **Clone the repository**

```bash
git clone https://github.com/yourusername/sales-data-analytics-dashboard.git
cd sales-data-analytics-dashboard
```

2️⃣ **Create a virtual environment** (optional but recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Install required libraries**

```bash
pip install -r requirements.txt
```

4️⃣ **Run the data cleaning script**

```bash
python scripts/data_cleaning.py
```

5️⃣ **Open and run the Jupyter notebook**

```bash
jupyter notebook notebooks/data_analysis.ipynb
```

6️⃣ **Open the Power BI dashboard**

```
Open Power BI Desktop → File → Open → Select dashboard/sales_dashboard.pbix
```

---

## 📦 Project Dependencies

```
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
jupyter>=1.0.0
openpyxl>=3.0.0
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 📝 Project Workflow

```mermaid
graph LR
    A[Raw Data] --> B[Data Cleaning]
    B --> C[Data Transformation]
    C --> D[Exploratory Analysis]
    D --> E[Visualization]
    E --> F[Power BI Dashboard]
    F --> G[Business Insights]
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Aman Panday**

- 💼 Data Analytics | Python | Power BI | Machine Learning Enthusiast
- 📧 Email: [your.email@example.com]
- 💼 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
- 🐙 GitHub: [github.com/yourusername](https://github.com/yourusername)

---

## 🙏 Acknowledgments

- Dataset inspiration from retail sales analysis projects
- Community contributions and feedback
- Open-source libraries and tools used in this project

---

## 📊 Project Stats

![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/sales-data-analytics-dashboard)
![GitHub issues](https://img.shields.io/github/issues/yourusername/sales-data-analytics-dashboard)
![GitHub stars](https://img.shields.io/github/stars/yourusername/sales-data-analytics-dashboard)

---

<div align="center">

### ⭐ If you find this project helpful, please give it a star!

Made with ❤️ by Aman Panday

</div>
