import streamlit as st
import openai
import os

st.title('한국어 번역 GPT')
st.write('만나서 반갑습니다. 한국어를 영어, 일본어, 중국어 번역이 가능합니다.')

with st.sidebar:
    openai_api_key = st.text_input("Your OpenAI API key: ", type="password")
    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key

if st.checkbox('영어 번역'):
    ko_to_en = st.text_input('번역하고 싶은 글을 해주세요.(영어)')
    if ko_to_en and openai_api_key:
        openai.api_key = openai_api_key
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                        {
                            "role": "system",
                            "content": """
                            당신은 한국어를 영어로 번역하는 전문 번역가입니다.
                            답변 속도가 느려도 됩니다. 번역을 완벽하게 해주세요.
                            """
                        },
                        {"role": "user", "content": ko_to_en}
                    ]
        )
        translated_text = response.choices[0].message.content
        st.write(translated_text)

elif st.checkbox('일본어 번역'):
    ko_to_jp = st.text_input('번역하고 싶은 글을 해주세요.(일본어)')
    if ko_to_jp and openai_api_key:
        openai.api_key = openai_api_key
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """
                                당신은 한국어를 일본어로 번역하는 전문 번역가입니다.
                                답변 속도가 느려도 됩니다. 번역을 완벽하게 해주세요.
                                """
                },
                {"role": "user", "content": ko_to_jp}
            ]
        )
        translated_text = response.choices[0].message.content
        st.write(translated_text)

elif st.checkbox('중국어 번역'):
    ko_to_ch = st.text_input('번역하고 싶은 글을 해주세요.(일본어)')
    if ko_to_ch and openai_api_key:
        openai.api_key = openai_api_key
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """
                                    당신은 한국어를 일본어로 번역하는 전문 번역가입니다.
                                    답변 속도가 느려도 됩니다. 번역을 완벽하게 해주세요.
                                    """
                },
                {"role": "user", "content": ko_to_ch}
            ]
        )
        translated_text = response.choices[0].message.content
        st.write(translated_text)

# 이미지 입력
# import time
# if st.button('랜덤 이미지 생성'):
#     st.image(f'https://picsum.photos/450/450?t={time.time()}')
#     # 버튼을 누른다고 이미지가 바뀌지 않는다 -> 캐싱



