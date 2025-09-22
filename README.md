# CORD-19 Data Analysis and Streamlit Application

## Overview

This project is a beginner-friendly data analysis and visualization of the CORD-19 research dataset. It guides you through loading, cleaning, exploring, and visualizing real-world research data on COVID-19, and building a simple Streamlit app to interactively display your findings.

## Objectives

- Practice loading and exploring real-world datasets with Python
- Learn basic data cleaning techniques using pandas
- Create meaningful visualizations with matplotlib, seaborn, and wordcloud
- Build a simple interactive web application using Streamlit
- Present and document data insights effectively

## Dataset

We use the `metadata.csv` file from the [CORD-19 dataset on Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge). This file contains details about COVID-19 research papers, including:
- Titles and abstracts
- Publication dates
- Authors and journals
- Source information

> **Tip:** Only the `metadata.csv` file is needed for this project.

## Requirements

- Python 3.7+
- pandas
- matplotlib
- seaborn
- wordcloud
- streamlit
- Jupyter Notebook (recommended for exploration)

Install all packages with:
```bash
pip install pandas matplotlib seaborn wordcloud streamlit
```

## Project Structure

- `cord19_analysis.ipynb` - Jupyter Notebook for step-by-step data analysis and visualizations
- `cord19_streamlit.py` - Streamlit app script for interactive exploration
- `FINDINGS_AND_REFLECTION.md` - Summary of findings and personal reflection
- `README.md` - This file

## How to Use

### 1. Download the Data
Download `metadata.csv` from Kaggle and place it in this project directory.

### 2. Run the Jupyter Notebook
Open `cord19_analysis.ipynb` in Jupyter Notebook or JupyterLab and run the cells to:
- Load and clean the data
- Explore and visualize publication trends
- Analyze top journals and sources
- Generate a word cloud of research topics

### 3. Launch the Streamlit App
Run the following command in your terminal:
```bash
streamlit run cord19_streamlit.py
```
Interact with the app to filter by publication year, view trends, see word clouds, and browse sample records.

### 4. Review Findings
Check `FINDINGS_AND_REFLECTION.md` for a written summary and reflection on the analysis process.

## Example Visualizations

- Publications by year (bar chart)
- Top journals and sources (bar charts)
- Word cloud of paper titles

## Tips

- Start small: If the full dataset is too large, work with a sample.
- Save your progress: Run and test code in small sections.
- Use documentation and Google for troubleshooting.
- Ask for help if you get stuck!

## License
MIT License
This project is for educational purposes.

---

Happy coding and data exploring!
