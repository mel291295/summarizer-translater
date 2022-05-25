#Python
#importing the libraries
import streamlit as st

#main function
def main():
    st.title("Summary and Text Preprocessing of Fairy Tales")
    
    #select fairytale
    option = st.selectbox("How would you like to be contacted?", ("Little Snow White", "The Ugly Duckling", "Aladdin and the Wonderful Lamp", "The Sleeping Beauty", "Beauty and the Beast", "The Story of Cinderella", "Hansel and Gretel"))
    st.write('You selected:', option)
    
    #give the user the option to choose between Text Summarization, Text processing and Translation
    activity1 = ["Summarize","Text Preprocessing", "Translation"]
    choice = st.sidebar.selectbox("Select Function",activity1)
            
if __name__ == "__main__":
  main()

  
