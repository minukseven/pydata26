# 스트립릿 관련된 내용만 들어갑니다.
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib import font_manager, rc
import mylib.myTextAnalyzer as ta

@st.dialog("데이터 확인하깅", width='large')
def view_raw_data_dialog(data_df):
    num_data = st.number_input("확인할 데이터 수", value=10)
    st.write(data_df.head(num_data))


# 데이터가 안바뀌었으면 다시 계산하지 않음
@st.cache_data
def visualize_graph(counter, num_word_graph):
    font_path = 'C:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname = font_path).get_name()
    rc('font', family=font_name)

    # 데이터 준비
    word_list = [word for word, _ in counter.most_common(num_word_graph)]       # x
    count_list = [count for _, count in counter.most_common(num_word_graph)]    # y

    # pyplot 객체를 streamlit과 연동
    fig, ax = plt.subplots()
    ax.barh(word_list[::-1], count_list[::-1])

    # streamlit에서 pyplot 실행
    st.pyplot(fig)

def visualize_wordcloud(counter, num_word_wc):
    fig, ax = plt.subplots()

    wc = ta.generate_wordcloud(counter, num_word_wc)

    ax.imshow(wc)
    ax.axis('off')
    st.pyplot(fig)