# 📊 **COMPREHENSIVE COMPUSTAT BALANCING MODELS GUIDE**

## 🎯 **OVERVIEW**

This guide provides a complete mathematical framework for understanding Compustat financial data balancing models. Each model represents structured templates that show how different financial statement components must mathematically balance (assets = liabilities + equity, income statement flows, cash flow reconciliation).

### **Available Models & Time Horizons**
- **Financial Statement Types**: Income Statement, Balance Sheet, Cash Flow Statement
- **Time Horizons**: Annual (A_), Semi-Annual (SA_), Quarterly (Q_), Year-to-Date (YTD_)
- **Data Frequency**: Annual, Semi-Annual, Quarterly, Year-to-Date

### **Core Identifiers**
- **GVKEY**: Global Company Key (6-digit unique identifier)
- **DATADATE**: Data Date (Financial statement date in YYYYMMDD format)

### **Data Selection**
- Use `GVKEY` for company identification
- Filter by `DATADATE` for specific periods

---

## 📋 **BALANCING MODELS MATHEMATICAL FRAMEWORK**

### **Balance Sheet Models**

#### **Annual Balance Sheet (A_Balance_Sheet.csv)**
**Asset Aggregations:**
- **Cash and Short-Term Investments**: `CHE = CH + IVST`
- **Receivables Total**: `RECT = RECTR + TXR + RECCO`
- **Inventories Total**: `INVT = INVRM + INVWIP + INVFG + INVO`
- **Current Assets - Other Total**: `ACO = XPP + ACOX`
- **Current Assets Total**: `ACT = CHE + RECT + INVT + ACO`
- **Property Plant & Equipment (Net)**: `PPENT = PPEGT - DPACT`
- **Intangible Assets Total**: `INTAN = GDWL + INTANO`
- **Assets - Other Total**: `AO = DC + AOX`
- **Total Assets**: `AT = ACT + PPENT + IVAEQ + IVAO + INTAN + AO`

**Liability Aggregations:**
- **Debt in Current Liabilities**: `DLC = DD1 + NP`
- **Current Liabilities Total**: `LCT = DLC + AP + TXP + LCO`
- **Total Liabilities**: `LT = LCT + DLTT + TXDITC + LO`

**Equity Aggregations:**
- **Preferred Stock Total**: `PSTK = PSTKR + PSTKN`
- **Retained Earnings**: `RE = REUNA + ACOMINC + SEQO`
- **Accumulated Other Comprehensive Income**: `ACOMINC = AOCIDERGL + AOCIOTHER + AOCIPEN + AOCISECGL - MSA - RECTA`
- **Common Equity Total**: `CEQ = CSTK + CAPS + RE - TSTK`
- **Stockholders Equity - Parent**: `SEQ = PSTK + CEQ`
- **Stockholders Equity - Total**: `TEQ = SEQ + MIBN`
- **Liabilities & Equity Total**: `LSE = LT + MIB + TEQ`

#### **Quarterly Balance Sheet (Q_Balance_Sheet.csv)**
**Asset Aggregations:**
- **Receivables Total**: `RECTQ = RECTOQ + RECTRQ`
- **Current Assets Total**: `ACTQ = CHEQ + RECTQ + INVTQ + ACOQ`
- **Property Plant & Equipment (Net)**: `PPENTQ = PPEGTQ - DPACTQ`
- **Total Assets**: `ATQ = ACTQ + PPENTQ + AOQ`

**Liability Aggregations:**
- **Debt in Current Liabilities**: `DLCQ = DD1Q + NPQ`
- **Current Liabilities - Other**: `LCOQ = XACCQ + LCOXQ`
- **Current Liabilities Total**: `LCTQ = DLCQ + APQ + TXPQ + LCOQ`
- **Total Liabilities**: `LTQ = LCTQ + DLTTQ + TXDITCQ + LOQ`

**Equity Aggregations:**
- **Preferred Stock Total**: `PSTKQ = PSTKNQ + PSTKRQ`
- **Retained Earnings**: `REQ = REUNAQ + ACOMINCQ + SEQOQ`
- **Accumulated Other Comprehensive Income**: `ACOMINCQ = AOCIDERGLQ + AOCIOTHERQ + AOCIPENQ + AOCISECGLQ - MSAQ - RECTA`
- **Common Equity Total**: `CEQQ = CSTKQ + CAPSQ + REQ - TSTKQ`
- **Stockholders Equity - Parent**: `SEQQ = PSTKQ + CEQQ`
- **Stockholders Equity - Total**: `TEQQ = SEQQ + MIBNQ`
- **Liabilities & Equity Total**: `LSEQ = LTQ + MIBQ + TEQQ`

