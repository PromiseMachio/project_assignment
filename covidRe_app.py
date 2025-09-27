import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

st.title("📊 CORD-19 Data Explorer")
st.write("A simple Streamlit app to explore COVID-19 research papers metadata.")

st.sidebar.header("Filters")
year_range = st.sidebar.slider(
    "Select Year Range", 
    int(df['year'].min()), 
    int(df['year'].max()), 
    (2020, 2021)
)

# filter data
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.subheader("Sample Data")
st.write(filtered.sample(5))

st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
st.bar_chart(year_counts)

st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
st.bar_chart(top_journals)

st.subheader("Word Cloud of Titles")
all_titles = " ".join(filtered['title'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_titles)

fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
