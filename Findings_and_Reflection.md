# Findings and Reflection: CORD-19 Data Analysis Assignment

## Summary of Findings

### 1. Data Overview
- The `metadata.csv` file from the CORD-19 dataset contains information about COVID-19 research papers, including titles, publication dates, authors, journals, sources, and abstracts.
- After cleaning, the dataset still included thousands of research papers from a variety of sources and journals, with publication dates mostly between 2019 and 2022.

### 2. Publications by Year
- The majority of publications were concentrated in 2020 and 2021, reflecting the intense global research focus during the initial COVID-19 pandemic period.
- There was a sharp increase in publications in 2020, peaking during the early pandemic months, and a gradual decrease after 2021 as the immediate crisis subsided.

### 3. Top Journals and Sources
- The most active journals publishing COVID-19 research included well-known medical and scientific journals.
- A handful of journals published a significant proportion of the papers, but research was distributed across many different sources.

### 4. Common Words in Titles
- Frequent words in paper titles included terms like “COVID”, “SARS-CoV-2”, “pandemic”, “coronavirus”, “case”, “infection”, and “patients”.
- This reflects the main research themes and the urgent focus on the new virus and its impacts.

### 5. Visualizations
- Bar charts made it easy to compare publication trends over time and see which journals were most active.
- The word cloud visualization highlighted major topics and keywords in the research literature.

### 6. Interactive App
- The Streamlit app allowed for easy filtering by year and interactive exploration of the dataset.
- Users could view publication trends, top journals, and keyword patterns for selected periods.

---

## Reflection: What I Learned

### Technical Skills
- **Data Loading and Cleaning:** I learned how to load large real-world CSV files using pandas, identify and handle missing data, and convert date strings to datetime objects.
- **Exploratory Data Analysis:** I practiced basic data exploration, including checking data types, generating statistics, and understanding the structure of a new dataset.
- **Visualization:** I learned how to create different types of visualizations using matplotlib, seaborn, and wordcloud to make data insights more accessible.
- **Simple Web Apps:** I built my first interactive data app using Streamlit, allowing users to explore data visually and interactively.
- **Documentation:** I practiced writing clear code comments and summarizing my findings in markdown.

### Challenges Faced
- **Large File Handling:** The full CORD-19 dataset is huge. I learned to start with a subset or sample to keep processing manageable.
- **Missing Data:** Many columns had missing or incomplete values, requiring careful filtering to maintain data quality.
- **Visualization Choices:** Deciding which insights to visualize and how to make charts readable for others was a valuable learning experience.

### Personal Insights
- Real-world datasets are often messy and require thoughtful cleaning before analysis.
- Interactive tools like Streamlit can make data findings more engaging and accessible to others.
- Incremental testing and visualization at each step helped me catch mistakes early and improve the quality of my analysis.

---

## Next Steps

- Explore more advanced analytics (e.g., topic modeling, network analysis) on this or similar datasets.
- Learn more about deploying Streamlit apps online for broader sharing.
- Practice working with even larger datasets and more complex data cleaning.

---

*Submitted as part of the Frameworks Assignment. For questions or feedback, please contact me.*
