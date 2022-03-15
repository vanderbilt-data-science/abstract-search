import streamlit as st
import pandas as pd
import altair as alt
from sentence_transformers import SentenceTransformer, util
import numpy as np
from urllib.error import URLError
#ip install -U sentence-transformers
# Load document embeddings

# set up title and sidebar
st.title(" Your Top 3 Important Sessions")
st.markdown("This application is a dashboard for displaying your top 3 seesions at the summit")

doc_emb = np.loadtxt("abstract-embed.txt", dtype=float)

#@st.cache
#def get_data():
    #AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    #df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    # Load data
df = pd.read_csv("sessions.csv", usecols=['Unique ID', 'Name', 'Description', 'Activity Code', 'Start Time', 'End Time', 'Location Name'])
#return df#.set_index("Region")
#st.dataframe(df[0:2])
#def main():
        # front end elements of the web page
html_temp = """
<div style ="background-color:lightblue;padding:13px">
<h1 style ="color:white;text-align:center;">Sentence Similarity App Nashville Analytic Summit</h1>
</div>
        """
def main():
        # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

        # Get attributes from dataframe
    docs = list(df["Description"])
    titles = list(df["Name"])
    start_times = list(df["Start Time"])
    end_times = list(df["End Time"])
    locations = list(df["Location Name"])
# Query
# Load model
    model = SentenceTransformer('sentence-transformers/multi-qa-MiniLM-L6-cos-v1')

    query =  st.text_input("Enter your query: ")

    if query:
#st.text_area('Text area')
        #age = st.number_input("Age in Years")
#Encode query and documents
        query_emb = model.encode(query).astype(float)

    #Compute dot score between query and all document embeddings
        scores = util.dot_score(query_emb, doc_emb.astype(float))[0].cpu().tolist()

    #Combine docs & scores with other attributes
        doc_score_pairs = list(zip(docs, scores, titles, start_times, end_times, locations))

    # top_k results to return
        top_k=3

        print(" Your top", top_k, "most similar sessions in the Summit:")

    #Sort by decreasing score
        doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)


    #Output presentation recommendations
        for doc, score, title, start_time, end_time, location in doc_score_pairs[:top_k]:

            st.write("Score: %f" %score)
            st.write("Title: %s" %title)
            st.write("Abstract: %s" %doc)
            st.write("Location: %s" %location)
            st.write(f"From {start_time} to {end_time}")
            st.write('\n')


if __name__ == "__main__":
    main()
    #main()
