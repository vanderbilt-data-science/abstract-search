import streamlit as st
import time
import pandas as pd
import numpy as np



!pip install -U sentence-transformers

from sentence_transformers import SentenceTransformer, util


# Load document embeddings
doc_emb = np.loadtxt("abstract-embed.txt", dtype=float)
doc_emb

# Load data
df = pd.read_csv("sessions.csv", usecols=['Unique ID', 'Name', 'Description', 'Activity Code', 'Start Time', 'End Time', 'Location Name'])
#df.head()

# set up title and sidebar
st.title("Sentence Similarity Model")
# subtitle
st.markdown("This application is a model for displaying the top three sessions to attend based on your input")

@st.cache
def load model():
# Get attributes from dataframe
    docs = list(df["Description"])
    titles = list(df["Name"])
    start_times = list(df["Start Time"])
    end_times = list(df["End Time"])
    locations = list(df["Location Name"])

# Load model
    model = SentenceTransformer('sentence-transformers/multi-qa-MiniLM-L6-cos-v1')


# Query
    query = input("Enter your query: ")

#Encode query and documents
    query_emb = model.encode(query).astype(float)

#Compute dot score between query and all document embeddings
    scores = util.dot_score(query_emb, doc_emb.astype(float))[0].cpu().tolist()

#Combine docs & scores with other attributes
    doc_score_pairs = list(zip(docs, scores, titles, start_times, end_times, locations))

#Sort by decreasing score
    doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)[0:3]


#Output presentation recommendations
    for doc, score, title, start_time, end_time, location in doc_score_pairs[:10]:
        print("Score: %f" %score)
        print("Title: %s" %title)
        print("Abstract: %s" %doc)
        print("Location: %s" %location)
        print(f"From {start_time} to {end_time}")
        print('\n')

st.caption("Made with passion by pB")
