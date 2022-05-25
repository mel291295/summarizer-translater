#Python
#importing the libraries
import streamlit as st
#from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

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
    activity1 = ["Summarize","Text Preprocessing", "Translation"]
    choice = st.sidebar.selectbox("Select Function",activity1)
    if choice == "Summarize":
        st.subheader("Summary with NLP")
        raw_text = st.text_area("Enter Text Here")
        summary_choice = st.selectbox("Summary Choice", ["Genism", "Sumy Lex Rank"])
                                                       

 
if __name__ == "__main__":
  main()

  
