import streamlit as st
import openai
import os

st.title('포스트 GPT')
st.write('만들고 싶은 것을 알려주세요.')

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
                            당신은 제품 홍보 포스터를 제작해 주는 제품 홍보 포스터 전문가 입니다.
                            속도가 느려도 괜찮습니다. 소비자가 원하는 느낌의 제품 홍보 포스터를 제작해 주세요.
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