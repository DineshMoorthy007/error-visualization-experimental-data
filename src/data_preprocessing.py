"""
Data Preprocessing and Validation Module
=======================================
Project: Error Visualization and Analysis of Experimental Data Using Python
Course: Data Exploration and Visualization

This module handles dataset loading, reproducible experimental dataset generation,
and comprehensive integrity validation for simple pendulum measurements.
"""

import os
import math
import numpy as np
import pandas as pd


def calculate_theoretical_period(length_m: float, g: float = 9.81) -> float:
    """
    Calculates theoretical period of a simple pendulum: T = 2 * pi * sqrt(L / g)

    Parameters:
        length_m (float): Pendulum length in meters.
        g (float): Acceleration due to gravity in m/s^2 (default: 9.81).

    Returns:
        float: Theoretical period in seconds.
    """
    if length_m <= 0:
        raise ValueError("Pendulum length must be strictly positive.")
    return 2.0 * math.pi * math.sqrt(length_m / g)


def generate_pendulum_dataset(
    output_path: str = "data/pendulum_experimental_data.csv",
    random_state: int = 42
) -> pd.DataFrame:
    """
    Generates a scientifically plausible, reproducible experimental dataset
    for a simple pendulum experiment across multiple lengths and trials.

    Parameters:
        output_path (str): Destination path for CSV export.
        random_state (int): Seed for NumPy random number generator.

    Returns:
        pd.DataFrame: Generated dataset containing raw experimental observations.
    """
    np.random.seed(random_state)

    lengths = [0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 1.00]
    trials_per_length = 10
    records = []

    exp_counter = 1
    for length in lengths:
        t_theo = calculate_theoretical_period(length)

        for trial in range(1, trials_per_length + 1):
            exp_id = f"EXP{exp_counter:03d}"

            # Base realistic measurement variation (human reaction time + slight stopwatch jitter)
            # Standard deviation ~ 0.022s with a subtle positive reaction lag of +0.008s
            random_noise = np.random.normal(loc=0.008, scale=0.022)

            # Introduce controlled realistic outlier perturbations on specific trials
            # to enable meaningful outlier detection in Phase 2
            outlier_shift = 0.0
            if exp_counter == 14:   # Length 0.30m, Trial 4: human reaction delay
                outlier_shift = 0.125
            elif exp_counter == 38: # Length 0.50m, Trial 8: premature stopwatch press
                outlier_shift = -0.095
            elif exp_counter == 55: # Length 0.70m, Trial 5: slight swing amplitude disturbance
                outlier_shift = 0.142
            elif exp_counter == 72: # Length 1.00m, Trial 2: timing error
                outlier_shift = -0.118

            t_exp = t_theo + random_noise + outlier_shift

            # Ensure all values remain strictly positive and realistic
            t_exp = max(t_exp, 0.1)

            records.append({
                "Experiment_ID": exp_id,
                "Trial_Number": trial,
                "Length_m": round(length, 2),
                "Theoretical_Period_s": round(t_theo, 4),
                "Experimental_Period_s": round(t_exp, 4)
            })

            exp_counter += 1

    df = pd.DataFrame(records)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[+] Dataset successfully generated and saved to: {output_path}")
    return df


