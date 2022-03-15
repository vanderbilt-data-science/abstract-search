# Using Transformers for semantic search over conference abstracts

This project uses [Sentence Transformer](https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1) to perform a semantic search over abstracts for presentations in the 2021 Nashville Analytics Summit.

To search over these abstracts, open "abstract_search.ipynb" in Google CoLab, and select "Run All". The last cell will allow you to input a search query. When prompted, enter the query, press Enter, and wait for results.

To run the streamlit app install streamlit in your machine

From command line/shell navigate to the abtract-search folder

Run the command below:

**streamlit run app.py**

This will open a web interface in your browser like the one below;

 *Local URL: http://localhost:8502*
  *Network URL: http://192.168.0.11:8502*
  
  Or click the link above and you can enter your query.



