# basic tests
from src.pars_subtitle import Subtitle
from src.pars_subtitle import DATA_DIR
from src.utils import read_json, write_json
from collections import Counter



def test_tokenizer():
    sub_file_path = DATA_DIR / 'src' / 'data' / \
        'Everybody Loves Raymond - 1x01 - Pilot.en.srt'
    difficult_file_path = DATA_DIR / 'src' / 'data' /  'word_diffculty.json'
    movie_name = Subtitle(sub_file_path)
    movie_name.tokenizer()
    assert Counter(movie_name.word).most_common(1)  == "."
    assert isinstance(movie_name.word, list)



