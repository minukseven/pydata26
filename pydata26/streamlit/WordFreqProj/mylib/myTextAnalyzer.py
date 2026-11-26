import pandas as pd
from collections import Counter
from konlpy.tag import Okt

def load_corpus(datafile):
    data_df = pd.read_csv(datafile)

    return data_df

def get_freg_word(data_df, target_col):
    # 분석 대상 컬럼을 리스트로 출력
    target_list = list(data_df[target_col])

    # 리스트의 문서를 단어 리스트로 생성 (품사태깅, 불용어 제거)
    word_list = get_korean_word_list(target_list)

    # 단어 리스트로부터 counter 객체 생성
    counter = Counter(word_list)
    return counter

def get_korean_word_list(review_list):
    tagger = Okt().pos
    my_tags = ['Noun', 'Adgective', 'Verb']
    my_stopwords = ['영화', '것', '이', '더']

    result_list = []
    for review in review_list:
        word_list = [ word for word, tag in tagger(review) if word not in my_stopwords and tag in my_tags]
        result_list.extend(word_list)
    return result_list

    
def generate_wordcloud(counter, num_word_wc):
    from wordcloud import WordCloud

    font_path = 'C:/Windows/Fonts/malgun.ttf'
    
    wc = WordCloud(
        font_path
        ,background_color='ivory'
        ,width = 800        #넓이
        ,height = 400       #높이
        ,max_words = num_word_wc    #출력할 단어 개수
    )

    return wc.generate_from_frequencies(counter)

