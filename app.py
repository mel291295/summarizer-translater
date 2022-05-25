#Python
#importing the libraries
import streamlit as st

#NLP

#Summary Pkgs
from gensim.summarization import sumarize

#sumy Sumary Pkgs
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

#Webscrapping Pkgs

#main function
def main():
    st.title("Summary and Text Preprocessing of Fairy Tales")
    
    #select fairytale
    option = st.selectbox("How would you like to be contacted?", ("Little Snow White", "The Ugly Duckling", "Aladdin and the Wonderful Lamp", "The Sleeping Beauty", "Beauty and the Beast", "The Story of Cinderella", "Hansel and Gretel"))
    st.write('You selected:', option)
    #if option == "Little Snow White":
        #uploaded_file = st.file_uploader("")
        #if uploaded_file:
            #for line in uploaded_file:
               # st.write(line)

    
    #give the user the option to choose between Text Summarization, Text processing and Translation
    activity1 = ["Summarize","Entity Checker", "Translation"]
    choice = st.sidebar.selectbox("Select Activity",activity1)
    
    if choice == "Summarize":
        st.subheader("Summary with NLP")
        raw_text = st.text_area("Enter Text Here", "Type Here")
        if st.button("Summarize"):
            st.write(raw_text)
    
     if choice == "Entity Checker"
                
           
                                                       

 
if __name__ == "__main__":
  main()

  
