"""
Data Visualization Module
=========================
Project: Error Visualization and Analysis of Experimental Data Using Python
Course: Data Exploration and Visualization

This module generates publication-quality academic visualizations using Matplotlib
and Seaborn for simple pendulum experimental data exploration and error analysis.
"""

import os
from typing import Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def set_academic_style():
    """
    Configures a cohesive, publication-quality academic styling theme
    with crisp typography, clean gridlines, and high figure DPI.
    """
    sns.set_theme(style="whitegrid", font_scale=1.05)
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica", "Calibri"],
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,
        "axes.labelweight": "semibold",
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "legend.title_fontsize": 10,
        "figure.titlesize": 14,
        "figure.titleweight": "bold",
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "savefig.bbox": "tight"
    })


def plot_experimental_vs_theoretical(
    df: pd.DataFrame,
    save_path: str = "visualizations/01_experimental_vs_theoretical_line.png"
) -> plt.Figure:
    """
    Visualization 1 — Line Chart: Experimental vs Theoretical Pendulum Period.
    Compares the mean experimental period against the theoretical physics prediction.
    """
    set_academic_style()
    fig, ax = plt.subplots(figsize=(9, 5.5))

    # Calculate length-wise aggregation
    grouped = df.groupby("Length_m").agg(
        Mean_Exp_Period=("Experimental_Period_s", "mean"),
        Std_Exp_Period=("Experimental_Period_s", "std"),
        Theoretical_Period=("Theoretical_Period_s", "first")
    ).reset_index().sort_values("Length_m")

    # Generate smooth theoretical curve
    lengths_dense = np.linspace(0.15, 1.05, 200)
    theoretical_dense = 2.0 * np.pi * np.sqrt(lengths_dense / 9.81)

    # Plot smooth theoretical line
    ax.plot(
        lengths_dense,
        theoretical_dense,
        color="#1f77b4",
        linestyle="--",
        linewidth=2.2,
        label=r"Theoretical Model: $T = 2\pi\sqrt{L/g}$ ($g=9.81\,\mathrm{m/s^2}$)"
    )

    # Plot aggregated mean experimental line with error bars
    ax.errorbar(
        grouped["Length_m"],
        grouped["Mean_Exp_Period"],
        yerr=grouped["Std_Exp_Period"],
        fmt="o-",
        color="#d62728",
        ecolor="#7f7f7f",
        elinewidth=1.2,
        capsize=4,
        capthick=1.2,
        markersize=6.5,
        linewidth=1.8,
        label=r"Mean Experimental Period $\pm 1\,\mathrm{SD}$"
    )

    ax.set_title("Experimental vs Theoretical Pendulum Period", pad=12)
    ax.set_xlabel("Pendulum Length (m)")
    ax.set_ylabel("Time Period (s)")
    ax.set_xlim(0.15, 1.05)
    ax.set_ylim(0.75, 2.15)
    ax.legend(loc="upper left", frameon=True, framealpha=0.9)
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        print(f"[+] Saved: {save_path}")

    return fig


def plot_percentage_error_bar(
    df: pd.DataFrame,
    save_path: str = "visualizations/02_percentage_error_bar.png"
) -> plt.Figure:
    """
    Visualization 2 — Bar Chart: Average Percentage Error by Pendulum Length.
    Displays average experimental percentage error across physical pendulum configurations.
    """
    set_academic_style()
    fig, ax = plt.subplots(figsize=(9, 5.5))

    grouped = df.groupby("Length_m")["Percentage_Error"].mean().reset_index().sort_values("Length_m")
    
    # Formatted x-axis labels
    x_labels = [f"{length:.2f} m" for length in grouped["Length_m"]]
    bars = ax.bar(
        x_labels,
        grouped["Percentage_Error"],
        color="#2b5c8f",
        edgecolor="#1a365d",
        width=0.55,
        alpha=0.88
    )

    # Add numeric data labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height:.2f}%",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9.5,
            fontweight="bold",
            color="#1a365d"
        )

    # Overall dataset average reference line
    overall_mean = df["Percentage_Error"].mean()
    ax.axhline(
        overall_mean,
        color="#d9534f",
        linestyle="--",
        linewidth=1.5,
        label=f"Dataset Overall Mean ({overall_mean:.2f}%)"
    )

    ax.set_title("Average Percentage Error by Pendulum Length", pad=12)
    ax.set_xlabel("Pendulum Length (m)")
    ax.set_ylabel("Mean Percentage Error (%)")
    ax.set_ylim(0, max(grouped["Percentage_Error"]) * 1.25)
    ax.legend(loc="upper right", frameon=True)
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        print(f"[+] Saved: {save_path}")

    return fig


