# Nashville Analytics Summit conference helper

## Overview

Since its inception in 2013 Nashville Analytics Summit event is held once a year in the months of September-October. There are dozens of talks covering analytics, data science, AI, career growth, new tools, specific industries and more. It has seen tremendous growth in sessions and participation increase. With the recent exponential need for data and its solutions, companies are looking forward to ways to leverage data in their organizations in order meet their business objectives. This has made it challenging for participants to navigate so many sessions and presentations at Nashville Analytics Summit. Therefore, if you are thinking of attending, Nashville Analytics Summit which talks might be of interest to you? Using a sentence similarity model, we'll pick out the top 3 talks for a participant based on their description of what they hope to get out of the Session/Talk.

This project utilizes Transformers sentence similarity model multi-qa-MiniLM-L6-cos-v1 to search for abstracts that have cosine similarity that matches the search query.The user will input a phrase of or a word of interest and the model will search for similarity contexts that matches the phrase and output the top 3 sessions that matches the phrase using Transformers model semantic search over conference abstracts.

## Huggingface spaces

Here is the Huggingface spaces

# Model Card

The link to the model card

## Critical Analysis


## Code Demonstration


To search over these abstracts, open "abstract_search.ipynb" in Google CoLab, and select "Run All". The last cell will allow you to input a search query. When prompted, enter the query, press Enter, and wait for results.

To run the streamlit app install streamlit in your machine

From command line/shell navigate to the abstract-search folder

Run the command below:

**streamlit run app.py**

This will open a web interface in your browser like the one below;

 *Local URL: http://localhost:8502*
  *Network URL: http://192.168.0.11:8502*

  Or click the link that was provided once you run the streamlit in your command line
  You can enter your query in the text box given to access your top three Sessions.

## Link to the video

## Resource Links

1. [Sentence Transformer](https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1)
2. 
