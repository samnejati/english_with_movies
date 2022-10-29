import streamlit as st
from src.pars_subtitle import Subtitle
from src.pars_subtitle import DATA_DIR
from src.utils import read_json, write_json


st.header(":clapper: Learn English with Movies")
st.file_uploader("Please upload  your file: ")
sidebar_diff_level = st.slider("The words with difficulty level: ", 1,10, 2)


sub_file_path = DATA_DIR / 'src' / 'data' / \
    'Everybody Loves Raymond - 1x01 - Pilot.en.srt'

difficult_file_path = DATA_DIR / 'src' / 'data' /  'word_diffculty.json'
movie_name = Subtitle(sub_file_path)
movie_name.tokenizer()

# read difficulty dict
difficult_dict = read_json(difficult_file_path)
st.write(movie_name.get_difficult_words(difficult_dict, sidebar_diff_level))
