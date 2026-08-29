"""
Error Analysis Module
=====================
Project: Error Visualization and Analysis of Experimental Data Using Python
Course: Data Exploration and Visualization

This module provides analytical functions for computing experimental error metrics,
group aggregations, and statistical outlier detection.
(Foundation created in Phase 1; core calculations executed in Phase 2)
"""

import pandas as pd
import numpy as np


def calculate_error_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes absolute error, relative error, and percentage error
    between experimental and theoretical period measurements.

    Formulas:
        Absolute Error   = |Experimental_Period_s - Theoretical_Period_s|
        Relative Error   = Absolute Error / Theoretical_Period_s
        Percentage Error = Relative Error * 100

    Parameters:
        df (pd.DataFrame): Dataset containing Theoretical_Period_s and Experimental_Period_s.

    Returns:
        pd.DataFrame: DataFrame augmented with error columns.
    """
    df_processed = df.copy()
    
    # Error computations (Phase 2 analysis pipeline)
    df_processed["Absolute_Error_s"] = (
        df_processed["Experimental_Period_s"] - df_processed["Theoretical_Period_s"]
    ).abs()
    
    df_processed["Relative_Error"] = (
        df_processed["Absolute_Error_s"] / df_processed["Theoretical_Period_s"]
    )
    
    df_processed["Percentage_Error"] = (
        df_processed["Relative_Error"] * 100.0
    )
    
    return df_processed


def compute_group_statistics(df: pd.DataFrame, group_col: str = "Length_m") -> pd.DataFrame:
    """
    Computes summary statistics (mean, std, min, max, variance) grouped by pendulum length.

    Parameters:
        df (pd.DataFrame): Experimental dataset.
        group_col (str): Column name to group by (default: 'Length_m').

    Returns:
        pd.DataFrame: Grouped descriptive statistics summary.
    """
    summary = df.groupby(group_col).agg(
        Theoretical_Period=("Theoretical_Period_s", "first"),
        Exp_Mean_Period=("Experimental_Period_s", "mean"),
        Exp_Std_Dev=("Experimental_Period_s", "std"),
        Exp_Min_Period=("Experimental_Period_s", "min"),
        Exp_Max_Period=("Experimental_Period_s", "max"),
        Trial_Count=("Trial_Number", "count")
    ).reset_index()
    
    return summary


def detect_outliers_iqr(df: pd.DataFrame, target_col: str = "Percentage_Error") -> pd.DataFrame:
    """
    Identifies experimental outliers using the Interquartile Range (IQR) method.

    Parameters:
        df (pd.DataFrame): Dataset containing the target error or measurement column.
        target_col (str): Column name to inspect for outliers.

    Returns:
        pd.DataFrame: Subset of records identified as outliers.
    """
    if target_col not in df.columns:
        raise ValueError(f"Column '{target_col}' not found in dataframe.")
        
    q1 = df[target_col].quantile(0.25)
    q3 = df[target_col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = df[(df[target_col] < lower_bound) | (df[target_col] > upper_bound)]
    return outliers
