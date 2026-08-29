"""
Error Analysis and Statistical Modeling Module
=============================================
Project: Error Visualization and Analysis of Experimental Data Using Python
Course: Data Exploration and Visualization

This module implements experimental error formulation, error classification,
Interquartile Range (IQR) outlier detection, comprehensive descriptive statistics,
length-wise group aggregations, and processed data export.
"""

import os
from typing import Dict, Any, Tuple, List, Optional
import numpy as np
import pandas as pd


def calculate_errors(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes algebraic error, absolute error, relative error, and percentage error
    between experimental time periods and theoretical predictions.

    Formulas:
        Error (s)            = Experimental_Period_s - Theoretical_Period_s
        Absolute Error (s)   = |Experimental_Period_s - Theoretical_Period_s|
        Relative Error       = Absolute_Error_s / Theoretical_Period_s
        Percentage Error (%) = Relative_Error * 100

    Parameters:
        df (pd.DataFrame): Dataset containing 'Theoretical_Period_s' and 'Experimental_Period_s'.

    Returns:
        pd.DataFrame: Enriched DataFrame with error metric columns.
    """
    df_calc = df.copy()

    df_calc["Error_s"] = (
        df_calc["Experimental_Period_s"] - df_calc["Theoretical_Period_s"]
    ).round(4)

    df_calc["Absolute_Error_s"] = (
        df_calc["Error_s"].abs()
    ).round(4)

    df_calc["Relative_Error"] = (
        df_calc["Absolute_Error_s"] / df_calc["Theoretical_Period_s"]
    ).round(6)

    df_calc["Percentage_Error"] = (
        df_calc["Relative_Error"] * 100.0
    ).round(4)

    return df_calc


def classify_errors(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Classifies observations into project-defined analytical error quality tiers:
    - Low Error:      Percentage Error < 1.0%
    - Moderate Error: 1.0% <= Percentage Error < 2.0%
    - High Error:     Percentage Error >= 2.0%

    Parameters:
        df (pd.DataFrame): Dataset containing 'Percentage_Error'.

    Returns:
        tuple: (df_with_category, category_distribution_summary_df)
    """
    df_classified = df.copy()

    conditions = [
        df_classified["Percentage_Error"] < 1.0,
        (df_classified["Percentage_Error"] >= 1.0) & (df_classified["Percentage_Error"] < 2.0),
        df_classified["Percentage_Error"] >= 2.0
    ]
    categories = ["Low Error (<1%)", "Moderate Error (1-2%)", "High Error (>=2%)"]

    df_classified["Error_Category"] = np.select(conditions, categories, default="Unclassified")

    # Generate category distribution table
    counts = df_classified["Error_Category"].value_counts().reindex(categories, fill_value=0)
    percentages = (counts / len(df_classified)) * 100.0

    dist_df = pd.DataFrame({
        "Error_Category": counts.index,
        "Observation_Count": counts.values,
        "Percentage_Share (%)": percentages.round(2).values
    })

    return df_classified, dist_df


def detect_outliers_iqr(
    df: pd.DataFrame,
    target_col: str = "Percentage_Error"
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Performs Interquartile Range (IQR) outlier detection on a target numerical column.
    Adds an 'Outlier_Flag' boolean column (True for potential outliers, False otherwise)
    without deleting any records.

    IQR Outlier Boundaries:
        IQR = Q3 - Q1
        Lower Bound = Q1 - 1.5 * IQR
        Upper Bound = Q3 + 1.5 * IQR

    Parameters:
        df (pd.DataFrame): Target dataframe.
        target_col (str): Column to evaluate for statistical anomalies.

    Returns:
        tuple: (df_with_flag, outlier_summary_dict)
    """
    df_out = df.copy()

    q1 = float(df_out[target_col].quantile(0.25))
    q3 = float(df_out[target_col].quantile(0.75))
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    is_outlier = (df_out[target_col] < lower_bound) | (df_out[target_col] > upper_bound)
    df_out["Outlier_Flag"] = is_outlier

    outlier_records = df_out[is_outlier]
    outlier_ids = outlier_records["Experiment_ID"].tolist() if "Experiment_ID" in df_out.columns else []

    summary = {
        "target_attribute": target_col,
        "Q1": round(q1, 4),
        "Q3": round(q3, 4),
        "IQR": round(iqr, 4),
        "lower_bound": round(lower_bound, 4),
        "upper_bound": round(upper_bound, 4),
        "outlier_count": int(is_outlier.sum()),
        "outlier_percentage": round(float(is_outlier.mean() * 100.0), 2),
        "outlier_experiment_ids": outlier_ids,
        "outlier_records": outlier_records
    }

    return df_out, summary


def calculate_descriptive_statistics(
    df: pd.DataFrame,
    columns: Optional[List[str]] = None
) -> pd.DataFrame:
    """
    Computes comprehensive descriptive statistical metrics required for academic analysis:
    - Mean
    - Median (Q2)
    - Mode (with continuous variable context)
    - Minimum
    - Maximum
    - Range (Max - Min)
    - Variance (Sample Variance)
    - Standard Deviation (Sample Std)
    - First Quartile (Q1)
    - Second Quartile / Median (Q2)
    - Third Quartile (Q3)

    Parameters:
        df (pd.DataFrame): Dataset containing target variables.
        columns (list, optional): Columns to analyze. Defaults to primary experimental variables.

    Returns:
        pd.DataFrame: Formatted statistical summary table.
    """
    if columns is None:
        columns = ["Experimental_Period_s", "Absolute_Error_s", "Percentage_Error"]

    stats_list = []

    for col in columns:
        if col not in df.columns:
            continue

        series = df[col].dropna()
        mean_val = series.mean()
        median_val = series.median()
        min_val = series.min()
        max_val = series.max()
        range_val = max_val - min_val
        var_val = series.var()
        std_val = series.std()
        q1_val = series.quantile(0.25)
        q2_val = series.quantile(0.50)
        q3_val = series.quantile(0.75)

        # Mode calculation: For continuous experimental floating points,
        # note exact mode vs rounded empirical mode
        mode_series = series.round(2).mode()
        mode_str = f"{mode_series.iloc[0]:.2f} (rounded)" if not mode_series.empty else "N/A"

        stats_list.append({
            "Metric_Variable": col,
            "Mean": round(mean_val, 4),
            "Median (Q2)": round(median_val, 4),
            "Mode": mode_str,
            "Minimum": round(min_val, 4),
            "Maximum": round(max_val, 4),
            "Range": round(range_val, 4),
            "Variance": round(var_val, 6),
            "Std_Deviation": round(std_val, 4),
            "Q1 (25th %)": round(q1_val, 4),
            "Q2 (50th %)": round(q2_val, 4),
            "Q3 (75th %)": round(q3_val, 4)
        })

    return pd.DataFrame(stats_list)


def generate_length_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates a grouped statistical summary aggregated by pendulum length (Length_m).

    Metrics computed per length:
    - Number of Observations
    - Mean Experimental Period (s)
    - Mean Theoretical Period (s)
    - Mean Absolute Error (s)
    - Mean Percentage Error (%)
    - Standard Deviation of Experimental Period (s)
    - Maximum Percentage Error (%)

    Parameters:
        df (pd.DataFrame): Enriched experimental dataset.

    Returns:
        pd.DataFrame: Grouped summary table.
    """
    summary = df.groupby("Length_m").agg(
        Observation_Count=("Experiment_ID", "count"),
        Mean_Exp_Period_s=("Experimental_Period_s", "mean"),
        Mean_Theo_Period_s=("Theoretical_Period_s", "first"),
        Mean_Absolute_Error_s=("Absolute_Error_s", "mean"),
        Mean_Percentage_Error=("Percentage_Error", "mean"),
        Std_Exp_Period_s=("Experimental_Period_s", "std"),
        Max_Percentage_Error=("Percentage_Error", "max")
    ).reset_index()

    # Round columns for presentation clarity
    summary["Length_m"] = summary["Length_m"].round(2)
    summary["Mean_Exp_Period_s"] = summary["Mean_Exp_Period_s"].round(4)
    summary["Mean_Theo_Period_s"] = summary["Mean_Theo_Period_s"].round(4)
    summary["Mean_Absolute_Error_s"] = summary["Mean_Absolute_Error_s"].round(4)
    summary["Mean_Percentage_Error"] = summary["Mean_Percentage_Error"].round(4)
    summary["Std_Exp_Period_s"] = summary["Std_Exp_Period_s"].round(4)
    summary["Max_Percentage_Error"] = summary["Max_Percentage_Error"].round(4)

    return summary


def save_processed_data(
    df: pd.DataFrame,
    output_path: str = "data/processed/pendulum_processed_data.csv"
) -> str:
    """
    Saves the preprocessed, error-augmented dataset to the processed data directory,
    ensuring the original raw CSV dataset remains completely untouched.

    Parameters:
        df (pd.DataFrame): Processed dataframe.
        output_path (str): File destination path.

    Returns:
        str: Absolute destination path.
    """
    if not os.path.isabs(output_path):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, ".."))
        abs_output_path = os.path.join(project_root, output_path)
    else:
        abs_output_path = output_path

    os.makedirs(os.path.dirname(abs_output_path), exist_ok=True)
    df.to_csv(abs_output_path, index=False)
    print(f"[+] Processed dataset saved successfully to: {abs_output_path}")
    return abs_output_path


