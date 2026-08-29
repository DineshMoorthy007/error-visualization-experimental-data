# Presentation Slides Content: Error Visualization & Analysis

**Project Title:** Error Visualization and Analysis of Experimental Data Using Python  
**Course:** Data Exploration and Visualization (Mini Project Presentation)  
**Author:** Dinesh Moorthy ([DineshMoorthy007](https://github.com/DineshMoorthy007))  
**Academic Environment:** Python, Jupyter Notebook, Pandas, NumPy, Matplotlib, Seaborn, Git, GitHub  

---

## Slide 1: Title Slide
- **Title:** Error Visualization and Analysis of Experimental Data Using Python
- **Subtitle:** Computational Diagnostics, Statistical Modeling & Visual Exploration of Simple Pendulum Measurements
- **Course:** Data Exploration and Visualization (Mini Project)
- **Author:** Dinesh Moorthy (DineshMoorthy007)
- **Tech Stack:** Python 3 | Pandas | NumPy | Matplotlib | Seaborn | Jupyter Notebook

---

## Slide 2: Problem Statement
- **Physical Reality:** Empirical laboratory measurements never match ideal theoretical models perfectly due to human latency, instrument limits, and environmental noise.
- **Pendulum Ambiguities:** Stopwatch triggers suffer from reaction latency ($\approx 0.02 - 0.04\text{ s}$), small-angle limits, and damping decay.
- **The Core Problem:** Without systematic error analysis and visual diagnostics, students and experimenters cannot distinguish between random measurement noise, systematic instrument bias, and genuine anomalies (outliers).
- **Solution:** A structured computational framework in Python to quantify, analyze, and visually diagnose experimental discrepancies.

---

## Slide 3: Aim and Objectives
- **Aim:** To explore, preprocess, validate, analyze, and visualize experimental pendulum data using Python, quantifying measurement discrepancies against theoretical physics models.
- **Key Objectives:**
  1. Ingest and validate 80 experimental records across 8 distinct pendulum lengths.
  2. Compute 4 foundational error metrics: Signed, Absolute, Relative, and Percentage Error.
  3. Detect statistical outliers using the non-parametric Interquartile Range (IQR) method.
  4. Classify observations into project-defined analytical error quality tiers.
  5. Calculate comprehensive descriptive statistics and length-wise group aggregations.
  6. Generate 7 publication-quality visual diagnostics covering all core chart types.

---

## Slide 4: Dataset & Physical Model
- **Theoretical Pendulum Physics:**
  $$T = 2\pi \sqrt{\frac{L}{g}} \quad (g = 9.81\text{ m/s}^2)$$
- **Scope & Dimensions:**
  - 80 experimental observations across 8 length configurations ($0.20\text{ m}$ to $1.00\text{ m}$).
  - 10 repeated measurement trials per length.
- **Attributes:**
  - Raw: `Experiment_ID`, `Trial_Number`, `Length_m`, `Theoretical_Period_s`, `Experimental_Period_s`.
  - Processed: `Error_s`, `Absolute_Error_s`, `Relative_Error`, `Percentage_Error`, `Error_Category`, `Outlier_Flag`.
- **Dataset Source:** Simulated educational experimental dataset modeling realistic laboratory timing noise and human reaction delay.

---

## Slide 5: Analytical Methodology
- **Structured 6-Stage Pipeline:**
  1. **Data Ingestion & Integrity Check:** Verification of 0 missing values and physical domain constraints ($L > 0, T > 0$).
  2. **Preprocessing & Taxonomy:** Enforcing strict data types and preserving measurement units ($\text{m}$ and $\text{s}$).
  3. **Mathematical Error Formulation:** Calculating signed, absolute, relative, and percentage errors.
  4. **IQR Outlier Flagging:** Applying $1.5 \times \text{IQR}$ threshold without data deletion.
  5. **Statistical Aggregation:** Computing central tendency, dispersion, and group summaries.
  6. **Visual Diagnostics:** Generating 7 academic figures via Matplotlib & Seaborn.

---

## Slide 6: Data Exploration & Preprocessing
- **Data Completeness:** 100% complete dataset (0 missing values, 0 duplicate rows).
- **Physical Validity:** 100% of length and time period readings are strictly positive.
- **Variable Classification:**
  - Controlled Independent Variable: `Length_m` ($0.20\text{ m} - 1.00\text{ m}$).
  - Measured Dependent Variable: `Experimental_Period_s` ($0.8948\text{ s} - 2.0485\text{ s}$).
  - Analytical Benchmark: `Theoretical_Period_s` ($0.8971\text{ s} - 2.0061\text{ s}$).
- **Precision Preservation:** Lengths formatted to 2 decimals; periods and errors formatted to 4 decimals.

---

## Slide 7: Error Analysis & Outlier Detection
- **Quantitative Error Metrics:**
  - **Mean Absolute Error (MAE):** $0.0214\text{ s}$ ($21.4\text{ ms}$, consistent with human stopwatch reaction latency).
  - **Mean Percentage Error:** $1.5243\%$ (Median: $1.0119\%$).
  - **Error Range:** $0.0298\%$ (Min, `EXP052`) to $10.2896\%$ (Max, `EXP055`).
- **Error Classification Breakdown:**
  - **Low Error (< 1%):** 39 trials (**48.75%**) — Modal, highly repeatable trials.
  - **Moderate Error (1–2%):** 23 trials (**28.75%**) — Normal laboratory variance.
  - **High Error ($\ge$ 2%):** 18 trials (**22.50%**) — Includes 5 IQR outliers.
  - **Sub-2% Cumulative Share:** **77.50%** of all observations.
- **IQR Outlier Results ($> 3.9822\%$):**
  - Exactly 5 potential outliers identified (6.25% of dataset): `EXP004`, `EXP007`, `EXP014`, `EXP038`, `EXP055`.
  - Retained with `Outlier_Flag = True` for transparency.

---

## Slide 8: Data Visualizations Overview (7 Academic Figures)
- **Line Chart (14.1):** Mean experimental period vs theoretical physics curve with $\pm 1\,\text{SD}$ error bars.
- **Bar Chart (14.2):** Mean percentage error across 8 lengths against the $1.52\%$ dataset average.
- **Pie Chart (14.3):** Proportional distribution of Low (48.8%), Moderate (28.8%), and High (22.5%) error tiers.
- **Box Plot (14.4):** Medians, spreads, IQRs, and flier outlier markers across length groups.
- **Scatter Plot (14.5):** All 80 individual trials (75 inliers vs 5 outliers) against theoretical curve.
- **Histogram & KDE (14.6):** Positively skewed percentage error distribution with mean/median markers.
- **Correlation Heatmap (14.7):** Pearson correlation matrix across all 7 numerical attributes.

---

## Slide 9: Key Analysis & Insights
- **Model Conformance:** Experimental period tightly tracks theoretical predictions ($r = +0.992$), confirming $T \propto \sqrt{L}$.
- **Scale Invariance:** Correlation between length and percentage error is negligible ($r = -0.123$), proving error does not accumulate systematically at longer lengths.
- **Error Distribution Skewness:** Mean error ($1.52\%$) exceeds median ($1.01\%$) due to a small right-tail minority ($n=5$ outliers).
- **Length Extremes:**
  - Highest mean percentage error: $L = 0.50\text{ m}$ ($2.10\%$, affected by outlier `EXP038`).
  - Lowest mean percentage error: $L = 0.80\text{ m}$ ($0.91\%$, highly consistent).
  - Greatest variability: $L = 0.70\text{ m}$ ($\text{SD} = 0.0533\text{ s}$).
  - Lowest variability: $L = 0.20\text{ m}$ ($\text{SD} = 0.0159\text{ s}$).

---

## Slide 10: Important Findings
1. **Strong Theoretical Conformance:** Experimental data confirms $T = 2\pi\sqrt{L/g}$ ($r = +0.992$).
2. **High Measurement Accuracy:** Mean absolute error of $0.0214\text{ s}$ reflects typical human reaction time.
3. **Sub-2% Precision Majority:** $77.50\%$ of all experimental trials achieve $< 2.0\%$ error.
4. **Length-Independent Error:** Percentage error exhibits no systematic correlation with pendulum length ($r = -0.123$).
5. **Effective Outlier Isolation:** IQR method successfully flagged 5 statistical anomalies ($6.25\%$) without data deletion.
6. **Positively Skewed Residuals:** Over $60\%$ of observations exhibit $< 1.5\%$ error, proving that large timing offsets are rare.
7. **Best/Worst Length Groups:** $L = 0.80\text{ m}$ achieved best precision ($0.91\%$); $L = 0.50\text{ m}$ showed highest error ($2.10\%$).

---

## Slide 11: SDG Mapping — SDG 4: Quality Education
- **Goal:** United Nations Sustainable Development Goal 4 (Quality Education).
- **Target Focus:** Targets 4.4 & 4.7 (Technical STEM skills & data-driven scientific literacy).
- **Educational Value Delivered:**
  - Practical training in exploratory data analysis and statistical computing.
  - Hands-on implementation of non-parametric outlier detection (IQR).
  - Clear translation of theoretical physics formulas into computational models.
  - Academic-grade visual communication and evidence-based scientific reporting.

---

## Slide 12: Conclusion & Future Scope
- **Conclusion:**
  - Successfully quantified and visualized measurement discrepancies across 80 pendulum trials.
  - Demonstrated that experimental discrepancies stem from stochastic human stopwatch reaction time ($21.4\text{ ms}$) rather than physical model failure.
  - Established a robust, reproducible Python workflow for academic laboratory data analysis.
- **Future Scope:**
  - Ingestion of live photogate / optical sensor laboratory data.
  - Multi-operator comparative studies with uncertainty propagation ($u(L), u(T), u(g)$).
  - Development of an interactive web dashboard for real-time physics error diagnostics.
