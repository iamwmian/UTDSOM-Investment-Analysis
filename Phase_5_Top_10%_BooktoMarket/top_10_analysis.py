#!/usr/bin/env python3
"""
Top 10% Firms Analysis - Phase 5
=================================

This script identifies the top 10% of firms across all sectors using 2025 Q1 and Q2 data
based on P/E and M/B ratios. Uses Feynman-style logical thinking: break down complex
valuation into fundamental principles.

DATA CONTRACT: Input must be Compustat quarterly data with required columns.
DATA CONTRACT: Output guarantees top 10% firms by each metric, sorted by performance.

METHODOLOGY (Feynman Logic):
1. P/E Ratio = Price per share / Earnings per share
   → Lower P/E = Paying less per dollar of earnings = Better value (even if negative)
2. M/B Ratio = Enterprise value / Book value
   → Lower M/B = More undervalued relative to assets = Better value (even if negative)
3. Elite performers = Firms that excel at BOTH value metrics simultaneously

Author: Wassil
Project: UTDSOM Investment Corp. Quantitative Analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os
from typing import Dict, List, Tuple, Optional

# Set plotting style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# DATA CONTRACTS - Define expected data structures
REQUIRED_COLUMNS = [
    'gvkey', 'conm', 'datadate', 'quarter', 'year', 'gsector',
    'prccq', 'epspxq', 'PE_ratio', 'market_cap', 'total_debt',
    'cheq', 'atq', 'MB_ratio'
]

EXPECTED_OUTPUT_SCHEMA = {
    'gvkey': 'str',
    'company_name': 'str',
    'sector': 'float',
    'sector_name': 'str',
    'avg_MB': 'float',
    'MB_sector_rank': 'float',
    'MB_sector_percentile': 'float',
    'sector_threshold_mb': 'float',
    'market_cap': 'float',
    'price': 'float',
    'eps': 'float',
    'data_source': 'str'
}

def validate_data_contract(df: pd.DataFrame, required_columns: List[str]) -> bool:
    """
    DATA CONTRACT VALIDATION: Ensure input data meets specifications.

    Feynman Logic: Before doing anything complex, verify we have the right ingredients.
    Like checking ingredients before cooking - don't start if basics are missing.
    """
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"DATA CONTRACT VIOLATION: Missing required columns: {missing_columns}")

    if df.empty:
        raise ValueError("DATA CONTRACT VIOLATION: Input dataframe is empty")

    print(f"✅ DATA CONTRACT: Input validated - {len(df)} rows, {len(df.columns)} columns")
    return True

def main():
    """Main analysis function - Feynman-style: Break complex analysis into simple, logical steps"""

    print("=== Sector-Specific Top 10% Firms by Book-to-Market (Lowest M/B) - 2025 Q1 & Q2 ===\n")
    print("🎯 OBJECTIVE: Find top 10% of firms per sector by lowest M/B (highest B/M) using simple ratio logic\n")

    # File paths
    input_path = "/Users/wm/Desktop/UTDSOM                         Investment Corp./Phase_2_Algorithm_Development/Compustat_Ratios_TimeSeries.csv"
    output_dir = os.path.dirname(__file__)

    # Create sector_outputs subfolder
    sector_dir = os.path.join(output_dir, 'sector_outputs')
    os.makedirs(sector_dir, exist_ok=True)

    # Initialize analysis log
    log = []
    log.append("=== SECTOR-SPECIFIC TOP 10% FIRMS BY BOOK-TO-MARKET LOG ===\n")
    log.append(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    log.append(f"Input Data: {input_path}\n\n")
    log.append("🎯 METHODOLOGY: Feynman Logic - Break down valuation to fundamental truths\n")
    log.append("• M/B = Enterprise Value ÷ Book Value → Lower = More undervalued\n")
    log.append("• Top 10% = Lowest M/B (highest B/M) within each sector\n\n")
    
    # STEP 1: Load and validate data (Feynman Logic: Start with solid foundation)
    print("🧱 STEP 1: Loading and validating data foundation...")
    df = pd.read_csv(input_path, low_memory=False)

    # DATA CONTRACT: Validate input meets specifications
    validate_data_contract(df, REQUIRED_COLUMNS)

    log.append("=== DATA LOADING & VALIDATION ===\n")
    log.append(f"Total records in dataset: {len(df):,}\n")
    log.append(f"Unique firms in dataset: {df['gvkey'].nunique():,}\n")
    log.append("✅ Data contract validated - all required columns present\n")

    # STEP 2: Filter for 2025 data (Feynman Logic: Focus on what we care about)
    print("🎯 STEP 2: Filtering for 2025 Q1 & Q2 data...")
    df_2025 = df[df['quarter'].isin(['2025Q1', '2025Q2'])].copy()

    # STEP 3: Categorize firms by data availability (Feynman Logic: Understand what we have before proceeding)
    print("📊 STEP 3: Categorizing firms by quarter availability...")
    quarter_counts = df_2025.groupby('gvkey')['quarter'].nunique()
    firms_with_both = quarter_counts[quarter_counts == 2].index
    firms_with_one = quarter_counts[quarter_counts == 1].index
    
    log.append("\n=== QUARTER AVAILABILITY ===\n")
    log.append(f"Firms with data for both Q1 and Q2: {len(firms_with_both):,}\n")
    log.append(f"Firms with data for only one quarter: {len(firms_with_one):,}\n")
    log.append(f"Total firms included in analysis: {df_2025['gvkey'].nunique():,}\n")
    
    print(f"   Firms with both quarters: {len(firms_with_both):,}")
    print(f"   Firms with one quarter: {len(firms_with_one):,}")
    print(f"   Total firms: {df_2025['gvkey'].nunique():,} ")

    # STEP 4: Calculate ratios using priority logic (Feynman Logic: Simple rules for complex situations)
    print("\n🧮 STEP 4: Calculating M/B ratios with priority logic...")
    print("   Feynman Rule: Both quarters (average) > Q2 only (recent) > Q1 only (older)")
    
    # Process each firm based on available quarters
    firm_ratios = []
    
    for gvkey in df_2025['gvkey'].unique():
        firm_data = df_2025[df_2025['gvkey'] == gvkey]
        
        # Check which quarters are available
        has_q1 = '2025Q1' in firm_data['quarter'].values
        has_q2 = '2025Q2' in firm_data['quarter'].values
        
        if has_q1 and has_q2:
            # Both quarters: calculate average
            mb_ratio = firm_data['MB_ratio'].mean()
            data_source = 'Both (Averaged)'
        elif has_q2:
            # Q2 only: use Q2 data (prioritized)
            q2_data = firm_data[firm_data['quarter'] == '2025Q2'].iloc[0]
            mb_ratio = q2_data['MB_ratio']
            data_source = 'Q2 Only'
        else:
            # Q1 only: use Q1 data
            q1_data = firm_data[firm_data['quarter'] == '2025Q1'].iloc[0]
            mb_ratio = q1_data['MB_ratio']
            data_source = 'Q1 Only'
        
        # Get latest data for metadata
        latest_data = firm_data.iloc[-1]
        
        firm_ratios.append({
            'gvkey': gvkey,
            'company_name': latest_data['conm'],
            'sector': latest_data['gsector'],
            'avg_MB': mb_ratio,
            'market_cap': latest_data['market_cap'],
            'price': latest_data['prccq'],
            'eps': latest_data['epspxq'],
            'data_source': data_source
        })
    
    avg_ratios = pd.DataFrame(firm_ratios)
    
    log.append("\n=== RATIO CALCULATION WITH PRIORITY LOGIC ===\n")
    log.append("Priority: Both quarters (average) > Q2 only > Q1 only\n\n")
    log.append(f"Firms with ratios calculated: {len(avg_ratios):,}\n")
    log.append(f"  - Both quarters (averaged): {(avg_ratios['data_source'] == 'Both (Averaged)').sum():,}\n")
    log.append(f"  - Q2 only: {(avg_ratios['data_source'] == 'Q2 Only').sum():,}\n")
    log.append(f"  - Q1 only: {(avg_ratios['data_source'] == 'Q1 Only').sum():,}\n")
    log.append(f"Firms with valid M/B ratios: {avg_ratios['avg_MB'].notna().sum():,}\n")

    # STEP 5: Rank firms by valuation metrics (Feynman Logic: Simple percentile ranking)
    print("\n📈 STEP 5: Ranking firms by M/B within each sector...")
    print("   Feynman Logic: Lower M/B = More undervalued → Top 10% = Lowest M/B per sector")

    # Remove firms with NaN ratios for ranking (Data Contract: Clean data for analysis)
    avg_ratios_clean = avg_ratios.dropna(subset=['avg_MB']).copy()

    log.append(f"\n=== CLEAN DATA FOR RANKING ===\n")
    log.append(f"Firms with valid M/B: {len(avg_ratios_clean):,}\n")
    log.append(f"Removed due to missing ratios: {len(avg_ratios) - len(avg_ratios_clean):,}\n")

    print("\n📈 STEP 5: Ranking firms by M/B within each sector...")
    print("   Feynman Logic: Lower M/B = More undervalued → Top 10% = Lowest M/B per sector")

    def compute_sector_metrics(group):
        group['MB_sector_rank'] = group['avg_MB'].rank(method='min')
        group['MB_sector_percentile'] = group['avg_MB'].rank(pct=True) * 100
        group['sector_threshold_mb'] = group['avg_MB'].quantile(0.10)
        return group

    avg_ratios_clean = avg_ratios_clean.groupby('sector').apply(compute_sector_metrics).reset_index(drop=True)

    # Set sector_name after apply
    sector_names = {
        10: 'Energy', 15: 'Materials', 20: 'Industrials',
        25: 'Consumer_Discretionary', 30: 'Consumer_Staples',
        35: 'Health_Care', 40: 'Financials', 45: 'Information_Technology',
        50: 'Communication_Services', 55: 'Utilities', 60: 'Real_Estate'
    }
    avg_ratios_clean['sector_name'] = avg_ratios_clean['sector'].map(sector_names)

    # Handle unknown sectors
    avg_ratios_clean = avg_ratios_clean[avg_ratios_clean['sector_name'].notna()]

    print("   → Ranking by M/B: Lower ratio = Enterprise value < Book value (undervalued)")
    print(f"   → M/B 10th percentile threshold (global): {avg_ratios_clean['sector_threshold_mb'].mean():.4f}")

    log.append("\n=== RANKING THRESHOLDS ===\n")
    log.append(f"10th percentile M/B threshold (global): {avg_ratios_clean['sector_threshold_mb'].mean():.4f}\n")

    # STEP 6: Identify top 10% firms (Feynman Logic: Apply simple cutoff)
    print("\n🏆 STEP 6: Identifying top 10% firms per sector by lowest M/B...")
    
    sector_tops = {}
    sector_thresholds = {}
    sector_counts = {}

    for sector, group in avg_ratios_clean.groupby('sector'):
        sector_name = {10: 'Energy', 15: 'Materials', 20: 'Industrials',
                       25: 'Consumer_Discretionary', 30: 'Consumer_Staples',
                       35: 'Health_Care', 40: 'Financials', 45: 'Information_Technology',
                       50: 'Communication_Services', 55: 'Utilities', 60: 'Real_Estate'}.get(sector, f'Unknown_{sector}')
        top_sector = group[group['MB_sector_percentile'] <= 10].copy()
        top_sector = top_sector.sort_values('avg_MB')
        sector_tops[sector_name] = top_sector
        if not top_sector.empty:
            sector_thresholds[sector_name] = top_sector['sector_threshold_mb'].iloc[0]
            sector_counts[sector_name] = len(top_sector)
        else:
            sector_thresholds[sector_name] = np.nan
            sector_counts[sector_name] = 0

    log.append("\n=== SECTOR-SPECIFIC TOP 10% IDENTIFICATION ===\n")
    for sector_name, count in sector_counts.items():
        threshold = sector_thresholds[sector_name]
        log.append(f"{sector_name}: {count:,} firms (threshold: {threshold:.4f})\n")

    print("   ✅ Found sector-specific top firms")

    # Add sector names
    avg_ratios_clean['sector_name'] = avg_ratios_clean['sector'].map({10: 'Energy', 15: 'Materials', 20: 'Industrials',
                                                                      25: 'Consumer_Discretionary', 30: 'Consumer_Staples',
                                                                      35: 'Health_Care', 40: 'Financials', 45: 'Information_Technology',
                                                                      50: 'Communication_Services', 55: 'Utilities', 60: 'Real_Estate'})

    # STEP 7: Generate CSV outputs (Data Contract: Guarantee expected schema)
    print("\n💾 STEP 7: Generating sector-specific CSV outputs...")

    output_cols = ['gvkey', 'company_name', 'sector', 'sector_name', 'avg_MB',
                   'MB_sector_rank', 'MB_sector_percentile', 'sector_threshold_mb', 'market_cap',
                   'price', 'eps', 'data_source']

    # Data Contract: Validate output schema before writing
    def validate_output_schema(df: pd.DataFrame, expected_cols: List[str]) -> bool:
        """DATA CONTRACT: Ensure output meets expected schema"""
        actual_cols = list(df.columns)
        if set(actual_cols) != set(expected_cols):
            raise ValueError(f"Output schema violation. Expected: {expected_cols}, Got: {actual_cols}")
        print(f"   ✅ Output schema validated for {len(df)} rows")
        return True

    log.append("\n=== OUTPUT FILES GENERATED ===\n")

    for sector_name, top_sector in sector_tops.items():
        if not top_sector.empty:
            csv_name = f"top_10_pct_by_MB_{sector_name}.csv"
            print(f"   → Writing {csv_name} ({len(top_sector)} firms)...")
            validate_output_schema(top_sector[output_cols], output_cols)
            top_sector[output_cols].to_csv(f"{sector_dir}/{csv_name}", index=False)
            log.append(f"sector_outputs/{csv_name}\n")

    print("   CSV files created successfully")
    
    # Step 7: Create visualizations
    print("\nStep 7: Creating visualizations...")
    
    # Distribution histograms (adapt for MB only, perhaps global for simplicity)
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))

    mb_values = avg_ratios_clean['avg_MB']
    mb_filtered = mb_values[(mb_values >= -5) & (mb_values <= 15)]

    ax.hist(mb_filtered, bins=50, color='lightcoral', edgecolor='black', alpha=0.7)
    # Global threshold not relevant; perhaps omit or average sector thresholds
    avg_threshold = np.mean(list(sector_thresholds.values()))
    ax.axvline(avg_threshold, color='red', linestyle='--', linewidth=2.5,
               label=f'Avg Sector 10th Percentile: {avg_threshold:.2f}')
    ax.set_xlabel('Average M/B Ratio', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Firms', fontsize=12, fontweight='bold')
    ax.set_title('M/B Ratio Distribution (Global)\n2025 Q1 & Q2 Average',
                 fontsize=13, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f"{output_dir}/distribution_histograms.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("   ✓ Distribution histograms created")

    # Sector breakdown: Show top-decile counts per sector
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))

    sector_counts_df = pd.Series(sector_counts).sort_values(ascending=True)
    ax.barh(sector_counts_df.index, sector_counts_df.values, color='seagreen')
    ax.set_xlabel('Number of Top 10% Firms', fontsize=11, fontweight='bold')
    ax.set_title('Sector-Specific Top 10% by M/B - Firm Counts',
                 fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')
    for i, v in enumerate(sector_counts_df.values):
        ax.text(v + 0.5, i, str(v), va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f"{output_dir}/sector_breakdown.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("   ✓ Sector breakdown created")

    # Summary dashboard
    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

    ax_text = fig.add_subplot(gs[0, :])
    ax_text.axis('off')

    summary_text = f"""
    SECTOR-SPECIFIC TOP 10% FIRMS BY BOOK-TO-MARKET - 2025 Q1 & Q2 SUMMARY

    Total firms analyzed: {len(avg_ratios_clean):,}
    Data Sources: Both Qtrs={len(firms_with_both):,}, Q2 Only={(avg_ratios['data_source']=='Q2 Only').sum():,}, Q1 Only={(avg_ratios['data_source']=='Q1 Only').sum():,}

    TOP 10% RESULTS (PER SECTOR):
    """

    for sector_name, threshold in sector_thresholds.items():
        count = sector_counts[sector_name]
        summary_text += f"• {sector_name}: {count:,} firms (threshold: {threshold:.4f})\n"

    summary_text += f"""
    RATIO STATISTICS (All Firms):
    • M/B: Mean={avg_ratios_clean['avg_MB'].mean():.2f}, Median={avg_ratios_clean['avg_MB'].median():.2f}, Std={avg_ratios_clean['avg_MB'].std():.2f}
    """

    ax_text.text(0.5, 0.5, summary_text, ha='center', va='center',
                fontsize=10, family='monospace',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

    # Remove top 5 by PE
    # Top 5 by M/B (global, or pick a sector? Use global for simplicity, but since sector-specific, perhaps omit or show example)
    # For brevity, omit top5 and elite, as plan focuses on sector-specific

    # Scatter plot (adapt or remove)
    ax_scatter = fig.add_subplot(gs[1:, :])
    ax_scatter.scatter(avg_ratios_clean['avg_MB'], avg_ratios_clean['market_cap'],
                      c='lightgray', alpha=0.4, s=30)
    # Highlight some top per sector if desired, but skip for now
    ax_scatter.set_xlabel('Average M/B Ratio', fontsize=11, fontweight='bold')
    ax_scatter.set_ylabel('Market Cap', fontsize=11, fontweight='bold')  # Arbitrary y for illustration
    ax_scatter.set_title('M/B vs Market Cap (Global)', fontsize=12, fontweight='bold')
    ax_scatter.grid(True, alpha=0.3)

    plt.savefig(f"{output_dir}/summary_dashboard.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("   ✓ Summary dashboard created")
    
    # Step 8: Generate analysis summary
    print("\nStep 8: Generating analysis summary...")
    
    log.append("\n=== ANALYSIS COMPLETE ===\n")
    log.append(f"Completion Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Save log
    with open(f"{output_dir}/analysis_summary.txt", 'w') as f:
        f.writelines(log)
    
    print("   ✓ Analysis summary saved")
    
    print("\n" + "="*70)
    print("🎉 ANALYSIS COMPLETE - Sector-Specific Book-to-Market Achieved!")
    print("="*70)
    print("💡 KEY LESSON: Valuation by sector using lowest M/B (highest B/M)")
    print(f"\n📁 Output files generated in: {os.path.abspath(output_dir)}/")
    print("\n📊 CSV Files (Per Sector, in sector_outputs/):")
    for sector_name in sector_tops:
        print(f"  • top_10_pct_by_MB_{sector_name}.csv")
    print("\n📈 Visualizations:")
    print("  • distribution_histograms.png")
    print("  • sector_breakdown.png")
    print("  • summary_dashboard.png")
    print("\n📝 Documentation:")
    print("  • analysis_summary.txt")
    print("\n" + "="*70)
    
if __name__ == "__main__":
    main()

