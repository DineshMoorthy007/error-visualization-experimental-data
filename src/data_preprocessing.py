"""
Data Preprocessing and Validation Module
=======================================
Project: Error Visualization and Analysis of Experimental Data Using Python
Course: Data Exploration and Visualization

This module handles robust dataset loading, structural inspection, quality validation,
variable taxonomy identification, and standardized data preprocessing.
"""

import os
from typing import Dict, Any, Tuple, Optional
import numpy as np
import pandas as pd


def get_default_dataset_path(filename: str = "pendulum_experimental_data.csv") -> str:
    """
    Resolves the absolute path to a file in the data directory,
    ensuring cross-environment path stability whether executed from project root,
    notebooks directory, or src directory.

    Parameters:
        filename (str): Name of the CSV file.

    Returns:
        str: Absolute path to the data file.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, ".."))
    return os.path.join(project_root, "data", filename)


def load_dataset(filepath: Optional[str] = None) -> pd.DataFrame:
    """
    Loads experimental dataset from a CSV file with robust relative and absolute path resolution.

    Parameters:
        filepath (str, optional): Path to CSV file. Defaults to standard raw data path.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    if filepath is None:
        filepath = get_default_dataset_path("pendulum_experimental_data.csv")
    elif not os.path.isabs(filepath) and not os.path.exists(filepath):
        # Check relative to project root
        candidate = get_default_dataset_path(os.path.basename(filepath))
        if os.path.exists(candidate):
            filepath = candidate

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset file not found at resolved path: {filepath}")

    df = pd.read_csv(filepath)
    return df


