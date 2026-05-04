import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Career Path Recommender", layout="wide")
st.title("AI Career Path Recommender")
st.write("A positive-impact app that helps students discover suitable IT and data careers.")

careers = pd.read_csv("data/career_profiles.csv")

st.sidebar.header("Rate your skills")
python = st.sidebar.slider("Python", 0, 5, 3)
sql = st.sidebar.slider("SQL", 0, 5, 3)
communication = st.sidebar.slider("Communication", 0, 5, 3)
problem_solving = st.sidebar.slider("Problem Solving", 0, 5, 3)
security = st.sidebar.slider("Cybersecurity Interest", 0, 5, 2)
data_viz = st.sidebar.slider("Data Visualization", 0, 5, 3)

student = [[python, sql, communication, problem_solving, security, data_viz]]
matrix = careers[["python","sql","communication","problem_solving","security","data_viz"]].values
careers["match_score"] = cosine_similarity(student, matrix)[0] * 100
ranked = careers.sort_values("match_score", ascending=False)

st.metric("Best Match", ranked.iloc[0]["career"])
st.dataframe(ranked[["career","match_score","recommended_skills","certifications"]], use_container_width=True)

st.subheader("30-Day Action Plan")
best = ranked.iloc[0]
st.write(f"Focus on: {best['recommended_skills']}")
st.write(f"Suggested certifications: {best['certifications']}")
