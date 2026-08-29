# Error Visualization and Analysis of Experimental Data Using Python

**Course:** Data Exploration and Visualization (Mini Project)  
**Author / GitHub:** [DineshMoorthy007](https://github.com/DineshMoorthy007)  
**Repository:** [error-visualization-experimental-data](https://github.com/DineshMoorthy007/error-visualization-experimental-data)  
**Status:** Completed & Submission-Ready  

---

## Overview
In physical and engineering sciences, empirical measurements are inherently subject to experimental uncertainties, instrument limitations, environmental disturbances, and human timing latencies. This mini project presents an end-to-end computational and statistical framework to explore, preprocess, validate, analyze, and visualize experimental data from a **Simple Pendulum Experiment**.

Using Python, Pandas, NumPy, Matplotlib, and Seaborn, this project analyzes 80 experimental observations across 8 distinct pendulum lengths. It formulates four foundational error metrics (Signed, Absolute, Relative, and Percentage Error), identifies statistical anomalies using the Interquartile Range (IQR) method, computes extensive descriptive statistics and group aggregations, and provides a publication-quality suite of **seven academic visualizations**.

---

## Problem Statement
Laboratory measurements rarely match theoretical mathematical predictions perfectly. When measuring the time period of a simple pendulum:
- Manual stopwatch triggers suffer from human visual-auditory reaction time delays ($\approx 0.02 - 0.04\,\text{s}$).
- Small-angle approximations ($\sin\theta \approx \theta$) introduce subtle non-linearities at higher oscillation amplitudes.
- Environmental damping and pivot friction alter oscillation cycles over time.

Without structured error visualization and statistical exploration, students and researchers struggle to distinguish whether discrepancies stem from systematic instrument bias, random environmental noise, or genuine experimental blunders (outliers). This project provides a computational framework to diagnose, quantify, and visualize these measurement errors.

---

## Aim
To explore, preprocess, validate, analyze, and visualize experimental measurement data from a simple pendulum system using Python, evaluating empirical time period variations against theoretical physics models, quantifying measurement uncertainties, detecting statistical anomalies, and generating publication-quality visual diagnostics.

---

## Objectives
1. **Dataset Ingestion & Exploration:** Ingest and inspect experimental observations covering 8 distinct pendulum lengths with 10 repeated trials ($N = 80$).
2. **Data Quality Verification:** Verify dataset completeness (0 missing values), absence of duplicates, and physical validity ($L > 0, T_{\text{theo}} > 0, T_{\text{exp}} > 0$).
3. **Data Preprocessing:** Standardize numeric types and precision while preserving original metric measurement units ($\text{m}$ and $\text{s}$).
4. **Variable Taxonomy:** Classify experimental attributes into independent, dependent, reference, and identifier categories.
5. **Outlier Detection:** Isolate statistical anomalies using the Interquartile Range (IQR) method ($1.5 \times \text{IQR}$) and flag them with `Outlier_Flag` without data deletion.
6. **Error Metrics Formulation:** Programmatically compute signed algebraic Error ($T_{\text{exp}} - T_{\text{theo}}$), Absolute Error, Relative Error, and Percentage Error.
7. **Error Classification:** Categorize experimental trials into project-defined analytical error quality tiers (Low Error $< 1\%$, Moderate Error $1 - 2\%$, High Error $\ge 2\%$).
8. **Descriptive Statistical Analysis:** Compute central tendency, dispersion, variance, standard deviation, quartiles, and length-wise group aggregations.
9. **Exploratory Data Visualization:** Programmatically generate seven distinct, publication-quality visualizations covering line, bar, pie, box, scatter, histogram, and correlation heatmap charts.
10. **Analysis & Academic Interpretation:** Synthesize quantitative findings, map project contributions to UN SDG 4 (Quality Education), document limitations, and define future research scope.

---

## Dataset

### Dataset Description
The dataset records the oscillation period of a simple pendulum across multiple physical lengths under gravitational acceleration ($g = 9.81\,\text{m/s}^2$).

#### Mathematical Model
The theoretical period $T$ of a simple pendulum undergoing small angular oscillations is given by:

$$T = 2\pi \sqrt{\frac{L}{g}}$$

Where:
- $L$: Length of the pendulum in metres ($\text{m}$)
- $T$: Theoretical period of oscillation in seconds ($\text{s}$)
- $g$: Acceleration due to gravity ($9.81\,\text{m/s}^2$)

### Dataset Source
**Simulated / Constructed Educational Experimental Dataset:**  
The dataset was synthetically generated for educational and analytical purposes using Python (`numpy.random` with fixed random seed `42`). It mathematically models theoretical pendulum physics while incorporating realistic Gaussian timing noise ($\sigma \approx 0.022\,\text{s}$), a slight positive human reaction bias ($+0.008\,\text{s}$), and controlled experimental perturbations for outlier analysis.

> *Note: This dataset does not originate from an external repository (such as Kaggle or UCI) nor does it claim to be physically gathered in a live laboratory.*

### Dataset Size
- **Total Records (Observations):** 80 rows
- **Raw Attributes (Variables):** 5 columns
- **Processed Attributes:** 11 columns (including error metrics, categories, and outlier flags)
- **Number of Length Groups:** 8 unique lengths ($0.20\,\text{m}, 0.30\,\text{m}, 0.40\,\text{m}, 0.50\,\text{m}, 0.60\,\text{m}, 0.70\,\text{m}, 0.80\,\text{m}, 1.00\,\text{m}$)
- **Trials per Length:** 10 trials
- **File Format:** CSV (Comma-Separated Values)
- **Raw Data Path:** `data/pendulum_experimental_data.csv`
- **Processed Data Path:** `data/processed/pendulum_processed_data.csv`

### Attributes
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

## Tools and Technologies
- **Python 3:** Core programming language for data analysis and modeling.
- **Pandas & NumPy:** Ingestion, data cleaning, mathematical array operations, and error metric formulation.
- **Matplotlib & Seaborn:** Academic visual diagnostics, custom figure themes, and 300 DPI rendering.
- **Jupyter Notebook:** Interactive, self-documenting analytical notebook environment.
- **Git & GitHub:** Version control, reproducible project structure, and repository hosting.

---

## Methodology
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

## Data Preprocessing
- **Type Casting:** Enforced `Experiment_ID` as string, `Trial_Number` as integer, and physical dimensions (`Length_m`, `Theoretical_Period_s`, `Experimental_Period_s`) as float64.
- **Precision Preservation:** Lengths rounded to 2 decimal places and periods/errors to 4 decimal places.
- **Physical Validation:** Verified $L > 0$, $T_{\text{theo}} > 0$, and $T_{\text{exp}} > 0$ across all 80 rows.
- **Zero Missing / Duplicates:** Verified 100% data completeness with 0 null values and 0 duplicate rows.
- **Unit Preservation:** Preserved physical units in metres ($\text{m}$) and seconds ($\text{s}$) without artificial scaling.

---

## Error Analysis
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

### Error Classification Breakdown
- **Low Error (< 1%):** 39 observations (**48.75%**) — Modal category, high precision.
- **Moderate Error (1–2%):** 23 observations (**28.75%**) — Typical laboratory tolerance.
- **High Error ($\ge$ 2%):** 18 observations (**22.50%**) — Includes 5 IQR outliers.
- **Cumulative Sub-2% Share:** **77.50%** of all observations.

---

## Statistical Analysis

### Descriptive Statistics Summary
| Metric Variable | Mean | Median ($Q_2$) | Min | Max | Std Dev | Variance | $Q_1$ | $Q_3$ | IQR |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Experimental_Period_s`** | $1.4704\,\text{s}$ | $1.4952\,\text{s}$ | $0.8948\,\text{s}$ | $2.0485\,\text{s}$ | $0.3547\,\text{s}$ | $0.1258\,\text{s}^2$ | $1.2616\,\text{s}$ | $1.7250\,\text{s}$ | $0.4634\,\text{s}$ |
| **`Absolute_Error_s`** | $0.0214\,\text{s}$ | $0.0152\,\text{s}$ | $0.0005\,\text{s}$ | $0.1727\,\text{s}$ | $0.0267\,\text{s}$ | $0.0007\,\text{s}^2$ | $0.0051\,\text{s}$ | $0.0260\,\text{s}$ | $0.0209\,\text{s}$ |
| **`Percentage_Error`** | $1.5243\%$ | $1.0119\%$ | $0.0298\%$ | $10.2896\%$ | $1.7770\%$ | $3.1578\%^2$ | $0.4075\%$ | $1.8374\%$ | $1.4299\%$ |

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

## Visualizations
The project generates a complete suite of **7 publication-quality academic visualizations** saved at 300 DPI in `visualizations/`:

| # | Visualization Title | File Name | Chart Type | Scientific Purpose & Focus |
| :-: | :--- | :--- | :--- | :--- |
| **1** | [Experimental vs Theoretical Period](visualizations/01_experimental_vs_theoretical_line.png) | `01_experimental_vs_theoretical_line.png` | Line Chart | Mean period vs theoretical curve $T = 2\pi\sqrt{L/g}$ with $\pm 1\,\text{SD}$ error bars. |
| **2** | [Average Percentage Error by Length](visualizations/02_percentage_error_bar.png) | `02_percentage_error_bar.png` | Bar Chart | Length-wise mean percentage error vs dataset grand average ($1.52\%$). |
| **3** | [Error Category Distribution](visualizations/03_error_category_pie.png) | `03_error_category_pie.png` | Pie Chart | Proportional share of Low ($48.8\%$), Moderate ($28.8\%$), and High ($22.5\%$) error tiers. |
| **4** | [Experimental Period Distribution](visualizations/04_experimental_period_boxplot.png) | `04_experimental_period_boxplot.png` | Box Plot | Medians, IQRs, whiskers, and flier outlier markers per length group. |
| **5** | [Length vs Experimental Period](visualizations/05_length_vs_period_scatter.png) | `05_length_vs_period_scatter.png` | Scatter Plot | Point-by-point scatter of all 80 trials (75 inliers vs 5 outliers) against theoretical curve. |
| **6** | [Percentage Error Distribution](visualizations/06_error_distribution_histogram.png) | `06_error_distribution_histogram.png` | Histogram & KDE | Skewed distribution of percentage errors with mean ($1.52\%$) and median ($1.01\%$) lines. |
| **7** | [Correlation Heatmap](visualizations/07_correlation_heatmap.png) | `07_correlation_heatmap.png` | Heatmap | Pearson correlation matrix ($r$) across all 7 numerical attributes. |

---

## Key Findings
1. **Strong Theoretical Conformance ($r = +0.992$):** Empirical oscillation periods strongly conform to the theoretical simple pendulum model $T = 2\pi\sqrt{L/g}$ ($r = +0.992$).
2. **Human-Scale Timing Accuracy ($\text{MAE} = 0.0214\,\text{s}$):** The overall mean absolute timing error is $0.0214\,\text{s}$ ($21.4\,\text{ms}$), matching expected human stopwatch reaction latencies.
3. **Sub-2% Precision Majority ($77.50\%$):** Over three-quarters of all trials have $< 2.0\%$ error, with $48.75\%$ achieving $< 1.0\%$ error.
4. **Length-Independent Error ($r = -0.123$):** Pearson correlation between length and percentage error is negligible ($r = -0.123$), proving error does not accumulate systematically with longer pendulums.
5. **Effective Outlier Isolation ($6.25\%$ Rate):** IQR method cleanly isolated 5 statistical anomalies ($> 3.9822\%$) without data deletion.
6. **Positively Skewed Residuals:** Over $60\%$ of observations exhibit $< 1.5\%$ error, proving that large discrepancies are rare events.
7. **Best/Worst Length Groups:** $L = 0.80\,\text{m}$ achieved best precision ($0.91\%$); $L = 0.50\,\text{m}$ showed highest error ($2.10\%$, driven by outlier `EXP038`).

---

## SDG Mapping: SDG 4 — Quality Education
- **Goal Alignment:** United Nations Sustainable Development Goal 4 (Quality Education) — Targets 4.4 and 4.7.
- **Pedagogical Impact:**
  - Integrates theoretical physics with computational data science and exploratory data analysis.
  - Teaches practical statistical reasoning, non-parametric outlier detection (IQR), and error quantification.
  - Implements publication-quality visual communication using open-source Python libraries.
  - Fosters reproducible scientific computing at the undergraduate collegiate level.

---

## Project Structure
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
│   ├── results_summary.md                   # Quantitative results & metrics summary table
│   ├── lab_record_checklist.md              # 38-point college lab record compliance checklist
│   ├── github_setup.md                      # Step-by-step GitHub publishing guide
│   ├── git_commit_plan.md                   # Version control and commit plan
│   └── final_project_status.md              # Final status and verification summary
│
├── notebooks/
│   └── error_visualization.ipynb            # Master Jupyter Notebook (Sections 1–23)
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
├── README.md                                # Master project documentation
└── requirements.txt                         # Python dependencies
```

---

## How to Run

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

### Launching the Master Notebook
```bash
jupyter notebook notebooks/error_visualization.ipynb
```

---

## Reproducibility
All analyses, figures, metrics, and tables are 100% reproducible. The dataset generation uses fixed random seed `42`, and relative paths are configured throughout all scripts and notebooks for cross-platform compatibility.

---

## Results
The experimental dataset `pendulum_experimental_data.csv` ($N = 80$ records across 8 distinct pendulum lengths) was successfully loaded, verified for data quality (0 missing values, 0 duplicate records, 100% physical validity), preprocessed, and classified into statistical taxonomies.

All four standard error metrics (Signed Error, Absolute Error, Relative Error, and Percentage Error) were programmatically formulated, yielding an overall mean absolute error of **$0.0214\,\text{s}$** ($21.4\,\text{ms}$) and a mean percentage error of **$1.5243\%$**. Outlier detection via the Interquartile Range ($1.5 \times \text{IQR}$) method identified exactly **5 statistical anomalies** ($6.25\%$) which were retained with `Outlier_Flag = True`. Comprehensive descriptive statistics and length-wise group summaries were computed.

A full suite of **seven publication-quality visualizations** (Line Chart, Bar Chart, Pie Chart, Box Plot, Scatter Plot, Histogram, and Correlation Heatmap) was successfully generated, confirming strong empirical conformance to theoretical pendulum physics ($r = +0.992$), scale-invariance of measurement errors ($r = -0.123$), and dominance of high-precision observations ($77.50\%$ with error $< 2.0\%$). All project objectives and college Data Exploration and Visualization lab record requirements have been completely fulfilled.

---

## Limitations
1. **Simulated Nature of Dataset:** The dataset is a constructed educational dataset modeling pendulum physics with Gaussian timing noise rather than live benchtop hardware measurements.
2. **Fixed Gravitational Assumption:** Standard acceleration due to gravity was treated as an exact constant ($g = 9.81\,\text{m/s}^2$) without local gravimetric or altitude adjustments.
3. **Project-Defined Thresholds:** Error categories (Low $< 1\%$, Moderate $1 - 2\%$, High $\ge 2\%$) represent analytical project tiers rather than standardized international metrological thresholds.
4. **Linear Correlation Boundaries:** Pearson correlation coefficients evaluate linear association only and do not imply causal mechanisms.
5. **Ideal Physics Scope:** Small-angle approximations ($\sin\theta \approx \theta$) were assumed throughout without incorporating non-linear damping decay or air resistance models.

---

## Future Scope
1. **Automated Laboratory Hardware Integration:** Connect the data ingestion pipeline directly to photogate timers, optical encoders, or smartphone accelerometer sensors.
2. **Expanded Multi-Operator Trials:** Scale sample size ($N \ge 500$) across multiple operators to systematically study inter-user reaction time variances.
3. **Formal Uncertainty Propagation:** Implement analytical Taylor-series and Monte Carlo uncertainty propagation models ($u(L), u(T), u(g)$).
4. **Interactive Visualization Dashboard:** Develop a lightweight web dashboard (using Streamlit or Plotly/Dash) for interactive parameter exploration, live curve fitting, and diagnostic plotting.
5. **Multi-Experiment Generalization:** Adapt this computational error analysis pipeline to other foundational physics and engineering experiments (e.g., Hooke's Law, Snell's Law, Ohm's Law, projectile motion).

---

## Conclusion
This computational exploration of experimental pendulum data successfully quantified and visualized measurement discrepancies across 80 laboratory trials. The analysis confirmed strong adherence to the theoretical small-angle pendulum model ($r = +0.992$) while revealing an average experimental percentage error of $1.52\%$. The IQR outlier method effectively isolated 5 anomalous trials ($6.25\%$) without necessitating arbitrary data deletion. Through the synthesis of descriptive statistics, group aggregations, and seven publication-quality visualizations, the project established that manual timing discrepancies represent stochastic human reaction latency rather than systematic physical bias, demonstrating the power of Python for experimental scientific validation.

---

## Disclaimer
The dataset used in this educational project is a simulated/constructed experimental dataset based on the theoretical simple pendulum model and is intended for demonstrating data exploration, error analysis, statistical analysis, and visualization techniques.
