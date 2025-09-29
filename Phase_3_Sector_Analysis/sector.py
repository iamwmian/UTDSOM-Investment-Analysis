#!/usr/bin/env python3
"""
Sector-Level Financial Ratio Analysis Script - Phase 3: Sector Analysis
==========================================================================

This script performs sector-level aggregation and analysis of P/E and Market-to-Book ratios
for the UTIMCO quantitative sector valuation analysis project.

Key tasks:
1. Load the time-series ratio data from Phase 2
2. Aggregate ratios by GICS sector and quarter
3. Calculate mean, median, and variance for each sector-quarter combination
4. Perform time-series trend analysis for each sector
5. Generate statistical summary datasets
6. Create visualization plots for trend identification
7. Generate comprehensive logging of findings and trends

Author: Wassil
Project: UTIMCO Quantitative Sector Valuation Analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime
from scipy import stats

def main():
    """Main sector analysis function"""

    print("=== Sector-Level Financial Ratio Analysis ===\n")

    # Set up plotting style
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")

    # Load data from Phase 2
    input_file = "../Phase_2_Algorithm_Development/Compustat_Ratios_TimeSeries.csv"
    print(f"Loading data from: {input_file}")

    try:
        df = pd.read_csv(input_file, low_memory=False)
        print(f"Loaded {len(df):,} observations")
    except FileNotFoundError:
        print(f"Error: Could not find {input_file}")
        return

    # Create log file
    log_entries = []
    log_entries.append("=== SECTOR-LEVEL FINANCIAL RATIO ANALYSIS LOG ===")
    log_entries.append(f"Processing Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_entries.append(f"Input Data: {input_file}")
    log_entries.append("")

    # Basic data exploration
    log_entries.append("=== INPUT DATA CHARACTERISTICS ===")
    log_entries.append(f"Total observations: {len(df):,}")
    log_entries.append(f"Unique companies: {df['gvkey'].nunique():,}")
    log_entries.append(f"Date range: {df['datadate'].min()} to {df['datadate'].max()}")
    log_entries.append(f"Sectors represented: {sorted(df['gsector'].unique())}")
    log_entries.append("")

    # Clean data for analysis
    df_clean = clean_data_for_analysis(df, log_entries)

    # Perform sector-quarter aggregation
    sector_stats = perform_sector_aggregation(df_clean, log_entries)

    # Save aggregated results
    output_csv = "Compustat_Sector_Statistics.csv"
    sector_stats.to_csv(output_csv, index=False)
    log_entries.append(f"Sector statistics saved to: {output_csv}")

    # Perform trend analysis
    perform_trend_analysis(sector_stats, log_entries)

    # Create visualizations
    create_sector_visualizations(sector_stats, log_entries)

    # Save log file
    log_filename = "sector_analysis_log.txt"
    with open(log_filename, 'w') as f:
        f.write('\n'.join(log_entries))

    print(f"\nAnalysis complete. Results saved to {output_csv}")
    print(f"Log saved to {log_filename}")

def clean_data_for_analysis(df, log_entries):
    """Clean data for sector analysis"""

    log_entries.append("=== DATA CLEANING FOR SECTOR ANALYSIS ===")

    # Remove rows with missing ratios
    original_count = len(df)
    df_clean = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['PE_ratio', 'MB_ratio'])

    log_entries.append(f"Original observations: {original_count:,}")
    log_entries.append(f"After removing missing ratios: {len(df_clean):,}")
    log_entries.append(".1f")
    log_entries.append("")

    # Ensure proper data types
    df_clean['datadate'] = pd.to_datetime(df_clean['datadate'])
    df_clean['year'] = df_clean['year'].astype(int)
    df_clean['gsector'] = df_clean['gsector'].astype(int)

    return df_clean

def perform_sector_aggregation(df_clean, log_entries):
    """Aggregate ratios by sector and quarter"""

    log_entries.append("=== SECTOR-QUARTER AGGREGATION ANALYSIS ===")

    # Group by sector and quarter, calculate statistics
    sector_stats = df_clean.groupby(['gsector', 'quarter']).agg(
        # P/E Ratio statistics
        PE_count=('PE_ratio', 'count'),
        PE_mean=('PE_ratio', 'mean'),
        PE_median=('PE_ratio', lambda x: x.median()),
        PE_std=('PE_ratio', 'std'),
        PE_var=('PE_ratio', lambda x: x.var()),  # Variance calculation
        PE_min=('PE_ratio', 'min'),
        PE_max=('PE_ratio', 'max'),

        # M/B Ratio statistics
        MB_count=('MB_ratio', 'count'),
        MB_mean=('MB_ratio', 'mean'),
        MB_median=('MB_ratio', lambda x: x.median()),
        MB_std=('MB_ratio', 'std'),
        MB_var=('MB_ratio', lambda x: x.var()),  # Variance calculation
        MB_min=('MB_ratio', 'min'),
        MB_max=('MB_ratio', 'max'),

        # Additional metadata
        company_count=('gvkey', 'nunique')
    ).reset_index()

    # Add GICS sector names
    gics_names = {
        10: 'Energy', 15: 'Materials', 20: 'Industrials', 25: 'Consumer Discretionary',
        30: 'Consumer Staples', 35: 'Health Care', 40: 'Financials', 45: 'Information Technology',
        50: 'Communication Services', 55: 'Utilities', 60: 'Real Estate'
    }
    sector_stats['sector_name'] = sector_stats['gsector'].map(gics_names)

    log_entries.append(f"Sector-quarter combinations: {len(sector_stats):,}")
    log_entries.append("")

    # Summary statistics by sector
    log_entries.append("=== SECTOR SUMMARY STATISTICS ===")

    sector_summary = sector_stats.groupby('gsector').agg({
        'PE_count': 'sum',
        'MB_count': 'sum',
        'company_count': 'mean',
        'quarter': 'count'
    }).round(0)

    sector_summary['sector_name'] = sector_summary.index.map(gics_names)

    for sector_code in sorted(sector_stats['gsector'].unique()):
        sector_name = gics_names[sector_code]
        sector_data = sector_stats[sector_stats['gsector'] == sector_code]

        log_entries.append(f"Sector {sector_code} ({sector_name}):")
        log_entries.append(f"  Quarters covered: {len(sector_data)}")
        log_entries.append(f"  Total P/E observations: {sector_data['PE_count'].sum():,.0f}")
        log_entries.append(f"  Total M/B observations: {sector_data['MB_count'].sum():,.0f}")
        log_entries.append("  P/E Ratio (mean of quarterly means): {:.2f}".format(sector_data['PE_mean'].mean()))
        log_entries.append("  M/B Ratio (mean of quarterly means): {:.2f}".format(sector_data['MB_mean'].mean()))
        log_entries.append("")

    return sector_stats

def perform_trend_analysis(sector_stats, log_entries):
    """Perform time-series trend analysis for each sector"""

    log_entries.append("=== TIME-SERIES TREND ANALYSIS ===")

    # Sort data by sector and quarter for trend analysis
    sector_stats = sector_stats.sort_values(['gsector', 'quarter'])

    # Convert quarter to datetime for trend analysis
    sector_stats['quarter_date'] = pd.to_datetime(sector_stats['quarter'].str.replace('Q', '-Q'))

    gics_names = {
        10: 'Energy', 15: 'Materials', 20: 'Industrials', 25: 'Consumer Discretionary',
        30: 'Consumer Staples', 35: 'Health Care', 40: 'Financials', 45: 'Information Technology',
        50: 'Communication Services', 55: 'Utilities', 60: 'Real Estate'
    }

    # Analyze trends for each sector
    for sector_code in sorted(sector_stats['gsector'].unique()):
        sector_name = gics_names[sector_code]
        sector_data = sector_stats[sector_stats['gsector'] == sector_code].copy()

        log_entries.append(f"Sector {sector_code} ({sector_name}) Trend Analysis:")

        # P/E Ratio trends
        pe_data = sector_data.dropna(subset=['PE_mean'])
        if len(pe_data) >= 4:  # Need minimum data points for trend
            pe_trend = calculate_trend(pe_data['PE_mean'].values)
            log_entries.append("  P/E Ratio Trend:")
            log_entries.append(".2f")
            log_entries.append("    Direction: {}".format("Upward" if pe_trend['slope'] > 0.1 else "Downward" if pe_trend['slope'] < -0.1 else "Stable"))
            log_entries.append(".2f")
        else:
            log_entries.append("  P/E Ratio: Insufficient data for trend analysis")

        # M/B Ratio trends
        mb_data = sector_data.dropna(subset=['MB_mean'])
        if len(mb_data) >= 4:
            mb_trend = calculate_trend(mb_data['MB_mean'].values)
            log_entries.append("  M/B Ratio Trend:")
            log_entries.append(".2f")
            log_entries.append("    Direction: {}".format("Upward" if mb_trend['slope'] > 0.1 else "Downward" if mb_trend['slope'] < -0.1 else "Stable"))
            log_entries.append(".2f")
        else:
            log_entries.append("  M/B Ratio: Insufficient data for trend analysis")

        log_entries.append("")

    # Overall market trends
    log_entries.append("=== OVERALL MARKET TREND ANALYSIS ===")

    # Calculate market-wide averages
    market_avg = sector_stats.groupby('quarter').agg({
        'PE_mean': 'mean',
        'MB_mean': 'mean'
    }).reset_index()

    market_avg = market_avg.sort_values('quarter')
    market_avg['quarter_date'] = pd.to_datetime(market_avg['quarter'].str.replace('Q', '-Q'))

    # Market P/E trend
    pe_market_trend = calculate_trend(market_avg['PE_mean'].dropna().values)
    log_entries.append("Market-wide P/E Ratio Trend:")
    log_entries.append(".2f")
    log_entries.append("  Direction: {}".format("Upward" if pe_market_trend['slope'] > 0.1 else "Downward" if pe_market_trend['slope'] < -0.1 else "Stable"))

    # Market M/B trend
    mb_market_trend = calculate_trend(market_avg['MB_mean'].dropna().values)
    log_entries.append("Market-wide M/B Ratio Trend:")
    log_entries.append(".2f")
    log_entries.append("  Direction: {}".format("Upward" if mb_market_trend['slope'] > 0.1 else "Downward" if mb_market_trend['slope'] < -0.1 else "Stable"))
    log_entries.append("")

def calculate_trend(values):
    """Calculate linear trend for a time series"""
    x = np.arange(len(values))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, values)

    return {
        'slope': slope,
        'intercept': intercept,
        'r_squared': r_value**2,
        'p_value': p_value,
        'std_err': std_err
    }

def create_sector_visualizations(sector_stats, log_entries):
    """Create visualization plots for sector analysis"""

    log_entries.append("=== VISUALIZATION GENERATION ===")

    gics_names = {
        10: 'Energy', 15: 'Materials', 20: 'Industrials', 25: 'Consumer Discretionary',
        30: 'Consumer Staples', 35: 'Health Care', 40: 'Financials', 45: 'Information Technology',
        50: 'Communication Services', 55: 'Utilities', 60: 'Real Estate'
    }

    # Prepare data for plotting
    sector_stats = sector_stats.sort_values(['gsector', 'quarter'])
    sector_stats['quarter_date'] = pd.to_datetime(sector_stats['quarter'].str.replace('Q', '-Q'))

    # Create subplots for P/E and M/B trends
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('GICS Sector Valuation Ratios Trends (2010-2025)', fontsize=16, fontweight='bold')

    # P/E Ratio Trends - Mean
    for sector_code in sorted(sector_stats['gsector'].unique()):
        sector_data = sector_stats[sector_stats['gsector'] == sector_code]
        sector_name = gics_names[sector_code]
        ax1.plot(sector_data['quarter_date'], sector_data['PE_mean'],
                label=sector_name, linewidth=2, alpha=0.8)

    ax1.set_title('P/E Ratio Trends by Sector (Mean)', fontweight='bold')
    ax1.set_ylabel('P/E Ratio')
    ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.grid(True, alpha=0.3)

    # M/B Ratio Trends - Mean
    for sector_code in sorted(sector_stats['gsector'].unique()):
        sector_data = sector_stats[sector_stats['gsector'] == sector_code]
        sector_name = gics_names[sector_code]
        ax2.plot(sector_data['quarter_date'], sector_data['MB_mean'],
                label=sector_name, linewidth=2, alpha=0.8)

    ax2.set_title('Market-to-Book Ratio Trends by Sector (Mean)', fontweight='bold')
    ax2.set_ylabel('M/B Ratio')
    ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax2.grid(True, alpha=0.3)

    # P/E Ratio Volatility (Standard Deviation)
    for sector_code in sorted(sector_stats['gsector'].unique()):
        sector_data = sector_stats[sector_stats['gsector'] == sector_code]
        sector_name = gics_names[sector_code]
        ax3.plot(sector_data['quarter_date'], sector_data['PE_std'],
                label=sector_name, linewidth=2, alpha=0.8)

    ax3.set_title('P/E Ratio Volatility by Sector (Std Dev)', fontweight='bold')
    ax3.set_ylabel('P/E Ratio Std Dev')
    ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax3.grid(True, alpha=0.3)

    # M/B Ratio Volatility (Standard Deviation)
    for sector_code in sorted(sector_stats['gsector'].unique()):
        sector_data = sector_stats[sector_stats['gsector'] == sector_code]
        sector_name = gics_names[sector_code]
        ax4.plot(sector_data['quarter_date'], sector_data['MB_std'],
                label=sector_name, linewidth=2, alpha=0.8)

    ax4.set_title('Market-to-Book Ratio Volatility by Sector (Std Dev)', fontweight='bold')
    ax4.set_ylabel('M/B Ratio Std Dev')
    ax4.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('sector_valuation_trends.png', dpi=300, bbox_inches='tight')
    log_entries.append("Created: sector_valuation_trends.png")

    # Create individual sector plots
    for sector_code in sorted(sector_stats['gsector'].unique()):
        sector_name = gics_names[sector_code]
        sector_data = sector_stats[sector_stats['gsector'] == sector_code]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        # P/E and M/B for this sector
        ax1.plot(sector_data['quarter_date'], sector_data['PE_mean'], 'b-', linewidth=2, label='P/E Mean')
        ax1.fill_between(sector_data['quarter_date'],
                        sector_data['PE_mean'] - sector_data['PE_std'],
                        sector_data['PE_mean'] + sector_data['PE_std'],
                        alpha=0.3, color='blue', label='±1 Std Dev')
        ax1.set_title(f'{sector_name} (Sector {sector_code}) - P/E Ratio')
        ax1.set_ylabel('P/E Ratio')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.tick_params(axis='x', rotation=45)

        ax2.plot(sector_data['quarter_date'], sector_data['MB_mean'], 'r-', linewidth=2, label='M/B Mean')
        ax2.fill_between(sector_data['quarter_date'],
                        sector_data['MB_mean'] - sector_data['MB_std'],
                        sector_data['MB_mean'] + sector_data['MB_std'],
                        alpha=0.3, color='red', label='±1 Std Dev')
        ax2.set_title(f'{sector_name} (Sector {sector_code}) - Market-to-Book Ratio')
        ax2.set_ylabel('M/B Ratio')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        ax2.tick_params(axis='x', rotation=45)

        plt.tight_layout()
        filename = f'sector_{sector_code}_{sector_name.lower().replace(" ", "_")}_trends.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()

        log_entries.append(f"Created: {filename}")

    log_entries.append("")

if __name__ == "__main__":
    main()