---

### **Income Statement Models**

#### **Annual Income Statement (A_Income_Statement.csv)**
**Revenue & Margin Calculations:**
- **Operating Expenses Total**: `XOPR = COGS + XSGA`
- **Gross Profit**: `GP = SALE - COGS`
- **Operating Income Before Depreciation**: `OIBDP = SALE - XOPR`
- **Operating Income After Depreciation**: `OIADP = OIBDP - DP`

**Income Flow:**
- **Nonoperating Income (Expense) - Total**: `NOPI = IDIT + NOPIO`
- **Pretax Income**: `PI = OIADP - XINT + NOPI + SPI`
- **Income Before Extraordinary Items and Noncontrolling Interest**: `IBMII = PI - TXT`
- **Income Before Extraordinary Items**: `IB = IBMII - MII`
- **Income Before Extraordinary Items - Available for Common**: `IBCOM = IB - DVP`
- **Income Before Extraordinary Items - Adjusted**: `IBADJ = IBCOM + CSTKE`
- **Extraordinary Items and Discontinued Operations**: `XIDO = XI + DO`
- **Net Income**: `NIADJ = IBADJ + XIDO`

**Tax Calculations:**
- **Income Taxes Total**: `TXT = TXC + TXDI + TXO`
- **Income Taxes - Current**: `TXC = TXFED + TXS + TXFO`
- **Income Taxes - Deferred**: `TXDI = TXDFED + TXDS + TXDFO`

**Per Share Metrics:**
- **Basic EPS (Excluding Extra)**: `EPSPX = IBCOM ÷ CSHPRI`
- **Diluted EPS (Excluding Extra)**: `EPSFX = IBCOM ÷ CSHFD`
- **Basic EPS (Including Extra)**: `EPSPI = IB ÷ CSHPRI`
- **Diluted EPS (Including Extra)**: `EPSFI = IB ÷ CSHFD`

#### **Semi-Annual Income Statement (SA_Income_Statement.csv)**
**Revenue & Margin Calculations:**
- **Operating Expenses Total**: `XOPRSA = COGSSA + XSGASA`
- **Operating Income Before Depreciation**: `OIBDPSA = SALESA - XOPRSA`
- **Operating Income After Depreciation**: `OIADPSA = OIBDPSA - DPSA`

**Income Flow:**
- **Pretax Income**: `PISA = OIADPSA - XINTSA + NOPISA + SPISA`
- **Income Before Extraordinary Items**: `IBSA = IBMIISA - MIISA`
- **Net Income**: `NISA = IBSA + XIDOSA`

**Per Share Metrics:**
- **Basic EPS (Excluding Extra)**: `EPSPXSA = IBCOMSA ÷ CSHPRSA`
- **Diluted EPS (Excluding Extra)**: `EPSFXSA = IBCOMSA ÷ CSHFDSA`

#### **Quarterly Income Statement (Q_Income_Statement.csv)**
**Revenue & Margin Calculations:**
- **Operating Expenses Total**: `XOPRQ = COGSQ + XSGAQ`
- **Operating Income Before Depreciation**: `OIBDPQ = SALEQ - XOPRQ`
- **Operating Income After Depreciation**: `OIADPQ = OIBDPQ - DPQ`

**Income Flow:**
- **Pretax Income**: `PIQ = OIADPQ - XINTQ + NOPIQ + SPIQ`
- **Income Before Extraordinary Items**: `IBQ = IBMIIQ - MIIQ`
- **Net Income**: `NIQ = IBQ + XIDOQ`

**Per Share Metrics:**
- **Basic EPS (Excluding Extra)**: `EPSPXQ = IBCOMQ ÷ CSHPRQ`
- **Diluted EPS (Excluding Extra)**: `EPSFXQ = IBCOMQ ÷ CSHFDQ`

#### **Year-To-Date Income Statement (YTD_Income_Statement_.csv)**
**Revenue & Margin Calculations:**
- **Operating Expenses Total**: `XOPRY = COGSY + XSGAY`
- **Operating Income Before Depreciation**: `OIBDPY = SALEY - XOPRY`
- **Operating Income After Depreciation**: `OIADPY = OIBDPY - DPY`

**Income Flow:**
- **Pretax Income**: `PIY = OIADPY - XINTY + NOPIY + SPIY`
- **Income Before Extraordinary Items**: `IBY = IBMIIY - MIIY`
- **Net Income**: `NIY = IBY + XIDOY`