def load_dataset(filepath: str = "data/pendulum_experimental_data.csv") -> pd.DataFrame:
    """
    Loads experimental dataset from a CSV file.

    Parameters:
        filepath (str): Path to CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset file not found at: {filepath}")
    return pd.read_csv(filepath)


def validate_dataset(df: pd.DataFrame) -> dict:
    """
    Performs comprehensive structural and statistical integrity validation on the dataset.

    Validation Checks:
    1. Total record count
    2. Total attribute count
    3. Required column presence
    4. Data types
    5. Missing values
    6. Duplicate records
    7. Positive value validation (Length_m > 0, Theoretical_Period_s > 0, Experimental_Period_s > 0)
    8. Minimum and maximum ranges
    9. Descriptive statistics

    Parameters:
        df (pd.DataFrame): Dataset to validate.

    Returns:
        dict: Validation results and summary metrics.
    """
    expected_columns = [
        "Experiment_ID",
        "Trial_Number",
        "Length_m",
        "Theoretical_Period_s",
        "Experimental_Period_s"
    ]

    total_records = len(df)
    total_attributes = len(df.columns)
    missing_values = int(df.isnull().sum().sum())
    duplicate_records = int(df.duplicated().sum())

    missing_cols = [col for col in expected_columns if col not in df.columns]
    has_expected_cols = len(missing_cols) == 0

    all_lengths_positive = bool((df["Length_m"] > 0).all()) if "Length_m" in df.columns else False
    all_theo_positive = bool((df["Theoretical_Period_s"] > 0).all()) if "Theoretical_Period_s" in df.columns else False
    all_exp_positive = bool((df["Experimental_Period_s"] > 0).all()) if "Experimental_Period_s" in df.columns else False

    validation_passed = (
        total_records > 0
        and has_expected_cols
        and missing_values == 0
        and duplicate_records == 0
        and all_lengths_positive
        and all_theo_positive
        and all_exp_positive
    )

    results = {
        "validation_passed": validation_passed,
        "total_records": total_records,
        "total_attributes": total_attributes,
        "columns": list(df.columns),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "missing_values_per_col": df.isnull().sum().to_dict(),
        "total_missing_values": missing_values,
        "duplicate_records": duplicate_records,
        "lengths_positive": all_lengths_positive,
        "theoretical_periods_positive": all_theo_positive,
        "experimental_periods_positive": all_exp_positive,
        "length_range": (float(df["Length_m"].min()), float(df["Length_m"].max())),
        "theoretical_period_range": (float(df["Theoretical_Period_s"].min()), float(df["Theoretical_Period_s"].max())),
        "experimental_period_range": (float(df["Experimental_Period_s"].min()), float(df["Experimental_Period_s"].max())),
        "unique_lengths": sorted(df["Length_m"].unique().tolist())
    }

    return results


def print_validation_report(results: dict, df: pd.DataFrame) -> None:
    """
    Prints a formatted, readable validation report to the console.
    """
    print("\n" + "=" * 65)
    print("      EXPERIMENTAL DATASET VALIDATION REPORT - PHASE 1")
    print("=" * 65)
    status_str = "PASSED [SUCCESS]" if results["validation_passed"] else "FAILED [ERROR]"
    print(f"Overall Status: {status_str}\n")
    print(f"1. Total Records (Rows)      : {results['total_records']}")
    print(f"2. Total Attributes (Cols)   : {results['total_attributes']}")
    print(f"3. Column Names              : {', '.join(results['columns'])}")
    print(f"4. Missing Values (Total)    : {results['total_missing_values']}")
    print(f"5. Duplicate Records         : {results['duplicate_records']}")
    print(f"6. Unique Pendulum Lengths   : {results['unique_lengths']}")
    print(f"7. Length_m Range            : [{results['length_range'][0]:.2f}, {results['length_range'][1]:.2f}] m (All Positive: {results['lengths_positive']})")
    print(f"8. Theoretical Period Range  : [{results['theoretical_period_range'][0]:.4f}, {results['theoretical_period_range'][1]:.4f}] s (All Positive: {results['theoretical_periods_positive']})")
    print(f"9. Experimental Period Range : [{results['experimental_period_range'][0]:.4f}, {results['experimental_period_range'][1]:.4f}] s (All Positive: {results['experimental_periods_positive']})")
    print("\nAttribute Data Types:")
    for col, dtype in results["dtypes"].items():
        print(f"   - {col:25s}: {dtype}")
    print("\nDescriptive Statistical Summary:")
    print("-" * 65)
    print(df.describe().to_string())
    print("=" * 65 + "\n")


if __name__ == "__main__":
    csv_file = os.path.join(os.path.dirname(__file__), "..", "data", "pendulum_experimental_data.csv")
    csv_file = os.path.abspath(csv_file)

    # Generate dataset
    df_generated = generate_pendulum_dataset(csv_file, random_state=42)

    # Validate dataset
    df_loaded = load_dataset(csv_file)
    val_results = validate_dataset(df_loaded)
    print_validation_report(val_results, df_loaded)
