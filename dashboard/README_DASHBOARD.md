# Power BI Dashboard Creation Guide

## Overview
This folder contains the Power BI dashboard file for the Retail Sales Analytics project.

## Creating the Dashboard

### Step 1: Import Data
1. Open Power BI Desktop
2. Click **Get Data** → **Text/CSV**
3. Navigate to `../data/cleaned_sales_data.csv`
4. Click **Load**

### Step 2: Data Modeling
1. Verify data types for all columns
2. Create relationships if using multiple tables
3. Create calculated columns and measures as needed

### Step 3: Create Visualizations

#### Recommended Visualizations:

**1. KPI Cards**
- Total Revenue
- Total Profit
- Total Orders
- Average Order Value
- Profit Margin %

**2. Line Chart - Revenue Trend**
- X-axis: Order Date (Month)
- Y-axis: Sales
- Add trend line

**3. Bar Chart - Revenue by Region**
- X-axis: Region
- Y-axis: Sales
- Sort: Descending

**4. Pie Chart - Category Distribution**
- Legend: Product Category
- Values: Sales
- Show percentages

**5. Map Visualization - Regional Performance**
- Location: Region
- Size: Sales
- Color: Profit

**6. Matrix - Category × Segment**
- Rows: Product Category
- Columns: Customer Segment
- Values: Sales

**7. Stacked Column Chart - Monthly Revenue by Category**
- X-axis: Month Name
- Y-axis: Sales
- Legend: Product Category

**8. Donut Chart - Customer Segment Revenue**
- Legend: Customer Segment
- Values: Sales

### Step 4: Add Interactivity

#### Filters/Slicers:
- Date Range (Order Date)
- Region (Multi-select)
- Product Category (Multi-select)
- Customer Segment (Multi-select)

#### Drill-through Pages:
- Product Details
- Regional Analysis
- Customer Segment Analysis

### Step 5: Design and Formatting
1. Apply consistent color scheme
2. Add company logo/branding
3. Use clear, descriptive titles
4. Add data labels where appropriate
5. Configure tooltips for additional context

### Step 6: DAX Measures

Create these calculated measures for enhanced analytics:

```dax
Total Revenue = SUM(Sales[Sales])

Total Profit = SUM(Sales[Profit])

Profit Margin = 
DIVIDE(
    [Total Profit],
    [Total Revenue],
    0
) * 100

Average Order Value = 
DIVIDE(
    [Total Revenue],
    DISTINCTCOUNT(Sales[Order ID]),
    0
)

YTD Revenue = 
TOTALYTD(
    [Total Revenue],
    Sales[Order Date]
)

Previous Month Revenue = 
CALCULATE(
    [Total Revenue],
    PREVIOUSMONTH(Sales[Order Date])
)

Revenue Growth % = 
DIVIDE(
    [Total Revenue] - [Previous Month Revenue],
    [Previous Month Revenue],
    0
) * 100

Top Region = 
FIRSTNONBLANK(
    TOPN(1, 
        VALUES(Sales[Region]), 
        [Total Revenue], 
        DESC
    ),
    1
)
```

### Step 7: Publishing (Optional)
1. Save your .pbix file
2. Click **Publish** to Power BI Service
3. Configure refresh schedule if using live data

## Dashboard Best Practices

✅ **Keep it simple** - Focus on key metrics  
✅ **Use consistent colors** - Maintain visual hierarchy  
✅ **Add context** - Include comparisons and benchmarks  
✅ **Enable interactivity** - Use filters and drill-downs  
✅ **Test performance** - Optimize for quick loading  
✅ **Mobile optimization** - Create mobile layouts  

## Sample Dashboard Layout

```
+-----------------+------------------+------------------+
|  Total Revenue  |   Total Profit   |  Total Orders    |
|    $XX,XXX      |     $X,XXX       |      XXX         |
+-----------------+------------------+------------------+
|                                                        |
|         Monthly Revenue Trend (Line Chart)            |
|                                                        |
+------------------------+-------------------------------+
|  Revenue by Region     |  Category Distribution       |
|  (Bar Chart)           |  (Pie Chart)                 |
+------------------------+-------------------------------+
|  Regional Map          |  Customer Segment Analysis   |
|  (Map Visual)          |  (Donut Chart)               |
+------------------------+-------------------------------+
```

## Tips for Creating Effective Dashboards

1. **Start with the end user in mind** - What questions do they need answered?
2. **Follow the rule of thirds** - Organize visual elements in a balanced layout
3. **Use conditional formatting** - Highlight key insights automatically
4. **Add bookmarks** - Create navigation between different views
5. **Include a date stamp** - Show when data was last refreshed

## Resources

- [Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/)
- [DAX Reference](https://dax.guide/)
- [Power BI Community](https://community.powerbi.com/)

---

**Note**: After creating your dashboard, save it as `sales_dashboard.pbix` in this folder and take a screenshot for the README.
