# app.py
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import matplotlib.pyplot as plt

# -------------------------------
# Title
# -------------------------------
st.title("🩺 HealthAssist: A Smart Medicine Recommendation Model Based on Symptom Analysis")
st.write("Enter your symptoms below to receive AI-powered medicine recommendations based on their descriptions and relevance.")

# -------------------------------
# Load Dataset
# -------------------------------
uploaded_file = st.file_uploader("Upload Medicine Description Excel File", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df["Reason"] = df["Reason"].fillna("")
    df["Description"] = df["Description"].fillna("")
    df["full_text"] = df["Reason"].astype(str) + " " + df["Description"].astype(str)

    names = df["Drug_Name"].astype(str).tolist()
    descriptions = df["Description"].astype(str).tolist()
    full_texts = df["full_text"].tolist()

    # -------------------------------
    # TF-IDF Vectorizer
    # -------------------------------
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english", max_features=8000)
    tfidf_matrix = vectorizer.fit_transform(full_texts)

    # -------------------------------
    # Recommendation Function
    # -------------------------------
    def recommend(query, top_n=5, min_score=0.05):
        q_vec = vectorizer.transform([query])
        cosine_sim = linear_kernel(q_vec, tfidf_matrix).flatten()
        top_idx = cosine_sim.argsort()[::-1][:top_n]
        results = []
        for idx in top_idx:
            score = float(cosine_sim[idx])
            if score >= min_score:
                results.append({
                    "name": names[idx],
                    "description": descriptions[idx],
                    "score": round(score * 100, 2)
                })
        return results

    # -------------------------------
    # User Input
    # -------------------------------
    query = st.text_area("Enter your symptoms here:")
    top_n = st.slider("Select number of recommendations to show:", 1, 10, 5)

    if st.button("Get Recommendations"):
        if query.strip() == "":
            st.warning("Please enter some symptoms to get recommendations.")
        else:
            recs = recommend(query, top_n=top_n)
            
            if recs:
                # Display Table
                rec_df = pd.DataFrame(recs)
                st.subheader("Top Recommendations")
                st.dataframe(rec_df)

                # Plot Bar Chart
                st.subheader("Match Score Bar Chart")
                fig, ax = plt.subplots(figsize=(10, 6))
                names_plot = [r['name'] for r in recs]
                scores_plot = [r['score'] for r in recs]
                ax.barh(names_plot[::-1], scores_plot[::-1], color='skyblue')
                ax.set_xlabel("Match Score (%)")
                ax.set_title(f"🩺 HealthAssist: A Smart Medicine Recommendation Model Based on Symptom Analysis: '{query}'")
                for i, v in enumerate(scores_plot[::-1]):
                    ax.text(v + 1, i, f"{v}%", va='center')
                st.pyplot(fig)
            else:
                st.warning("❌ No matches found. Try rephrasing symptoms.")
else:
    st.info("Please upload your Excel file to start.")
