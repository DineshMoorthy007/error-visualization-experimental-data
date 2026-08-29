# Error Visualization and Analysis of Experimental Data Using Python

**Course:** Data Exploration and Visualization (Mini Project)  
**Author / GitHub:** [DineshMoorthy007](https://github.com/DineshMoorthy007)  
**Repository:** [error-visualization-experimental-data](https://github.com/DineshMoorthy007/error-visualization-experimental-data)  
**Current Status:** Phase 3 Completed (Data Visualization & Visual Analysis)

---

## 1. Project Overview
In physical and engineering sciences, experimental measurements are inherently subject to experimental uncertainties, environmental disturbances, instrumental limits, and human timing errors. This mini project investigates measurement discrepancies by analyzing experimental data from a **Simple Pendulum Experiment**.

Using Python, Pandas, Matplotlib, and Seaborn, this project explores experimental observations, calculates discrepancy metrics (Error, Absolute Error, Relative Error, and Percentage Error), identifies statistical outliers using the Interquartile Range (IQR) method, evaluates descriptive statistical properties, and provides a publication-quality suite of **seven academic visualizations**.

---

## 2. Problem Statement
Laboratory measurements rarely match theoretical mathematical predictions perfectly. When measuring the time period of a simple pendulum:
- Stopwatch triggers suffer from human reaction latency ($\approx 0.02 - 0.04\,\text{s}$).
- Small-angle approximations ($\sin\theta \approx \theta$) introduce subtle non-linearities at higher oscillation amplitudes.
- Damping from aerodynamic resistance alters oscillation decay.

Without structured error visualization and statistical exploration, students and researchers struggle to determine whether discrepancies arise from systematic instrument bias, random environmental noise, or genuine experimental blunders (outliers). This project provides a computational framework to diagnose, quantify, and visualize these measurement errors.

---

## 3. Aim
To explore, preprocess, validate, analyze, and visualize experimental measurement data from a simple pendulum system using Python, evaluating empirical time period variations against theoretical physics models, quantifying measurement error metrics, detecting statistical anomalies, and generating publication-quality visual diagnostics.

---

## 4. Objectives
1. **Dataset Ingestion & Exploration:** Load and inspect experimental measurements covering 8 distinct pendulum lengths with 10 repeated trials ($N = 80$).
2. **Data Quality Verification:** Verify dataset completeness, absence of duplicates, and physical validity ($L > 0, T_{\text{theo}} > 0, T_{\text{exp}} > 0$).
3. **Data Preprocessing:** Standardize numeric types and precision while preserving original measurement units (metres and seconds).
4. **Error Metrics Formulation:** Calculate algebraic Error ($T_{\text{exp}} - T_{\text{theo}}$), Absolute Error, Relative Error, and Percentage Error.
5. **Outlier Detection:** Isolate experimental anomalies using the Interquartile Range (IQR) method on measurement errors and flag them without data deletion.
6. **Error Classification:** Categorize experimental trials into project-defined analytical error quality tiers (Low, Moderate, High Error).
7. **Descriptive Statistical Analysis:** Compute central tendency, dispersion, variance, standard deviation, and quartiles.
8. **Length-wise Group Aggregation:** Generate aggregated statistical summaries across all 8 pendulum length configurations.
9. **Exploratory Data Visualization:** Programmatically generate seven distinct, publication-quality visualizations covering line, bar, pie, box, scatter, histogram, and correlation heatmap charts.

---

## 5. Dataset
The dataset records the oscillation period of a simple pendulum across multiple physical lengths under gravitational acceleration ($g = 9.81\,\text{m/s}^2$).

### Mathematical Model
The theoretical period $T$ of a simple pendulum undergoing small oscillations is given by:

$$T = 2\pi \sqrt{\frac{L}{g}}$$

Where:
- $L$ = Length of the pendulum in metres ($\text{m}$)
- $T$ = Theoretical period of oscillation in seconds ($\text{s}$)
- $g$ = Acceleration due to gravity ($9.81\,\text{m/s}^2$)

---

## 6. Dataset Source
**Simulated / Constructed Educational Dataset:**  
The dataset was synthetically generated for educational and analytical purposes using Python (`numpy.random` with fixed random seed `42`). It mathematically models theoretical pendulum physics while incorporating realistic Gaussian timing noise ($\sigma \approx 0.022\,\text{s}$), a slight positive human reaction bias ($+0.008\,\text{s}$), and controlled experimental perturbations for outlier analysis.

> *Note: This dataset does not originate from an external repository (such as Kaggle or UCI) nor does it claim to be physically gathered in a live laboratory.*

---

## 7. Dataset Size
- **Total Records (Observations):** 80 rows
- **Raw Attributes (Variables):** 5 columns
- **Processed Attributes:** 11 columns (including error metrics, categories, and outlier flags)
- **Number of Length Groups:** 8 unique lengths ($0.20\,\text{m}, 0.30\,\text{m}, 0.40\,\text{m}, 0.50\,\text{m}, 0.60\,\text{m}, 0.70\,\text{m}, 0.80\,\text{m}, 1.00\,\text{m}$)
- **Trials per Length:** 10 trials
- **Raw Data Path:** `data/pendulum_experimental_data.csv`
- **Processed Data Path:** `data/processed/pendulum_processed_data.csv`

---

## 8. Attributes
| Attribute Name | Data Type | Description | Role / Format |
| :--- | :--- | :--- | :--- |
| `Experiment_ID` | String / Object | Unique observation identifier | Nominal (`EXP001` - `EXP080`) |
| `Trial_Number` | Integer | Repetition trial index for a given length | Discrete Numerical ($1 - 10$) |
| `Length_m` | Float | Measured length of the pendulum | Continuous Numerical (metres) |
| `Theoretical_Period_s` | Float | Theoretical period from $T = 2\pi\sqrt{L/g}$ | Continuous Numerical (seconds) |
| `Experimental_Period_s` | Float | Recorded experimental oscillation period | Continuous Numerical (seconds) |
| `Error_s` | Float | Signed error ($T_{\text{exp}} - T_{\text{theo}}$) | Derived Measurement (seconds) |
| `Absolute_Error_s` | Float | Magnitude of error ($|T_{\text{exp}} - T_{\text{theo}}|$) | Derived Measurement (seconds) |
| `Relative_Error` | Float | Dimensionless ratio ($\text{Absolute Error} / T_{\text{theo}}$) | Derived Dimensionless Metric |
| `Percentage_Error` | Float | Scaled percentage error ($\text{Relative Error} \times 100$) | Derived Percentage Metric (%) |
| `Error_Category` | String | Analytical error tier (Low, Moderate, High) | Ordinal Categorical Grouping |
| `Outlier_Flag` | Boolean | Statistical outlier indicator via IQR | Binary Flag (`True` / `False`) |

---

## 9. Error Metrics Formulation
The project computes four core error metrics to analyze experimental discrepancies:

1. **Signed Error ($\text{Error}_s$):**
   $$\text{Error}_s = T_{\text{exp}} - T_{\text{theo}}$$
   Quantifies directionality and timing bias (e.g., positive value indicates delayed stopwatch press).

2. **Absolute Error ($\text{Absolute\_Error}_s$):**
   $$\text{Absolute\_Error}_s = |T_{\text{exp}} - T_{\text{theo}}|$$
   Quantifies the absolute magnitude of deviation in physical time units (seconds).

3. **Relative Error ($\text{Relative\_Error}$):**
   $$\text{Relative\_Error} = \frac{\text{Absolute\_Error}_s}{T_{\text{theo}}}$$
   Measures error proportional to the physical magnitude of the theoretical period.

4. **Percentage Error ($\text{Percentage\_Error}$):**
   $$\text{Percentage\_Error} = \text{Relative\_Error} \times 100\%$$
   Normalizes the error across all pendulum lengths for uniform comparative analysis.

---

## 10. Data Preprocessing & Quality Assurance
The preprocessing pipeline applies explicit verification rules:
- **Completeness Check:** Confirmed 0 missing/null values across all columns.
- **Duplicate Check:** Confirmed 0 duplicate rows across all 80 observations.
- **Physical Validity:** Confirmed all $L > 0$, $T_{\text{theo}} > 0$, and $T_{\text{exp}} > 0$.
- **Precision Standardization:** Formatted lengths to 2 decimal places and time periods to 4 decimal places.
- **Preservation of Units:** Retained original SI units (metres and seconds) without artificial scaling to preserve direct physical meaning.
- **Outlier Retention:** Flagged 5 IQR statistical outliers without deletion to maintain experimental integrity.

---

## 11. Visualizations
All visualizations are generated programmatically using Python, Matplotlib, and Seaborn with a consistent high-resolution academic styling theme (300 DPI) and stored in `visualizations/`:

1. **Experimental vs Theoretical Period (`01_experimental_vs_theoretical_line.png`):** Line chart comparing mean experimental periods (with standard deviation error bars) against the theoretical physics prediction across all lengths.
2. **Average Percentage Error by Length (`02_percentage_error_bar.png`):** Bar chart displaying length-wise mean percentage errors annotated with exact values and benchmarked against the dataset mean ($1.52\%$).
3. **Error Category Distribution (`03_error_category_pie.png`):** Pie chart showing proportional composition across Low Error (48.8%), Moderate Error (28.8%), and High Error (22.5%) tiers.
4. **Experimental Period Box Plot (`04_experimental_period_boxplot.png`):** Box and whisker plot visualizing medians, interquartile spreads, and visible outlier points across all 8 length configurations.
5. **Length vs Experimental Period Scatter Plot (`05_length_vs_period_scatter.png`):** Scatter plot displaying all 80 individual experimental observations distinguished into inliers and flagged outliers against the theoretical curve.
6. **Percentage Error Distribution (`06_error_distribution_histogram.png`):** Histogram and KDE plot showing the right-skewed distribution of percentage errors with mean ($1.52\%$) and median ($1.01\%$) reference markers.
7. **Correlation Heatmap (`07_correlation_heatmap.png`):** Annotated Pearson correlation matrix evaluating linear dependencies between physical dimensions and error metrics.

---

## 12. Technologies Used
- **Python (>= 3.10):** Core programming language
- **Pandas (>= 2.0.0):** Tabular data manipulation, aggregation, and statistical summarization
- **NumPy (>= 1.24.0):** Numerical computation and vectorized error formulas
- **Matplotlib (>= 3.7.0):** Foundation visualization engine
- **Seaborn (>= 0.12.0):** Statistical plotting and visual aesthetic management
- **Jupyter Notebook (>= 1.0.0):** Interactive exploratory analysis and documentation
- **Git & GitHub:** Version control, collaborative tracking, and project repository hosting

---

## 13. Project Structure
```
error-visualization-experimental-data/
│
├── data/
│   ├── pendulum_experimental_data.csv       # Raw experimental dataset (80 records)
│   └── processed/
│       └── pendulum_processed_data.csv      # Enriched processed dataset (80 records, 11 attributes)
│
├── notebooks/
│   └── error_visualization.ipynb            # Complete Jupyter Notebook (Sections 1 to 14)
│
├── src/
│   ├── data_preprocessing.py                # Dataset loader, exploration & validation routines
│   ├── error_analysis.py                    # Error calculation, classification & statistics
│   └── visualization.py                     # Modular plotting routines & batch figure generator
│
├── visualizations/                          # Output directory for exported 300 DPI figures
│   ├── 01_experimental_vs_theoretical_line.png
│   ├── 02_percentage_error_bar.png
│   ├── 03_error_category_pie.png
│   ├── 04_experimental_period_boxplot.png
│   ├── 05_length_vs_period_scatter.png
│   ├── 06_error_distribution_histogram.png
│   └── 07_correlation_heatmap.png
│
├── docs/                                    # Academic reports and documentation
│
├── README.md                                # Comprehensive project documentation
├── requirements.txt                         # Python dependencies
├── .gitignore                               # Git ignore configuration
└── LICENSE                                  # MIT Open-Source License
```

---

## 14. Methodology
```
[ Raw Dataset Ingestion ]
          │
          ▼
[ Exploratory Data Analysis ] (Head, Tail, Shape, Attributes, Dtypes, Info)
          │
          ▼
[ Data Quality Verification ] (Nulls, Duplicates, Physical Constraints L > 0, T > 0)
          │
          ▼
[ Data Preprocessing ] (Explicit Type Casting, Precision Standardization)
          │
          ▼
[ Variable Taxonomy Classification ] (Discrete/Continuous Numerical, Identifiers, Flags)
          │
          ▼
[ Error Metric Formulation ] (Error, Absolute Error, Relative Error, Percentage Error)
          │
          ▼
[ Outlier Detection ] (1.5 × IQR Thresholding, Outlier_Flag assignment)
          │
          ▼
[ Error Classification ] (Low <1%, Moderate 1-2%, High >=2% Tiers)
          │
          ▼
[ Descriptive Statistics & Group Summaries ] (11-metric statistical summary, Length-wise groupby)
          │
          ▼
[ Save Processed Dataset ] (data/processed/pendulum_processed_data.csv)
          │
          ▼
[ Data Visualization Suite ] (7 High-Resolution Figures: Line, Bar, Pie, Box, Scatter, Hist, Heatmap)
```

---

## 15. Current Phase Status
### Phase 3: Data Visualization & Visual Analysis (Completed)
- [x] All 7 required visualizations implemented in `src/visualization.py`.
- [x] All 7 high-resolution PNG images generated and saved to `visualizations/`.
- [x] Jupyter Notebook `notebooks/error_visualization.ipynb` updated with Section 14 (subsections 14.1 to 14.7) and data-grounded interpretations.
- [x] README updated with complete Visualizations catalog and methodology.
- [x] All automated validation tests passed.

---

## 16. How to Run

### Step 1: Clone the Repository
```bash
git clone https://github.com/DineshMoorthy007/error-visualization-experimental-data.git
cd error-visualization-experimental-data
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run Data Processing & Visualization Scripts
```bash
# Run data preprocessing and exploration
python src/data_preprocessing.py

# Run complete error analysis and statistical pipeline
python src/error_analysis.py

# Generate all 7 visualization plots
python src/visualization.py
```

### Step 4: Launch Interactive Jupyter Notebook
```bash
jupyter notebook notebooks/error_visualization.ipynb
```

---

## 17. Sustainable Development Goals (SDG) Mapping & Disclaimer

### SDG Alignment
- **SDG 4: Quality Education (Target 4.4):** Fosters computational data literacy and measurement error awareness in STEM education.
- **SDG 9: Industry, Innovation, and Infrastructure (Target 9.5):** Emphasizes precision measurement modeling, calibration standards, and scientific anomaly detection.

### Disclaimer
This dataset is a **synthetically constructed educational experimental dataset** created for the *Data Exploration and Visualization* course project. While modeled around theoretical pendulum physics ($T = 2\pi\sqrt{L/g}$) with realistic human reaction variances, the values were generated using computational algorithms and were not recorded in a physical laboratory session.
