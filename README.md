# HealthAssist
A Smart Medicine Recommendation Model Based on Symptom Analysis
🧠 HealthAssist: A Smart Medicine Recommendation System using Machine Learning
📖 Overview

HealthAssist is an intelligent medicine recommendation system built using Machine Learning and Natural Language Processing (NLP) techniques.
It analyzes the user’s symptoms and suggests relevant medicines based on similarity in medical descriptions and dataset patterns.
This project aims to assist users in identifying possible medicines for common health issues — making healthcare information more accessible.

⚙️ Features

✅ User-friendly Streamlit Web Interface
✅ Symptom-based medicine recommendations
✅ TF-IDF Vectorization for text processing
✅ Cosine Similarity for finding related medicines
✅ Interactive visualization of recommendation scores
✅ Option to upload your own dataset (CSV)

🧩 Technologies Used

Python 3.9+

Streamlit (for web interface)

Pandas (for data handling)

Scikit-learn (for ML model – TF-IDF, cosine similarity)

Matplotlib (for plotting bar charts)

🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/yourusername/HealthAssist.git
cd HealthAssist

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

4️⃣ Upload Dataset

Upload your medicine dataset (CSV file) containing at least these columns:

name – Name of the medicine

description – Description or uses of the medicine

📊 Example Use

Input:

“fever and body pain”

Output:

Recommended Medicines:

Paracetamol

Crocin

Dolo 650

📘 Reference Papers and Datasets

A. Gupta, S. Goyal, & M. S. Joshi, “Medicine Recommendation System using Machine Learning”, IRJET, 2020.

S. M. Shamrat et al., “A Review on Machine Learning Algorithms for Disease Prediction and Recommendation System”, IJCA, 2021.

Kaggle Dataset – Medicine Recommendation Based on Symptoms

UCI Repository – Drug Review Dataset (Drugs.com)

🧾 Project Structure
HealthAssist/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── dataset.csv             # Sample medicine dataset
├── README.md               # Project documentation
└── images/                 # Optional - screenshots or plots

💡 Future Improvements

Add disease prediction based on multiple symptoms.

Integrate voice input for accessibility.

Connect with real-time medical APIs for accurate suggestions.

Implement medicine side-effect detection.

🧑‍💻 Author

Developed by: Parthib Ghosh