def plot_error_category_pie(
    df: pd.DataFrame,
    save_path: str = "visualizations/03_error_category_pie.png"
) -> plt.Figure:
    """
    Visualization 3 — Pie Chart: Distribution of Experimental Error Categories.
    Shows the proportion and frequency of observations in Low, Moderate, and High Error tiers.
    """
    set_academic_style()
    fig, ax = plt.subplots(figsize=(8, 6))

    categories = ["Low Error (<1%)", "Moderate Error (1-2%)", "High Error (>=2%)"]
    counts = df["Error_Category"].value_counts().reindex(categories, fill_value=0)
    
    # Curated academic color palette: green for low error, amber for moderate, coral for high
    colors = ["#2ca02c", "#ff7f0e", "#d62728"]
    explode = (0.04, 0.02, 0.06)

    def format_autopct(pct):
        total = sum(counts)
        val = int(round(pct * total / 100.0))
        return f"{pct:.1f}%\n({val} obs)"

    wedges, texts, *autotexts_list = ax.pie(
        counts,
        labels=categories,
        autopct=format_autopct,
        startangle=140,
        colors=colors,
        explode=explode,
        textprops={'fontsize': 10, 'fontweight': 'medium'},
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5, 'antialiased': True}
    )
    autotexts = autotexts_list[0] if autotexts_list else []

    for autotext in autotexts:
        autotext.set_color("white")
        autotext.set_fontsize(9.5)
        autotext.set_weight("bold")

    ax.set_title("Distribution of Experimental Error Categories", pad=14)
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        print(f"[+] Saved: {save_path}")

    return fig


def plot_experimental_period_boxplot(
    df: pd.DataFrame,
    save_path: str = "visualizations/04_experimental_period_boxplot.png"
) -> plt.Figure:
    """
    Visualization 4 — Box Plot: Distribution of Experimental Period by Pendulum Length.
    Displays medians, interquartile ranges, spreads, and potential outliers per length.
    """
    set_academic_style()
    fig, ax = plt.subplots(figsize=(10, 6))

    lengths_sorted = sorted(df["Length_m"].unique())
    data_by_length = [df[df["Length_m"] == l]["Experimental_Period_s"].values for l in lengths_sorted]
    theo_by_length = [df[df["Length_m"] == l]["Theoretical_Period_s"].iloc[0] for l in lengths_sorted]

    box = ax.boxplot(
        data_by_length,
        tick_labels=[f"{l:.2f} m" for l in lengths_sorted],
        patch_artist=True,
        showmeans=True,
        meanline=True,
        flierprops=dict(marker="o", markerfacecolor="#d62728", markersize=6.5, linestyle="none", markeredgecolor="black"),
        medianprops=dict(color="#1a365d", linewidth=2.0),
        meanprops=dict(color="#2ca02c", linestyle="--", linewidth=1.5),
        boxprops=dict(facecolor="#dbeafe", color="#1e3a8a", linewidth=1.2),
        whiskerprops=dict(color="#1e3a8a", linewidth=1.2),
        capprops=dict(color="#1e3a8a", linewidth=1.2)
    )

    # Plot theoretical point reference markers
    ax.scatter(
        range(1, len(lengths_sorted) + 1),
        theo_by_length,
        color="#b91c1c",
        marker="D",
        s=45,
        zorder=5,
        label=r"Theoretical Reference $T_{\mathrm{theo}}$"
    )

    # Custom legend items
    ax.plot([], [], color="#1a365d", linewidth=2, label="Median Period")
    ax.plot([], [], color="#2ca02c", linestyle="--", linewidth=1.5, label="Mean Period")
    ax.scatter([], [], marker="o", color="#d62728", s=40, label="Statistical Outlier Point")

    ax.set_title("Distribution of Experimental Period by Pendulum Length", pad=12)
    ax.set_xlabel("Pendulum Length (m)")
    ax.set_ylabel("Experimental Period (s)")
    ax.legend(loc="upper left", frameon=True, framealpha=0.9)
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        print(f"[+] Saved: {save_path}")

    return fig


