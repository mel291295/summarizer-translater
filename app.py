#Python

#importing the libraries
import streamlit as st
from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

#main function
def main():
    st.title("Summary and Text Preprocessing of Fairy Tales")
    
    #give the user the option to choose between Text Summarization, Text processing and Translation
    activity1 = ["Summarize","Text Preprocessing", "Translation]
    choice = st.sidebar.selectbox("Select Function",activity1)
            
if __name__ == "__main__":
  main()

  
