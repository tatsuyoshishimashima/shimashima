import streamlit as st

st.title('タイトル')

condition = st.slider('あなたの今の調子は?',0, 100, 50)
'コンディション:',condition

from PIL import Image
img = Image.open('C:/Users/島　龍祥/Pictures/S__206061574.jpg')
st.image(img, caption='犀川の石',use_column_width=True)