def plot_length_vs_period_scatter(
    df: pd.DataFrame,
    save_path: str = "visualizations/05_length_vs_period_scatter.png"
) -> plt.Figure:
    """
    Visualization 5 — Scatter Plot: Pendulum Length vs Experimental Period.
    Plots all 80 individual experimental trials against theoretical curve and empirical trend.
    """
    set_academic_style()
    fig, ax = plt.subplots(figsize=(9, 5.5))

    # Plot inlier observations
    inliers = df[~df["Outlier_Flag"]]
    outliers = df[df["Outlier_Flag"]]

    ax.scatter(
        inliers["Length_m"],
        inliers["Experimental_Period_s"],
        color="#2563eb",
        alpha=0.75,
        edgecolors="#1e3a8a",
        linewidth=0.8,
        s=55,
        label=f"Experimental Trials (Inliers, n={len(inliers)})"
    )

    # Plot outlier observations with distinct highlighting
    if len(outliers) > 0:
        ax.scatter(
            outliers["Length_m"],
            outliers["Experimental_Period_s"],
            color="#dc2626",
            alpha=0.95,
            edgecolors="#7f1d1d",
            linewidth=1.2,
            s=75,
            marker="^",
            label=f"Flagged Outlier Trials (n={len(outliers)})"
        )

    # Theoretical curve
    lengths_dense = np.linspace(0.15, 1.05, 200)
    theoretical_dense = 2.0 * np.pi * np.sqrt(lengths_dense / 9.81)
    ax.plot(
        lengths_dense,
        theoretical_dense,
        color="#0f172a",
        linestyle="--",
        linewidth=2.0,
        label=r"Theoretical Reference: $T = 2\pi\sqrt{L/g}$"
    )

    ax.set_title("Pendulum Length vs Experimental Period", pad=12)
    ax.set_xlabel("Pendulum Length (m)")
    ax.set_ylabel("Experimental Period (s)")
    ax.set_xlim(0.15, 1.05)
    ax.set_ylim(0.75, 2.15)
    ax.legend(loc="upper left", frameon=True, framealpha=0.9)
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        print(f"[+] Saved: {save_path}")

    return fig


def plot_error_distribution(
    df: pd.DataFrame,
    save_path: str = "visualizations/06_error_distribution_histogram.png"
) -> plt.Figure:
    """
    Visualization 6 — Histogram: Distribution of Percentage Error.
    Visualizes frequency distribution of percentage error across observations.
    """
    set_academic_style()
    fig, ax = plt.subplots(figsize=(9, 5.5))

    mean_err = df["Percentage_Error"].mean()
    median_err = df["Percentage_Error"].median()

    # Histogram with KDE
    sns.histplot(
        df["Percentage_Error"],
        bins=16,
        kde=True,
        color="#3b82f6",
        edgecolor="#1e3a8a",
        alpha=0.65,
        ax=ax
    )

    # Vertical reference lines for central tendency
    ax.axvline(
        mean_err,
        color="#dc2626",
        linestyle="--",
        linewidth=2.0,
        label=f"Mean Percentage Error ({mean_err:.2f}%)"
    )
    ax.axvline(
        median_err,
        color="#16a34a",
        linestyle="-.",
        linewidth=2.0,
        label=f"Median Percentage Error ({median_err:.2f}%)"
    )

    ax.set_title("Distribution of Percentage Error", pad=12)
    ax.set_xlabel("Percentage Error (%)")
    ax.set_ylabel("Frequency (Number of Observations)")
    ax.legend(loc="upper right", frameon=True, framealpha=0.9)
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        print(f"[+] Saved: {save_path}")

    return fig


