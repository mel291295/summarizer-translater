#Python
#importing the libraries
import streamlit as st
import os
from gtts import gTTS
from googletrans import Translator
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import jieba
from xpinyin import Pinyin

#main function
def main():
    st.title("Summary and Text Preprocessing of Fairy Tales")
    
    #select fairytale
    option = st.selectbox("How would you like to be contacted?", ("Little Snow White", "The Ugly Duckling", "Aladdin and the Wonderful Lamp", "The Sleeping Beauty", "Beauty and the Beast", "The Story of Cinderella", "Hansel and Gretel"))
    st.write('You selected:', option)
    
    #give the user the option to choose between Text Summarization, Text processing and Translation
    activity1 = ["Summarize","Text Preprocessing", "Translation"]
    choice = st.sidebar.selectbox("Select Function",activity1)

#translation function
def translation_func(input_language, output_language, text):
    translator = Translator()
    translation = translator.translate(text, src=input_language, dest=output_language)
    translation_text = translation.text
    tts = gTTS(translation_text, lang=output_language,  slow=True)
    try:
        audio_file = text[0:20]
    except:
        audio_file = "audio"
    tts.save(f"temp_folder/{audio_file}.mp3")
    return audio_file, translation_text

if choose == "Chinese":
    if st.button("Show Translation and Audio"):
        input='en'                   
        output='zh-cn'
        audio_file, translation_text = translation_func(input, output, text)

        st.write('  ')
        segments = jieba.cut(translation_text) #used for chinese text segmentation
        seg_output = " ".join(segments)
        html_str = f"""
        <style>
        p.a {{
        font: bold {30}px Courier;
        }}
        </style>
        <p class="a">{seg_output}</p>
        """
        st.markdown(html_str, unsafe_allow_html=True) #display the translated text in Chinese characters
        st.write('  ')

        p = Pinyin()
        pinyined = p.get_pinyin(seg_output, splitter='', tone_marks='marks') #Get pinyin (the official romanization system for Standard Chinese in mainland China)
        html_str2 = f"""
        <style>
        p.a {{
        font: bold {25}px Courier;
        }}
        </style>
        <p class="a">{pinyined}</p>
        """
        st.markdown(html_str2, unsafe_allow_html=True) #display pin yin

        audio_file = open(f"temp_folder/{audio_file}.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", start_time=0) #displays the audio player 
  
 elif choose == "French":

    if st.button("Show Translation and Audio"):
        output='fr'
        audio_file, translation_text = translation_func(input, output, text)

        st.write('  ')
        html_str = f"""
        <style>
        p.a {{
        font: bold {30}px Courier;
        }}
        </style>
        <p class="a">{translation_text}</p>
        """
        st.markdown(html_str, unsafe_allow_html=True)
        st.write('  ')

        audio_file = open(f"temp_folder/{audio_file}.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", start_time=0)


 
if __name__ == "__main__":
  main()

  
