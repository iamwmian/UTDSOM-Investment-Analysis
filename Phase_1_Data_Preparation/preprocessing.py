#!/usr/bin/env python3
"""
Compustat Quarterly Data Preprocessing Script
===========================================

This script performs data cleaning and preprocessing on the Compustat Quarterly dataset
for the UTIMCO quantitative sector valuation analysis project.

Key tasks:
1. Load the raw Compustat quarterly data (2010-2025)
2. Explore dataset characteristics and structure
3. Remove rows with null values in GICS sector classification (gsector)
4. Generate metadata and cleaning log
5. Save cleaned dataset

Author: Wassil
Project: UTIMCO Quantitative Sector Valuation Analysis
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime

def main():
    """Main preprocessing function"""

    print("=== Compustat Quarterly Data Preprocessing ===\n")

    # File paths
    raw_data_path = "../Compustat Qtrly Data 2010-2025/Compustat_Quarterl_2010_2025.csv"
    cleaned_data_path = "Compustat_Quarterl_2010_2025_cleaned.csv"
    metadata_path = "data_preprocessing_metadata.txt"

    # Initialize metadata log
    metadata = []
    metadata.append("=== COMPUSTAT QUARTERLY DATA PREPROCESSING METADATA ===\n")
    metadata.append(f"Processing Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    metadata.append(f"Raw Data Source: {raw_data_path}\n")
    metadata.append(f"Cleaned Data Output: {cleaned_data_path}\n\n")

    try:
        # Step 1: Load the raw dataset
        print("1. Loading raw dataset...")
        df_raw = pd.read_csv(raw_data_path, low_memory=False)

        metadata.append("=== ORIGINAL DATASET CHARACTERISTICS ===\n")
        metadata.append(f"Number of rows: {len(df_raw):,}\n")
        metadata.append(f"Number of columns: {len(df_raw.columns)}\n")

        # Get basic info about key columns
        key_columns = ['gvkey', 'datadate', 'conm', 'gsector', 'gind', 'gsubind', 'prccq', 'epspxq', 'atq', 'seqq']
        metadata.append("\n=== KEY COLUMN ANALYSIS ===\n")

        for col in key_columns:
            if col in df_raw.columns:
                non_null = df_raw[col].notna().sum()
                null_count = df_raw[col].isna().sum()
                null_pct = (null_count / len(df_raw)) * 100
                metadata.append(f"{col:15} | Non-null: {non_null:8,} | Null: {null_count:8,} | Null %: {null_pct:5.2f}%\n")
            else:
                metadata.append(f"{col}: COLUMN NOT FOUND\n")

        # Step 2: Focus on GICS sector classification cleaning
        print("\n2. Analyzing GICS sector classification...")

        if 'gsector' in df_raw.columns:
            gsector_null_count = df_raw['gsector'].isna().sum()
            gsector_valid_count = df_raw['gsector'].notna().sum()

            metadata.append("\n=== GICS SECTOR CLASSIFICATION ANALYSIS ===\n")
            metadata.append(f"Total observations: {len(df_raw):,}\n")
            metadata.append(f"Valid GICS sector codes: {gsector_valid_count:,}\n")
            metadata.append(f"Missing GICS sector codes: {gsector_null_count:,}\n")
            metadata.append(f"Missing data rate: {(gsector_null_count / len(df_raw)) * 100:.2f}%\n")

            # Show distribution of GICS sectors
            sector_dist = df_raw['gsector'].value_counts().sort_index()
            metadata.append("\nGICS Sector Distribution (before cleaning):\n")
            for sector_code, count in sector_dist.items():
                metadata.append(f"  Sector {sector_code:2.0f}: {count:8,} observations\n")

            print(f"   Found {gsector_null_count:,} rows with missing GICS sector codes")
        else:
            raise ValueError("gsector column not found in dataset")

        # Step 3: Clean the dataset by removing rows with null gsector
        print("\n3. Cleaning dataset by removing rows with null GICS sectors...")

        df_cleaned = df_raw.dropna(subset=['gsector']).copy()

        metadata.append("\n\n=== CLEANED DATASET CHARACTERISTICS ===\n")
        metadata.append(f"Number of rows after cleaning: {len(df_cleaned):,}\n")
        metadata.append(f"Rows removed: {len(df_raw) - len(df_cleaned):,}\n")
        metadata.append(f"Data retention rate: {(len(df_cleaned) / len(df_raw)) * 100:.2f}%\n")

        # Update sector distribution after cleaning
        sector_dist_cleaned = df_cleaned['gsector'].value_counts().sort_index()
        metadata.append("\nGICS Sector Distribution (after cleaning):\n")
        for sector_code, count in sector_dist_cleaned.items():
            metadata.append(f"  Sector {sector_code:2.0f}: {count:8,} observations\n")

        # Step 4: Additional data quality checks
        print("\n4. Performing additional data quality checks...")

        metadata.append("\n\n=== DATA QUALITY CHECKS ===\n")

        # Check for other critical missing values in key financial variables
        critical_vars = ['prccq', 'epspxq', 'atq', 'seqq']
        for var in critical_vars:
            if var in df_cleaned.columns:
                null_count = df_cleaned[var].isna().sum()
                null_pct = (null_count / len(df_cleaned)) * 100
                metadata.append(f"{var:8} | Null count: {null_count:8,} | Null %: {null_pct:5.2f}%\n")

        # Check date range
        if 'datadate' in df_cleaned.columns:
            df_cleaned['datadate'] = pd.to_datetime(df_cleaned['datadate'], errors='coerce')
            date_range = df_cleaned['datadate'].agg(['min', 'max'])
            metadata.append(f"\nDate range: {date_range['min']} to {date_range['max']}\n")

        # Check number of unique companies
        if 'gvkey' in df_cleaned.columns:
            unique_companies = df_cleaned['gvkey'].nunique()
            metadata.append(f"Number of unique companies (GVKEY): {unique_companies:,}\n")

        # Step 5: Save cleaned dataset
        print("\n5. Saving cleaned dataset...")

        # Ensure output directory exists
        os.makedirs(os.path.dirname(cleaned_data_path) if os.path.dirname(cleaned_data_path) else '.', exist_ok=True)

        df_cleaned.to_csv(cleaned_data_path, index=False)
        metadata.append(f"\nCleaned dataset saved to: {cleaned_data_path}\n")
        metadata.append(f"File size: {os.path.getsize(cleaned_data_path):,} bytes\n")

        print(f"   Cleaned dataset saved with {len(df_cleaned):,} rows")

        # Step 6: Save metadata log
        print("\n6. Saving preprocessing metadata...")

        with open(metadata_path, 'w') as f:
            f.writelines(metadata)

        print(f"   Metadata saved to: {metadata_path}")

        print("\n=== PREPROCESSING COMPLETED SUCCESSFULLY ===")
        print(f"Original dataset: {len(df_raw):,} rows")
        print(f"Cleaned dataset: {len(df_cleaned):,} rows")
        print(f"Rows removed: {len(df_raw) - len(df_cleaned):,}")

    except Exception as e:
        error_msg = f"\nERROR during preprocessing: {str(e)}\n"
        print(error_msg)

        # Save error to metadata file
        with open(metadata_path, 'w') as f:
            f.write("=== PREPROCESSING ERROR LOG ===\n")
            f.write(error_msg)
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        raise

if __name__ == "__main__":
    main()