if __name__ == "__main__":
    from data_preprocessing import load_dataset, preprocess_data

    raw_df = load_dataset()
    clean_df, _ = preprocess_data(raw_df)

    # 1. Error calculation
    df_with_errors = calculate_errors(clean_df)

    # 2. Error classification
    df_classified, dist_df = classify_errors(df_with_errors)

    # 3. Outlier detection
    df_processed, outlier_info = detect_outliers_iqr(df_classified, target_col="Percentage_Error")

    # 4. Descriptive statistics
    stats_df = calculate_descriptive_statistics(df_processed)

    # 5. Length summary
    length_summary_df = generate_length_summary(df_processed)

    # 6. Save processed dataset
    save_processed_data(df_processed)

    print("\n=== Outlier Summary ===")
    print(f"Target: {outlier_info['target_attribute']}")
    print(f"IQR: {outlier_info['IQR']}, Bounds: [{outlier_info['lower_bound']}, {outlier_info['upper_bound']}]")
    print(f"Outlier count: {outlier_info['outlier_count']} ({outlier_info['outlier_experiment_ids']})")

    print("\n=== Error Category Distribution ===")
    print(dist_df.to_string(index=False))

    print("\n=== Descriptive Statistics ===")
    print(stats_df.to_string(index=False))

    print("\n=== Length-wise Summary ===")
    print(length_summary_df.to_string(index=False))
