
---
# 📈 **Quantitative Sector Valuation Analysis for UTIMCO Investment Initiative**

**Project:** Analysis of quarterly valuation data for over 15,000 U.S. Corporations as part of a new $2.5M investment initiative funded by UTIMCO.

## 🏛️ **About UTIMCO**

UTIMCO is a 501(c)(3) investment management corporation whose sole purpose is the management of investment assets under the fiduciary care of the Board of Regents of The University of Texas System. Created in March 1996, UTIMCO is the first external investment corporation formed by a public university system in the nation. It invests endowment and operating funds in excess of $19 billion (AUM).

### **Endowment Pools Managed:**
1. **Permanent University Fund (PUF)** - Primary focus for this analysis
2. **Permanent Health Fund (PHF)**
3. **Long Term Fund (LTF)**
4. **Separately Invested Funds (SIF)**

### **Contact Information:**
- **Email:** ContactUs@utimco.org
- **Phone:** 512.225.1600
- **Address:** 210 West 7th Street, Suite 1700, Austin, Texas 78701
- **Website:** [utimco.org](https://www.utimco.org/)

### **Key Resources:**
- [UTIMCO Homepage](https://www.utimco.org)
- [Funds Managed](https://www.utimco.org/funds-managed/)
- [Permanent University Fund (PUF)](https://www.utimco.org/funds-managed/endowment-funds/permanent-university-fund-puf/)
- [Student Investment Programs](https://news.utdallas.edu/students-teaching/student-run-investment-funds-to-yield-high-educati/)
- [UT System Overview](https://www.utsystem.edu/about/university-texas-texas-am-investment-management-company)

---

## 🎯 **Objective**

**Quantitative sector valuation analysis to guide $2.5M fund allocation across 11 GICS sectors** through computing P/E and Market-to-Book ratios for each firm from Compustat quarterly financial data (2010-2025), then characterizing the mean and variance of those ratios by sector over each quarter to prioritize maximum return on investment.

---

## 📁 **Project Structure & Data Sources**

### **Core Data Sources:**

#### **📊 Balancing Models/**
Comprehensive mathematical frameworks for Compustat financial statement balancing models across multiple time horizons:
- **Financial Statement Types:** Income Statement, Balance Sheet, Cash Flow Statement
- **Time Horizons:** Annual (A_), Semi-Annual (SA_), Quarterly (Q_), Year-to-Date (YTD_)

#### **💾 Compustat Qtrly Data 2010-2025/**
Primary dataset containing standardized financial data for analysis:
- **Main Dataset:** `Compustat_Quarterl_2010_2025.csv` (~714,894 quarterly observations)
- **Financial Variables Dictionary:** Complete A-Z reference of 1,300+ Compustat variables
- **Coverage:** Over 3,000 U.S. corporations (2010-2025)

#### **🏷️ GICS Codes/**
Global Industry Classification Standard (GICS) system for sector classification:
- **11 Sectors:** Energy, Materials, Industrials, Consumer Discretionary, Consumer Staples, Health Care, Financials, Information Technology, Communication Services, Utilities, Real Estate
- **Hierarchical Structure:** 11 Sectors → 25 Industry Groups → 74 Industries → 163 Sub-Industries
- **Purpose:** Market-oriented classification superior to NAICS for investment analysis

#### **🏭 NAICS Codes/**
North American Industry Classification System (alternative classification):
- **Purpose:** Government statistical classification system
- **Note:** GICS preferred over NAICS for this investment-focused analysis

### **Analysis Phases:**

#### **🧹 Phase 1: Data Preparation**
- Data cleaning and preprocessing
- Null value removal and data validation
- Financial ratio calculations preparation

#### **⚙️ Phase 2: Algorithm Development**
- Financial ratio computation algorithms (P/E, Market-to-Book)
- Time series analysis implementation
- Sector aggregation logic development

#### **📈 Phase 3: Sector Analysis**
- GICS sector grouping and aggregation
- Statistical analysis (mean, median, variance) by sector and quarter
- Panel dataset creation with sector × quarter × ratio × statistics dimensions

#### **💼 Phase 4: Investment Decisions**
- Relative returns analysis vs. benchmarks
- Portfolio allocation optimization
- Risk-adjusted return assessment

---

## 🏗️ **Investment Philosophy & Key Principles**

### **Core Investment Tenets:**
- **Productive Assets:** Investing is about owning productive assets that generate cash flow and value over time
- **Equity as Asset Bundles:** Public companies are bundles of assets known as equity securities, valued by what they earn (income) and what they own (assets)
- **Risk-Adjusted Returns:** A fund's capital should be allocated where the risk-adjusted future return is likely to be highest
- **Price vs. Value Gap:** Price (what buyers pay) and value (fundamentals) can and do diverge — opportunity arises in that gap
- **Firm Filtering:** The investment process involves systematically filtering firms based on valuation metrics 

---

## 📚 **Valuation Theory & Financial Concepts**

### **Stock Valuation Fundamentals**
**The value of a stock is the present value of all future dividends.**

**Dividend Discount Model:**
```
P₀ = current price of the stock
P₁ = price in one period
D₁ = cash dividend paid at the end of the period
R = required return

P₀ = (D₁ + P₁) / (1 + R)
```

### **Valuation Ratios and Multiples**
Valuation multiples are ratios that relate a company's market value to some measure of its economic activity or asset base. They serve as standardized metrics for comparing companies across different sizes, industries, and growth stages. Multiples can also be calculated with   non-financial variables if they affect the share price. For mobile telecommunications, for example, the number of subscribers is defined as the      relevant performance indicator. For hospitals and hotels, the relevant performance indicator is the number of beds, while for social media companies, it is the number of registered users.

#### **Important Valuation Concepts:**
- **Intrinsic Value:** True fundamental value based on discounted cash flows (DCF)
- **Relative Valuation:** Comparison with similar companies or benchmarks
- **Comparables Method:** Using peer company multiples for valuation
- **Law of One Price:** Similar assets should trade at similar prices; two identical assets trade at the same price
- **GARP Strategy:** Growth at a Reasonable Price investment strategy
- **Alpha:** Excess return relative to benchmark

#### **Two Main Approaches to Multiples:**
1. **Relative Valuation:** Uses multiples from similar publicly traded companies to assess the value of an equity security against a benchmark
2. **Intrinsic Valuation:** Intrinsic value of an equity security determined from a cash flow model using growth rate of cash flows and expected return

> **Note:** Valuation multiples provide a standardized way to compare companies and assess relative value. The key is understanding both the market's current assessment (comparable approach) and what fundamentals justify (fundamental approach). Combining both methods with careful consideration of growth, risk, and industry characteristics leads to more robust valuation conclusions. Remember that multiples are tools, not definitive answers. They should be used as part of a comprehensive valuation framework that includes discounted cash flow analysis, comparable transactions, and qualitative factors.

---

## 🔢 **Multiples Overview**

### **Enterprise vs. Price Multiples**
- **Enterprise Value Multiples:** Place the value of the operating company in relation to quantities attributable to providers of capital (e.g., EBITDA, EBIT)
- **Price Multiples:** Divide share price by quantities allocable to equity providers (e.g., EPS, book value per share)

### **Enterprise Value vs. Equity Value**
- **Equity Value:** Market value of shareholders' stake
- **Enterprise Value:** Value of the entire business (Equity + Debt - Cash)
- **EV Advantage:** Better for comparing companies with different capital structures

### **Justified vs. Market Multiples**
- **Market Multiples:** What investors are currently paying
- **Justified Multiples:** What fundamentals suggest they should pay
- **Gap Analysis:** Helps identify mispriced securities

### **Price Multiples (Equity-Based)**
1. **P/E Ratio:** Price-to-Earnings = Share Price ÷ Annual EPS
2. **P/B Ratio:** Price-to-Book = Share Price ÷ Book Value per Share
3. **P/C Ratio:** Price-to-Cash Flow = Share Price ÷ Cash Flow per Share
4. **PEG Ratio:** Price/Earnings-to-Growth = P/E ÷ Expected Growth Rate (g)

### **Enterprise Value Multiples (Entity-Based)**
1. **EV/EBITDA:** Enterprise Value to EBITDA = Enterprise Value ÷ EBITDA
2. **EV/S:** Enterprise Value to Sales = Enterprise Value ÷ Annual Sales
3. **EV Formula:** Market Value of Equity + Debt - Cash

### **Justified Multiples (Gordon Growth Model)**
1. **Justified P/E:** P/E* = (1 - b) × (1 + g) ÷ (r - g)
2. **Justified P/B:** P/B* = (ROE × (1 - b) × (1 + g)) ÷ (r - g)
3. **Justified PEG:** PEG* = P/E* ÷ g

**Where:**
- **b** = Retention rate = (1 - dividend payout ratio)
- **g** = Expected growth rate = (1 - Dividend Payout) × ROE
- **r** = Required return on equity = (Risk-free Rate + Beta × Market Risk Premium)
- **ROE** = Return on Equity

**Gordon Growth Model:** P₀ = D₁ ÷ (r - g), where D₁ = E₁ × (1 - b), and E₁ = E₀ × (1 + g) 


---

## 📊 **Multiples In-Depth**

### **Price-to-Earnings (P/E) Ratios**
The Price-to-Earnings ratio compares a company's stock price to its earnings per share: **P/E = Share Price ÷ Annual EPS**

**Key Components:**
- **Share Price:** Current market price per share (Market Value of Equity ÷ Number of Outstanding Shares)
*a two-for-one stock split doubles the number of shares, which halves the share price*
- **Annual EPS:** Net Income ÷ Number of Shares Outstanding
- **P/E Ratio:** How much investors pay per dollar of earnings
- **EPS:** = earnings per share which reflects the profitability of the equity

**P/E Ratio Types:**
- **Trailing P/E:** Based on past 12 months of earnings
- **Forward P/E:** Based on expected future earnings
- **Current P/E:** Based on earnings of past financial year

**Example Calculation:**
```
Company XYZ:
- Current stock price: $50
- Annual EPS: $2.50
- Trailing P/E = $50 ÷ $2.50 = 20
```
*Investors are willing to pay $20 for every $1 of annual earnings.*

**Key Assumptions:**
- Markets value stocks based on expected future earnings, not past results
- Forward P/E better reflects expectation-driven reality than trailing P/E
- Peer company valuations provide fair market benchmarks

**Real-World Example - NVIDIA vs Intel:**
- **Intel (INTC):** Lower trailing P/E due to stable but slow growth
- **NVIDIA (NVDA):** Higher forward P/E due to expected massive AI-driven growth
- **Rationale:** Paying more per €1 of earnings for NVIDIA is rational if future earnings will expand sharply


### **Price-to-Book (P/B) Ratios**
The Price-to-Book ratio compares a company's market value to its book value: **P/B = Share Price ÷ Book Value per Share**

**Key Components:**
- **Book Value:** Accounting value of assets and liabilities in the balance sheet
- **Book Value per Share:** (Total Assets - Total Liabilities) ÷ Number of Shares Outstanding
- **Alternative Formula:** P/B = Market Value of Equity ÷ Book Value of Equity

**Interpretation:**
- **P/B > 1:** Trading above book value (premium)
- **P/B < 1:** Trading below book value (discount)
- **P/B = 1:** Trading at book value

**Example:** P/B = $67.59 ÷ $67.25 = 1.01 → Company trading at slight premium to book value.

**Assumptions & Limitations:**
- Works when book value of equity is positive (unlike P/E which fails with zero/negative earnings)
- **Best for:** Banks, insurers, REITs with liquid, transparent assets such as loans, securities, deposits. 
*Their market value ≈ book value, so if the P/B deviates a lot from 1.0, it signals potential mispricing (undervaluation or overvaluation).*
- **Limitations:** Ignores intangible value drivers (human capital, brand, IP, reputation, customer relationships or proprietary technology)
- **Poor fit for:** Tech firms, consulting firms, software companies where assets aren't captured in book value, making P/B misleading.
- **Positive correlation:** High ROE stocks tend to trade at high P/B ratios

**Mispricing Matrix - P/B & Profitability Spread (ROE - r):**  
*four quadrants in the mispricing matrix for stocks, based on Price-to-Book (P/B) ratio and the profitability spread (ROE - r):*  
High P/B, High ROE - r: Fairly Valued - High P/B is justified by strong profitability (ROE exceeds cost of equity).  
High P/B, Low ROE - r: Overvalued - High P/B is not supported by weak profitability.  
Low P/B, High ROE - r: Undervalued - Strong profitability is not reflected in the low P/B, making it attractive for investors.  
Low P/B, Low ROE - r: Fairly Valued - Low P/B aligns with weak profitability.  


### **Price-to-Cash-Flow (P/C) Ratios**
The Price-to-Cash-Flow ratio compares a company's stock price to its cash flow per share: **P/C = Share Price ÷ Cash Flow per Share**

**Key Components:**
- **Cash Flow per Share:** (Net Income + Depreciation & Amortization) ÷ Number of Shares Outstanding
- **Alternative:** Price-to-Free-Cash-Flow when using Free Cash Flow
- **Advantages:** More conservative than P/E, focuses on actual cash generation, less affected by accounting policies

**Use Cases:**
- Capital-intensive industries with significant depreciation
- Companies with volatile earnings but stable cash flows

**Example:** Share price $50, Cash Flow per Share $4.00 → P/C = $50 ÷ $4.00 = 12.5

### **PEG Ratio (Growth-adjusted P/E)**
The Price/Earnings-to-Growth ratio compares a company's P/E ratio to its expected growth rate: **PEG = P/E ÷ Expected Growth Rate (g)**

**Interpretation:**
- **PEG < 1:** Potentially undervalued relative to growth
- **PEG > 1:** Potentially overvalued relative to growth
- **PEG = 1:** Fairly valued relative to growth

**Example:** P/E = 15, g = 0.10 (10%) → PEG = 15 ÷ 0.10 = 1.5

**Statistical Foundation:**
- Expected earnings growth rate has highest impact on P/E ratio (regression analysis)
- PEG reflects P/E ratio for one percentage point of expected earnings growth
- Low PEG ratios indicate attractive investments (low P/E + high growth)

### **GARP Strategy (Growth at Reasonable Price)**
Combines value investing (low P/E) with growth investing through PEG ratio:
- **Target:** PEG ratio of 1.0 or less
- **Rationale:** P/E ratio lower than expected earnings growth rate × 100

### **PEG Calculation Best Practices**
- Use **trailing P/E** (or current P/E) based on last 12 months earnings
- Avoid forward P/E to prevent double-counting future earnings
- Forward P/E would make PEG ratio artificially low

### **Enterprise Value Multiples**

#### **EV/EBITDA Ratio**
Enterprise Value to EBITDA accounts for a company's entire capital structure: **EV/EBITDA = Enterprise Value ÷ EBITDA**

**Components:**
- **Enterprise Value:** Market Value of Equity + Debt - Cash
- **EBITDA:** Earnings Before Interest, Taxes, Depreciation, and Amortization
- **Forward EV/EBITDA:** EV ÷ Expected Future EBITDA

**Example:** EV = $34,938M, EBITDA = $5,962M → EV/EBITDA = $34,938M ÷ $5,962M = 5.86

**Advantages:**
- Eliminates distortions from different capital intensities and tax rates 
- Better for capital-intensive sectors (telecom, utilities, steel, infrastructure)
- Approximates pre-capex operating performance

**Limitations:**
- Free cash flow to firm has stronger link to equity valuation than EBITDA

#### **EV/Sales (EV/S) Ratio**
The Enterprise Value to Sales ratio compares a company's enterprise value to its revenue: **EV/S = Enterprise Value ÷ Annual Sales**

**Components:**
- **Enterprise Value:** Market Value of Equity + Debt - Cash
- **Sales:** Total revenue for the period

**Advantages:**
- Useful for companies with negative earnings or high growth
- Less volatile than earnings-based multiples
- Good for comparing companies in different growth stages
- Typically ranges from 1x to 4x depending on industry

**Example:** EV = $100M, Annual Sales = $50M → EV/S = $100M ÷ $50M = 2.0

### **Gordon Growth Model & Justified Multiples**
By calculating the P/E ratio using a cash flow model, it is possible to determine the share price that must be paid for one unit of earnings. This incorporates forecast fundamentals of profitability, growth, and risk.

#### **Justified P/E Ratio Derivation**
```
P₀ = D₁ ÷ (r - g)
P/E = [D₁ ÷ E₁] × [E₁ ÷ (r - g)] = (Dividend Payout) × [1 ÷ (r - g)]
Justified P/E = (1 - b) × (1 + g) ÷ (r - g)
```

**Where:**
- **b** = Retention rate (1 - dividend payout ratio)
- **1 - b** = Payout ratio of earnings
- **P₀** = Current stock price
- **D₁** = Expected dividend next year
- **r** = Required rate of return
- **g** = Expected growth rate

**Example Calculation:**
```
Company with:
- Retention rate (b) = 0.7356
- Growth rate (g) = 2.8%
- Required return (r) = 6.7%

Justified P/E = (1 - 0.7356) × (1 + 0.028) ÷ (0.067 - 0.028)
            = 0.7356 × 1.028 ÷ 0.039
            = 0.756 ÷ 0.039 = 19.39
```

#### **Key Relationships**
- **P/B*** = **P/E*** × **ROE**
- **PEG*** = **P/E*** ÷ **g**
- **g** = **b** × **ROE**

#### **Fundamental Assumptions**
- For a given growth rate, the higher (lower) the earnings payout ratio, the higher (lower) the P/E ratio. This relationship can be explained by the fact that companies with low investment needs have higher earnings payout ratio and hence a higher P/E ratio than firms of high capital expenditure.
- A stock has the same price as the stock of an identical peer company if the forecast fundamentals such as cash flows, growth rate, and expected return are the same. The implicit assumption is that stocks in the same industry sector have the same risk, growth, and cash flow patterns and are therefore comparable to each other.

#### **Interpretation Framework**
- **P/E_actual > P/E*** → Potentially overvalued
- **P/B_actual < P/B*** → Potentially undervalued
- **PEG* < 1** → Undervalued relative to growth
- **PEG* > 1** → Overvalued relative to growth

#### **Fundamental Drivers of Justified Multiples**
- **Higher growth (g)** → Higher justified multiples
- **Higher profitability (ROE)** → Higher justified multiples
- **Higher risk (r)** → Lower justified multiples
- **Higher retention (b)** → Higher justified multiples

### **Multiples Classification & Ranges**

| Multiple Type | Description | Common Range |
|---------------|-------------|--------------|
| **P/E** | Price to Earnings | 10-25x |
| **PEG** | Price/Earnings to Growth | Varies by growth |
| **P/B** | Price to Book Value | 0.5-3.0x |
| **P/C** | Price to Cash Flow | 5-15x |
| **EV/EBITDA** | Enterprise Value to EBITDA | 5-12x |
| **EV/S** | Enterprise Value to Sales | 1-4x |

**Categories of Multiples:**
- **Price Multiples:** Both numerator and denominator are equity-related (share price vs. EPS, book value, free cash flow)
- **Value Multiples:** Based on total capital-related variables (enterprise value vs. EBIT, EBITDA, free cash flow to firm, sales)

### **Overvaluation/Undervaluation Matrix**
- High P/B + High ROE = Potentially overvalued
- High P/B + Low ROE = Significantly overvalued
- Low P/B + High ROE = Potentially undervalued
- Low P/B + Low ROE = Significantly undervalued

### **Growth-Adjusted Valuation**
- **High-growth companies** deserve higher multiples
- **PEG ratio** helps compare companies with different growth rates
- **Growth must be sustainable and funded**

### **Risk Adjustment**
- **Higher risk** requires higher returns (lower multiples)
- **Beta** measures systematic risk
- **Required return** adjusts for company-specific risk factors

---

## 🏭 **Industry-Specific Considerations**

Different industries have different typical multiple ranges due to varying growth prospects, risk profiles, capital intensity, and profitability characteristics.

### **High-Growth Industries (Tech, Biotech)**
- **Higher P/E multiples:** 20-30x (justified by growth expectations)
- **Lower P/B ratios:** Due to intangible assets not captured in book value
- **Higher PEG ratios:** Acceptable given growth prospects

### **Mature Industries (Utilities, Consumer Staples)**
- **Lower P/E multiples:** 10-15x (stable but slow growth)
- **Higher P/B ratios:** 1.5-2.5x (tangible assets, stable valuations)
- **More stable valuations:** Less volatility in multiples

### **Cyclical Industries (Manufacturing, Commodities)**
- **Volatile multiples:** Wide swings with economic cycles
- **P/B ratios often below 1:** During economic downturns
- **EV/EBITDA preferred:** Better for cyclical companies with varying capital structures

---

## ❓ **Key Questions & Rationale**

### **Why Use Ratios Like P/E and M/B?**
- **P/E (Price-to-Earnings):** Tells how much investors are paying for each dollar of earnings. Lower is often "cheaper," which can mean higher possible returns. Reflects company profitability directly.
- **Market-to-Book (M/B):** Tells how much investors are paying for each dollar of equity (assets minus debts). Lower can mean "safer" or "undervalued" unless there's a fundamental reason for pessimism (= Market Value / Book Value).

### **Limitations to P/E and M/B Ratios**
- **P/E Vulnerabilities:** Subject to accounting manipulation and earnings volatility
- **M/B Limitations:** Book value may not reflect true economic value, especially for intangible-heavy companies

### **Why Aggregate by Sector and Quarter?**
- **Sector Grouping:** Companies with similar drivers, enabling apples-to-apples comparisons
- **Quarterly Aggregation:** Removes short-term noise, reveals patterns/trends over longer horizons
- **Time Horizon Advantage:** Think in 5-10 year terms rather than 6-month blips

### **Why GICS over NAICS for Sector Classification?**
- **GICS Advantages:** Globally recognized standard designed for financial markets, used by investors and analysts worldwide. Hierarchical structure (11 sectors → 24 groups → 69 industries → 158 sub-industries). Classifies by revenue generation and market competition, aligning with investor priorities.
- **NAICS Limitations:** U.S./North America focused, designed for government statistical reporting, less relevant for global investment analysis.

### **Industry Classification Systems Overview: GICS, ICB, SIC, NAICS codes**
- GICS: Global Industry Classification Standard (MSCI/S&P): 2-digit sectors → 4-digit groups → 6-digit industries → 8-digit sub-industries
- SIC: Standard Industrial Classification : 4-digit codes for principal products and services
- NAICS: North American Industry Classification System : 6-digit codes classifying economic activities by sector, subsector, and industry
- ICB: Industry Classification Benchmark (FTSE) : Industry (2 digits), Supersector (4 digits), Sector (6 digits), and Subsector (8 digits)

### **Why Compute Statistics (Mean, Median, Variance)?**
- **Mean/Median:** Show typical sector valuation - what's "normal" currently
- **Variance:** Measures risk/uncertainty; higher variance indicates riskier sector selection
- **Median Advantage:** Unlike arithmetic mean, median is unaffected by outliers and more suitable for benchmarks

### **Why Allocate Based on These Metrics?**
- **Rational Allocation:** Direct capital toward sectors where value-price gap is widest and uncertainty manageable

**Allocation Examples:**
- **Sector A:** Low P/E + Low variance → Cheap and stable → Allocate more capital
- **Sector B:** High P/E + High variance → Expensive and risky → Avoid or deprioritize

**Real-World Application:**
*Comparing Technology (high P/E, high variance) vs. Utilities (low P/E, low variance):*
- If sectors grow earnings similarly, paying 40x earnings for Tech is riskier than 15x for Utilities unless Tech has superior fundamentals
- Fund capital naturally shifts toward sectors offering more earnings/asset value per dollar invested

**Core Investment Philosophy:**
- Own assets where you get most future earnings per dollar today, with risk you can stomach.
- Use clean, comparable company data to spot these opportunities at the sector level.
- Allocate more where the value/price gap is wide, but only if you understand the variance (risk) behind those numbers.

---

## 💾 **COMPUSTAT Database Overview**

### **Database Description**
COMPUSTAT (North America), developed by Standard & Poor's, is a comprehensive financial research tool providing standardized financial data for analyzing companies, industries, and economies. Enables comparative analysis, portfolio management, and financial modeling through extensive financial statements, market data, and segment information.

### **Financial Analysis Applications**
- **Comparative Analysis:** Company performance vs. competitors
- **Corporate Planning:** Business opportunities through industry comparisons
- **Divestiture:** Potential buyers for business operations
- **Portfolio Management:** Risk, return, and beta characteristics analysis
- **Marketing:** Customer identification using financial characteristics
- **M&A Defense:** Takeover vulnerability evaluation
- **M&A Offense:** Acquisition targets and value creation opportunities
- **Securities Analysis:** Detailed company and stock performance reports

### **Data Source for This Analysis**
- **Provider:** [S&P Global Marketplace](https://www.marketplace.spglobal.com/en/datasets/compustat-financials-(8))
- **Dataset:** Compustat Quarterly Data (2010-2025)
- **Significance:** Gold standard for empirical equity research with standardized financial variables across thousands of public firms

### **compustat data variables:** costat,curcdq,datafmt,indfmt,consol,tic,datadate,gvkey,conm,cusip,cik,exchg,fyr,fic,add1,add2,add3,add4,addzip,busdesc,city,conml,county,dldte,dlrsn,ein,fax,fyrc,ggroup,gind,gsector,gsubind,idbflag,incorp,ipodate,loc,naics,phone,prican,prirow,priusa,sic,spcindcd,spcseccd,spcsrc,state,stko,weburl,acctchgq,acctstdq,adrrq,ajexq,ajpq,apdedateq,bsprq,compstq,curncdq,currtrq,curuscnq,datacqtr,datafqtr,fdateq,finalq,fqtr,fyearq,ogmq,pdateq,rdq,rp,scfq,srcq,staltq,updq,acchgq,acomincq,acoq,actq,altoq,ancq,anoq,aociderglq,aociotherq,aocipenq,aocisecglq,aol2q,aoq,apq,aqaq,aqdq,aqepsq,aqpl1q,aqpq,arcedq,arceepsq,arceq,atq,aul3q,billexceq,capr1q,capr2q,capr3q,capsftq,capsq,ceiexbillq,ceqq,cheq,chq,cibegniq,cicurrq,ciderglq,cimiiq,ciotherq,cipenq,ciq,cisecglq,citotalq,cogsq,csh12q,cshfd12,cshfdq,cshiq,cshopq,cshoq,cshprq,cstkcvq,cstkeq,cstkq,dcomq,dd1q,deracq,deraltq,derhedglq,derlcq,derlltq,diladq,dilavq,dlcq,dlttq,doq,dpacreq,dpactq,dpq,dpretq,drcq,drltq,dteaq,dtedq,dteepsq,dtepq,dvintfq,dvpq,epsf12,epsfi12,epsfiq,epsfxq,epspi12,epspiq,epspxq,epsx12,esopctq,esopnrq,esoprq,esoptq,esubq,fcaq,ffoq,finacoq,finaoq,finchq,findlcq,findltq,finivstq,finlcoq,finltoq,finnpq,finreccq,finrecltq,finrevq,finxintq,finxoprq,gdwlamq,gdwlia12,gdwliaq,gdwlid12,gdwlidq,gdwlieps12,gdwliepsq,gdwlipq,gdwlq,glaq,glcea12,glceaq,glced12,glcedq,glceeps12,glceepsq,glcepq,gldq,glepsq,glivq,glpq,hedgeglq,ibadj12,ibadjq,ibcomq,ibmiiq,ibq,icaptq,intaccq,intanoq,intanq,invfgq,invoq,invrmq,invtq,invwipq,ivaeqq,ivaoq,ivltq,ivstq,lcoq,lctq,lltq,lnoq,lol2q,loq,loxdrq,lqpl1q,lseq,ltmibq,ltq,lul3q,mibnq,mibq,mibtq,miiq,msaq,ncoq,niitq,nimq,niq,nopiq,npatq,npq,nrtxtdq,nrtxtepsq,nrtxtq,obkq,oepf12,oeps12,oepsxq,oiadpq,oibdpq,opepsq,optdrq,optfvgrq,optlifeq,optrfrq,optvolq,piq,pllq,pnc12,pncd12,pncdq,pnceps12,pncepsq,pnciapq,pnciaq,pncidpq,pncidq,pnciepspq,pnciepsq,pncippq,pncipq,pncpd12,pncpdq,pncpeps12,pncpepsq,pncpq,pncq,pncwiapq,pncwiaq,pncwidpq,pncwidq,pncwiepq,pncwiepsq,pncwippq,pncwipq,pnrshoq,ppegtq,ppentq,prcaq,prcd12,prcdq,prce12,prceps12,prcepsq,prcpd12,prcpdq,prcpeps12,prcpepsq,prcpq,prcraq,prshoq,pstknq,pstkq,pstkrq,rcaq,rcdq,rcepsq,rcpq,rdipaq,rdipdq,rdipepsq,rdipq,recdq,rectaq,rectoq,rectq,rectrq,recubq,req,retq,reunaq,revtq,rllq,rra12,rraq,rrd12,rrdq,rreps12,rrepsq,rrpq,rstcheltq,rstcheq,saleq,seqoq,seqq,seta12,setaq,setd12,setdq,seteps12,setepsq,setpq,spce12,spced12,spcedpq,spcedq,spceeps12,spceepsp12,spceepspq,spceepsq,spcep12,spcepd12,spcepq,spceq,spidq,spiepsq,spioaq,spiopq,spiq,sretq,stkcoq,stkcpaq,teqq,tfvaq,tfvceq,tfvlq,tieq,tiiq,tstknq,tstkq,txdbaq,txdbcaq,txdbclq,txdbq,txdiq,txditcq,txpq,txtq,txwq,uacoq,uaoq,uaptq,ucapsq,ucconsq,uceqq,uddq,udmbq,udoltq,udpcoq,udvpq,ugiq,uinvq,ulcoq,uniamiq,unopincq,uopiq,updvpq,upmcstkq,upmpfq,upmpfsq,upmsubpq,upstkcq,upstkq,urectq,uspiq,usubdvpq,usubpcvq,utemq,wcapq,wdaq,wddq,wdepsq,wdpq,xaccq,xidoq,xintq,xiq,xoprq,xopt12,xoptd12,xoptd12p,xoptdq,xoptdqp,xopteps12,xoptepsp12,xoptepsq,xoptepsqp,xoptq,xoptqp,xrdq,xsgaq,adjex,cshtrq,dvpspq,dvpsxq,mkvaltq,prccq,prchq,prclq

### **Database Architecture**

**Database Schema:**
- **Calendar Year:** January 1 - December 31 for market data comparison
- **Fiscal Year:** 12-month accounting period (may not align with calendar years)
- **Industry Groups:** NAICS, GICS, or SIC codes
- **Stock Exchanges:** NYSE, AMEX, NASDAQ
- **Data Maintenance:** Maximum 20 years annual data, quarterly updates (August production)

**Quarter Definitions:**
- **May fiscal year-end:** Q1 = Jun-Aug, Q2 = Sep-Nov, Q3 = Dec-Feb, Q4 = Mar-May
- **December fiscal year-end:** Q1 = Jan-Mar, Q2 = Apr-Jun, Q3 = Jul-Sep, Q4 = Oct-Dec
- **Calendar Quarter 1:** Feb, Mar, Apr
- **Calendar Quarter 2:** May, Jun, Jul
- **Calendar Quarter 3:** Aug, Sep, Oct
- **Calendar Quarter 4:** Nov, Dec, Jan

### **Core Data Identifiers**
- **GVKEY:** Global Company Key (6-digit unique identifier)
- **DATADATE:** Financial statement date (YYYYMMDD format)

### **Data Selection Guidelines**
- Use `GVKEY` for company identification
- Filter by `DATADATE` for specific time periods

### **Time Period Variations**
- Annual: Standard variables (e.g., `SALE`, `AT`, `OANCF`)
- Quarterly: Q suffix (e.g., `SALEQ`, `ATQ`, `OANCFQ`)
- Semi-Annual: SA suffix (e.g., `SALESA`, `ATSA`)
- Year-to-Date: Y suffix (e.g., `SALEY`, `ATY`, `OANCFY`)

### **Financial Variables Dictionary**
A comprehensive A-Z dictionary of 1,300+ Compustat data variables is available in `Financial_Variables.md` within the Compustat folder, alongside the source data file `Compustat_Quarterl_2010_2025.csv`.

---

## 🧮 **Balancing Models**
A balancing model is a structured template that shows how different financial statement components must mathematically balance (assets = liabilities + equity, income statement flows, cash flow reconciliation). These models break down complex financial data into digestible components.

### **Available Models & Time Horizons**
- **Financial Statement Types**: Income Statement, Balance Sheet, Cash Flow Statement
- **Time Horizons**: Annual (A_), Semi-Annual (SA_), Quarterly (Q_), Year-to-Date (YTD_)
- **Data Frequency**: Annual, Semi-Annual, Quarterly, Year-to-Date

### **Balance Sheet**

#### **Annual Balance Sheet (A_Balance_Sheet.csv)**

**Asset Aggregations:**
- **Cash and Short-Term Investments** [`CHE`]: `CH + IVST` (cash + investments)
- **Receivables Total** [`RECT`]: `RECTR + TXR + RECCO` (trade receivables + taxes + contra receivables)
- **Inventories Total** [`INVT`]: `INVRM + INVWIP + INVFG + INVO` (raw materials, WIP, finished goods, other)
- **Current Assets - Other Total** [`ACO`]: `XPP + ACOX` (prepaid expenses + other current assets)
- **Current Assets Total** [`ACT`]: `CHE + RECT + INVT + ACO`
- **Property, Plant & Equipment (Net)** [`PPENT`]: `PPEGT - DPACT` (gross PP&E minus depreciation)
- **Intangible Assets Total** [`INTAN`]: `GDWL + INTANO` (goodwill + other intangibles)
- **Assets - Other Total** [`AO`]: `DC + AOX` (deferred charges + other assets)
- **Total Assets** [`AT`]: `ACT + PPENT + IVAEQ + IVAO + INTAN + AO`

**Liability Aggregations:**
- **Debt in Current Liabilities** [`DLC`]: `DD1 + NP` (short-term debt + notes payable)
- **Current Liabilities Total** [`LCT`]: `DLC + AP + TXP + LCO` (debt + accounts payable + taxes payable + other current liabilities)
- **Long-Term Debt** [`DLTT`]: Borrowings with maturities over one year
- **Total Liabilities** [`LT`]: `LCT + DLTT + TXDITC + LO`

**Equity Aggregations:**
- **Preferred Stock Total** [`PSTK`]: `PSTKR + PSTKN` (preferred stock redeemable + non-redeemable)
- **Retained Earnings** [`RE`]: `REUNA + ACOMINC + SEQO` (unrestricted + comprehensive income + other equity)
- **Accumulated Other Comprehensive Income**: `ACOMINC = AOCIDERGL + AOCIOTHER + AOCIPEN + AOCISECGL - MSA - RECTA`
- **Common Equity Total** [`CEQ`]: `CSTK + CAPS + RE - TSTK` (common stock + paid-in capital + retained earnings - treasury stock)
- **Stockholders Equity - Parent**: `SEQ = PSTK + CEQ`
- **Stockholders' Equity - Total** [`TEQ`]: `PSTK + CEQ + MIBN` (preferred + common equity + minority interest in subsidiaries)
- **Liabilities & Equity Total** [`LSE`]: `LT + MIB + TEQ` (must equal Total Assets for balance)

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

### **Income Statement Models**

#### **Annual Income Statement (A_Income_Statement.csv)**

**Primary Income Statement Items:**
- **Sales (Net)** [`SALE`]: Gross billings reduced by discounts, returns, and allowances
- **Cost of Goods Sold** [`COGS`]: Direct costs of producing goods/services sold
- **Selling, General & Administrative** [`XSGA`]: Operating expenses not directly tied to production
- **Depreciation & Amortization** [`DP`]: Systematic allocation of asset costs over time
- **Interest Expense** [`XINT`]: Cost of borrowed funds
- **Special Items** [`SPI`]: Non-recurring gains/losses, discontinued operations, accounting changes

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
- **Net Income**: `NIADJ = IBADJ + XIDO` (bottom-line profit after all expenses and taxes)

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

### **Cash Flow**

#### **Annual Cash Flow (A_Cash_Flow.csv)**

**Operating Activities:**
- **Funds from Operations - Other**: `FOPO = TXBCO + FOPOX`
- **Operating Activities Net Cash Flow**: `OANCF = IBC + DPC + XIDOC + TXDC + ESUBC + SPPIV + FOPO + RECCH + INVCH + APALCH + TXACH + AOLOCH`

*Includes income before extraordinary items, depreciation, tax effects, changes in working capital*

**Investing Activities:**
- **Capital Expenditures** [`CAPX`]: Cash used for property, plant, and equipment
- **Investing Activities Net Cash Flow**: `IVNCF = -IVCH + SIV + IVSTCH - CAPX + SPPE - AQC + IVACO`

*Includes changes in investments, acquisitions, disposals of fixed assets*

**Financing Activities:**
- **Dividends Paid** [`DV`]: Cash distributions to shareholders
- **Debt Issuance/Reduction** [`DLTIS - DLTR`]: Cash flows from borrowing/lending activities
- **Financing Activities Net Cash Flow**: `FINCF = SSTK + TXBCOF - PRSTKC - DV + DLTIS - DLTR + DLCCH + FIAO`

*Includes stock issuance, debt transactions, dividend payments*

**Cash Flow Reconciliation:**
- **Change in Cash**: `CHECH = OANCF + IVNCF + FINCF + EXRE`
- *Exchange rate effects; must equal the change in cash balance on balance sheet*

#### **Year-To-Date Cash Flow (YTD_Cash_Flow.csv)**
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

---

## 🎯 **GICS Sector Classification System**

### **Overview**
The Global Industry Classification Standard (GICS®) is a comprehensive system for categorizing companies globally, jointly developed by S&P Dow Jones Indices and MSCI in 1999. It provides a consistent framework for comparing companies, sectors, and industries across countries, regions, and globally.

### **Hierarchical Structure**
GICS consists of 4 hierarchical levels:
1. **11 Sectors** - The broadest level of classification
2. **25 Industry Groups** - Groups sectors into logical clusters
3. **74 Industries** - More specific industry classifications
4. **163 Sub-Industries** - The most detailed level of classification

### **Current GICS Sectors (Effective March 17, 2023)**

*Tabular Format*
| Code | Sector Name | Description |
|------|-------------|-------------|
| 10 | **Energy** | Companies engaged in exploration, production, refining, and distribution of energy products |
| 15 | **Materials** | Companies that mine, refine, or process materials used in manufacturing and construction |
| 20 | **Industrials** | Companies providing goods and services to industrial and commercial customers |
| 25 | **Consumer Discretionary** | Companies producing goods and services for discretionary consumer spending |
| 30 | **Consumer Staples** | Companies producing essential consumer goods and services |
| 35 | **Health Care** | Companies providing health care goods and services |
| 40 | **Financials** | Companies providing financial services including banking, insurance, and investment services |
| 45 | **Information Technology** | Companies involved in technology hardware, software, and IT services |
| 50 | **Communication Services** | Companies providing communication and media services |
| 55 | **Utilities** | Companies providing electric, gas, and water utilities |
| 60 | **Real Estate** | Companies engaged in real estate development, management, and services |

---

## 💻 **Python Implementation & Analysis Phases**

### **Programming Tools & Libraries**

**Core Python Libraries:**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib/Seaborn**: Data visualization
- **Scikit-learn**: Statistical analysis and modeling

**Data Analysis Capabilities:**
- **Financial Ratios**: Automated calculation of key metrics
- **Valuation Models**: Implementation of DCF and relative valuation
- **Statistical Analysis**: Regression, correlation, and trend analysis
- **Data Visualization**: Charts, graphs, and interactive dashboards

---

### **Phase 1: Data Cleaning and Preparation**

**Key Tasks:**
- Remove null values in GICS sector classification
- Data validation and preprocessing
- Financial ratio calculations preparation

**Dataset Characteristics:**
- **Rows:** 714,894 (quarterly data for ~3,000 U.S. corporations)
- **Time Period:** 2010-2025
- **Structure:** [714,893 rows × 442 columns] panel dataset

#### **Data Cleaning Results**

| Metric | Value |
|--------|-------|
| **Total observations** | 714,893 |
| **Valid GICS sector codes** | 522,018 |
| **Missing GICS sector codes** | 192,875 |
| **Missing data rate** | 26.98% |
| **Rows removed** | 192,875 |
| **Data retention rate** | 73.02% |

#### **Final Cleaned Dataset**
- **File:** `Compustat_Quarterl_2010_2025_cleaned.csv`
- **Unique companies (GVKEY):** 15,474 companies
- **Total rows after cleaning:** 522,018 observations
- **Time coverage:** 62 calendar quarters (2010-Q1 through 2025-Q2)

#### **GICS Sector Distribution**

| Sector Code | Sector Name | Observations |
|-------------|-------------|--------------|
| **10** | Energy | 44,186 |
| **15** | Materials | 61,287 |
| **20** | Industrials | 58,624 |
| **25** | Consumer Discretionary | 49,833 |
| **30** | Consumer Staples | 21,412 |
| **35** | Health Care | 83,857 *(highest)* |
| **40** | Financials | 81,340 |
| **45** | Information Technology | 61,341 |
| **50** | Communication Services | 22,420 |
| **55** | Utilities | 17,405 *(lowest)* |
| **60** | Real Estate | 20,313 |

---

### **Phase 2: Algorithm Development**

#### **Data Processing Approach**
- Identify unique `gvkey` values for each firm
- Extract quarterly time series data (2010-2025) for each company
- Implement financial ratio calculations for each firm-quarter observation

#### **Financial Ratios Implemented**

| Ratio | Formula | Description |
|-------|---------|-------------|
| **P/E Ratio** | `Market Price / Earnings Per Share` | Valuation relative to earnings |
| **M/B Ratio** | `(Market Cap + Total Debt - Cash) / Total Assets` | Market value vs. book value |

#### **Compustat Variable Mapping**

| Component | Variable | Description |
|-----------|----------|-------------|
| **Market Price** | `prccq` | Quarterly closing price |
| **Earnings Per Share** | `epspxq` | Quarterly diluted EPS (excl. extraordinary items) |
| **Market Capitalization** | `prccq * cshoq` | Shares outstanding × price per share |
| **Total Debt** | `dlcq + dlttq` | Short-term + long-term debt |
| **Cash & Equivalents** | `cheq` | Cash and short-term investments |
| **Total Assets** | `atq` | Quarterly total assets |

#### **Calculation Results Summary**

##### **Price-to-Earnings (P/E) Ratio**
- **Formula:** `PE_ratio = prccq / epspxq`
- **Successfully calculated:** 405,570 ratios
- **Missing ratios:** 116,448 (22.31%)

**P/E Statistics (excluding missing values):**
- Mean: 30.75 | Median: 22.86
- Std Dev: 390.12 | Range: -66,666.67 to 41,375.00

##### **Market-to-Book (M/B) Ratio**
- **Formula:** `MB_ratio = (prccq * cshoq + dlcq + dlttq - cheq) / atq`
- **Successfully calculated:** 443,862 ratios
- **Missing ratios:** 78,156 (14.97%)

**M/B Statistics (excluding missing values):**
- Mean: 91.11 | Median: 1.00
- Std Dev: 7,766.74 | Range: -806.54 to 3,543,842.50

#### **Sector-Level Statistics**

| Sector | Companies | P/E Count | P/E Mean | P/E Median | M/B Count | M/B Mean | M/B Median |
|--------|-----------|-----------|----------|------------|-----------|----------|------------|
| **10 Energy** | 1,386 | 34,432 | 20.0 | 2.43 | 38,969 | 34.06 | 0.92 |
| **15 Materials** | 1,713 | 40,470 | 3.79 | -5.0 | 55,434 | 47.56 | 1.14 |
| **20 Industrials** | 1,694 | 48,648 | 45.17 | 43.64 | 51,427 | 84.91 | 1.08 |
| **25 Consumer Disc.** | 1,609 | 39,745 | 43.19 | 34.22 | 41,589 | 182.61 | 1.07 |
| **30 Consumer Staples** | 638 | 16,252 | 44.07 | 43.3 | 17,951 | 197.23 | 1.31 |
| **35 Health Care** | 2,700 | 64,578 | 3.25 | -9.5 | 68,713 | 176.04 | 1.72 |
| **40 Financials** | 2,203 | 69,553 | 48.52 | 43.5 | 70,562 | 44.31 | 0.2 |
| **45 Information Tech** | 2,058 | 48,837 | 27.62 | 7.53 | 53,279 | 55.96 | 1.39 |
| **50 Communication** | 628 | 17,276 | 25.27 | 18.99 | 18,772 | 34.77 | 1.04 |
| **55 Utilities** | 385 | 8,647 | 50.7 | 49.85 | 9,121 | 136.59 | 0.87 |
| **60 Real Estate** | 460 | 17,132 | 69.46 | 50.35 | 18,045 | 48.37 | 1.04 |

#### **Output Dataset: `Compustat_Ratios_TimeSeries.csv`**
- **Total rows:** 522,018 observations
- **Total columns:** 14 columns
- **Time coverage:** 62 calendar quarters (2010-Q1 through 2025-Q2)

##### **Column Structure**

**Company Identifiers:**
- `gvkey`: Global Company Key (6-digit unique identifier)
- `conm`: Company name (full legal name)
- `gsector`: GICS sector code (10=Energy, 15=Materials, etc.)

**Time-Series Identifiers:**
- `datadate`: Financial statement date (YYYY-MM-DD format)
- `quarter`: Calendar quarter (YYYYQX format, e.g., 2023Q1)
- `year`: Calendar year (YYYY format)

**Raw Financial Data:**
- `prccq`: Quarterly closing stock price
- `epspxq`: Quarterly diluted EPS (excluding extraordinary items)
- `cheq`: Cash and short-term investments
- `atq`: Total assets

**Calculated Components:**
- `market_cap`: Market capitalization (`prccq * cshoq`)
- `total_debt`: Total debt (`dlcq + dlttq`)

**Financial Ratios:**
- `PE_ratio`: Price-to-Earnings ratio
  - Formula: `prccq / epspxq`
  - Measures investor willingness to pay per dollar of earnings
  - Can be negative for loss-making companies
- `MB_ratio`: Market-to-Book ratio
  - Formula: `(market_cap + total_debt - cheq) / atq`
  - Compares market valuation to accounting book value
  - Values > 1.0 indicate premium to book value

**Data Quality Notes:**
- All ratios handle division by zero and infinite values appropriately
- Missing values are represented as empty cells in CSV
- Dataset sorted by `gvkey` and `datadate` for time-series integrity

---

### **Phase 3: Sector Analysis**

#### **Methodology Overview**

**GICS Sector Classification:**
- Uses GICS sector codes (`gsector`) for sector-level aggregation
- Groups firms into 11 GICS sectors for superior investment analysis (vs. NAICS)
- Enables apples-to-apples sector comparisons

**Sector Mapping:** Energy(10), Materials(15), Industrials(20), Consumer Discretionary(25), Consumer Staples(30), Health Care(35), Financials(40), Information Technology(45), Communication Services(50), Utilities(55), Real Estate(60)

**Statistical Analysis:**
- Computes mean, median, standard deviation, and variance for each sector-quarter combination
- Performs time series analysis to identify valuation trends across quarters
- Generates panel dataset: `11 sectors × 62 quarters × 2 ratios × 4 statistics`

#### **Dataset Summary**

| Metric | Value |
|--------|-------|
| **Input dataset** | Compustat Quarterly Ratios Time-Series (Phase 2 output) |
| **Total observations** | 522,018 |
| **Unique companies** | 15,474 (across 11 GICS sectors) |
| **Time coverage** | 62 calendar quarters (2010-Q1 through 2025-Q2) |
| **After cleaning** | 402,263 observations |
| **Data retention rate** | 77.1% |
| **Primary data loss sources** | Loss-making companies (negative EPS), zero book value |

#### **Analysis Process**
- Groups data by `['gsector', 'quarter']` for sector-quarter aggregation
- Calculates statistics for every sector-quarter combination
- Removes infinite/null ratios for robust statistical analysis
- Produces comprehensive panel dataset for investment decision-making

#### **Output Files**

| File | Description | Size/Details |
|------|-------------|--------------|
| **`Compustat_Sector_Statistics.csv`** | Panel dataset: `(sector × quarter × ratio × statistics)` | - |
| **`sector_valuation_trends.png`** | 4-panel sector overview visualization | 1.6MB |
| **`sector_XX_name_trends.png`** | 11 individual sector trend plots | Confidence bands (±1 std dev) |
| **`sector_analysis_log.txt`** | Complete analysis documentation | Processing details & results |

#### **Key Investment Insights**

##### **Valuation Rankings**
- **Most Undervalued (by P/E):** Materials, Health Care, Energy
- **Most Expensive (by P/E):** Real Estate, Utilities, Financials

##### **Risk Assessment**
- **Lowest Volatility:** Financials, Materials, Energy
- **Highest Volatility:** Information Technology, Real Estate, Health Care

##### **Sector Performance Analysis**
- **Materials Sector:** Consistent undervaluation throughout period
- **Technology Sector:** Explosive growth with extreme volatility
- **Financials Sector:** Remarkable stability despite interest rate cycles
- **Real Estate Sector:** Deteriorating fundamentals (rising P/E, stable M/B)

##### **Trend Analysis**
- **P/E Momentum Leaders:** Materials and Energy sectors
- **M/B Growth Leaders:** Health Care sector shows extreme asset value growth
- **Volatility Leaders:** Information Technology and Real Estate
- **Risk-Adjusted Opportunities:** Materials combines low P/E with moderate volatility

---

### **Phase 4: Investment Decisions**

#### **Strategic Objectives**

1. **Relative Returns Analysis**
   - Compare sector portfolio returns against market benchmarks
   - Evaluate S&P 500 index and sector-specific ETFs (XLK, XLF, etc.)
   - Assess whether value-based strategies outperform passive benchmarks

2. **Risk-Adjusted Portfolio Construction**
   - **Aggressive Approach:** Exclude sectors with high valuations + high variance (expensive & uncertain)
   - **Conservative Approach:** Allocate to sectors with low valuations + stable variance (bargains with margin of safety)

#### **Investment Allocation Framework**

##### **Step 1: Data Collection**
- Pull quarterly P/E and M/B ratios for all firms in each sector
- Ensure comprehensive coverage across all 11 GICS sectors

##### **Step 2: Statistical Aggregation**
- Calculate mean and variance for each sector-quarter combination
- Generate risk-return profiles for each sector

##### **Step 3: Scoring System**
- Prioritize sectors that are "cheaper" (lower valuations) and more stable (lower variance)
- Implement quantitative scoring algorithm for objective decision-making

##### **Step 4: Portfolio Allocation**
- Assign capital weights based on composite scores
- Apply diversification limits to manage concentration risk
- Balance between high-conviction opportunities and risk management

##### **Step 5: Performance Monitoring**
- Track quarterly portfolio results against benchmarks
- Adjust allocations based on changing market conditions
- Rebalance periodically to maintain target exposures

#### **Forecast Accuracy & Assumption Testing**

**Key Investment Principle:** Returns depend not just on numbers, but on the validity of underlying assumptions. Investment success often hinges on the "why" behind decisions rather than the numbers themselves.

- **Growth Assumption Validation:** Test reasonableness of earnings growth projections
- **Valuation Model Stress Testing:** Assess sensitivity to different scenarios
- **Benchmark Comparison:** Evaluate strategy performance vs. passive alternatives
- **Risk Factor Analysis:** Understand drivers of sector volatility and correlations

---

## 📋 **Project Information**

**Analyst:** Wassil Mian  
**Project Duration:** July 14, 2025 - Present  
**Supervisor:** Dr. Robert Kieschnick, Director of MS in Financial Technology and Analytics  
**License:** Copyright (c) 2025 The University of Texas at Dallas, FinTech Department and UTDSOM Investment Corporation. 

---

*This README provides comprehensive documentation for the UTIMCO quantitative sector valuation analysis project in affiliation with UTDSOM Investment Corporation, guiding a $2.5M investment allocation across 11 GICS sectors using Compustat quarterly financial data (2010-2025).*
