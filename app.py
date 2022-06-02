#!Python
#importing the libraries
import streamlit as st


#sumy Sumary Pkgs
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

#main function
def main():
  st.title("Once upon a time")
  st.write("Summary, Translation and Text Preprocessing of Fairy Tales")

  #give the user the option to choose between Text Summarization, Text processing and Translation
  activity1 = ["Summarize","Entity Checker", "Translation"]
  choice = st.sidebar.selectbox("Select Activity",activity1)

if __name__=="__main__":
  main()