def plot_correlation_heatmap(
    df: pd.DataFrame,
    save_path: str = "visualizations/07_correlation_heatmap.png"
) -> plt.Figure:
    """
    Visualization 7 — Heatmap: Correlation Heatmap of Experimental Variables.
    Displays Pearson correlation matrix across physical dimensions and error metrics.
    """
    set_academic_style()
    fig, ax = plt.subplots(figsize=(8.5, 7))

    numeric_cols = [
        "Length_m",
        "Theoretical_Period_s",
        "Experimental_Period_s",
        "Error_s",
        "Absolute_Error_s",
        "Relative_Error",
        "Percentage_Error"
    ]
    
    available_cols = [c for c in numeric_cols if c in df.columns]
    corr_matrix = df[available_cols].corr()

    # Clean display labels
    clean_labels = [
        "Length (m)",
        "Theo Period (s)",
        "Exp Period (s)",
        "Signed Error (s)",
        "Abs Error (s)",
        "Relative Error",
        "% Error (%)"
    ]

    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="vlag",
        vmin=-1.0,
        vmax=1.0,
        square=True,
        linewidths=1.0,
        cbar_kws={"label": "Pearson Correlation Coefficient ($r$)", "shrink": 0.82},
        xticklabels=clean_labels[:len(available_cols)],
        yticklabels=clean_labels[:len(available_cols)],
        ax=ax
    )

    ax.set_title("Correlation Heatmap of Experimental Variables", pad=14)
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        print(f"[+] Saved: {save_path}")

    return fig


def generate_all_visualizations(
    df: pd.DataFrame,
    output_dir: str = "visualizations"
) -> dict:
    """
    Executes the entire suite of 7 academic visualizations and saves figures.

    Parameters:
        df (pd.DataFrame): Processed experimental dataset.
        output_dir (str): Destination folder.

    Returns:
        dict: Mapping of visualization titles to file paths.
    """
    os.makedirs(output_dir, exist_ok=True)

    paths = {
        "line_chart": os.path.join(output_dir, "01_experimental_vs_theoretical_line.png"),
        "bar_chart": os.path.join(output_dir, "02_percentage_error_bar.png"),
        "pie_chart": os.path.join(output_dir, "03_error_category_pie.png"),
        "box_plot": os.path.join(output_dir, "04_experimental_period_boxplot.png"),
        "scatter_plot": os.path.join(output_dir, "05_length_vs_period_scatter.png"),
        "histogram": os.path.join(output_dir, "06_error_distribution_histogram.png"),
        "heatmap": os.path.join(output_dir, "07_correlation_heatmap.png")
    }

    plot_experimental_vs_theoretical(df, paths["line_chart"])
    plot_percentage_error_bar(df, paths["bar_chart"])
    plot_error_category_pie(df, paths["pie_chart"])
    plot_experimental_period_boxplot(df, paths["box_plot"])
    plot_length_vs_period_scatter(df, paths["scatter_plot"])
    plot_error_distribution(df, paths["histogram"])
    plot_correlation_heatmap(df, paths["heatmap"])

    plt.close("all")
    print(f"\n[+] Successfully generated all 7 academic visualizations in: {output_dir}")
    return paths


if __name__ == "__main__":
    # Resolve processed dataset path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, ".."))
    processed_path = os.path.join(project_root, "data", "processed", "pendulum_processed_data.csv")
    output_dir = os.path.join(project_root, "visualizations")

    if not os.path.exists(processed_path):
        raise FileNotFoundError(f"Processed dataset not found at: {processed_path}")

    df_proc = pd.read_csv(processed_path)
    generate_all_visualizations(df_proc, output_dir)
