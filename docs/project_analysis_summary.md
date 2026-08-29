# Comprehensive Project Analysis & Report Summary

**Project Title:** Error Visualization and Analysis of Experimental Data Using Python  
**Course:** Data Exploration and Visualization (Mini Project)  
**Author:** Dinesh Moorthy S R ([DineshMoorthy007](https://github.com/DineshMoorthy007))  
**Repository:** [error-visualization-experimental-data](https://github.com/DineshMoorthy007/error-visualization-experimental-data)  
**Academic Environment:** Python, Jupyter Notebook, Pandas, NumPy, Matplotlib, Seaborn, Git, GitHub  

---

## 1. Aim
To perform a systematic computational investigation, exploratory data analysis (EDA), data preprocessing, Interquartile Range (IQR) outlier detection, error formulation, and publication-quality diagnostic visualization on measurement data from a simple pendulum experiment using Python; evaluating empirical time periods against theoretical physics predictions, quantifying measurement uncertainties, and deriving evidence-based statistical insights.

---

## 2. Dataset Description
The dataset contains **80 individual experimental records** capturing the oscillation period of a simple pendulum across **8 distinct physical lengths** ($0.20\text{ m}, 0.30\text{ m}, 0.40\text{ m}, 0.50\text{ m}, 0.60\text{ m}, 0.70\text{ m}, 0.80\text{ m}, 1.00\text{ m}$) with **10 repeated trials** per length configuration.

### Theoretical Physics Model
The theoretical oscillation period $T$ of a simple gravity pendulum undergoing small angular displacements ($\theta \le 5^\circ$) in a uniform gravitational field is governed by:

$$T = 2\pi \sqrt{\frac{L}{g}}$$

Where:
- $L$: Length of the pendulum in metres ($\text{m}$)
- $T$: Theoretical oscillation period in seconds ($\text{s}$)
- $g$: Standard acceleration due to gravity ($9.81\text{ m/s}^2$)

### Dataset Provenance & Source
- **Nature of Dataset:** Simulated / Constructed Educational Experimental Dataset.
- **Generation Method:** Programmatically synthesized using Python (`numpy.random`, random seed `42`) to model realistic laboratory conditions, combining deterministic theoretical periods with Gaussian timing noise ($\sigma \approx 0.022\text{ s}$), positive manual reaction time bias ($+0.008\text{ s}$), and controlled experimental perturbations.
- **Completeness:** 100% complete (0 missing values, 0 duplicate records, 100% positive physical domain constraints).

---

## 3. Methodology
The project follows a rigorous 6-stage computational and statistical workflow:
1. **Data Ingestion & Quality Audit:** Load raw experimental observations, verify structural dimensionality ($80 \times 5$), confirm absence of missing entries or duplicates, and enforce physical validity ($L > 0, T > 0$).
2. **Data Preprocessing & Taxonomy:** Standardize numerical data types (float64, int64), preserve precision, maintain physical units ($\text{m}$ and $\text{s}$), and classify variables into independent, dependent, and reference taxonomies.
3. **Error Metrics Formulation:** Programmatically compute signed algebraic Error ($T_{\text{exp}} - T_{\text{theo}}$), Absolute Error, Relative Error, and Percentage Error.
4. **Outlier Detection via IQR:** Apply the non-parametric Interquartile Range method ($1.5 \times \text{IQR}$) on percentage errors to flag statistical anomalies with `Outlier_Flag` while preserving all observations for empirical transparency.
5. **Categorical Error Discretization & Statistical Aggregation:** Classify trials into project-defined analytical error quality tiers (Low, Moderate, High Error) and compute central tendency, dispersion, variance, standard deviation, quartiles, and length-wise group summaries.
6. **Exploratory Visual Diagnostics:** Construct seven publication-quality visualizations using Matplotlib and Seaborn to communicate trends, distributions, error compositions, box spreads, scatter regressions, error frequencies, and bivariate Pearson correlations.

---

## 4. Data Preprocessing
- **Type Casting:** Enforced `Experiment_ID` as string/object, `Trial_Number` as integer, and physical quantities (`Length_m`, `Theoretical_Period_s`, `Experimental_Period_s`) as standard 64-bit floating-point numbers.
- **Precision Preservation:** Preserved length measurements to 2 decimal places and time period measurements to 4 decimal places, avoiding precision loss.
- **Zero Infiltration:** Confirmed 0 null values, 0 duplicate rows, and verified all length and time variables strictly satisfy $L > 0$ and $T > 0$.
- **Unit Integrity:** Maintained original metric units (metres and seconds) throughout without artificial feature scaling or normalization.

---

## 5. Error Metrics & Formulations
Discrepancies between empirical observations and theoretical predictions were quantified using four foundational metrics:

1. **Signed Algebraic Error** (`Error_s`):
   $$E = T_{\text{exp}} - T_{\text{theo}}$$
   *Mean Result:* $+0.0069\text{ s}$ (Range: $-0.1301\text{ s}$ to $+0.1727\text{ s}$).

2. **Absolute Error** (`Absolute_Error_s`):
   $$E_{\text{abs}} = |T_{\text{exp}} - T_{\text{theo}}|$$
   *Mean Result:* $0.0214\text{ s}$ ($\text{SD} = 0.0267\text{ s}$; Median = $0.0152\text{ s}$).

3. **Relative Error** (`Relative_Error`):
   $$E_{\text{rel}} = \frac{|T_{\text{exp}} - T_{\text{theo}}|}{T_{\text{theo}}}$$
   *Mean Result:* $0.015243$ (Range: $0.000298$ to $0.102896$).

4. **Percentage Error** (`Percentage_Error`):
   $$E_{\text{pct}} = E_{\text{rel}} \times 100 = \left(\frac{|T_{\text{exp}} - T_{\text{theo}}|}{T_{\text{theo}}}\right) \times 100$$
   *Mean Result:* $1.5243\%$ ($\text{SD} = 1.7770\%$; Median = $1.0119\%$; Min = $0.0298\%$; Max = $10.2896\%$).

---

## 6. Statistical Analysis & Group Summaries

### Descriptive Statistics of Core Variables
- **Experimental Period ($T_{\text{exp}}$):** Mean = $1.4704\text{ s}$, Median = $1.4952\text{ s}$, Std Dev = $0.3547\text{ s}$, Variance = $0.1258\text{ s}^2$, Range = $1.1537\text{ s}$ ($0.8948\text{ s}$ to $2.0485\text{ s}$), $Q_1 = 1.2616\text{ s}$, $Q_3 = 1.7250\text{ s}$.
- **Percentage Error (`Percentage_Error`):** Mean = $1.5243\%$, Median = $1.0119\%$, Std Dev = $1.7770\%$, Variance = $3.1578\%^2$, Range = $10.2598\%$ ($0.0298\%$ to $10.2896\%$), $Q_1 = 0.4075\%$, $Q_3 = 1.8374\%$, $\text{IQR} = 1.4299\%$.

### Error Category Distribution (Project-Defined Tiers)
- **Low Error (< 1.0%):** 39 observations (**48.75%** share) — Represents modal, high-precision laboratory measurements.
- **Moderate Error (1.0% – 2.0%):** 23 observations (**28.75%** share) — Represents typical laboratory operational variance.
- **High Error ($\ge$ 2.0%):** 18 observations (**22.50%** share) — Comprises 5 IQR outliers and 13 moderately perturbed observations.
- **Cumulative Performance:** **77.50%** of all experimental trials achieve discrepancies strictly under $2.0\%$.

### Outlier Detection Summary (IQR Method)
- **IQR Thresholds:** $\text{Lower Bound} = -1.7374\%$ (no negative percentage errors exist); $\text{Upper Bound} = 3.9822\%$.
- **Identified Outliers ($n = 5$, 6.25% of dataset):**
  1. `EXP004` ($L=0.20\text{ m}$): $4.6260\%$ error ($+0.0415\text{ s}$)
  2. `EXP007` ($L=0.20\text{ m}$): $4.7709\%$ error ($+0.0428\text{ s}$)
  3. `EXP014` ($L=0.30\text{ m}$): $8.2727\%$ error ($+0.0909\text{ s}$)
  4. `EXP038` ($L=0.50\text{ m}$): $9.1717\%$ error ($-0.1301\text{ s}$)
  5. `EXP055` ($L=0.70\text{ m}$): $10.2896\%$ error ($+0.1727\text{ s}$)
- **Treatment:** Preserved in dataset with `Outlier_Flag = True` to uphold scientific transparency and study extreme timing variances.

---

## 7. Visualization Analysis & Diagnostics

1. **Figure 1 — Line Chart (`01_experimental_vs_theoretical_line.png`):**
   - *Visualization:* Plots mean experimental period with $\pm 1\,\text{SD}$ error bars against the continuous theoretical prediction curve $T = 2\pi\sqrt{L/g}$.
   - *Key Pattern:* Empirical points trace the theoretical curve with high fidelity across all lengths from $0.20\text{ m}$ to $1.00\text{ m}$.
   - *Scientific Insight:* Confirms square-root scaling ($T \propto \sqrt{L}$) and demonstrates tight measurement repeatability.

2. **Figure 2 — Bar Chart (`02_percentage_error_bar.png`):**
   - *Visualization:* Displays mean percentage error per length configuration alongside the dataset overall average ($1.52\%$).
   - *Key Pattern:* Highest error occurs at $L=0.50\text{ m}$ ($2.10\%$) and $L=0.20\text{ m}$ ($2.05\%$); lowest error occurs at $L=0.80\text{ m}$ ($0.91\%$) and $L=0.60\text{ m}$ ($1.00\%$).
   - *Scientific Insight:* Non-monotonic, irregular variation demonstrates that timing errors represent stochastic human reaction noise rather than length-dependent systematic bias.

3. **Figure 3 — Pie Chart (`03_error_category_pie.png`):**
   - *Visualization:* Illustrates proportional share across Low Error (48.8%), Moderate Error (28.8%), and High Error (22.5%) quality tiers.
   - *Key Pattern:* Low error observations dominate the distribution.
   - *Scientific Insight:* 77.5% of observations reside below $2.0\%$ error, verifying high overall experimental consistency.

4. **Figure 4 — Box Plot (`04_experimental_period_boxplot.png`):**
   - *Visualization:* Renders medians, IQRs, whiskers, and flier outlier points for experimental period across all 8 lengths against theoretical reference diamonds.
   - *Key Pattern:* Medians align with theoretical diamonds at every length. Fliers are visibly separated at lengths $0.30\text{ m}$, $0.50\text{ m}$, and $0.70\text{ m}$.
   - *Scientific Insight:* Intra-group dispersion is narrowest at $0.20\text{ m}$ ($\text{SD} = 0.0159\text{ s}$) and widest at $0.70\text{ m}$ ($\text{SD} = 0.0533\text{ s}$).

5. **Figure 5 — Scatter Plot (`05_length_vs_period_scatter.png`):**
   - *Visualization:* Plots all 80 individual trial observations (75 inliers in blue, 5 outliers in red triangles) against the theoretical model curve.
   - *Key Pattern:* All 80 observations cluster closely along the physics curve without structural distortion.
   - *Scientific Insight:* Flagged outliers are isolated vertical timing offsets rather than systemic physical breakdowns.

6. **Figure 6 — Histogram (`06_error_distribution_histogram.png`):**
   - *Visualization:* Depicts frequency distribution and KDE of percentage errors with mean ($1.52\%$) and median ($1.01\%$) reference lines.
   - *Key Pattern:* Strongly positive (right) skewness with high modal concentration in the $0.0\% - 1.5\%$ region.
   - *Scientific Insight:* The mean ($1.52\%$) is pulled above the median ($1.01\%$) by a small right-tail minority ($n=5$ outliers), showing that large timing errors are infrequent anomalies.

7. **Figure 7 — Heatmap (`07_correlation_heatmap.png`):**
   - *Visualization:* Displays Pearson correlation matrix ($r$) across all 7 numerical physical and error variables.
   - *Key Pattern:* Near-perfect correlation between physical dimensions ($r(\text{Length}, T_{\text{exp}}) = +0.992$). Negligible correlation between length and percentage error ($r = -0.123$).
   - *Scientific Insight:* Demonstrates that measurement accuracy is scale-invariant and timing error does not accumulate systematically with longer pendulums (noting that correlation does not establish causation).

---

## 8. Important Findings

1. **Strong Agreement with Theoretical Physics Model:**  
   Empirical oscillation periods trace the theoretical equation $T = 2\pi\sqrt{L/g}$ across all 8 pendulum lengths ($0.20\text{ m} - 1.00\text{ m}$), exhibiting a near-perfect Pearson correlation of $r = +0.992$.

2. **High Experimental Measurement Precision:**  
   The overall mean absolute error across all 80 trials is $0.0214\text{ s}$ ($21.4\text{ ms}$) with a mean percentage error of $1.5243\%$, which aligns with expected human visual-auditory stopwatch reaction latencies ($20 - 40\text{ ms}$).

3. **Dominance of Low-Error Observations:**  
   Nearly half of all measurements (**48.75%**, 39 observations) exhibit less than $1.0\%$ percentage error, and **77.50%** (62 observations) fall within the sub-2.0% quality boundary.

4. **Length-Invariant Error Behavior:**  
   The Pearson correlation between pendulum length and percentage error is negligible ($r = -0.123$), proving that percentage error is independent of pendulum length and does not systematically degrade as length increases.

5. **Isolation of Statistical Outliers via IQR:**  
   Exactly 5 observations (**6.25%** of the dataset) were identified as statistical outliers under the $1.5 \times \text{IQR}$ threshold ($> 3.9822\%$ error), with maximum error reaching $10.2896\%$ in trial `EXP055` ($L=0.70\text{ m}$).

6. **Right-Skewed Error Distribution:**  
   The percentage error distribution displays pronounced right-skewness, evidenced by a median ($1.0119\%$) substantially lower than the mean ($1.5243\%$), demonstrating that severe experimental discrepancies are rare events.

7. **Highest vs Lowest Error Configurations:**  
   The highest mean percentage error occurred at length $0.50\text{ m}$ ($2.1026\%$, driven by outlier `EXP038`), whereas the lowest mean percentage error occurred at length $0.80\text{ m}$ ($0.9080\%$).

---

## 9. SDG Mapping: SDG 4 — Quality Education

### Target Alignment: SDG 4.4 & 4.7
- **Project Contribution:** This project directly supports **United Nations Sustainable Development Goal 4: Quality Education** by offering a structured computational template for STEM pedagogy, integrating scientific physics principles with data science practices.
- **Competency Building:** The workflow develops essential student proficiencies in:
  - Practical data exploration and statistical reasoning.
  - Objective error quantification and scientific anomaly detection.
  - Reproducible computational modeling using standard open-source Python libraries.
  - Academic-grade visual communication and evidence-based interpretation.
- **Realistic Educational Impact:** By bridging abstract physical equations with concrete data-driven error diagnostics, the project fosters rigorous analytical thinking and reproducible scientific computing at the undergraduate collegiate level.

---

## 10. Conclusion
This computational exploration of experimental pendulum data successfully quantified and visualized measurement discrepancies across 80 laboratory trials. The analysis confirmed strong adherence to the theoretical small-angle pendulum model ($r = +0.992$) while revealing an average experimental percentage error of $1.52\%$. The IQR outlier method effectively isolated 5 anomalous trials ($6.25\%$) without necessitating arbitrary data deletion. Through the synthesis of descriptive statistics, group aggregations, and seven publication-quality visualizations, the project established that manual timing discrepancies represent stochastic human reaction latency rather than systematic physical bias, demonstrating the power of Python for experimental scientific validation.

---

## 11. Limitations
1. **Simulated Nature of Dataset:** The dataset is an educational, programmatically generated dataset modeling pendulum physics rather than live physical benchtop hardware readings.
2. **Fixed Parameter Assumptions:** Gravitational acceleration was assumed constant at $g = 9.81\text{ m/s}^2$ without local gravimetric calibration or altitude correction.
3. **Project-Defined Thresholds:** Error categorization boundaries (1% and 2%) represent analytical project-defined tiers rather than universal scientific standards.
4. **Correlation vs Causation:** Pearson correlation coefficients evaluate linear association only and do not establish causal physical mechanisms.
5. **Single Physical Domain:** The current analytical pipeline is restricted to simple pendulum dynamics and does not account for complex non-linear oscillations or aerodynamic damping models.

---

## 12. Future Scope
1. **Physical Laboratory Ingestion:** Interface the data pipeline with real-world laboratory sensors (photogates, optical encoders, laser timers) to capture automated oscillation data.
2. **Expansion of Sample Size:** Scale the dataset to multi-operator, multi-laboratory studies ($N \ge 500$) to evaluate inter-operator variability and systematic instrument biases.
3. **Formal Uncertainty Propagation:** Implement analytical Taylor-series and Monte Carlo error propagation models to quantify composite instrument uncertainties ($u(L), u(T), u(g)$).
4. **Interactive Analytical Dashboard:** Develop a web-based dashboard (using Streamlit or Dash) for real-time parameter tuning, curve fitting, and dynamic visual diagnostics.
5. **Cross-Domain Physics Extension:** Generalize the computational error analysis framework to other foundational physics experiments (e.g., Hooke's Law, Snell's Law, Boyle's Law).
