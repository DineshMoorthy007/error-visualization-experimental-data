"""
Visualization Module
====================
Project: Error Visualization and Analysis of Experimental Data Using Python
Course: Data Exploration and Visualization

This module defines plotting routines for visualizing experimental pendulum data,
error distributions, residual patterns, and statistical comparisons using Matplotlib and Seaborn.
(Foundation created in Phase 1; visualization plotting executed in Phase 2)
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def set_plot_style():
    """Configures consistent, publication-quality aesthetic styling for visualizations."""
    sns.set_theme(style="whitegrid", palette="deep")
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.size": 11,
        "axes.titlesize": 13,
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.titlesize": 14
    })


def plot_theoretical_vs_experimental(
    df: pd.DataFrame,
    save_path: str = "visualizations/01_theoretical_vs_experimental_period.png"
):
    """
    Generates a scatter and line comparison between theoretical and experimental time periods.
    (Planned for Phase 2 implementation)
    """
    set_plot_style()
    plt.figure(figsize=(9, 5), dpi=300)
    
    # Plot theoretical curve
    lengths = sorted(df["Length_m"].unique())
    theo_periods = [df[df["Length_m"] == l]["Theoretical_Period_s"].iloc[0] for l in lengths]
    plt.plot(lengths, theo_periods, color="#1f77b4", linestyle="--", linewidth=2, label="Theoretical Model $T = 2\\pi\\sqrt{L/g}$")
    
    # Plot experimental points
    plt.scatter(
        df["Length_m"],
        df["Experimental_Period_s"],
        color="#d62728",
        alpha=0.65,
        edgecolors="k",
        linewidth=0.5,
        label="Experimental Observations"
    )
    
    plt.title("Simple Pendulum: Theoretical vs. Experimental Period")
    plt.xlabel("Pendulum Length $L$ (m)")
    plt.ylabel("Time Period $T$ (s)")
    plt.legend()
    plt.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
    plt.close()
