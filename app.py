#!Python
#importing the libraries
import streamlit as st
import stramlit.components.v1 as stc
import pandas as pd


#sumy Sumary Pkgs
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

#translate Pkgs
from googletrans import Translator
from gtts import gTTS

#function for Sumy summarization
def sumy_summarizer(docx):
    parser = PlaintextParser.from_docx(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    #summarize the doc with 10 sentences
    summary = lex_summarizer(parser.document,10)
    summary_list = [str(sentence) for sentence in summary]
    result = " ".join(summary_list)
    return result 

#main function
def main():
  st.title("Once upon a time")
  st.write("Summary, Translation and Text Preprocessing of Fairy Tales")
  
  #select fairytale
  option = st.selectbox("How would you like to be contacted?", ("Little Snow White", "The Ugly Duckling", "Aladdin and the Wonderful Lamp", "The Sleeping Beauty", "Beauty and the Beast", "The Story of Cinderella", "Hansel and Gretel"))
  st.write('You selected:', option)
    
    uploaded_file = st.file_upoader("Upload Files", type = ["cvs"])
                                    
    if option == "Little Snow White":
        uploaded_file = st.file_uploader("")
        if uploaded_file:
            for line in uploaded_file:
              st.write(line)

  #give the user the option to choose between Text Summarization, Text processing and Translation
  activity1 = ["Summarize","Entity Checker", "Translation"]
  choice = st.sidebar.selectbox("Select Activity",activity1)
  
  if choice == "Summarize":
    st.subheader("Summary with NLP")
        raw_text = st.text_area("Enter Text Here", "Type Here")
        if st.button("Summarize"):
           summary_choice = st.selectbox("Select choice", ["Gensim", "Sumy Lex Rank"])
  
  
  if choice == "Translation":
    user_text = st.text_input("Give me some text you want me to translate in English and read for you: ")
    user_text = Translator()
    text_to_translate = translator.translate(text=user_text, dest='de')
    
    text_to_speech = text_to_translate.text
    st.write(text_to_speech)
    # it converts the translated text to speech.
    tts=gTTS(text=text_to_speech, lang='de')
    
    tts.save("audio.mp3")
    
    st.write("Your text would sound like this in German:")
    audio_file = open('audio.mp3', 'rb')
    st.audio(data=audio_file, format="audio/mp3", start_time=0)

if __name__=="__main__":
  main()




st.write("Your text would sound like this in English:")
audio_file = open('audio.mp3', 'rb')
st.audio(data=audio_file, format="audio/mp3", start_time=0)
