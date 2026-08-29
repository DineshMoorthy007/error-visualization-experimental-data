# Git Commit & Version Control Plan

**Project Title:** Error Visualization and Analysis of Experimental Data Using Python  
**Course:** Data Exploration and Visualization (Mini Project)  

This document outlines a structured, logical commit sequence for tracking project milestones throughout development without destructive git operations.

---

## Recommended Commit Sequence

### Commit 1: Initial Project Structure & Dataset
- **Scope:** Repository foundation, directory layout, raw dataset, requirements, `.gitignore`, and licensing.
- **Affected Files:**
  - `data/pendulum_experimental_data.csv`
  - `requirements.txt`
  - `.gitignore`
  - `LICENSE`
  - `src/__init__.py`
- **Suggested Commit Message:**
  ```bash
  git add data/ requirements.txt .gitignore LICENSE src/__init__.py
  git commit -m "chore: initialize project structure and add raw pendulum dataset"
  ```

---

### Commit 2: Data Preprocessing & Error Analysis Modules
- **Scope:** Implementation of data ingestion, validation checks, error calculation routines, and IQR outlier detection.
- **Affected Files:**
  - `src/data_preprocessing.py`
  - `src/error_analysis.py`
  - `data/processed/pendulum_processed_data.csv`
- **Suggested Commit Message:**
  ```bash
  git add src/data_preprocessing.py src/error_analysis.py data/processed/
  git commit -m "feat(analysis): implement data preprocessing, error formulations, and IQR outlier detection"
  ```

---

### Commit 3: Visualization Suite & Figures Generation
- **Scope:** Implementation of the academic plotting module and generation of all 7 diagnostic figures (Line, Bar, Pie, Box, Scatter, Histogram, Correlation Heatmap).
- **Affected Files:**
  - `src/visualization.py`
  - `visualizations/01_experimental_vs_theoretical_line.png`
  - `visualizations/02_percentage_error_bar.png`
  - `visualizations/03_error_category_pie.png`
  - `visualizations/04_experimental_period_boxplot.png`
  - `visualizations/05_length_vs_period_scatter.png`
  - `visualizations/06_error_distribution_histogram.png`
  - `visualizations/07_correlation_heatmap.png`
- **Suggested Commit Message:**
  ```bash
  git add src/visualization.py visualizations/
  git commit -m "feat(visualization): generate publication-quality 7-figure visual diagnostic suite"
  ```

---

### Commit 4: Master Jupyter Notebook Integration
- **Scope:** Complete master notebook containing sections 1 through 23, including exploratory analysis, statistical computations, visual figures, and interpretations.
- **Affected Files:**
  - `notebooks/error_visualization.ipynb`
- **Suggested Commit Message:**
  ```bash
  git add notebooks/error_visualization.ipynb
  git commit -m "feat(notebook): complete end-to-end 23-section master analysis notebook"
  ```

---

### Commit 5: Documentation & Presentation Content
- **Scope:** Detailed project summary, presentation slides deck, quantitative results table, and lab record checklist.
- **Affected Files:**
  - `docs/project_analysis_summary.md`
  - `docs/presentation_content.md`
  - `docs/results_summary.md`
  - `docs/lab_record_checklist.md`
  - `docs/github_setup.md`
- **Suggested Commit Message:**
  ```bash
  git add docs/
  git commit -m "docs: add comprehensive project analysis, presentation slides, and results summary"
  ```

---

### Commit 6: Final Polish & Submission Readiness
- **Scope:** Complete professional README documentation, SDG 4 mapping, final status report, and quality audit.
- **Affected Files:**
  - `README.md`
  - `docs/final_project_status.md`
  - `docs/git_commit_plan.md`
- **Suggested Commit Message:**
  ```bash
  git add README.md docs/
  git commit -m "docs(release): finalize README, lab record checklist, and submission readiness"
  ```

---

## Execution Guidelines
- Do NOT perform force-pushes (`git push --force`).
- Do NOT delete or rewrite historical commits.
- Ensure working directory is clean before making release tags:
  ```bash
  git status
  ```
