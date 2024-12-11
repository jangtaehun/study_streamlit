import streamlit as st
import openai
import os

st.title('몽타주 GPT')
st.write('얼굴 형태를 입력해주세요.')

# OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

with st.sidebar:
    openai_api_key = st.text_input("Your OpenAI API key: ", type="password")
    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key

post_word = st.text_input('입력해주세요.')
post_button = st.button('생성하기')
if post_button and openai_api_key:
    with st.spinner('생성 중입니다.'):
        openai.api_key = openai_api_key
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                        {
                            "role": "system",
                            "content": """
                            당신은 몽타주를 제작해 주는 몽타주 전문가 입니다.
                            속도가 느려도 괜찮습니다. 생성자가 원하는 느낌의 몽타주를 제작해 주세요.
                            사람의 얼굴을 그려해. 중요해 사람 얼굴.
                            그리고 150자 이내로 만들어줘
                            """
                        },
                        {"role": "user", "content": post_word}
                    ]
        )
        translated_text = response.choices[0].message.content

        response_img = openai.images.generate(
            model="dall-e-3",
            prompt=translated_text
        )
        image_url = response_img.data[0].url

        st.success(translated_text)
        st.image(image_url)