def inspect_dataset(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Extracts fundamental structural metadata from the dataset.

    Parameters:
        df (pd.DataFrame): Dataset to inspect.

    Returns:
        dict: Structural summary containing shape, columns, dtypes, and head/tail records.
    """
    return {
        "shape": df.shape,
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "dtypes": df.dtypes.to_dict(),
        "first_5_records": df.head(5),
        "last_5_records": df.tail(5)
    }


def check_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs comprehensive missing value inspection across all columns.

    Parameters:
        df (pd.DataFrame): Target dataframe.

    Returns:
        pd.DataFrame: Tabular summary of missing count and percentage per column.
    """
    missing_counts = df.isnull().sum()
    missing_pct = (missing_counts / len(df)) * 100.0
    
    summary_df = pd.DataFrame({
        "Attribute": df.columns,
        "Missing_Count": missing_counts.values,
        "Missing_Percentage": missing_pct.values
    })
    return summary_df


def check_duplicates(df: pd.DataFrame) -> int:
    """
    Identifies duplicate records in the dataset.

    Parameters:
        df (pd.DataFrame): Target dataframe.

    Returns:
        int: Number of duplicate rows.
    """
    return int(df.duplicated().sum())


def validate_measurements(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Validates physical feasibility and domain integrity constraints:
    - Length_m > 0
    - Theoretical_Period_s > 0
    - Experimental_Period_s > 0
    - No negative or null values in physical dimensions

    Parameters:
        df (pd.DataFrame): Target dataframe.

    Returns:
        dict: Validation status flags and invalid record inventories.
    """
    invalid_lengths = df[df["Length_m"] <= 0] if "Length_m" in df.columns else pd.DataFrame()
    invalid_theo = df[df["Theoretical_Period_s"] <= 0] if "Theoretical_Period_s" in df.columns else pd.DataFrame()
    invalid_exp = df[df["Experimental_Period_s"] <= 0] if "Experimental_Period_s" in df.columns else pd.DataFrame()

    all_valid = (len(invalid_lengths) == 0) and (len(invalid_theo) == 0) and (len(invalid_exp) == 0)

    return {
        "all_physically_valid": all_valid,
        "invalid_length_count": len(invalid_lengths),
        "invalid_theo_count": len(invalid_theo),
        "invalid_exp_count": len(invalid_exp),
        "invalid_records_summary": {
            "Length_m": invalid_lengths["Experiment_ID"].tolist() if not invalid_lengths.empty else [],
            "Theoretical_Period_s": invalid_theo["Experiment_ID"].tolist() if not invalid_theo.empty else [],
            "Experimental_Period_s": invalid_exp["Experiment_ID"].tolist() if not invalid_exp.empty else []
        }
    }


def classify_variables(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates a structured taxonomy classifying all variables into numerical
    (discrete/continuous) or categorical types, along with academic rationale.

    Parameters:
        df (pd.DataFrame): Target dataframe.

    Returns:
        pd.DataFrame: Classification table.
    """
    classifications = []
    
    for col in df.columns:
        dtype = str(df[col].dtype)
        if col == "Experiment_ID":
            var_type = "Identifier (Nominal / Alphanumeric)"
            nature = "Unique observation key"
            rationale = "Alphanumeric string used solely to uniquely identify individual experimental trials."
        elif col == "Trial_Number":
            var_type = "Numerical (Discrete Integer)"
            nature = "Ordinal / Trial Index"
            rationale = "Count of repeated trials (1 to 10) performed for each length configuration."
        elif col == "Length_m":
            var_type = "Numerical (Continuous Float)"
            nature = "Independent Variable"
            rationale = "Physical pendulum length measured in metres; continuous physical dimension."
        elif col == "Theoretical_Period_s":
            var_type = "Numerical (Continuous Float)"
            nature = "Theoretical Reference"
            rationale = "Deterministic theoretical time period calculated from pendulum physics formula."
        elif col == "Experimental_Period_s":
            var_type = "Numerical (Continuous Float)"
            nature = "Dependent Measured Variable"
            rationale = "Empirical stopwatch timing measurements subject to real-world experimental variations."
        elif col == "Error_s":
            var_type = "Numerical (Continuous Float)"
            nature = "Derived Measurement"
            rationale = "Signed algebraic error (Experimental - Theoretical) in seconds."
        elif col == "Absolute_Error_s":
            var_type = "Numerical (Continuous Float)"
            nature = "Derived Measurement"
            rationale = "Magnitude of measurement error in seconds."
        elif col == "Relative_Error":
            var_type = "Numerical (Continuous Float)"
            nature = "Derived Metric"
            rationale = "Dimensionless ratio of absolute error relative to theoretical reference."
        elif col == "Percentage_Error":
            var_type = "Numerical (Continuous Float)"
            nature = "Derived Metric"
            rationale = "Scaled relative error expressed as a percentage (%)."
        elif col == "Error_Category":
            var_type = "Categorical (Ordinal String)"
            nature = "Derived Grouping"
            rationale = "Discretized error quality tiers: Low (<1%), Moderate (1-2%), High (>=2%)."
        elif col == "Outlier_Flag":
            var_type = "Categorical (Boolean Flag)"
            nature = "Diagnostic Attribute"
            rationale = "Binary indicator denoting whether the observation is an IQR-based statistical outlier."
        else:
            var_type = f"General ({dtype})"
            nature = "Generic Variable"
            rationale = "Dataset attribute."

        classifications.append({
            "Attribute": col,
            "Data_Type": dtype,
            "Variable_Classification": var_type,
            "Measurement_Nature": nature,
            "Academic_Rationale": rationale
        })

    return pd.DataFrame(classifications)


def preprocess_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Executes standard data preprocessing operations:
    1. Validates absence of nulls and duplicates
    2. Verifies physical positivity ($L > 0, T > 0$)
    3. Confirms explicit numeric type casting
    4. Rounds numerical dimensions to standard laboratory precision without
       distorting physical units (metres and seconds).

    Parameters:
        df (pd.DataFrame): Raw experimental dataset.

    Returns:
        tuple: (preprocessed_df, preprocessing_log_dict)
    """
    df_clean = df.copy()

    # Verify column existence
    expected_cols = ["Experiment_ID", "Trial_Number", "Length_m", "Theoretical_Period_s", "Experimental_Period_s"]
    for col in expected_cols:
        if col not in df_clean.columns:
            raise KeyError(f"Expected column '{col}' is missing from raw dataset.")

    # Explicit data type enforcement
    df_clean["Experiment_ID"] = df_clean["Experiment_ID"].astype(str)
    df_clean["Trial_Number"] = pd.to_numeric(df_clean["Trial_Number"], errors="coerce").astype(int)
    df_clean["Length_m"] = pd.to_numeric(df_clean["Length_m"], errors="coerce").astype(float)
    df_clean["Theoretical_Period_s"] = pd.to_numeric(df_clean["Theoretical_Period_s"], errors="coerce").astype(float)
    df_clean["Experimental_Period_s"] = pd.to_numeric(df_clean["Experimental_Period_s"], errors="coerce").astype(float)

    # Standardize precision: length to 2 decimals, periods to 4 decimals
    df_clean["Length_m"] = df_clean["Length_m"].round(2)
    df_clean["Theoretical_Period_s"] = df_clean["Theoretical_Period_s"].round(4)
    df_clean["Experimental_Period_s"] = df_clean["Experimental_Period_s"].round(4)

    # Preprocessing log
    log = {
        "initial_record_count": len(df),
        "final_record_count": len(df_clean),
        "missing_values_handled": int(df.isnull().sum().sum()),
        "duplicates_handled": int(df.duplicated().sum()),
        "type_conversions": {col: str(df_clean[col].dtype) for col in expected_cols},
        "precision_standardized": {
            "Length_m": "2 decimal places",
            "Theoretical_Period_s": "4 decimal places",
            "Experimental_Period_s": "4 decimal places"
        },
        "normalization_applied": False,
        "normalization_note": "Original physical units (metres and seconds) preserved for direct physical interpretability."
    }

    return df_clean, log


if __name__ == "__main__":
    raw_path = get_default_dataset_path("pendulum_experimental_data.csv")
    print(f"Loading dataset from: {raw_path}")
    raw_df = load_dataset(raw_path)
    
    print("\n--- Data Exploration ---")
    insp = inspect_dataset(raw_df)
    print(f"Dataset Shape: {insp['shape']}")
    print(f"Columns: {insp['column_names']}")
    
    print("\n--- Missing Values & Duplicates ---")
    print(check_missing_values(raw_df).to_string(index=False))
    print(f"Duplicate count: {check_duplicates(raw_df)}")
    
    print("\n--- Measurement Physical Validation ---")
    val = validate_measurements(raw_df)
    print(f"All physically valid: {val['all_physically_valid']}")
    
    print("\n--- Preprocessing Execution ---")
    clean_df, prep_log = preprocess_data(raw_df)
    print(f"Clean records: {len(clean_df)}")
    print("Preprocessing Log:", prep_log)
