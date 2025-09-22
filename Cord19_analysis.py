import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from wordcloud import WordCloud
import os

# ---------- PART 1: DATA LOADING & BASIC EXPLORATION ----------

# Load the metadata.csv file
DATA_PATH = 'metadata.csv'  # Change this if your file is in a different location

# Check if file exists
if not os.path.isfile(DATA_PATH):
    st.error(f"File '{DATA_PATH}' not found. Please make sure it is in the same folder as this script.")
    st.stop()

df = pd.read_csv(DATA_PATH)

# Show some basic info
print("First 5 rows:")
print(df.head())
print("\nShape (rows, columns):", df.shape)
print("\nColumn info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# ---------- PART 2: DATA CLEANING & PREPARATION ----------

# Drop columns with too many missing values (example: more than 60% missing)
threshold = 0.6
missing_percent = df.isnull().mean()
cols_to_drop = missing_percent[missing_percent > threshold].index
df_clean = df.drop(columns=cols_to_drop)

# Drop rows with missing publish_time or title (important fields)
df_clean = df_clean.dropna(subset=['publish_time', 'title'])

# Convert publish_time to datetime
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
df_clean = df_clean.dropna(subset=['publish_time'])  # Drop rows where conversion failed

# Extract year
df_clean['year'] = df_clean['publish_time'].dt.year

# Add abstract word count column
df_clean['abstract_word_count'] = df_clean['abstract'].fillna("").apply(lambda x: len(x.split()))

print("\nCleaned DataFrame shape:", df_clean.shape)

# ---------- PART 3: DATA ANALYSIS & VISUALIZATION ----------

# 1. Publications by year
year_counts = df_clean['year'].value_counts().sort_index()

# 2. Top journals
top_journals = df_clean['journal'].value_counts().head(10)

# 3. Most frequent words in titles (basic)
from collections import Counter
import re

def get_top_words(texts, n=20):
    words = []
    for text in texts.dropna():
        words += re.findall(r'\b\w+\b', text.lower())
    common_words = Counter(words).most_common(n)
    return dict(common_words)

title_words = get_top_words(df_clean['title'], 20)

# 4. Publications by source
source_counts = df_clean['source_x'].value_counts().head(10)

# 5. Word cloud for titles
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df_clean['title'].dropna()))

# ---------- PART 4: STREAMLIT APPLICATION ----------

st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers (metadata.csv)")

# Interactive year slider
min_year = int(df_clean['year'].min())
max_year = int(df_clean['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (min_year, max_year))
filtered = df_clean[(df_clean['year'] >= year_range[0]) & (df_clean['year'] <= year_range[1])]

st.header("Number of Publications by Year")
year_counts_filtered = filtered['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.bar(year_counts_filtered.index, year_counts_filtered.values)
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Publications')
st.pyplot(fig1)

st.header("Top 10 Journals Publishing COVID-19 Research")
top_journals_filtered = filtered['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(y=top_journals_filtered.index, x=top_journals_filtered.values, ax=ax2, orient="h")
ax2.set_xlabel('Number of Publications')
ax2.set_ylabel('Journal')
st.pyplot(fig2)

st.header("Word Cloud of Paper Titles")
fig3, ax3 = plt.subplots(figsize=(8, 4))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

st.header("Source Distribution (Top 10)")
source_counts_filtered = filtered['source_x'].value_counts().head(10)
fig4, ax4 = plt.subplots()
source_counts_filtered.plot(kind='bar', ax=ax4)
ax4.set_xlabel('Source')
ax4.set_ylabel('Number of Publications')
st.pyplot(fig4)

st.header("Sample Data")
st.write(filtered[['title', 'authors', 'journal', 'publish_time']].head(10))

