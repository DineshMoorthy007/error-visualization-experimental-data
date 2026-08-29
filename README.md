# Error Visualization and Analysis of Experimental Data Using Python

**Course:** Data Exploration and Visualization (Mini Project)  
**Author / GitHub:** [DineshMoorthy007](https://github.com/DineshMoorthy007)  
**Repository:** [error-visualization-experimental-data](https://github.com/DineshMoorthy007/error-visualization-experimental-data)  
**Current Status:** Phase 1 Completed (Foundation, Dataset Construction & Validation)

---

## 1. Project Overview
In physical and engineering sciences, experimental measurements are inherently subject to experimental uncertainties, environmental disturbances, instrumental limits, and human timing errors. This mini project investigates measurement discrepancies by analyzing experimental data from a **Simple Pendulum Experiment**.

Using Python and data visualization techniques, this project explores experimental observations, calculates discrepancy metrics (Absolute Error, Relative Error, and Percentage Error), identifies statistical outliers, and visualizes error trends across varying physical dimensions.

---

## 2. Problem Statement
Laboratory measurements rarely match theoretical mathematical predictions perfectly. When measuring the time period of a simple pendulum:
- Stopwatch triggers suffer from human reaction latency ($\approx 0.02 - 0.04\,\text{s}$).
- Small-angle approximations ($\sin\theta \approx \theta$) introduce subtle non-linearities at higher oscillation amplitudes.
- Damping from aerodynamic resistance alters oscillation decay.

Without structured error visualization and statistical exploration, students and researchers struggle to determine whether discrepancies arise from systematic instrument bias, random environmental noise, or genuine experimental blunders (outliers). This project provides a computational framework to diagnose, quantify, and visualize these measurement errors.

---

## 3. Aim
To explore, validate, and visualize experimental measurement data from a simple pendulum system using Python, evaluating experimental time period variations against theoretical physics models, performing descriptive statistical error analysis, and building an end-to-end exploratory pipeline for experimental data verification.

---

## 4. Objectives
1. **Design and Construct Dataset:** Formulate a scientifically plausible, reproducible experimental dataset covering 8 distinct pendulum lengths with 10 repeated measurement trials each ($N = 80$).
2. **Data Exploration & Preprocessing:** Conduct foundational data sanity checks, missing value assessments, duplicate record inspections, and data type verifications.
3. **Error Modeling & Metrics Formulation (Phase 2):** Compute Absolute Error ($|T_{\text{exp}} - T_{\text{theo}}|$), Relative Error, and Percentage Error across all trials.
4. **Descriptive Statistical Analysis (Phase 2):** Calculate central tendency, dispersion (mean, standard deviation, variance), and interquartile ranges per length group.
5. **Outlier Detection (Phase 2):** Identify anomalies and extreme errors using Interquartile Range (IQR) and Z-score criteria.
6. **Exploratory Data Visualization (Phase 2):** Produce publication-quality plots (scatter comparison, error distributions, group boxplots, and residual charts).

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
- **Total Attributes (Variables):** 5 columns
- **Number of Length Groups:** 8 unique lengths ($0.20\,\text{m}, 0.30\,\text{m}, 0.40\,\text{m}, 0.50\,\text{m}, 0.60\,\text{m}, 0.70\,\text{m}, 0.80\,\text{m}, 1.00\,\text{m}$)
- **Trials per Length:** 10 trials
- **File Format:** CSV (`data/pendulum_experimental_data.csv`)

---

## 8. Attributes
| Attribute Name | Data Type | Description | Unit / Format |
| :--- | :--- | :--- | :--- |
| `Experiment_ID` | String / Object | Unique observation identifier | `EXP001` - `EXP080` |
| `Trial_Number` | Integer | Repetition trial index for a given length | $1 - 10$ |
| `Length_m` | Float | Measured length of the pendulum | Metres ($\text{m}$) |
| `Theoretical_Period_s` | Float | Theoretical period from $T = 2\pi\sqrt{L/g}$ | Seconds ($\text{s}$) |
| `Experimental_Period_s` | Float | Recorded experimental oscillation period | Seconds ($\text{s}$) |

*Note: In accordance with Phase 1 design guidelines, calculated error columns (`Absolute_Error`, `Relative_Error`, `Percentage_Error`) are excluded from raw data and computed in Phase 2.*

---

## 9. Technologies Used
- **Python (>= 3.10):** Core programming language
- **Pandas (>= 2.0.0):** Data manipulation, loading, tabular exploration, and aggregation
- **NumPy (>= 1.24.0):** Numerical computation and controlled random data synthesis
- **Matplotlib (>= 3.7.0):** Base charting and visualization engine
- **Seaborn (>= 0.12.0):** Statistical plots and visual theme management
- **Jupyter Notebook (>= 1.0.0):** Interactive exploratory analysis and documentation
- **Git & GitHub:** Version control, collaborative tracking, and project repository hosting

---

## 10. Project Structure
```
error-visualization-experimental-data/
│
├── data/
│   └── pendulum_experimental_data.csv       # Raw experimental dataset (80 records)
│
├── notebooks/
│   └── error_visualization.ipynb            # Jupyter Notebook with Phase 1 foundation
│
├── src/
│   ├── data_preprocessing.py                # Dataset generator, loader & validation script
│   ├── error_analysis.py                    # Error calculation & statistical metric functions
│   └── visualization.py                     # Plotting routines & visualization helpers
│
├── visualizations/                          # Output directory for exported figures
│
├── docs/                                    # Academic reports and documentation
│
├── README.md                                # Comprehensive project documentation
├── requirements.txt                         # Python dependencies
├── .gitignore                               # Git ignore configuration
└── LICENSE                                  # MIT Open-Source License
```

---

## 11. Methodology
1. **Dataset Synthesis & Parameterization:** Define physical lengths and calculate exact theoretical periods.
2. **Stochastic Variation Modeling:** Inject realistic normal measurement noise and controlled perturbation points.
3. **Data Quality Validation:** Execute automated tests checking dimensions, completeness, types, and physical validity (all $L > 0, T > 0$).
4. **Exploratory Inspection:** Load dataset into Jupyter Notebook and inspect tabular summaries, missing values, and distributions.
5. **Phase 2 Pipeline (Upcoming):** Compute error variables, group statistics, run IQR outlier filters, and generate diagnostic charts.

---

## 12. Current Phase
### Phase 1: Project Foundation & Initial Data Exploration (Completed)
- [x] Standard modular repository structure initialized.
- [x] Reproducible synthetic experimental dataset created (`80` observations, `5` raw attributes).
- [x] Comprehensive data validation module created (`src/data_preprocessing.py`).
- [x] Automated integrity checks executed: `80` records, `0` missing values, `0` duplicates, `100%` positive values.
- [x] Interactive Jupyter Notebook established (`notebooks/error_visualization.ipynb`) containing sections 1 to 13.
- [x] Phase 2 modular skeletons prepared (`src/error_analysis.py`, `src/visualization.py`).
- [x] Dependencies specified in `requirements.txt`.
- [x] Git configuration (`.gitignore`, `LICENSE`) finalized.

---

## 13. Future Analysis (Phase 2 Roadmap)
In Phase 2, the following analytical milestones will be implemented:
1. **Error Metrics Pipeline:** Compute Absolute Error, Relative Error, and Percentage Error columns.
2. **Descriptive Statistics:** Calculate mean experimental period, standard deviation, and variance grouped by length.
3. **Outlier Detection:** Apply IQR (Interquartile Range) and Z-score criteria to isolate human timing anomalies.
4. **Visualization Suite:**
   - Plot 1: Theoretical vs. Experimental Period Curve (Scatter & Line)
   - Plot 2: Absolute and Percentage Error Distributions (Histogram / KDE)
   - Plot 3: Period Distribution Across Length Groups (Box & Whisker Plots)
   - Plot 4: Error Residuals vs. Pendulum Length (Residual Scatter Plot)
   - Plot 5: Correlation Heatmap of Physical and Error Variables
5. **Key Findings & Interpretations:** Document insights on measurement precision, length-period non-linear scaling, and outlier patterns.

---

## 14. How to Run

### Step 1: Clone the Repository
```bash
git clone https://github.com/DineshMoorthy007/error-visualization-experimental-data.git
cd error-visualization-experimental-data
```

### Step 2: Set Up Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Dataset Validation
```bash
python src/data_preprocessing.py
```

### Step 5: Launch Jupyter Notebook
```bash
jupyter notebook notebooks/error_visualization.ipynb
```

---

## 15. GitHub Usage
- **Repository URL:** `https://github.com/DineshMoorthy007/error-visualization-experimental-data`
- **Branching Strategy:** Main branch for verified project phases (`main`).
- **Commit Format:** Conventional semantic commits (e.g., `feat: setup phase 1 foundation and synthetic dataset`, `docs: update readme`).

---

## 16. Sustainable Development Goals (SDG) Mapping

| SDG Goal | Target / Focus | Project Alignment |
| :--- | :--- | :--- |
| **SDG 4: Quality Education** | Target 4.4 (Technical and STEM Skills) | Enhances experiential STEM education by providing a reproducible computational framework for physics students to analyze experimental uncertainties and master data exploration techniques. |
| **SDG 9: Industry, Innovation, and Infrastructure** | Target 9.5 (Scientific Research & Quality Assurance) | Emphasizes rigorous measurement verification, error modeling, and data-driven anomaly detection critical for industrial sensor calibration and scientific experimentation. |

---

## 17. Disclaimer
This dataset is a **synthetically constructed educational experimental dataset** created for the *Data Exploration and Visualization* course project. While mathematically and physically modeled around the theoretical formula $T = 2\pi\sqrt{L/g}$ with realistic human reaction variance, the values were generated using computational algorithms and were not recorded in a physical laboratory session.
