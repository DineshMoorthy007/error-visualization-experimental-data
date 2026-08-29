# Error Visualization and Analysis of Experimental Data Using Python

**Course:** Data Exploration and Visualization (Mini Project)  
**Author / GitHub:** [DineshMoorthy007](https://github.com/DineshMoorthy007)  
**Repository:** [error-visualization-experimental-data](https://github.com/DineshMoorthy007/error-visualization-experimental-data)  
**Status:** Completed (Phases 1–4 Fully Integrated)  

---

## 1. Project Overview
In physical and engineering sciences, empirical measurements are inherently subject to experimental uncertainties, instrument limitations, environmental disturbances, and human timing latencies. This mini project presents an end-to-end computational and statistical framework to explore, preprocess, validate, analyze, and visualize experimental data from a **Simple Pendulum Experiment**.

Using Python, Pandas, NumPy, Matplotlib, and Seaborn, this project analyzes 80 experimental observations across 8 distinct pendulum lengths. It formulates four foundational error metrics (Signed, Absolute, Relative, and Percentage Error), identifies statistical anomalies using the Interquartile Range (IQR) method, computes extensive descriptive statistics and group aggregations, and provides a publication-quality suite of **seven academic visualizations**.

---

## 2. Problem Statement
Laboratory measurements rarely match theoretical mathematical predictions perfectly. When measuring the time period of a simple pendulum:
- Manual stopwatch triggers suffer from human visual-auditory reaction time delays ($\approx 0.02 - 0.04\,\text{s}$).
- Small-angle approximations ($\sin\theta \approx \theta$) introduce non-linearities at higher initial release angles.
- Environmental damping and pivot friction alter oscillation cycles.

Without systematic error visualization and statistical exploration, students and researchers struggle to distinguish whether discrepancies stem from systematic instrument bias, random environmental noise, or genuine experimental blunders (outliers). This project provides a structured computational framework to diagnose, quantify, and visualize these measurement errors.

---

## 3. Aim
To perform systematic data exploration, quality verification, data preprocessing, outlier detection, experimental error analysis, and publication-quality visual diagnostics on measurement data from a simple pendulum experiment using Python, evaluating empirical time period variations against theoretical physics models, quantifying measurement uncertainties, and generating evidence-based scientific insights.

---

## 4. Objectives
1. **Dataset Ingestion & Exploration:** Ingest and inspect experimental observations covering 8 distinct pendulum lengths with 10 repeated trials ($N = 80$).
2. **Data Quality Verification:** Verify dataset completeness (0 missing values), absence of duplicates, and physical validity ($L > 0, T_{\text{theo}} > 0, T_{\text{exp}} > 0$).
3. **Data Preprocessing:** Standardize numeric types and precision while preserving original metric measurement units ($\text{m}$ and $\text{s}$).
4. **Error Metrics Formulation:** Programmatically compute signed algebraic Error ($T_{\text{exp}} - T_{\text{theo}}$), Absolute Error, Relative Error, and Percentage Error.
5. **Outlier Detection:** Isolate statistical anomalies using the non-parametric Interquartile Range (IQR) method ($1.5 \times \text{IQR}$) and flag them with `Outlier_Flag` without data deletion.
6. **Error Classification:** Categorize experimental trials into project-defined analytical error quality tiers (Low Error $< 1\%$, Moderate Error $1 - 2\%$, High Error $\ge 2\%$).
7. **Descriptive Statistical Analysis:** Compute central tendency, dispersion, variance, standard deviation, quartiles, and interquartile spread.
8. **Length-wise Group Aggregation:** Generate aggregated statistical summaries across all 8 pendulum length configurations.
9. **Exploratory Data Visualization:** Programmatically generate seven distinct, publication-quality visualizations covering line, bar, pie, box, scatter, histogram, and correlation heatmap charts.
10. **Analysis & Academic Interpretation:** Synthesize quantitative findings, map project contributions to UN SDG 4 (Quality Education), document limitations, and define future research scope.

---

## 5. Dataset
The dataset records the oscillation time period of a simple pendulum across multiple physical lengths under Earth's gravitational acceleration ($g = 9.81\,\text{m/s}^2$).

### Mathematical Model
The theoretical period $T$ of a simple pendulum undergoing small angular oscillations is given by:

$$T = 2\pi \sqrt{\frac{L}{g}}$$

Where:
- $L$: Length of the pendulum in metres ($\text{m}$)
- $T$: Theoretical period of oscillation in seconds ($\text{s}$)
- $g$: Acceleration due to gravity ($9.81\,\text{m/s}^2$)

---

## 6. Dataset Description
- **Total Records (Observations):** 80 rows
- **Raw Attributes (Variables):** 5 columns
- **Processed Attributes:** 11 columns (including error metrics, categories, and outlier flags)
- **Number of Length Groups:** 8 unique lengths ($0.20\,\text{m}, 0.30\,\text{m}, 0.40\,\text{m}, 0.50\,\text{m}, 0.60\,\text{m}, 0.70\,\text{m}, 0.80\,\text{m}, 1.00\,\text{m}$)
- **Trials per Length:** 10 trials
- **Raw Data Path:** `data/pendulum_experimental_data.csv`
- **Processed Data Path:** `data/processed/pendulum_processed_data.csv`

### Attributes Table
| Attribute Name | Data Type | Description | Role / Format |
| :--- | :--- | :--- | :--- |
| `Experiment_ID` | String / Object | Unique observation identifier | Nominal (`EXP001` - `EXP080`) |
| `Trial_Number` | Integer | Repetition trial index for a given length | Discrete Numerical ($1 - 10$) |
| `Length_m` | Float | Measured length of the pendulum | Continuous Independent ($0.20 - 1.00\,\text{m}$) |
| `Theoretical_Period_s` | Float | Theoretical period from $T = 2\pi\sqrt{L/g}$ | Continuous Reference ($0.8971 - 2.0061\,\text{s}$) |
| `Experimental_Period_s` | Float | Recorded experimental oscillation period | Continuous Dependent ($0.8948 - 2.0485\,\text{s}$) |
| `Error_s` | Float | Signed error ($T_{\text{exp}} - T_{\text{theo}}$) | Derived Metric (seconds) |
| `Absolute_Error_s` | Float | Magnitude of error ($|T_{\text{exp}} - T_{\text{theo}}|$) | Derived Metric (seconds) |
| `Relative_Error` | Float | Dimensionless ratio ($\text{Absolute Error} / T_{\text{theo}}$) | Derived Dimensionless Metric |
| `Percentage_Error` | Float | Scaled percentage error ($\text{Relative Error} \times 100$) | Derived Percentage Metric (%) |
| `Error_Category` | String | Analytical error tier (Low, Moderate, High) | Ordinal Categorical Grouping |
| `Outlier_Flag` | Boolean | Statistical outlier indicator via IQR | Binary Flag (`True` / `False`) |

---

## 7. Dataset Source
**Simulated / Constructed Educational Experimental Dataset:**  
The dataset was programmatically synthesized for educational and analytical purposes using Python (`numpy.random` with fixed random seed `42`). It mathematically models theoretical pendulum physics while incorporating realistic Gaussian timing noise ($\sigma \approx 0.022\,\text{s}$), a slight positive human reaction bias ($+0.008\,\text{s}$), and controlled experimental perturbations for outlier analysis.

> *Note: This dataset does not originate from an external repository (such as Kaggle or UCI) nor does it claim to be physically gathered in a live laboratory.*

---

## 8. Technologies Used
- **Programming Language:** Python 3.10+
- **Data Manipulation & Preprocessing:** Pandas, NumPy
- **Data Visualization & Plotting:** Matplotlib, Seaborn
- **Interactive Computing & Notebooks:** Jupyter Notebook
- **Version Control & Repository:** Git, GitHub

---

## 9. Methodology
```
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│   Raw Data Ingestion    │ ──> │   Data Quality Audit    │ ──> │   Data Preprocessing    │
│  80 Records × 5 Columns │     │ Missing = 0, Dupes = 0  │     │ Type Cast & Formatting  │
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
                                                                             │
                                                                             ▼
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│   Error Formulation     │ ──> │  IQR Outlier Detection  │ ──> │  Error Classification   │
│ Signed, Abs, Rel, % Err │     │ 1.5×IQR (n=5 Outliers)  │     │ Low, Moderate, High Tiers│
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
                                                                             │
                                                                             ▼
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│   Publication Figures   │ ──> │ Descriptive Statistics  │ ──> │  Report & SDG Mapping   │
│  7 Academic Diagnostics │     │ Central Tendency & IQR  │     │ SDG 4 Quality Education │
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
```

---

## 10. Data Preprocessing
- **Type Casting:** Enforced `Experiment_ID` as string, `Trial_Number` as integer, and physical dimensions (`Length_m`, `Theoretical_Period_s`, `Experimental_Period_s`) as float64.
- **Precision Preservation:** Lengths rounded to 2 decimal places and periods/errors to 4 decimal places.
- **Physical Validation:** Verified $L > 0$, $T_{\text{theo}} > 0$, and $T_{\text{exp}} > 0$ across all 80 rows.
- **Zero Missing / Duplicates:** Verified 100% data completeness with 0 null values and 0 duplicate rows.
- **Unit Preservation:** Preserved physical units in metres ($\text{m}$) and seconds ($\text{s}$) without artificial scaling.

---

## 11. Error Metrics
Discrepancies were formulated using four standard mathematical equations:

1. **Signed Algebraic Error ($\text{Error}_s$):**
   $$\text{Error}_s = T_{\text{exp}} - T_{\text{theo}}$$
   *Mean Result:* $+0.0069\,\text{s}$ (Net positive bias due to stopwatch trigger delay).

2. **Absolute Error ($\text{Absolute\_Error}_s$):**
   $$\text{Absolute\_Error}_s = |T_{\text{exp}} - T_{\text{theo}}|$$
   *Mean Result:* $0.0214\,\text{s}$ ($21.4\,\text{ms}$, typical of human visual-auditory reaction time).

3. **Relative Error ($\text{Relative\_Error}$):**
   $$\text{Relative\_Error} = \frac{|T_{\text{exp}} - T_{\text{theo}}|}{T_{\text{theo}}}$$
   *Mean Result:* $0.015243$ ($1.52\%$).

4. **Percentage Error ($\text{Percentage\_Error}$):**
   $$\text{Percentage\_Error} = \text{Relative\_Error} \times 100\%$$
   *Mean Result:* $1.5243\%$ (Median: $1.0119\%$, Min: $0.0298\%$, Max: $10.2896\%$).

---

## 12. Statistical Analysis & Outlier Detection

### Descriptive Statistics Summary
| Metric Variable | Mean | Median ($Q_2$) | Min | Max | Std Dev | Variance | $Q_1$ | $Q_3$ | IQR |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Experimental_Period_s`** | $1.4704\,\text{s}$ | $1.4952\,\text{s}$ | $0.8948\,\text{s}$ | $2.0485\,\text{s}$ | $0.3547\,\text{s}$ | $0.1258\,\text{s}^2$ | $1.2616\,\text{s}$ | $1.7250\,\text{s}$ | $0.4634\,\text{s}$ |
| **`Absolute_Error_s`** | $0.0214\,\text{s}$ | $0.0152\,\text{s}$ | $0.0005\,\text{s}$ | $0.1727\,\text{s}$ | $0.0267\,\text{s}$ | $0.0007\,\text{s}^2$ | $0.0051\,\text{s}$ | $0.0260\,\text{s}$ | $0.0209\,\text{s}$ |
| **`Percentage_Error`** | $1.5243\%$ | $1.0119\%$ | $0.0298\%$ | $10.2896\%$ | $1.7770\%$ | $3.1578\%^2$ | $0.4075\%$ | $1.8374\%$ | $1.4299\%$ |

### Error Category Distribution
- **Low Error (< 1%):** 39 observations (**48.75%**) — Modal category, high precision.
- **Moderate Error (1–2%):** 23 observations (**28.75%**) — Typical laboratory tolerance.
- **High Error ($\ge$ 2%):** 18 observations (**22.50%**) — Includes 5 IQR outliers.
- **Cumulative Sub-2% Share:** **77.50%** of all observations.

### Outlier Analysis (IQR Method)
- **IQR Threshold:** $\text{Upper Bound} = Q_3 + 1.5 \times \text{IQR} = 3.9822\%$
- **Identified Outliers ($n=5$, 6.25%):**
  - `EXP004` ($L=0.20\,\text{m}$): $4.6260\%$ error ($+0.0415\,\text{s}$)
  - `EXP007` ($L=0.20\,\text{m}$): $4.7709\%$ error ($+0.0428\,\text{s}$)
  - `EXP014` ($L=0.30\,\text{m}$): $8.2727\%$ error ($+0.0909\,\text{s}$)
  - `EXP038` ($L=0.50\,\text{m}$): $9.1717\%$ error ($-0.1301\,\text{s}$)
  - `EXP055` ($L=0.70\,\text{m}$): $10.2896\%$ error ($+0.1727\,\text{s}$)
- **Retention:** Flagged with `Outlier_Flag = True` and retained to preserve scientific transparency.

---

## 13. Visualizations
The project generates a complete suite of **7 publication-quality academic visualizations** saved at 300 DPI in `visualizations/`:

| # | Visualization Title | File Name | Chart Type | Scientific Focus |
| :-: | :--- | :--- | :--- | :--- |
| **1** | [Experimental vs Theoretical Period](visualizations/01_experimental_vs_theoretical_line.png) | `01_experimental_vs_theoretical_line.png` | Line Chart | Mean period vs theoretical curve $T = 2\pi\sqrt{L/g}$ with $\pm 1\,\text{SD}$ error bars. |
| **2** | [Average Percentage Error by Length](visualizations/02_percentage_error_bar.png) | `02_percentage_error_bar.png` | Bar Chart | Length-wise mean percentage error vs dataset overall average ($1.52\%$). |
| **3** | [Error Category Distribution](visualizations/03_error_category_pie.png) | `03_error_category_pie.png` | Pie Chart | Proportional share of Low ($48.8\%$), Moderate ($28.8\%$), and High ($22.5\%$) error tiers. |
| **4** | [Experimental Period Distribution](visualizations/04_experimental_period_boxplot.png) | `04_experimental_period_boxplot.png` | Box Plot | Medians, IQRs, whiskers, and flier outlier markers per length. |
| **5** | [Length vs Experimental Period](visualizations/05_length_vs_period_scatter.png) | `05_length_vs_period_scatter.png` | Scatter Plot | Point-by-point scatter of all 80 trials (75 inliers vs 5 outliers) against theoretical curve. |
| **6** | [Percentage Error Distribution](visualizations/06_error_distribution_histogram.png) | `06_error_distribution_histogram.png` | Histogram & KDE | Skewed distribution of percentage errors with mean ($1.52\%$) and median ($1.01\%$) lines. |
| **7** | [Correlation Heatmap](visualizations/07_correlation_heatmap.png) | `07_correlation_heatmap.png` | Heatmap | Pearson correlation matrix ($r$) across all 7 numerical variables. |

---

## 14. Analysis and Interpretation
1. **Model Compliance:** The empirical periods closely trace theoretical physics predictions ($r = +0.992$), confirming that the simple pendulum obeys $T \propto \sqrt{L}$.
2. **Reaction Latency Bias:** Mean signed error is $+0.0069\,\text{s}$, indicating a slight positive human reaction time delay during stopwatch triggering.
3. **Scale Invariance:** The correlation between pendulum length and percentage error is negligible ($r = -0.123$), proving that relative timing error does not accumulate with longer pendulums.
4. **Error Distribution Skewness:** The percentage error distribution is strongly right-skewed; the median error ($1.01\%$) is substantially lower than the mean ($1.52\%$) due to the 5 right-tail outliers.
5. **Length Extremes:** Length $0.80\,\text{m}$ achieved the lowest mean percentage error ($0.91\%$), while $0.50\,\text{m}$ recorded the highest ($2.10\%$, driven by outlier `EXP038`).

---

## 15. Key Findings
1. **Strong Theoretical Conformance ($r = +0.992$):** Experimental oscillation periods strongly validate Newtonian pendulum physics.
2. **Human-Scale Timing Accuracy ($\text{MAE} = 0.0214\,\text{s}$):** Average absolute discrepancy is $21.4\,\text{ms}$, consistent with human stopwatch reaction latencies.
3. **Sub-2% Accuracy Majority ($77.50\%$):** Over three-quarters of all trials have $< 2.0\%$ error, with $48.75\%$ achieving $< 1.0\%$ error.
4. **Length-Independent Error ($r = -0.123$):** Experimental percentage error exhibits no systematic correlation with pendulum length.
5. **Effective Outlier Isolation ($6.25\%$ Rate):** IQR method cleanly isolated 5 manual timing outliers ($> 3.9822\%$).
6. **Positively Skewed Residuals:** Over $60\%$ of observations exhibit $< 1.5\%$ error, proving that large discrepancies are rare events.
7. **Best/Worst Length Groups:** $L = 0.80\,\text{m}$ achieved highest precision ($0.91\%$); $L = 0.50\,\text{m}$ showed highest error ($2.10\%$).

---

## 16. SDG Mapping: SDG 4 — Quality Education
- **Goal Alignment:** United Nations Sustainable Development Goal 4 (Quality Education) — Targets 4.4 and 4.7.
- **Pedagogical Impact:**
  - Integrates theoretical physics with computational data science and exploratory data analysis.
  - Teaches practical statistical reasoning, non-parametric outlier detection (IQR), and error quantification.
  - Implements publication-quality visual communication using open-source Python libraries.
  - Fosters reproducible scientific computing at the undergraduate collegiate level.

---

## 17. Limitations
1. **Simulated Dataset:** The dataset is an educational construct modeling pendulum physics with Gaussian timing noise rather than live benchtop hardware measurements.
2. **Fixed Gravitational Constant:** Standard gravity was assumed constant ($g = 9.81\,\text{m/s}^2$) without local altitude or gravimetric adjustments.
3. **Project-Defined Categories:** Error categories (1% and 2%) represent project-defined analytical groupings rather than international metrological standards.
4. **Correlation vs Causation:** Pearson correlation evaluates linear association only and does not establish causal mechanisms.
5. **Small-Angle Physics Scope:** Analysis assumes idealized small-angle harmonic motion ($\sin\theta \approx \theta$) without aerodynamic drag decay.

---

## 18. Future Scope
1. **Live Sensor Ingestion:** Interface the data pipeline with photogates, optical encoders, or smartphone accelerometer sensors.
2. **Multi-Operator Studies:** Scale to $N \ge 500$ observations across multiple operators to study inter-user reaction time variance.
3. **Formal Uncertainty Propagation:** Implement analytical Taylor-series and Monte Carlo error propagation models ($u(L), u(T), u(g)$).
4. **Interactive Dashboard:** Build an interactive web application (Streamlit or Dash) for real-time curve fitting and visual diagnostics.
5. **Cross-Domain Physics Extension:** Generalize the analysis pipeline to Hooke's Law, Snell's Law, and projectile motion.

---

## 19. Conclusion
This computational exploration of experimental pendulum data successfully quantified and visualized measurement discrepancies across 80 laboratory trials. The analysis confirmed strong adherence to the theoretical small-angle pendulum model ($r = +0.992$) while revealing an average experimental percentage error of $1.52\%$. The IQR outlier method effectively isolated 5 anomalous trials ($6.25\%$) without necessitating arbitrary data deletion. Through the synthesis of descriptive statistics, group aggregations, and seven publication-quality visualizations, the project established that manual timing discrepancies represent stochastic human reaction latency rather than systematic physical bias, demonstrating the power of Python for experimental scientific validation.

---

## 20. Project Structure
```
error-visualization-experimental-data/
│
├── data/
│   ├── pendulum_experimental_data.csv       # Raw experimental dataset (80 rows x 5 cols)
│   └── processed/
│       └── pendulum_processed_data.csv      # Enriched processed dataset (80 rows x 11 cols)
│
├── docs/
│   ├── project_analysis_summary.md          # Comprehensive report-ready analysis document
│   ├── presentation_content.md              # 12-slide presentation content
│   └── results_summary.md                   # Quantitative results & metrics summary table
│
├── notebooks/
│   └── error_visualization.ipynb            # Master Jupyter Notebook (Sections 1–20)
│
├── src/
│   ├── __init__.py                          # Package initialization
│   ├── data_preprocessing.py                # Ingestion, validation, and type casting module
│   ├── error_analysis.py                    # Error formulation, IQR outliers, descriptive stats
│   └── visualization.py                     # Academic plotting suite (7 figures)
│
├── visualizations/
│   ├── 01_experimental_vs_theoretical_line.png
│   ├── 02_percentage_error_bar.png
│   ├── 03_error_category_pie.png
│   ├── 04_experimental_period_boxplot.png
│   ├── 05_length_vs_period_scatter.png
│   ├── 06_error_distribution_histogram.png
│   └── 07_correlation_heatmap.png
│
├── .gitignore                               # Git ignore configuration
├── LICENSE                                  # MIT License
├── README.md                                # Project documentation
└── requirements.txt                         # Python dependencies
```

---

## 21. How to Run

### Prerequisites
- Python 3.10 or higher
- Git

### Installation
```bash
# 1. Clone repository
git clone https://github.com/DineshMoorthy007/error-visualization-experimental-data.git
cd error-visualization-experimental-data

# 2. Install dependencies
pip install -r requirements.txt
```

### Running the Analysis Modules
```bash
# Run data preprocessing
python src/data_preprocessing.py

# Run error analysis & statistical modeling
python src/error_analysis.py

# Generate all 7 publication visualizations
python src/visualization.py
```

### Launching the Jupyter Notebook
```bash
jupyter notebook notebooks/error_visualization.ipynb
```

---

## 22. Reproducibility
All analyses, figures, metrics, and tables are 100% reproducible. The dataset generation uses fixed random seed `42`, and relative paths are configured throughout all scripts and notebooks for cross-platform compatibility.

---

## 23. Disclaimer
This repository was developed for educational and academic mini-project coursework in **Data Exploration and Visualization**. The experimental dataset is synthetically generated to model physics laboratory conditions and does not claim to originate from live physical hardware sensors.
