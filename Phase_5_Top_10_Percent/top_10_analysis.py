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
    'avg_PE': 'float',
    'avg_MB': 'float',
    'PE_rank': 'float',
    'PE_percentile': 'float',
    'MB_rank': 'float',
    'MB_percentile': 'float',
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

def apply_feynman_logic_to_ratios(pe_ratio: float, mb_ratio: float) -> Dict[str, str]:
    """
    FEYNMAN-STYLE LOGIC: Break down valuation ratios into fundamental truths.

    P/E = Price ÷ Earnings → Lower P/E means paying less for each dollar of earnings
    M/B = Enterprise Value ÷ Book Value → Lower M/B means enterprise value < book value (undervalued)

    Even negative ratios have meaning: Negative P/E means paying for future profitability.
    Negative M/B means market values firm below its recorded assets (deep distress).
    """
    pe_interpretation = ""
    mb_interpretation = ""

    if pe_ratio < 0:
        pe_interpretation = "Loss-making firm - paying for future profitability (speculative value)"
    elif pe_ratio < 10:
        pe_interpretation = "Cheap relative to earnings (bargain territory)"
    elif pe_ratio < 20:
        pe_interpretation = "Reasonably priced"
    else:
        pe_interpretation = "Expensive relative to earnings"

    if mb_ratio < 0:
        mb_interpretation = "Enterprise value < book value (severely distressed/undervalued)"
    elif mb_ratio < 0.5:
        mb_interpretation = "Significantly undervalued relative to assets"
    elif mb_ratio < 1.0:
        mb_interpretation = "Somewhat undervalued"
    elif mb_ratio < 2.0:
        mb_interpretation = "Fairly valued"
    else:
        mb_interpretation = "Overvalued relative to assets"

    return {
        'PE_interpretation': pe_interpretation,
        'MB_interpretation': mb_interpretation
    }

