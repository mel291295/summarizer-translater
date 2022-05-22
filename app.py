import streamlit as st

#NLP
#Summary Packages
from gensim.summarization import summarize
#Sumy PKG
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizer.lex_rank import LexRankSummarizer

#Funktion for Sumy Summarization
def sumy_summarizer(docx):
    parser = PlaintextParser.from_string(docx, Tokenizer("english))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, 3)
    summary_list = [st(sentence) for sentence in summary]
    result = " ".join(sumary_list)
    return result
                                                       
                                                       
#Webscaping Packages

def main():
  """Fairytales Summary and Entity Checker"""
  
  st.title("Fairytales Summary and Entity Checker")
  
  activities= ["Summarize", "NER Checker", "NER for URL"]
  choice = st.sidebar.selectbox("Select Activity", activities)
  
  if choice == "Summarize":
    st.subheader("Summarz with NLP")
    raw.text = st.text_area("Enter Text Here", "Type Here")
    summary_choice = st.selectbox("Summary Choice", ["Gensim", "Sumy Lex Rank"]                                                            
    if st.button("Summarize"):
                                                  
      if sumary_choice == "Gensim":
         summary_result = summarizer(raw_text)
      
       elif summary_choice == "Sumy Lex Rank":
            sumary_result = sumy_sumarizer(raw_text)
                                  
       st.write(summary_result)
     
   
  
if __name__ == "__main__":
  main()

  
