# Experimental Results & Quantitative Metrics Summary

**Project:** Error Visualization and Analysis of Experimental Data Using Python  
**Course:** Data Exploration and Visualization  
**Dataset:** Simple Pendulum Experimental Dataset ($N = 80$ observations across 8 length configurations)  
**Processed Data Path:** `data/processed/pendulum_processed_data.csv`

---

## 1. Key Quantitative Metrics Table

| Metric Category | Parameter / Metric | Empirical Result | Scientific & Analytical Interpretation |
| :--- | :--- | :--- | :--- |
| **Dataset Scope** | Total Observations ($N$) | **80 records** | 10 repeated experimental trials across 8 distinct physical pendulum lengths. |
| **Dataset Scope** | Total Attributes | **11 columns** | 5 raw experimental variables + 6 derived metrics (error, relative, percentage, category, outlier flag). |
| **Dataset Scope** | Tested Length Range ($L$) | **0.20 m – 1.00 m** | Physical pendulum lengths: 0.20 m, 0.30 m, 0.40 m, 0.50 m, 0.60 m, 0.70 m, 0.80 m, 1.00 m. |
| **Data Quality** | Missing / Null Values | **0 (0.00%)** | 100% complete dataset with zero missing entries or unrecorded trials. |
| **Data Quality** | Duplicate Records | **0 (0.00%)** | Every record uniquely indexed via `Experiment_ID` (`EXP001`–`EXP080`). |
| **Central Tendency** | Mean Experimental Period | **1.4704 s** | Average oscillation time period across all 80 multi-length trials. |
| **Central Tendency** | Median Experimental Period ($Q_2$) | **1.4952 s** | 50th percentile period, closely matching the mean ($1.4704\text{ s}$). |
| **Central Tendency** | Theoretical Period Mean | **1.4635 s** | Analytical mean predicted by $T = 2\pi\sqrt{L/g}$ ($g = 9.81\text{ m/s}^2$). |
| **Central Tendency** | Mean Signed Error | **+0.0069 s** | Slight positive mean bias reflecting human reaction time in manual stopwatch triggering. |
| **Dispersion** | Experimental Period Std Dev | **0.3547 s** | Reflects broad spread across 8 physical lengths from 0.20 m to 1.00 m. |
| **Dispersion** | Experimental Period Variance | **0.1258 s²** | Total variance in measured periods across the multi-length spectrum. |
| **Dispersion** | Experimental Period Range | **1.1537 s** | Minimum observed period: 0.8948 s (at 0.20 m); Maximum: 2.0485 s (at 1.00 m). |
| **Error Magnitude** | Mean Absolute Error (MAE) | **0.0214 s** | Typical timing deviation per oscillation trial ($21.4\text{ ms}$), typical of human stopwatch latency. |
| **Error Magnitude** | Absolute Error Std Dev | **0.0267 s** | Low dispersion in timing deviations across the experimental dataset. |
| **Relative Precision** | Mean Relative Error | **0.015243 (1.52%)** | Average proportional discrepancy relative to theoretical benchmark. |
| **Relative Precision** | Median Percentage Error | **1.0119%** | Half of all experimental observations have less than $\approx 1.01\%$ discrepancy. |
| **Relative Precision** | Mean Percentage Error | **1.5243%** | Dataset overall average percentage error across all 80 trials. |
| **Relative Precision** | Minimum Percentage Error | **0.0298%** | Best-case precision recorded in trial `EXP052` ($L = 0.70\text{ m}$, Trial 2). |
| **Relative Precision** | Maximum Percentage Error | **10.2896%** | Maximum discrepancy recorded in outlier trial `EXP055` ($L = 0.70\text{ m}$, Trial 5). |
| **Error Distribution** | Percentage Error $Q_1$ (25th %) | **0.4075%** | 25% of trials have error $< 0.41\%$. |
| **Error Distribution** | Percentage Error $Q_3$ (75th %) | **1.8374%** | 75% of trials have error $< 1.84\%$. |
| **Error Distribution** | Percentage Error IQR | **1.4299%** | Middle 50% interquartile range of experimental percentage errors. |
| **Outlier Detection** | IQR Upper Bound ($Q_3 + 1.5\text{IQR}$) | **3.9822%** | Quantitative boundary beyond which observations are flagged as statistical anomalies. |
| **Outlier Detection** | Potential Outliers Count | **5 observations (6.25%)** | Trials `EXP004` (4.63%), `EXP007` (4.77%), `EXP014` (8.27%), `EXP038` (9.17%), `EXP055` (10.29%). |
| **Classification** | Low Error (< 1%) Count | **39 observations (48.75%)** | Modal category; represents high-precision, repeatable laboratory trials. |
| **Classification** | Moderate Error (1–2%) Count | **23 observations (28.75%)** | Standard laboratory measurement variance within normal operational tolerance. |
| **Classification** | High Error ($\ge$ 2%) Count | **18 observations (22.50%)** | Includes the 5 IQR outliers and 13 moderately perturbed timing trials. |
| **Classification** | Sub-2% Cumulative Share | **62 observations (77.50%)** | Over three-quarters of all trials exhibit discrepancies under $2.0\%$. |
| **Length Extremes** | Highest Mean % Error Length | **0.50 m (2.1026%)** | Driven by single negative outlier trial `EXP038` ($-0.1301\text{ s}$, $9.17\%$). |
| **Length Extremes** | Lowest Mean % Error Length | **0.80 m (0.9080%)** | Highest consistency length group with all trials below $2.11\%$. |
| **Length Extremes** | Maximum Variability Length | **0.70 m ($\text{SD} = 0.0533\text{ s}$)** | Highest intra-group period standard deviation due to outlier `EXP055` ($1.8511\text{ s}$). |
| **Length Extremes** | Minimum Variability Length | **0.20 m ($\text{SD} = 0.0159\text{ s}$)** | Most tightly clustered intra-group oscillation readings. |
| **Correlation** | $r(\text{Length}, T_{\text{exp}})$ | **+0.992** | Near-perfect positive correlation verifying the physical law $T \propto \sqrt{L}$. |
| **Correlation** | $r(\text{Length}, \text{Percentage Error})$ | **-0.123** | Negligible correlation confirming timing error is independent of pendulum length. |