def main():
    """Main analysis function - Feynman-style: Break complex analysis into simple, logical steps"""

    print("=== Top 10% Firms Analysis - 2025 Q1 & Q2 ===\n")
    print("🎯 OBJECTIVE: Find top 10% of firms by valuation metrics using simple ratio logic\n")

    # File paths
    input_path = "../Phase_2_Algorithm_Development/Compustat_Ratios_TimeSeries.csv"
    output_dir = "."

    # Initialize analysis log
    log = []
    log.append("=== TOP 10% FIRMS ANALYSIS LOG ===\n")
    log.append(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    log.append(f"Input Data: {input_path}\n\n")
    log.append("🎯 METHODOLOGY: Feynman Logic - Break down valuation to fundamental truths\n")
    log.append("• P/E = Price ÷ Earnings → Lower = Better value\n")
    log.append("• M/B = Enterprise Value ÷ Book Value → Lower = More undervalued\n")
    log.append("• Top 10% = Best performers by these simple metrics\n\n")
    
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
    print(f"   Total firms: {df_2025['gvkey'].nunique():,}")

    # STEP 4: Calculate ratios using priority logic (Feynman Logic: Simple rules for complex situations)
    print("\n🧮 STEP 4: Calculating P/E and M/B ratios with priority logic...")
    print("   Feynman Rule: Both quarters (average) > Q2 only (recent) > Q1 only (older)")
    print("   Why? More data points = more reliable, recent data = more relevant")
    
    # Process each firm based on available quarters
    firm_ratios = []
    
    for gvkey in df_2025['gvkey'].unique():
        firm_data = df_2025[df_2025['gvkey'] == gvkey]
        
        # Check which quarters are available
        has_q1 = '2025Q1' in firm_data['quarter'].values
        has_q2 = '2025Q2' in firm_data['quarter'].values
        
        if has_q1 and has_q2:
            # Both quarters: calculate average
            pe_ratio = firm_data['PE_ratio'].mean()
            mb_ratio = firm_data['MB_ratio'].mean()
            data_source = 'Both (Averaged)'
        elif has_q2:
            # Q2 only: use Q2 data (prioritized)
            q2_data = firm_data[firm_data['quarter'] == '2025Q2'].iloc[0]
            pe_ratio = q2_data['PE_ratio']
            mb_ratio = q2_data['MB_ratio']
            data_source = 'Q2 Only'
        else:
            # Q1 only: use Q1 data
            q1_data = firm_data[firm_data['quarter'] == '2025Q1'].iloc[0]
            pe_ratio = q1_data['PE_ratio']
            mb_ratio = q1_data['MB_ratio']
            data_source = 'Q1 Only'
        
        # Get latest data for metadata
        latest_data = firm_data.iloc[-1]
        
        firm_ratios.append({
            'gvkey': gvkey,
            'company_name': latest_data['conm'],
            'sector': latest_data['gsector'],
            'avg_PE': pe_ratio,
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
    log.append(f"Firms with valid P/E ratios: {avg_ratios['avg_PE'].notna().sum():,}\n")
    log.append(f"Firms with valid M/B ratios: {avg_ratios['avg_MB'].notna().sum():,}\n")
    
    # STEP 5: Rank firms by valuation metrics (Feynman Logic: Simple percentile ranking)
    print("\n📈 STEP 5: Ranking firms by valuation metrics...")
    print("   Feynman Logic: Lower ratios = Better value → Top 10% = Best performers")
    print("   Method: Sort by ratio value, take bottom 10% (ascending order)")

    # Remove firms with NaN ratios for ranking (Data Contract: Clean data for analysis)
    avg_ratios_clean = avg_ratios.dropna(subset=['avg_PE', 'avg_MB']).copy()

    log.append(f"\n=== CLEAN DATA FOR RANKING ===\n")
    log.append(f"Firms with both valid P/E and M/B: {len(avg_ratios_clean):,}\n")
    log.append(f"Removed due to missing ratios: {len(avg_ratios) - len(avg_ratios_clean):,}\n")

    # Feynman Logic: Rank by P/E (ascending - lower is better value)
    print("   → Ranking by P/E: Lower ratio = Paying less per dollar of earnings")
    avg_ratios_clean['PE_rank'] = avg_ratios_clean['avg_PE'].rank(method='min')
    avg_ratios_clean['PE_percentile'] = avg_ratios_clean['avg_PE'].rank(pct=True) * 100

    # Feynman Logic: Rank by M/B (ascending - lower is more undervalued)
    print("   → Ranking by M/B: Lower ratio = Enterprise value < Book value (undervalued)")
    avg_ratios_clean['MB_rank'] = avg_ratios_clean['avg_MB'].rank(method='min')
    avg_ratios_clean['MB_percentile'] = avg_ratios_clean['avg_MB'].rank(pct=True) * 100

    # Calculate 10th percentile thresholds (Feynman Logic: Simple statistical cutoff)
    pe_threshold = avg_ratios_clean['avg_PE'].quantile(0.10)
    mb_threshold = avg_ratios_clean['avg_MB'].quantile(0.10)

    print(f"   → P/E 10th percentile threshold: {pe_threshold:.4f}")
    print(f"   → M/B 10th percentile threshold: {mb_threshold:.4f}")

    log.append("\n=== RANKING THRESHOLDS ===\n")
    log.append(f"10th percentile P/E threshold: {pe_threshold:.4f}\n")
    log.append(f"10th percentile M/B threshold: {mb_threshold:.4f}\n")

    # STEP 6: Identify top 10% firms (Feynman Logic: Apply simple cutoff)
    print("\n🏆 STEP 6: Identifying top 10% firms by each metric...")
    
    # Feynman Logic: Top 10% by P/E (lowest 10% = best value)
    print("   → Finding top 10% by P/E: Firms with lowest ratios (best value)")
    top_pe = avg_ratios_clean[avg_ratios_clean['PE_percentile'] <= 10].copy()
    top_pe = top_pe.sort_values('avg_PE')

    # Feynman Logic: Top 10% by M/B (lowest 10% = most undervalued)
    print("   → Finding top 10% by M/B: Firms with lowest ratios (most undervalued)")
    top_mb = avg_ratios_clean[avg_ratios_clean['MB_percentile'] <= 10].copy()
    top_mb = top_mb.sort_values('avg_MB')

    # Feynman Logic: Elite performers - intersection of both metrics
    print("   → Finding elite performers: Firms in top 10% of BOTH metrics (rare excellence)")
    top_both = avg_ratios_clean[
        (avg_ratios_clean['PE_percentile'] <= 10) &
        (avg_ratios_clean['MB_percentile'] <= 10)
    ].copy()
    top_both = top_both.sort_values(['PE_percentile', 'MB_percentile'])

    log.append("\n=== TOP 10% IDENTIFICATION ===\n")
    log.append(f"Top 10% by P/E ratio: {len(top_pe):,} firms\n")
    log.append(f"Top 10% by M/B ratio: {len(top_mb):,} firms\n")
    log.append(f"Top 10% in BOTH metrics (Elite): {len(top_both):,} firms\n")

    print(f"   ✅ Found {len(top_pe):,} firms in top 10% by P/E")
    print(f"   ✅ Found {len(top_mb):,} firms in top 10% by M/B")
    print(f"   ✅ Found {len(top_both):,} elite firms (both metrics)")
    
    # Add sector names
    sector_names = {
        10: 'Energy', 15: 'Materials', 20: 'Industrials', 
        25: 'Consumer Discretionary', 30: 'Consumer Staples', 
        35: 'Health Care', 40: 'Financials', 45: 'Information Technology',
        50: 'Communication Services', 55: 'Utilities', 60: 'Real Estate'
    }
    
    for df in [top_pe, top_mb, top_both, avg_ratios_clean]:
        df['sector_name'] = df['sector'].map(sector_names)
    
    # STEP 7: Generate CSV outputs (Data Contract: Guarantee expected schema)
    print("\n💾 STEP 7: Generating CSV outputs with guaranteed schema...")

    output_cols = ['gvkey', 'company_name', 'sector', 'sector_name', 'avg_PE', 'avg_MB',
                   'PE_rank', 'PE_percentile', 'MB_rank', 'MB_percentile', 'market_cap',
                   'price', 'eps', 'data_source']

    # Data Contract: Validate output schema before writing
    def validate_output_schema(df: pd.DataFrame, expected_cols: List[str]) -> bool:
        """DATA CONTRACT: Ensure output meets expected schema"""
        actual_cols = list(df.columns)
        if set(actual_cols) != set(expected_cols):
            raise ValueError(f"Output schema violation. Expected: {expected_cols}, Got: {actual_cols}")
        print(f"   ✅ Output schema validated for {len(df)} rows")
        return True

    print("   → Writing top 10% by P/E firms...")
    validate_output_schema(top_pe[output_cols], output_cols)
    top_pe[output_cols].to_csv(f"{output_dir}/top_10_pct_by_PE.csv", index=False)

    print("   → Writing top 10% by M/B firms...")
    validate_output_schema(top_mb[output_cols], output_cols)
    top_mb[output_cols].to_csv(f"{output_dir}/top_10_pct_by_MB.csv", index=False)

    print("   → Writing elite performers (both metrics)...")
    validate_output_schema(top_both[output_cols], output_cols)
    top_both[output_cols].to_csv(f"{output_dir}/top_10_pct_both_metrics.csv", index=False)
    
    log.append("\n=== OUTPUT FILES GENERATED ===\n")
    log.append("1. top_10_pct_by_PE.csv\n")
    log.append("2. top_10_pct_by_MB.csv\n")
    log.append("3. top_10_pct_both_metrics.csv\n")
    
    print("   CSV files created successfully")
    
    # Step 7: Create visualizations
    print("\nStep 7: Creating visualizations...")
    
    # Visualization 1: Distribution histograms
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # P/E distribution
    pe_values = avg_ratios_clean['avg_PE']
    pe_filtered = pe_values[(pe_values >= -50) & (pe_values <= 100)]  # Filter extremes
    
    ax1.hist(pe_filtered, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
    ax1.axvline(pe_threshold, color='red', linestyle='--', linewidth=2.5, 
                label=f'10th Percentile: {pe_threshold:.2f}')
    ax1.set_xlabel('Average P/E Ratio', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Number of Firms', fontsize=12, fontweight='bold')
    ax1.set_title('P/E Ratio Distribution\n2025 Q1 & Q2 Average', 
                  fontsize=13, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # M/B distribution
    mb_values = avg_ratios_clean['avg_MB']
    mb_filtered = mb_values[(mb_values >= -5) & (mb_values <= 15)]  # Filter extremes
    
    ax2.hist(mb_filtered, bins=50, color='lightcoral', edgecolor='black', alpha=0.7)
    ax2.axvline(mb_threshold, color='red', linestyle='--', linewidth=2.5,
                label=f'10th Percentile: {mb_threshold:.2f}')
    ax2.set_xlabel('Average M/B Ratio', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Number of Firms', fontsize=12, fontweight='bold')
    ax2.set_title('M/B Ratio Distribution\n2025 Q1 & Q2 Average', 
                  fontsize=13, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/distribution_histograms.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    print("   ✓ Distribution histograms created")
    
    # Visualization 3: Sector breakdown
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Top 10% by P/E - sector breakdown
    pe_sector_counts = top_pe['sector_name'].value_counts().sort_values(ascending=True)
    ax1.barh(pe_sector_counts.index, pe_sector_counts.values, color='steelblue')
    ax1.set_xlabel('Number of Firms', fontsize=11, fontweight='bold')
    ax1.set_title(f'Top 10% by P/E Ratio - Sector Distribution\n(Total: {len(top_pe)} firms)', 
                  fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='x')
    for i, v in enumerate(pe_sector_counts.values):
        ax1.text(v + 0.5, i, str(v), va='center', fontweight='bold')
    
    # Top 10% by M/B - sector breakdown
    mb_sector_counts = top_mb['sector_name'].value_counts().sort_values(ascending=True)
    ax2.barh(mb_sector_counts.index, mb_sector_counts.values, color='seagreen')
    ax2.set_xlabel('Number of Firms', fontsize=11, fontweight='bold')
    ax2.set_title(f'Top 10% by M/B Ratio - Sector Distribution\n(Total: {len(top_mb)} firms)', 
                  fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='x')
    for i, v in enumerate(mb_sector_counts.values):
        ax2.text(v + 0.5, i, str(v), va='center', fontweight='bold')
    
    # Elite performers - sector breakdown
    if len(top_both) > 0:
        both_sector_counts = top_both['sector_name'].value_counts().sort_values(ascending=True)
        ax3.barh(both_sector_counts.index, both_sector_counts.values, color='crimson')
        ax3.set_xlabel('Number of Firms', fontsize=11, fontweight='bold')
        ax3.set_title(f'Elite Performers (Both Metrics) - Sector Distribution\n(Total: {len(top_both)} firms)', 
                      fontsize=12, fontweight='bold')
        ax3.grid(True, alpha=0.3, axis='x')
        for i, v in enumerate(both_sector_counts.values):
            ax3.text(v + 0.1, i, str(v), va='center', fontweight='bold')
    else:
        ax3.text(0.5, 0.5, 'No firms in top 10% for both metrics', 
                ha='center', va='center', fontsize=14)
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)
    
    # All firms - sector distribution (for comparison)
    all_sector_counts = avg_ratios_clean['sector_name'].value_counts().sort_values(ascending=True)
    ax4.barh(all_sector_counts.index, all_sector_counts.values, color='lightgray')
    ax4.set_xlabel('Number of Firms', fontsize=11, fontweight='bold')
    ax4.set_title(f'All Firms - Sector Distribution\n(Total: {len(avg_ratios_clean)} firms)', 
                  fontsize=12, fontweight='bold')
    ax4.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/sector_breakdown.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    print("   ✓ Sector breakdown created")
    
    # Visualization 4: Summary dashboard
    # Calculate percentiles for axis limits
    pe_95 = avg_ratios_clean['avg_PE'].quantile(0.95)
    mb_95 = avg_ratios_clean['avg_MB'].quantile(0.95)
    
    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # Summary statistics text
    ax_text = fig.add_subplot(gs[0, :])
    ax_text.axis('off')
    
    summary_text = f"""
    TOP 10% FIRMS ANALYSIS - 2025 Q1 & Q2 SUMMARY
    
    Total firms analyzed: {len(avg_ratios_clean):,}
    Data Sources: Both Qtrs={len(firms_with_both):,}, Q2 Only={(avg_ratios['data_source']=='Q2 Only').sum():,}, Q1 Only={(avg_ratios['data_source']=='Q1 Only').sum():,}
    
    TOP 10% RESULTS:
    • Firms in top 10% by P/E ratio: {len(top_pe):,} (threshold: {pe_threshold:.4f})
    • Firms in top 10% by M/B ratio: {len(top_mb):,} (threshold: {mb_threshold:.4f})
    • Elite performers (both metrics): {len(top_both):,}
    
    RATIO STATISTICS (All Firms):
    • P/E: Mean={avg_ratios_clean['avg_PE'].mean():.2f}, Median={avg_ratios_clean['avg_PE'].median():.2f}, Std={avg_ratios_clean['avg_PE'].std():.2f}
    • M/B: Mean={avg_ratios_clean['avg_MB'].mean():.2f}, Median={avg_ratios_clean['avg_MB'].median():.2f}, Std={avg_ratios_clean['avg_MB'].std():.2f}
    """
    
    ax_text.text(0.5, 0.5, summary_text, ha='center', va='center', 
                fontsize=12, family='monospace', 
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    # Top 5 by P/E
    ax_top_pe = fig.add_subplot(gs[1, 0])
    top5_pe = top_pe.head(5)[['company_name', 'avg_PE']].copy()
    top5_pe['company_name'] = top5_pe['company_name'].str[:25]  # Truncate names
    ax_top_pe.barh(range(len(top5_pe)), top5_pe['avg_PE'], color='steelblue')
    ax_top_pe.set_yticks(range(len(top5_pe)))
    ax_top_pe.set_yticklabels(top5_pe['company_name'], fontsize=9)
    ax_top_pe.set_xlabel('P/E Ratio', fontsize=10, fontweight='bold')
    ax_top_pe.set_title('Top 5 Firms by P/E', fontsize=11, fontweight='bold')
    ax_top_pe.invert_yaxis()
    ax_top_pe.grid(True, alpha=0.3, axis='x')
    
    # Top 5 by M/B
    ax_top_mb = fig.add_subplot(gs[1, 1])
    top5_mb = top_mb.head(5)[['company_name', 'avg_MB']].copy()
    top5_mb['company_name'] = top5_mb['company_name'].str[:25]
    ax_top_mb.barh(range(len(top5_mb)), top5_mb['avg_MB'], color='seagreen')
    ax_top_mb.set_yticks(range(len(top5_mb)))
    ax_top_mb.set_yticklabels(top5_mb['company_name'], fontsize=9)
    ax_top_mb.set_xlabel('M/B Ratio', fontsize=10, fontweight='bold')
    ax_top_mb.set_title('Top 5 Firms by M/B', fontsize=11, fontweight='bold')
    ax_top_mb.invert_yaxis()
    ax_top_mb.grid(True, alpha=0.3, axis='x')
    
    # Elite performers list
    ax_elite = fig.add_subplot(gs[1, 2])
    ax_elite.axis('off')
    if len(top_both) > 0:
        elite_text = "ELITE PERFORMERS\n(Top 10% in BOTH metrics)\n\n"
        for idx, row in top_both.head(10).iterrows():
            name = row['company_name'][:30]
            elite_text += f"{name}\n"
        ax_elite.text(0.1, 0.9, elite_text, ha='left', va='top', fontsize=9, 
                     family='monospace',
                     bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.3))
    else:
        ax_elite.text(0.5, 0.5, 'No Elite Performers', ha='center', va='center', fontsize=12)
    
    # Scatter plot (mini version)
    ax_scatter = fig.add_subplot(gs[2, :])
    ax_scatter.scatter(avg_ratios_clean['avg_PE'], avg_ratios_clean['avg_MB'], 
                      c='lightgray', alpha=0.4, s=30)
    ax_scatter.scatter(top_both['avg_PE'], top_both['avg_MB'], 
                      c='red', alpha=0.8, s=100, marker='*', label='Elite Performers')
    ax_scatter.axvline(pe_threshold, color='blue', linestyle='--', alpha=0.5)
    ax_scatter.axhline(mb_threshold, color='green', linestyle='--', alpha=0.5)
    ax_scatter.set_xlabel('Average P/E Ratio', fontsize=11, fontweight='bold')
    ax_scatter.set_ylabel('Average M/B Ratio', fontsize=11, fontweight='bold')
    ax_scatter.set_title('Elite Performers Visualization', fontsize=12, fontweight='bold')
    ax_scatter.set_xlim(-10, min(pe_95, 100))
    ax_scatter.set_ylim(-1, min(mb_95, 10))
    ax_scatter.legend()
    ax_scatter.grid(True, alpha=0.3)
    
    plt.savefig(f"{output_dir}/summary_dashboard.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    print("   ✓ Summary dashboard created")
    
    # Step 8: Generate analysis summary
    print("\nStep 8: Generating analysis summary...")
    
    log.append("\n=== SECTOR DISTRIBUTION ANALYSIS ===\n")
    log.append("\nTop 10% by P/E - Sector Breakdown:\n")
    for sector, count in pe_sector_counts.items():
        log.append(f"  {sector}: {count} firms\n")
    
    log.append("\nTop 10% by M/B - Sector Breakdown:\n")
    for sector, count in mb_sector_counts.items():
        log.append(f"  {sector}: {count} firms\n")
    
    if len(top_both) > 0:
        log.append("\nElite Performers - Sector Breakdown:\n")
        for sector, count in both_sector_counts.items():
            log.append(f"  {sector}: {count} firms\n")
    else:
        log.append("\nNo firms qualified as elite performers (top 10% in both metrics)\n")
    
    log.append("\n=== STATISTICAL COMPARISON ===\n")
    log.append("\nAll Firms Statistics:\n")
    log.append(f"  P/E: Mean={avg_ratios_clean['avg_PE'].mean():.4f}, Median={avg_ratios_clean['avg_PE'].median():.4f}, Std={avg_ratios_clean['avg_PE'].std():.4f}\n")
    log.append(f"  M/B: Mean={avg_ratios_clean['avg_MB'].mean():.4f}, Median={avg_ratios_clean['avg_MB'].median():.4f}, Std={avg_ratios_clean['avg_MB'].std():.4f}\n")
    
    log.append("\nTop 10% by P/E Statistics:\n")
    log.append(f"  P/E: Mean={top_pe['avg_PE'].mean():.4f}, Median={top_pe['avg_PE'].median():.4f}, Std={top_pe['avg_PE'].std():.4f}\n")
    log.append(f"  M/B: Mean={top_pe['avg_MB'].mean():.4f}, Median={top_pe['avg_MB'].median():.4f}, Std={top_pe['avg_MB'].std():.4f}\n")
    
    log.append("\nTop 10% by M/B Statistics:\n")
    log.append(f"  P/E: Mean={top_mb['avg_PE'].mean():.4f}, Median={top_mb['avg_PE'].median():.4f}, Std={top_mb['avg_PE'].std():.4f}\n")
    log.append(f"  M/B: Mean={top_mb['avg_MB'].mean():.4f}, Median={top_mb['avg_MB'].median():.4f}, Std={top_mb['avg_MB'].std():.4f}\n")
    
    if len(top_both) > 0:
        log.append("\nElite Performers Statistics:\n")
        log.append(f"  P/E: Mean={top_both['avg_PE'].mean():.4f}, Median={top_both['avg_PE'].median():.4f}, Std={top_both['avg_PE'].std():.4f}\n")
        log.append(f"  M/B: Mean={top_both['avg_MB'].mean():.4f}, Median={top_both['avg_MB'].median():.4f}, Std={top_both['avg_MB'].std():.4f}\n")
    
    log.append("\n=== TOP 5 PERFORMERS ===\n")
    log.append("\nTop 5 by P/E Ratio:\n")
    for idx, (i, row) in enumerate(top_pe.head(5).iterrows(), 1):
        log.append(f"  {idx}. {row['company_name']} - P/E: {row['avg_PE']:.4f}, M/B: {row['avg_MB']:.4f}, Sector: {row['sector_name']}\n")
    
    log.append("\nTop 5 by M/B Ratio:\n")
    for idx, (i, row) in enumerate(top_mb.head(5).iterrows(), 1):
        log.append(f"  {idx}. {row['company_name']} - M/B: {row['avg_MB']:.4f}, P/E: {row['avg_PE']:.4f}, Sector: {row['sector_name']}\n")
    
    if len(top_both) > 0:
        log.append("\nTop Elite Performers (Both Metrics):\n")
        for idx, (i, row) in enumerate(top_both.head(10).iterrows(), 1):
            log.append(f"  {idx}. {row['company_name']} - P/E: {row['avg_PE']:.4f}, M/B: {row['avg_MB']:.4f}, Sector: {row['sector_name']}\n")
    
    log.append("\n=== ANALYSIS COMPLETE ===\n")
    log.append(f"Completion Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Save log
    with open(f"{output_dir}/analysis_summary.txt", 'w') as f:
        f.writelines(log)
    
    print("   ✓ Analysis summary saved")
    
    print("\n" + "="*70)
    print("🎉 ANALYSIS COMPLETE - Feynman Wisdom Achieved!")
    print("="*70)
    print("💡 KEY LESSON: Complex valuation boiled down to simple ratios")
    print("   • P/E = Price ÷ Earnings (lower = better value)")
    print("   • M/B = Enterprise Value ÷ Book Value (lower = more undervalued)")
    print("   • Top 10% = Best performers by these fundamental metrics")
    print(f"\n📁 Output files generated in: {os.path.abspath(output_dir)}/")
    print("\n📊 CSV Files (Data Contract Compliant):")
    print(f"  • top_10_pct_by_PE.csv ({len(top_pe)} firms - best value by earnings)")
    print(f"  • top_10_pct_by_MB.csv ({len(top_mb)} firms - most undervalued by assets)")
    print(f"  • top_10_pct_both_metrics.csv ({len(top_both)} firms - elite performers)")
    print("\n📈 Visualizations:")
    print("  • distribution_histograms.png - ratio distributions")
    print("  • sector_breakdown.png - sector analysis")
    print("  • summary_dashboard.png - executive overview")
    print("\n📝 Documentation:")
    print("  • analysis_summary.txt - complete methodology & results")
    print("\n" + "="*70)
    
if __name__ == "__main__":
    main()

