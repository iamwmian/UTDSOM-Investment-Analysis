#!/usr/bin/env python3
"""
Financial Ratio Calculation Script - Phase 2: Algorithm Development
==================================================================

This script performs financial ratio calculations on the cleaned Compustat dataset
for the UTIMCO quantitative sector valuation analysis project.

Key tasks:
1. Load the cleaned dataset from Phase 1
2. Calculate Price-to-Earnings (P/E) ratio for each firm-quarter
3. Calculate Market-to-Book (M/B) ratio for each firm-quarter
4. Handle missing values and data quality issues
5. Create time-series dataset with ratio calculations
6. Generate comprehensive logging of calculations and findings

Author: Wassil
Project: UTIMCO Quantitative Sector Valuation Analysis
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime

def main():
    """Main ratio calculation function"""

    print("=== Financial Ratio Calculation - Phase 2 ===\n")

    # File paths
    input_path = "../Phase_1_Data_Preparation/Compustat_Quarterl_2010_2025_cleaned.csv"
    output_path = "Compustat_Ratios_TimeSeries.csv"
    log_path = "ratio_calculation_log.txt"

    # Initialize log
    log = []
    log.append("=== FINANCIAL RATIO CALCULATION LOG ===\n")
    log.append(f"Processing Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    log.append(f"Input Data: {input_path}\n")
    log.append(f"Output Data: {output_path}\n\n")

    try:
        # Step 1: Load cleaned dataset
        print("1. Loading cleaned dataset...")
        df = pd.read_csv(input_path, low_memory=False)

        log.append("=== INPUT DATASET CHARACTERISTICS ===\n")
        log.append(f"Number of rows: {len(df):,}\n")
        log.append(f"Number of columns: {len(df.columns)}\n")
        log.append(f"Date range: {df['datadate'].min()} to {df['datadate'].max()}\n")
        log.append(f"Unique companies: {df['gvkey'].nunique():,}\n")

        # Step 2: Data preparation and validation
        print("\n2. Preparing data for ratio calculations...")

        # Ensure date column is datetime
        df['datadate'] = pd.to_datetime(df['datadate'], errors='coerce')

        # Create calendar quarter identifier for time-series analysis
        df['quarter'] = df['datadate'].dt.to_period('Q').astype(str)
        df['year'] = df['datadate'].dt.year

        log.append("\n=== TIME-SERIES STRUCTURE ===\n")
        log.append(f"Calendar quarters covered: {df['quarter'].nunique()}\n")
        log.append(f"Years covered: {df['year'].min()} - {df['year'].max()}\n")

        # Step 3: Calculate P/E Ratio
        print("\n3. Calculating Price-to-Earnings (P/E) ratios...")

        # P/E = Market Price / Earnings Per Share
        # prccq = quarterly closing price
        # epspxq = quarterly EPS excluding extraordinary items

        df['PE_ratio'] = df['prccq'] / df['epspxq']

        # Handle edge cases
        df['PE_ratio'] = df['PE_ratio'].replace([np.inf, -np.inf], np.nan)

        pe_stats = df['PE_ratio'].describe()
        pe_null_pct = (df['PE_ratio'].isna().sum() / len(df)) * 100

        log.append("\n=== PRICE-TO-EARNINGS (P/E) RATIO CALCULATION ===\n")
        log.append("Formula: PE_ratio = prccq / epspxq\n")
        log.append(f"Successfully calculated: {df['PE_ratio'].notna().sum():,} ratios\n")
        log.append(f"Missing ratios: {df['PE_ratio'].isna().sum():,} ({pe_null_pct:.2f}%)\n")
        log.append("P/E Ratio Statistics (excluding missing):\n")
        log.append(f"  Mean: {pe_stats['mean']:.2f}\n")
        log.append(f"  Median: {pe_stats['50%']:.2f}\n")
        log.append(f"  Std Dev: {pe_stats['std']:.2f}\n")
        log.append(f"  Min: {pe_stats['min']:.2f}\n")
        log.append(f"  Max: {pe_stats['max']:.2f}\n")

        # Step 4: Calculate Market-to-Book (M/B) Ratio
        print("\n4. Calculating Market-to-Book (M/B) ratios...")

        # M/B = (Market Cap + Total Debt - Cash) / Total Assets
        # Market Cap = prccq * cshoq
        # Total Debt = dlcq + dlttq (short-term + long-term debt)
        # Cash = cheq
        # Total Assets = atq

        # Calculate components
        df['market_cap'] = df['prccq'] * df['cshoq']
        df['total_debt'] = df['dlcq'].fillna(0) + df['dlttq'].fillna(0)
        df['net_debt'] = df['total_debt'] - df['cheq'].fillna(0)
        df['enterprise_value'] = df['market_cap'] + df['net_debt']

        # Calculate M/B ratio
        df['MB_ratio'] = df['enterprise_value'] / df['atq']

        # Handle edge cases
        df['MB_ratio'] = df['MB_ratio'].replace([np.inf, -np.inf], np.nan)

        mb_stats = df['MB_ratio'].describe()
        mb_null_pct = (df['MB_ratio'].isna().sum() / len(df)) * 100

        log.append("\n=== MARKET-TO-BOOK (M/B) RATIO CALCULATION ===\n")
        log.append("Formula: MB_ratio = (prccq * cshoq + dlcq + dlttq - cheq) / atq\n")
        log.append(f"Successfully calculated: {df['MB_ratio'].notna().sum():,} ratios\n")
        log.append(f"Missing ratios: {df['MB_ratio'].isna().sum():,} ({mb_null_pct:.2f}%)\n")
        log.append("M/B Ratio Statistics (excluding missing):\n")
        log.append(f"  Mean: {mb_stats['mean']:.2f}\n")
        log.append(f"  Median: {mb_stats['50%']:.2f}\n")
        log.append(f"  Std Dev: {mb_stats['std']:.2f}\n")
        log.append(f"  Min: {mb_stats['min']:.2f}\n")
        log.append(f"  Max: {mb_stats['max']:.2f}\n")

        # Step 5: Data quality assessment
        print("\n5. Assessing data quality and ratio distributions...")

        # Check for negative ratios (potential data issues)
        negative_pe = (df['PE_ratio'] < 0).sum()
        negative_mb = (df['MB_ratio'] < 0).sum()

        log.append("\n=== DATA QUALITY ASSESSMENT ===\n")
        log.append(f"Negative P/E ratios: {negative_pe:,} ({negative_pe/len(df)*100:.2f}%)\n")
        log.append(f"Negative M/B ratios: {negative_mb:,} ({negative_mb/len(df)*100:.2f}%)\n")

        # Check extreme values
        extreme_pe_high = (df['PE_ratio'] > 1000).sum()
        extreme_mb_high = (df['MB_ratio'] > 100).sum()

        log.append(f"P/E ratios > 1000: {extreme_pe_high:,}\n")
        log.append(f"M/B ratios > 100: {extreme_mb_high:,}\n")

        # Step 6: Sector-level summary statistics
        print("\n6. Generating sector-level summary statistics...")

        sector_stats = df.groupby('gsector').agg({
            'PE_ratio': ['count', 'mean', 'median', 'std'],
            'MB_ratio': ['count', 'mean', 'median', 'std'],
            'gvkey': 'nunique'
        }).round(2)

        log.append("\n=== SECTOR-LEVEL RATIO STATISTICS ===\n")
        log.append("Statistics by GICS Sector (mean, median, std dev):\n\n")

        sector_names = {
            10: 'Energy', 15: 'Materials', 20: 'Industrials', 25: 'Consumer Discretionary',
            30: 'Consumer Staples', 35: 'Health Care', 40: 'Financials', 45: 'Information Technology',
            50: 'Communication Services', 55: 'Utilities', 60: 'Real Estate'
        }

        for sector_code in sorted(sector_names.keys()):
            if sector_code in sector_stats.index:
                stats = sector_stats.loc[sector_code]
                log.append(f"Sector {sector_code} ({sector_names[sector_code]}):\n")
                log.append(f"  Companies: {stats[('gvkey', 'nunique')]:,}\n")
                log.append(f"  P/E - Count: {stats[('PE_ratio', 'count')]:,} | Mean: {stats[('PE_ratio', 'mean')]} | Median: {stats[('PE_ratio', 'median')]} | Std: {stats[('PE_ratio', 'std')]}\n")
                log.append(f"  M/B - Count: {stats[('MB_ratio', 'count')]:,} | Mean: {stats[('MB_ratio', 'mean')]} | Median: {stats[('MB_ratio', 'median')]} | Std: {stats[('MB_ratio', 'std')]}\n")
                log.append("\n")

        # Step 7: Create final time-series dataset
        print("\n7. Creating final time-series dataset...")

        # Select relevant columns for output
        output_columns = [
            'gvkey', 'conm', 'datadate', 'quarter', 'year', 'gsector',
            'prccq', 'epspxq', 'PE_ratio',
            'market_cap', 'total_debt', 'cheq', 'atq', 'MB_ratio'
        ]

        df_output = df[output_columns].copy()

        # Sort by company and date for time-series integrity
        df_output = df_output.sort_values(['gvkey', 'datadate'])

        log.append("=== OUTPUT DATASET STRUCTURE ===\n")
        log.append(f"Final dataset rows: {len(df_output):,}\n")
        log.append(f"Final dataset columns: {len(df_output.columns)}\n")
        log.append(f"Columns included: {', '.join(output_columns)}\n")

        # Step 8: Save results
        print("\n8. Saving results...")

        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)

        df_output.to_csv(output_path, index=False)

        log.append(f"\nOutput saved to: {output_path}\n")
        log.append(f"File size: {os.path.getsize(output_path):,} bytes\n")

        # Save log
        with open(log_path, 'w') as f:
            f.writelines(log)

        print(f"   Time-series dataset saved with {len(df_output):,} rows")
        print(f"   Log saved to: {log_path}")

        print("\n=== RATIO CALCULATION COMPLETED SUCCESSFULLY ===")
        print(f"P/E ratios calculated: {df['PE_ratio'].notna().sum():,}")
        print(f"M/B ratios calculated: {df['MB_ratio'].notna().sum():,}")
        print(f"Output file: {output_path}")

    except Exception as e:
        error_msg = f"\nERROR during ratio calculation: {str(e)}\n"
        print(error_msg)

        # Save error to log file
        with open(log_path, 'w') as f:
            f.write("=== RATIO CALCULATION ERROR LOG ===\n")
            f.write(error_msg)
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        raise

if __name__ == "__main__":
    main()
