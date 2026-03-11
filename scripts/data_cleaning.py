"""
Data Cleaning Script for Retail Sales Data
Author: Aman Panday
Description: This script cleans and preprocesses raw retail sales data
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

def load_data(file_path):
    """Load raw sales data from CSV file"""
    print("Loading data...")
    df = pd.read_csv(file_path)
    print(f"Data loaded successfully. Shape: {df.shape}")
    return df

def check_data_quality(df):
    """Check data quality and print summary"""
    print("\n" + "="*50)
    print("DATA QUALITY REPORT")
    print("="*50)
    
    print(f"\nTotal Records: {len(df)}")
    print(f"Total Columns: {len(df.columns)}")
    
    print("\nMissing Values:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Column': missing.index,
        'Missing Count': missing.values,
        'Percentage': missing_pct.values
    })
    print(missing_df[missing_df['Missing Count'] > 0])
    
    print(f"\nDuplicate Records: {df.duplicated().sum()}")
    
    print("\nData Types:")
    print(df.dtypes)
    
    return df

def remove_duplicates(df):
    """Remove duplicate records"""
    initial_count = len(df)
    df = df.drop_duplicates()
    removed_count = initial_count - len(df)
    print(f"\n✓ Removed {removed_count} duplicate records")
    return df

def handle_missing_values(df):
    """Handle missing values in the dataset"""
    print("\n" + "="*50)
    print("HANDLING MISSING VALUES")
    print("="*50)
    
    # Fill missing Product Category with 'Unknown'
    if df['Product Category'].isnull().any():
        df['Product Category'].fillna('Unknown', inplace=True)
        print("✓ Filled missing Product Category with 'Unknown'")
    
    # Fill missing Product Name with 'Unknown Product'
    if df['Product Name'].isnull().any():
        df['Product Name'].fillna('Unknown Product', inplace=True)
        print("✓ Filled missing Product Name with 'Unknown Product'")
    
    # Fill numeric columns with 0
    numeric_columns = ['Sales', 'Quantity', 'Profit', 'Discount']
    for col in numeric_columns:
        if df[col].isnull().any():
            df[col].fillna(0, inplace=True)
            print(f"✓ Filled missing {col} with 0")
    
    # Fill missing categorical columns
    categorical_columns = ['Region', 'Customer Segment']
    for col in categorical_columns:
        if df[col].isnull().any():
            df[col].fillna('Unknown', inplace=True)
            print(f"✓ Filled missing {col} with 'Unknown'")
    
    return df

def format_dates(df):
    """Convert Order Date to datetime format"""
    print("\n✓ Converting Order Date to datetime format...")
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    
    # Remove records with invalid dates
    invalid_dates = df['Order Date'].isnull().sum()
    if invalid_dates > 0:
        df = df[df['Order Date'].notnull()]
        print(f"✓ Removed {invalid_dates} records with invalid dates")
    
    return df

def remove_invalid_records(df):
    """Remove records with invalid or negative values"""
    print("\n" + "="*50)
    print("REMOVING INVALID RECORDS")
    print("="*50)
    
    initial_count = len(df)
    
    # Remove records with negative sales or profit
    df = df[df['Sales'] >= 0]
    df = df[df['Quantity'] > 0]
    
    # Remove records with discount >= 1 (should be percentage)
    df = df[df['Discount'] < 1]
    
    removed_count = initial_count - len(df)
    print(f"✓ Removed {removed_count} invalid records")
    
    return df

def add_derived_features(df):
    """Add derived features for analysis"""
    print("\n" + "="*50)
    print("ADDING DERIVED FEATURES")
    print("="*50)
    
    # Extract date components
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['Month Name'] = df['Order Date'].dt.month_name()
    df['Quarter'] = df['Order Date'].dt.quarter
    df['Day of Week'] = df['Order Date'].dt.day_name()
    df['Week'] = df['Order Date'].dt.isocalendar().week
    
    # Calculate profit margin
    df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100
    df['Profit Margin'] = df['Profit Margin'].round(2)
    
    # Calculate revenue per unit
    df['Revenue Per Unit'] = (df['Sales'] / df['Quantity']).round(2)
    
    print("✓ Added Year, Month, Quarter columns")
    print("✓ Added Month Name and Day of Week")
    print("✓ Calculated Profit Margin")
    print("✓ Calculated Revenue Per Unit")
    
    return df

def save_cleaned_data(df, output_path):
    """Save cleaned data to CSV"""
    df.to_csv(output_path, index=False)
    print(f"\n✓ Cleaned data saved to: {output_path}")
    print(f"Final dataset shape: {df.shape}")

def main():
    """Main execution function"""
    print("\n" + "="*60)
    print("RETAIL SALES DATA CLEANING PIPELINE")
    print("="*60)
    
    # File paths
    input_file = "../data/raw_sales_data.csv"
    output_file = "../data/cleaned_sales_data.csv"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        input_file = "data/raw_sales_data.csv"
        output_file = "data/cleaned_sales_data.csv"
    
    try:
        # Load data
        df = load_data(input_file)
        
        # Check data quality
        df = check_data_quality(df)
        
        # Data cleaning steps
        df = remove_duplicates(df)
        df = format_dates(df)
        df = handle_missing_values(df)
        df = remove_invalid_records(df)
        
        # Add derived features
        df = add_derived_features(df)
        
        # Save cleaned data
        save_cleaned_data(df, output_file)
        
        print("\n" + "="*60)
        print("DATA CLEANING COMPLETED SUCCESSFULLY!")
        print("="*60)
        
        # Display sample of cleaned data
        print("\nSample of cleaned data:")
        print(df.head(10).to_string())
        
        print("\nSummary Statistics:")
        print(df[['Sales', 'Quantity', 'Profit', 'Discount']].describe())
        
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()