**Per Share Metrics:**
- **Basic EPS (Excluding Extra)**: `EPSPXY = IBCOMY ÷ CSHPRY`
- **Diluted EPS (Excluding Extra)**: `EPSFXY = IBCOMY ÷ CSHFDY`

---

### **Cash Flow Models**

#### **Annual Cash Flow (A_Cash_Flow.csv)**
**Operating Activities:**
- **Funds from Operations - Other**: `FOPO = TXBCO + FOPOX`
- **Operating Activities Net Cash Flow**: `OANCF = IBC + DPC + XIDOC + TXDC + ESUBC + SPPIV + FOPO + RECCH + INVCH + APALCH + TXACH + AOLOCH`

**Investing Activities:**
- **Investing Activities Net Cash Flow**: `IVNCF = -IVCH + SIV + IVSTCH - CAPX + SPPE - AQC + IVACO`

**Financing Activities:**
- **Financing Activities Net Cash Flow**: `FINCF = SSTK + TXBCOF - PRSTKC - DV + DLTIS - DLTR + DLCCH + FIAO`

**Cash Flow Reconciliation:**
- **Change in Cash**: `CHECH = OANCF + IVNCF + FINCF + EXRE`

#### **YTD Cash Flow (YTD_Cash_Flow.csv)**
*Note: Quarterly Cash Flow is presented as period data (1st quarter = 3 months; 2nd quarter = 6 months; 3rd quarter = 9 months, 4th quarter = 12 months)*

**Operating Activities:**
- **Funds from Operations - Other**: `FOPOY = TXBCOY + FOPOXY`
- **Operating Activities Net Cash Flow**: `OANCFY = IBCY + DPCY + XIDOCY + TXDCY + ESUBCY + SPPIVY + FOPOY + RECCHY + INVCHY + APALCHY + TXACHY + AOLOCHY`

**Investing Activities:**
- **Investing Activities Net Cash Flow**: `IVNCFY = -IVCHY + SIVY + IVSTCHY - CAPXY + SPPEY - AQCY + IVACOY`

**Financing Activities:**
- **Financing Activities Net Cash Flow**: `FINCFY = SSTKY + TXBCOFY - PRSTKCY - DVY + DLTISY - DLTRY + DLCCHY + FIAOY`

**Cash Flow Reconciliation:**
- **Change in Cash**: `CHECHY = OANCFY + IVNCFY + FINCFY + EXREY`

---

### **Summary Models**

#### **Annual Industry Summary (A_INDL_SUMM_STD.csv)**
**Income Statement Aggregation:**
- **Pretax Income**: `PI = SALE - COGS - XSGA - DP - XINT + NOPI`
- **Income Before Extraordinary Items**: `IB = IBMII - MII`
- **Basic EPS (Excluding Extra)**: `EPSPX` (calculated by dividing by adjustment factor)
- **Diluted EPS (Excluding Extra)**: `EPSFX` (calculated by dividing by adjustment factor)
- **Basic EPS (Including Extra)**: `EPSPI` (calculated by dividing by adjustment factor)
- **Diluted EPS (Including Extra)**: `EPSFI` (calculated by dividing by adjustment factor)

**Key Variables Available:**
- **Revenue & Expenses**: `SALE`, `COGS`, `XSGA`, `DP`, `XINT`, `NOPI`, `TXT`
- **Income Metrics**: `PI`, `IBMII`, `MII`, `IB`, `XIDO`, `NI`
- **Per Share Data**: `EPSPX`, `EPSPI`, `EPSFX`, `EPSFI`, `CSHPRI`, `CSHFD`
- **Balance Sheet**: `WCAP`, `PPENT`, `DLTT`, `REUNA`, `SEQ`, `TEQ`, `AT`
- **Cash Flow**: `CAPX`, `EMP`



## 📈 **FINANCIAL ANALYSIS FRAMEWORK**

### **Balance Sheet Analysis**
- **Liquidity**: Current ratio = `ACT / LCT`
- **Leverage**: Debt-to-equity = `LT / TEQ`
- **Efficiency**: Asset turnover = `SALE / AT`

### **Income Statement Analysis**
- **Profitability**: ROA = `NI / AT`, ROE = `NI / TEQ`
- **Margins**: Gross margin = `GP / SALE`, Operating margin = `OIADP / SALE`

### **Cash Flow Analysis**
- **Operating Cash Flow Margin**: `OANCF / SALE`
- **Free Cash Flow**: `OANCF - CAPX`
- **Cash Conversion**: `OANCF / NI`