---

## 2. Length-Wise Aggregation Breakdown

| Length $L$ (m) | $T_{\text{theo}}$ (s) | Mean $T_{\text{exp}}$ (s) | Std Dev $T_{\text{exp}}$ (s) | Mean Abs Error (s) | Mean % Error (%) | Min % Error (%) | Max % Error (%) | Outliers Count |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0.20** | 0.8971 | 0.9150 | 0.0159 | 0.0184 | 2.0476 | 0.2564 | 4.7709 | 2 (`EXP004`, `EXP007`) |
| **0.30** | 1.0988 | 1.1019 | 0.0345 | 0.0208 | 1.8885 | 0.2002 | 8.2727 | 1 (`EXP014`) |
| **0.40** | 1.2687 | 1.2719 | 0.0175 | 0.0131 | 1.0315 | 0.1261 | 3.1765 | 0 |
| **0.50** | 1.4185 | 1.4102 | 0.0478 | 0.0298 | 2.1026 | 0.3666 | 9.1717 | 1 (`EXP038`) |
| **0.60** | 1.5539 | 1.5563 | 0.0201 | 0.0155 | 0.9996 | 0.0901 | 2.0079 | 0 |
| **0.70** | 1.6784 | 1.7050 | 0.0533 | 0.0302 | 1.8024 | 0.0298 | 10.2896 | 1 (`EXP055`) |
| **0.80** | 1.7943 | 1.8020 | 0.0189 | 0.0163 | 0.9080 | 0.1449 | 2.1067 | 0 |
| **1.00** | 2.0061 | 2.0012 | 0.0357 | 0.0270 | 1.3444 | 0.0698 | 3.7984 | 0 |

---

## 3. Potential Outlier Inventory ($1.5 \times \text{IQR}$ Criterion)

| Experiment ID | Length $L$ (m) | Trial | $T_{\text{theo}}$ (s) | $T_{\text{exp}}$ (s) | Signed Error (s) | % Error (%) | Suspected Cause / Phenomenon |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **EXP004** | 0.20 | 4 | 0.8971 | 0.9386 | +0.0415 | 4.6260% | Manual stopwatch stop delay at high oscillation frequency. |
| **EXP007** | 0.20 | 7 | 0.8971 | 0.9399 | +0.0428 | 4.7709% | Stopwatch release latency during short-period oscillation. |
| **EXP014** | 0.30 | 4 | 1.0988 | 1.1897 | +0.0909 | 8.2727% | Multi-cycle counting offset or severe human trigger latency. |
| **EXP038** | 0.50 | 8 | 1.4185 | 1.2884 | -0.1301 | 9.1717% | Premature stopwatch stopping prior to complete cycle passage. |
| **EXP055** | 0.70 | 5 | 1.6784 | 1.8511 | +0.1727 | 10.2896% | Significant stopwatch trigger delay or initial amplitude perturbation. |

---

## 4. Summary of Statistical Inferences

1. **Physical Law Conformance:** The empirical observations adhere strongly to the Newtonian pendulum equation $T = 2\pi\sqrt{L/g}$ ($r = 0.992$).
2. **Error Predictability:** Mean experimental percentage error across the entire project is $1.52\%$, with $77.50\%$ of trials achieving discrepancies under $2.0\%$.
3. **Absence of Systematic Bias by Dimension:** Discrepancy metrics show no significant linear correlation with pendulum length ($r = -0.123$), proving that experimental percentage error is length-invariant.
4. **Data Integrity:** All 5 detected outliers represent genuine experimental perturbations and are fully preserved in the dataset with `Outlier_Flag = True` for analytical transparency.
