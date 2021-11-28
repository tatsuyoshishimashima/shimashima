import streamlit as st
from PIL import Image

st.title('タイトル')

s = st.selectbox('行きたい場所を選んでください',('北海道（札幌市）','東京（新宿）','沖縄（那覇市）','愛知（名古屋市）'))
if s == '北海道（札幌市）':
    dis = 1000
elif s =='東京（新宿）':
    dis = 230
elif s == '沖縄（那覇市）':
    dis = 2100
elif s == '愛知（名古屋市）':
    dis = 280
    

tim = float(st.number_input('何時間で着きたいですか？(h)',0.01))

speed = dis / tim
if 0 < speed <= 8:
    cal = '歩き'
elif 8 < speed <=30:
    cal ='自転車'
elif 30 < speed <=60:
    cal ='車（下道）'
elif 60 < speed <=120:    
    cal ='車（高速）'
elif 120 < speed <=400:
    cal ='新幹線'
elif 400 < speed <=600:
    cal ='リニア'
elif 600 < speed <=1000:
    cal ='飛行機'
else :
    cal ='瞬間移動'


button = st.button('Result')
if button == True:
    if cal == '歩き':
        st.write('適した移動手段は歩きで、時速',speed,'kmです。')
        img = Image.open('歩き.jpg')
        st.image(img, caption='歩き',use_column_width=True)
    elif cal =='自転車':
        st.write('適した移動手段は自転車で、時速',speed,'kmです。')
        img = Image.open('自転車.jpg')
        st.image(img, caption='自転車',use_column_width=True)
    elif cal =='車（下道）':
        st.write('適した移動手段は車（下道）で、時速',speed,'kmです。')
        img = Image.open('車（下道）.jpg')
        st.image(img, caption='車（下道）',use_column_width=True)
    elif cal =='車（高速）':
        st.write('適した移動手段は車（高速）で、時速',speed,'kmです。')
        img = Image.open('車（高速）.jpg')
        st.image(img, caption='車（高速）',use_column_width=True)
    elif cal =='新幹線':
        st.write('適した移動手段は新幹線で、時速',speed,'kmです。')
        img = Image.open('新幹線.jpg')
        st.image(img, caption='新幹線',use_column_width=True)
    elif cal =='リニア':
        st.write('適した移動手段はリニアで、時速',speed,'kmです。')
        img = Image.open('リニア.jpg')
        st.image(img, caption='リニア',use_column_width=True)
    elif cal =='飛行機':
        st.write('適した移動手段は飛行機で、時速',speed,'kmです。')
        img = Image.open('飛行機.jpg')
        st.image(img, caption='飛行機',use_column_width=True)
    elif cal =='瞬間移動':
        st.write('適した移動手段は瞬間移動で、時速',speed,'kmです。')
        img = Image.open('瞬間移動.jpg')
        st.image(img, caption='瞬間移動',use_column_width=True)






#from PIL import Image
#img = Image.open('C:/Users/島　龍祥/Pictures/S__206061574.jpg')
#st.image(img, caption='犀川の石',use_column_width=True)
