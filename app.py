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

#function for Sumy summarization
def sumy_summarizer(docx):
    parser = PlaintextParser.from_docx(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    #summarize the doc with 10 sentences
    summary = lex_summarizer(parser.document,10)
    summary_list = [str(sentence) for sentence in summary]
    result = " ".join(summary_list)
    return result                                    
                                         

#Webscrapping Pkgs

#main function
def main():
    st.title("Once upon a time")
    st.write("Summary, Translation and Text Preprocessing of Fairy Tales")
    
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
           summary_choice = st.selectbox("Select choice", ["Gensim", "Sumy Lex Rank"])   
            
    
     if choice == "Entity Checker"
                
           
                                                       
 
if __name__ == "__main__":
  main()

  
