# GitHub Setup Guide

**Project Title:** Error Visualization and Analysis of Experimental Data Using Python  
**Course:** Data Exploration and Visualization (Mini Project)  

This guide provides clean, step-by-step instructions for initializing, committing, and publishing the project repository to GitHub.

---

## 1. Prerequisites
Ensure that Git and Python are installed on your local machine:
```bash
git --version
python --version
```

---

## 2. Step-by-Step Repository Setup

### Step 1: Initialize Git Repository (if not already initialized)
Open a terminal in the root project directory (`error-visualization-experimental-data/`) and execute:
```bash
git init
```

### Step 2: Verify Repository Status and Exclusions
Check which files are untracked and verify that `.gitignore` properly excludes temporary caches, virtual environments, and checkpoint folders:
```bash
git status
```

### Step 3: Stage Project Files
Stage all essential project files, source modules, datasets, notebooks, documentation, and visualizations:
```bash
git add .
```

### Step 4: Create Initial Commit
Create a structured initial commit:
```bash
git commit -m "feat: complete Error Visualization and Analysis mini-project"
```

### Step 5: Link Local Repository to GitHub Remote
Create a new, empty repository on GitHub (without initializing a README, `.gitignore`, or license, as these already exist). Then link your local repository:
```bash
# Rename the default branch to main
git branch -M main

# Add the remote repository URL (replace with your actual GitHub repository URL)
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

### Step 6: Push Project to GitHub
Push your local branches and commits to the remote GitHub repository:
```bash
git push -u origin main
```

---

## 3. Post-Push Verification
Once pushed, open your browser and navigate to `YOUR_GITHUB_REPOSITORY_URL`:
1. Verify that `README.md` renders cleanly on the main page.
2. Confirm that `notebooks/error_visualization.ipynb` displays properly with formatted tables and figures.
3. Verify that all 7 academic diagnostic figures are accessible in `visualizations/`.
4. Ensure documentation files are located in `docs/`.
