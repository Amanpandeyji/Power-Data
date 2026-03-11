"""
Quick Visualization Script
Generate sample charts without running full notebook
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def quick_analysis():
    """Run quick analysis on cleaned data"""
    
    try:
        # Load cleaned data
        df = pd.read_csv('data/cleaned_sales_data.csv')
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        
        print("✓ Data loaded successfully!")
        print(f"Records: {len(df)}")
        
        # Set style
        plt.style.use('seaborn-v0_8-darkgrid')
        
        # Create figure with subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Retail Sales Quick Analytics Dashboard', fontsize=16, fontweight='bold')
        
        # 1. Revenue by Region
        regional_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
        regional_sales.plot(kind='bar', ax=axes[0, 0], color='steelblue')
        axes[0, 0].set_title('Revenue by Region', fontweight='bold')
        axes[0, 0].set_ylabel('Revenue ($)')
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # 2. Category Distribution
        category_sales = df.groupby('Product Category')['Sales'].sum()
        axes[0, 1].pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=90)
        axes[0, 1].set_title('Revenue by Category', fontweight='bold')
        
        # 3. Monthly Trend
        monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
        monthly_sales.plot(kind='line', marker='o', ax=axes[1, 0], color='green', linewidth=2)
        axes[1, 0].set_title('Monthly Revenue Trend', fontweight='bold')
        axes[1, 0].set_ylabel('Revenue ($)')
        axes[1, 0].grid(True, alpha=0.3)
        
        # 4. Top 10 Products
        top_products = df.groupby('Product Name')['Sales'].sum().nlargest(10)
        top_products.plot(kind='barh', ax=axes[1, 1], color='coral')
        axes[1, 1].set_title('Top 10 Products by Revenue', fontweight='bold')
        axes[1, 1].set_xlabel('Revenue ($)')
        
        plt.tight_layout()
        plt.savefig('images/quick_analysis.png', dpi=300, bbox_inches='tight')
        print("\n✓ Visualization saved as 'images/quick_analysis.png'")
        plt.show()
        
        # Print summary
        print("\n" + "="*60)
        print("QUICK SUMMARY")
        print("="*60)
        print(f"Total Revenue: ${df['Sales'].sum():,.2f}")
        print(f"Total Profit: ${df['Profit'].sum():,.2f}")
        print(f"Average Order: ${df['Sales'].mean():,.2f}")
        print(f"Total Orders: {df['Order ID'].nunique()}")
        print("="*60)
        
    except FileNotFoundError:
        print("❌ Error: cleaned_sales_data.csv not found!")
        print("Please run: python scripts/data_cleaning.py first")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    quick_analysis()
