#!/usr/bin/env python3
"""
Sector-Specific Top 10% Firms by Book-to-Market - Phase 5
=========================================================

This script identifies the top 10% of firms per GICS sector using 2025 Q1 data only
based on highest Book-to-Market (B/M) ratios, implementing
Fama-French value investing principles with quarterly-only variables.

KEY FEATURES:
- Reads Phase 1 cleaned quarterly data directly (no Phase 2 dependencies)
- Computes B/M = book_equity / market_cap
- Enforces positive book equity constraint (book_equity > 0)
- Includes dividend yield (TTM from quarterly dvpsxq) for Fama-French evidence
- Outputs 11 sector-specific CSVs with audit fields for outlier detection
- Generates market vs book scatter plots and distribution visuals

DATA CONTRACT: Input requires quarterly Compustat fields from Phase 1 cleaned data.
DATA CONTRACT: Output guarantees top 10% firms per sector by highest B/M, sorted descending.

METHODOLOGY (Feynman Logic - Break down valuation to fundamental truths):
1. B/M Ratio = Book Equity / Market Cap
   → Higher B/M = More undervalued relative to market price = Better value
   → Highest B/M = Most attractive value investment (Fama-French factor)
2. Positive Book Equity: seqq + txditcq - preferred_stock > 0
   → Excludes firms in financial distress (negative equity)
3. Dividend Yield (TTM): Rolling 4-quarter sum of dvpsxq / prccq
   → Additional Fama-French evidence of value characteristics
4. Sector-Specific Selection: Top 10% (highest B/M) within each GICS sector
   → Controls for industry differences in valuation norms

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

# DATA CONTRACTS - Define expected data structures (quarterly raw fields only)
REQUIRED_COLUMNS = [
    'gvkey', 'conm', 'datadate', 'gsector',
    'prccq', 'cshoq',
    'dlcq', 'dlttq', 'cheq', 'atq',
    'seqq', 'txditcq', 'pstkrq', 'pstkq', 'pstknq',
    'dvpsxq', 'epspxq',
    'ltq'  # Added for precise book_equity = atq - ltq
]

EXPECTED_OUTPUT_SCHEMA = {
    'gvkey': 'str',
    'company_name': 'str',
    'sector': 'float',
    'sector_name': 'str',
    'BM_ratio': 'float',
    'BM_sector_rank': 'float',
    'BM_sector_percentile': 'float',
    'sector_threshold_bm': 'float',
    'market_cap': 'float',
    'price': 'float',
    'eps': 'float',
    'book_equity': 'float',
    'dividend_yield_ttm': 'float',
    'dlcq': 'float',
    'dlttq': 'float',
    'cheq': 'float',
    'atq': 'float',
    'cshoq': 'float',
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

    print("=== Sector-Specific Top 10% Firms by Book-to-Market (Highest B/M) - 2025 Q1 Only ===\n")
    print("🎯 OBJECTIVE: Find top decile (highest 10%) of firms per sector by B/M using simple ratio logic\n")

    # File paths (read directly from Phase 1 cleaned quarterly file)
    input_path = "/Users/wm/Desktop/UTDSOM                         Investment Corp./Phase_1_Data_Preparation/Compustat_Quarterl_2010_2025_cleaned.csv"
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
    log.append("• B/M = Book Equity ÷ Market Cap → Higher = More undervalued\n")
    log.append("• Top decile = Highest 10% B/M (90th percentile and above) within each sector\n\n")
    
    # STEP 1: Load and validate data (Feynman Logic: Start with solid foundation)
    print("🧱 STEP 1: Loading and validating data foundation...")
    df = pd.read_csv(input_path, low_memory=False)

    # Explicitly drop firms without GICS sector coding (per cleaned data requirement)
    df = df.dropna(subset=['gsector'])
    print(f"   → Dropped {len(df) - df['gvkey'].nunique()} firms without GICS sector")

    # DATA CONTRACT: Validate input meets specifications (raw quarterly fields)
    validate_data_contract(df, REQUIRED_COLUMNS)

    # Build time features from datadate
    df['datadate'] = pd.to_datetime(df['datadate'], errors='coerce')
    df['quarter'] = df['datadate'].dt.to_period('Q').astype(str)
    df['year'] = df['datadate'].dt.year

    # Compute required quarterly metrics strictly from available fields
    # Market Cap
    df['market_cap'] = df['prccq'] * df['cshoq']

    # M/B per requested formula
    mb_numerator = (df['prccq'] * df['cshoq']) + df['dlcq'].fillna(0) + df['dlttq'].fillna(0) - df['cheq'].fillna(0)
    df['MB_ratio'] = mb_numerator / df['atq']
    df['MB_ratio'] = df['MB_ratio'].replace([np.inf, -np.inf], np.nan)

    # Preferred stock fallback (keep for potential future use, but not in book_equity)
    df['preferred_stock'] = df['pstkrq'].combine_first(df['pstkq']).combine_first(df['pstknq']).fillna(0)

    # Book Equity per user's exact definition: Total Assets - Total Liabilities
    df['book_equity'] = df['atq'] - df['ltq']

    # Dividend per share (quarter) and Dividend Yield (TTM)
    dps_q = df['dvpsxq'].copy()
    dps_q = dps_q.fillna(0)
    dps_q = dps_q.clip(lower=0)
    df['dps_q'] = dps_q
    df = df.sort_values(['gvkey', 'datadate'])
    df['dividend_yield_ttm'] = (
        df.groupby('gvkey')['dps_q']
          .rolling(window=4, min_periods=1)
          .sum()
          .reset_index(level=0, drop=True)
    ) / df['prccq']

    log.append("=== DATA LOADING & VALIDATION ===\n")
    log.append(f"Total records in dataset: {len(df):,}\n")
    log.append(f"Unique firms in dataset: {df['gvkey'].nunique():,}\n")
    log.append("✅ Data contract validated - all required columns present\n")

    # STEP 2: Filter for 2025 data (Feynman Logic: Focus on what we care about)
    print("🎯 STEP 2: Filtering for 2025 Q1 data only...")

    df_2025 = df[df['quarter'] == '2025Q1'].copy()

    # Enforce positive Book Equity constraint before any aggregation
    df_2025 = df_2025[df_2025['book_equity'] > 0].copy()

    # STEP 3: No multi-quarter logic needed since only Q1
    print("📊 STEP 3: Processing Q1 2025 data...")
    log.append("\n=== QUARTER AVAILABILITY ===\n")
    log.append(f"Total firms with Q1 2025 data: {df_2025['gvkey'].nunique():,}\n")

    print(f"   Total firms: {df_2025['gvkey'].nunique():,} ")

    # STEP 4: Calculate B/M ratios (Feynman Logic: Simple rules)
    print("\n🧮 STEP 4: Calculating B/M ratios...")

    firm_ratios = []

    for gvkey in df_2025['gvkey'].unique():
        chosen = df_2025[df_2025['gvkey'] == gvkey].iloc[0]
        bm_ratio = chosen['book_equity'] / chosen['market_cap'] if chosen['market_cap'] != 0 else np.nan

        firm_ratios.append({
            'gvkey': gvkey,
            'company_name': chosen['conm'],
            'sector': chosen['gsector'],
            'BM_ratio': bm_ratio,
            'market_cap': chosen['market_cap'],
            'price': chosen['prccq'],
            'eps': chosen['epspxq'],
            'book_equity': chosen['book_equity'],
            'dividend_yield_ttm': chosen['dividend_yield_ttm'],
            # Audit fields (keep for transparency, even if not used in B/M)
            'dlcq': chosen['dlcq'],
            'dlttq': chosen['dlttq'],
            'cheq': chosen['cheq'],
            'atq': chosen['atq'],
            'cshoq': chosen['cshoq'],
            'data_source': 'Q1 Only'
        })

    firm_ratios_df = pd.DataFrame(firm_ratios)

    log.append("\n=== RATIO CALCULATION ===\n")
    log.append(f"Firms with ratios calculated: {len(firm_ratios_df):,}\n")
    log.append(f"Firms with valid B/M ratios: {firm_ratios_df['BM_ratio'].notna().sum():,}\n")

    # STEP 5: Rank firms by B/M (highest first)
    print("\n📈 STEP 5: Ranking firms by B/M within each sector...")
    print("   Feynman Logic: Higher B/M = More undervalued → Top decile = Highest 10% B/M per sector")

    # No further filtering—BVE > 0 is the only constraint; proceed with all (including any NaN B/M)
    firm_ratios_clean = firm_ratios_df.copy()

    log.append(f"\n=== CLEAN DATA FOR RANKING ===\n")
    log.append(f"Firms after BVE > 0 filter (only constraint): {len(firm_ratios_clean):,}\n")
    log.append(f"No further removals applied\n")

    def compute_sector_metrics(group):
        group['BM_sector_rank'] = group['BM_ratio'].rank(method='min', ascending=False)
        group['BM_sector_percentile'] = group['BM_ratio'].rank(pct=True, ascending=False) * 100
        group['sector_threshold_bm'] = group['BM_ratio'].quantile(0.90)
        return group

    firm_ratios_clean = firm_ratios_clean.groupby('sector').apply(compute_sector_metrics).reset_index(drop=True)

    # Set sector_name after apply
    sector_names = {
        10: 'Energy', 15: 'Materials', 20: 'Industrials',
        25: 'Consumer_Discretionary', 30: 'Consumer_Staples',
        35: 'Health_Care', 40: 'Financials', 45: 'Information_Technology',
        50: 'Communication_Services', 55: 'Utilities', 60: 'Real_Estate'
    }
    firm_ratios_clean['sector_name'] = firm_ratios_clean['sector'].map(sector_names)

    # Handle unknown sectors
    firm_ratios_clean = firm_ratios_clean[firm_ratios_clean['sector_name'].notna()]

    print("   → Ranking by B/M: Higher ratio = Book value > Market value (undervalued)")
    print(f"   → B/M 90th percentile threshold (global average): {firm_ratios_clean['sector_threshold_bm'].mean():.4f}")

    log.append("\n=== RANKING THRESHOLDS ===\n")
    log.append(f"90th percentile B/M threshold (global average): {firm_ratios_clean['sector_threshold_bm'].mean():.4f}\n")

    # STEP 6: Identify top 10% firms (highest B/M)
    print("\n🏆 STEP 6: Identifying top decile firms per sector by highest B/M...")

    sector_tops = {}
    sector_thresholds = {}
    sector_counts = {}

    for sector, group in firm_ratios_clean.groupby('sector'):
        sector_name = sector_names.get(sector, f'Unknown_{sector}')
        top_sector = group[group['BM_sector_percentile'] >= 90].copy()  # Highest 10%
        top_sector = top_sector.sort_values('BM_ratio', ascending=False)  # Highest first
        sector_tops[sector_name] = top_sector
        if not top_sector.empty:
            sector_thresholds[sector_name] = top_sector['sector_threshold_bm'].iloc[0]
            sector_counts[sector_name] = len(top_sector)
        else:
            sector_thresholds[sector_name] = np.nan
            sector_counts[sector_name] = 0

    log.append("\n=== SECTOR-SPECIFIC TOP 10% IDENTIFICATION ===\n")
    for sector_name, count in sector_counts.items():
        threshold = sector_thresholds[sector_name]
        log.append(f"{sector_name}: {count:,} firms (threshold: {threshold:.4f})\n")

    print("   ✅ Found sector-specific top firms")

    # STEP 7: Generate CSV outputs
    print("\n💾 STEP 7: Generating sector-specific CSV outputs...")

    output_cols = ['gvkey', 'company_name', 'sector', 'sector_name', 'BM_ratio',
                   'BM_sector_rank', 'BM_sector_percentile', 'sector_threshold_bm',
                   'market_cap', 'price', 'eps', 'book_equity', 'dividend_yield_ttm',
                   'dlcq', 'dlttq', 'cheq', 'atq', 'cshoq', 'data_source']

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
            csv_name = f"top_10_pct_by_BM_{sector_name}.csv"  # Updated filename
            print(f"   → Writing {csv_name} ({len(top_sector)} firms)...")
            validate_output_schema(top_sector[output_cols], output_cols)
            top_sector[output_cols].to_csv(f"{sector_dir}/{csv_name}", index=False)
            log.append(f"sector_outputs/{csv_name}\n")

    print("   CSV files created successfully")
    
    # Step 7: Create visualizations
    print("\nStep 7: Creating visualizations...")
    
    # Distribution histograms (adapt for BM)
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))

    bm_values = firm_ratios_clean['BM_ratio']
    bm_filtered = bm_values[(bm_values >= 0) & (bm_values <= 10)]  # Adjusted for positive BM

    ax.hist(bm_filtered, bins=50, color='lightcoral', edgecolor='black', alpha=0.7)
    # Average of sector 90th-percentile thresholds (for highest BM)
    avg_threshold = np.mean(list(sector_thresholds.values()))
    ax.axvline(avg_threshold, color='red', linestyle='--', linewidth=2.5,
               label=f'Avg Sector 90th Percentile: {avg_threshold:.2f}')
    ax.set_xlabel('B/M Ratio', fontsize=13, fontweight='bold')
    ax.set_ylabel('Number of Firms', fontsize=13, fontweight='bold')
    ax.set_title('B/M Ratio Distribution (Global)\n2025 Q1',
                 fontsize=14, fontweight='bold')
    # Add formula and value context into legend for auditability
    ax.plot([], [], ' ', label='Definition: Higher B/M = more undervalued; M/B = 1 / B/M')
    ax.plot([], [], ' ', label='Top 10% selection = highest B/M within each sector')
    ax.plot([], [], ' ', label='MC=prccq×cshoq; BE=seqq+txditcq−pref(pstkrq→pstkq→pstknq)')
    ax.plot([], [], ' ', label=f"Median MC={firm_ratios_clean['market_cap'].median():,.0f}; Median BE={firm_ratios_clean['book_equity'].median():,.0f}")
    ax.plot([], [], ' ', label='Q1 2025 data only; BE>0 only')
    ax.legend(fontsize=11, frameon=True)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f"{output_dir}/distribution_histograms.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("   ✓ Distribution histograms created")

    # Sector breakdown: Show top-decile counts per sector
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))

    sector_counts_df = pd.Series(sector_counts).sort_values(ascending=True)
    ax.barh(sector_counts_df.index, sector_counts_df.values, color='seagreen')
    ax.set_xlabel('Number of Top 10% Firms', fontsize=12, fontweight='bold')
    ax.set_title('Sector-Specific Top Decile by B/M - Firm Counts',
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')
    for i, v in enumerate(sector_counts_df.values):
        ax.text(v + 0.5, i, str(v), va='center', fontweight='bold')
    # Legend with formulas, definitions, and value context (global medians)
    ax.plot([], [], ' ', label='Top 10% = highest B/M within sector (lowest M/B)')
    ax.plot([], [], ' ', label='M/B = (prccq×cshoq + dlcq + dlttq − cheq) / atq')
    ax.plot([], [], ' ', label='MC=prccq×cshoq; BE=seqq+txditcq−pref(pstkrq→pstkq→pstknq)')
    ax.plot([], [], ' ', label=f"Median MC={firm_ratios_clean['market_cap'].median():,.0f}; Median BE={firm_ratios_clean['book_equity'].median():,.0f}")
    ax.plot([], [], ' ', label='Chosen quarter: Q2 prioritized, else Q1; BE>0 only')
    ax.legend(fontsize=11, frameon=True, loc='lower right')

    plt.tight_layout()
    plt.savefig(f"{output_dir}/sector_breakdown.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("   ✓ Sector breakdown created")

    # Note: Market vs Book scatter is integrated into the summary dashboard below

    # Summary dashboard
    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

    ax_text = fig.add_subplot(gs[0, :])
    ax_text.axis('off')

    summary_text = f"""
    SECTOR-SPECIFIC TOP 10% FIRMS BY BOOK-TO-MARKET - 2025 Q1 SUMMARY

    Total firms analyzed: {len(firm_ratios_clean):,}
    Data Sources: Q1 2025 Only

    TOP 10% RESULTS (PER SECTOR):
    """

    for sector_name, threshold in sector_thresholds.items():
        count = sector_counts[sector_name]
        summary_text += f"• {sector_name}: {count:,} firms (threshold: {threshold:.4f})\n"

    summary_text += f"""
    RATIO STATISTICS (All Firms):
    • B/M: Mean={firm_ratios_clean['BM_ratio'].mean():.2f}, Median={firm_ratios_clean['BM_ratio'].median():.2f}, Std={firm_ratios_clean['BM_ratio'].std():.2f}
    """

    ax_text.text(0.5, 0.5, summary_text, ha='center', va='center',
                fontsize=10, family='monospace',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

    # Remove top 5 by PE
    # Top 5 by M/B (global, or pick a sector? Use global for simplicity, but since sector-specific, perhaps omit or show example)
    # For brevity, omit top5 and elite, as plan focuses on sector-specific

    # Scatter plot inside dashboard: Market Cap vs Book Equity (log-log, chosen quarter)
    ax_scatter = fig.add_subplot(gs[1:, :])
    ax_scatter.scatter(firm_ratios_clean['market_cap'], firm_ratios_clean['book_equity'],
                       c='steelblue', alpha=0.5, s=30)
    ax_scatter.set_xscale('log')
    ax_scatter.set_yscale('log')
    ax_scatter.set_xlabel('Market Cap (log)', fontsize=11, fontweight='bold')
    ax_scatter.set_ylabel('Book Equity (log)', fontsize=11, fontweight='bold')
    ax_scatter.set_title('Market Cap vs Book Equity (Q1 2025)', fontsize=12, fontweight='bold')
    ax_scatter.grid(True, alpha=0.3, which='both')

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
    print("💡 KEY LESSON: Valuation by sector using highest B/M (top decile)")
    print(f"\n📁 Output files generated in: {os.path.abspath(output_dir)}/")
    print("\n📊 CSV Files (Per Sector, in sector_outputs/):")
    for sector_name in sector_tops:
        print(f"  • top_10_pct_by_BM_{sector_name}.csv")
    print("\n📈 Visualizations:")
    print("  • distribution_histograms.png")
    print("  • sector_breakdown.png")
    print("  • summary_dashboard.png")
    print("\n📝 Documentation:")
    print("  • analysis_summary.txt")
    print("\n" + "="*70)
    
if __name__ == "__main__":
    main()

