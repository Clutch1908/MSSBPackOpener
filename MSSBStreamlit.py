import streamlit as st
import MSSBCardGenerator as MSSB
from importlib import reload

st.markdown('<h1 align="center">MSSB Pack Opener </h1>', unsafe_allow_html=True)
        
if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i
    if st.session_state.stage == 1:
        MSSB.openPack()
        MSSB.returnPackString()
    if st.session_state.stage == 2:
        MSSB.getSummary()
    if st.session_state.stage == 3:
        reload(MSSB)
        MSSB.openPack()
        MSSB.returnPackString()
    
if st.session_state.stage == 0:
    with st.sidebar:
            st.header('Pack Opener Options')
            st.button('Open Your First Pack!', on_click=set_state, args = [1])
            st.write("Learn more about the MSSB Pack Opener at: https://docs.google.com/document/d/15mSM5e-75sTMnLULELV6tsG4GjSAjoVwGSOdWHuCewE/edit?usp=sharing")

if st.session_state.stage == 1:
    #store the image output for each card
    selectedCardImage_1 = MSSB.selectedCardImage_1
    html_img1 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_1} alt="Error"> </div>'
    selectedCardImage_2 = MSSB.selectedCardImage_2
    html_img2 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_2} alt="Error"> </div>'
    selectedCardImage_3 = MSSB.selectedCardImage_3
    html_img3 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_3} alt="Error"> </div>'
    selectedCardImage_4 = MSSB.selectedCardImage_4
    html_img4 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_4} alt="Error"> </div>'
    selectedCardImage_5 = MSSB.selectedCardImage_5
    html_img5 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_5} alt="Error"> </div>'
    selectedCardImage_6 = MSSB.selectedCardImage_6
    html_img6 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_6} alt="Error"> </div>'
    selectedCardImage_7 = MSSB.selectedCardImage_7
    html_img7 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_7} alt="Error"> </div>'
    selectedCardImage_8 = MSSB.selectedCardImage_8
    html_img8 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_8} alt="Error"> </div>'
    selectedCardImage_9 = MSSB.selectedCardImage_9
    html_img9 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_9} alt="Error"> </div>'
 
    #store the text output for each card
    selectedCardOutput_1 = MSSB.selectedCardOutput_1
    html_str1 = f'<p align="center">{selectedCardOutput_1} </p>'
    selectedCardOutput_2 = MSSB.selectedCardOutput_2
    html_str2 = f'<p align="center">{selectedCardOutput_2} </p>'
    selectedCardOutput_3 = MSSB.selectedCardOutput_3
    html_str3 = f'<p align="center">{selectedCardOutput_3} </p>'
    selectedCardOutput_4 = MSSB.selectedCardOutput_4
    html_str4 = f'<p align="center">{selectedCardOutput_4} </p>'
    selectedCardOutput_5 = MSSB.selectedCardOutput_5
    html_str5 = f'<p align="center">{selectedCardOutput_5} </p>'
    selectedCardOutput_6 = MSSB.selectedCardOutput_6
    html_str6 = f'<p align="center">{selectedCardOutput_6} </p>'
    selectedCardOutput_7 = MSSB.selectedCardOutput_7
    html_str7 = f'<p align="center">{selectedCardOutput_7} </p>'
    selectedCardOutput_8 = MSSB.selectedCardOutput_8
    html_str8 = f'<p align="center">{selectedCardOutput_8} </p>'
    selectedCardOutput_9 = MSSB.selectedCardOutput_9
    html_str9 = f'<p align="center">{selectedCardOutput_9} </p>'

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(html_img1, unsafe_allow_html=True)
        st.markdown(html_str1, unsafe_allow_html=True)
        st.markdown(html_img4, unsafe_allow_html=True)
        st.markdown(html_str4, unsafe_allow_html=True)
        st.markdown(html_img7, unsafe_allow_html=True)
        st.markdown(html_str7, unsafe_allow_html=True)
    with col2:
        st.markdown(html_img2, unsafe_allow_html=True)
        st.markdown(html_str2, unsafe_allow_html=True)
        st.markdown(html_img5, unsafe_allow_html=True)
        st.markdown(html_str5, unsafe_allow_html=True)
        st.markdown(html_img8, unsafe_allow_html=True)
        st.markdown(html_str8, unsafe_allow_html=True)
    with col3:
        st.markdown(html_img3, unsafe_allow_html=True)
        st.markdown(html_str3, unsafe_allow_html=True)
        st.markdown(html_img6, unsafe_allow_html=True)
        st.markdown(html_str6, unsafe_allow_html=True)
        st.markdown(html_img9, unsafe_allow_html=True)
        st.markdown(html_str9, unsafe_allow_html=True)
    
    with st.sidebar:
            packsOpenedStr = MSSB.packsOpenedStr
            st.header('Pack Opener Options')
            st.button('Open Next Pack', on_click=set_state, args = [1])
            st.write(MSSB.packsOpenedStr)
            st.button('End This Pack Opening', on_click=set_state, args = [2])
            st.write("Learn more about the MSSB Pack Opener at: https://docs.google.com/document/d/15mSM5e-75sTMnLULELV6tsG4GjSAjoVwGSOdWHuCewE/edit?usp=sharing")

if st.session_state.stage == 2:
    summaryChar = MSSB.summaryChar
    html_strChar = f'<p align="center">{summaryChar} </p>'
    summaryStadium = MSSB.summaryStadium
    html_strStadium = f'<p align="center">{summaryStadium} </p>'
    summaryToken = MSSB.summaryToken
    html_strToken = f'<p align="center">{summaryToken} </p>'
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(html_strChar, unsafe_allow_html=True)
    with col2:
        st.markdown(html_strStadium, unsafe_allow_html=True)
    with col3:
        st.markdown(html_strToken, unsafe_allow_html=True)
    
    with st.sidebar:
            packsOpenedStr = MSSB.packsOpenedStr
            st.header('Pack Opener Options')
            st.write(MSSB.packsOpenedStr)
            st.button('Start a New Pack Opening!', on_click=set_state, args = [3])
            st.write("Learn more about the MSSB Pack Opener at: https://docs.google.com/document/d/15mSM5e-75sTMnLULELV6tsG4GjSAjoVwGSOdWHuCewE/edit?usp=sharing")

if st.session_state.stage == 3:
     #store the image output for each card
    selectedCardImage_1 = MSSB.selectedCardImage_1
    html_img1 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_1} alt="Error"> </div>'
    selectedCardImage_2 = MSSB.selectedCardImage_2
    html_img2 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_2} alt="Error"> </div>'
    selectedCardImage_3 = MSSB.selectedCardImage_3
    html_img3 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_3} alt="Error"> </div>'
    selectedCardImage_4 = MSSB.selectedCardImage_4
    html_img4 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_4} alt="Error"> </div>'
    selectedCardImage_5 = MSSB.selectedCardImage_5
    html_img5 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_5} alt="Error"> </div>'
    selectedCardImage_6 = MSSB.selectedCardImage_6
    html_img6 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_6} alt="Error"> </div>'
    selectedCardImage_7 = MSSB.selectedCardImage_7
    html_img7 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_7} alt="Error"> </div>'
    selectedCardImage_8 = MSSB.selectedCardImage_8
    html_img8 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_8} alt="Error"> </div>'
    selectedCardImage_9 = MSSB.selectedCardImage_9
    html_img9 = f'<div style="text-align: center;"> <img align="center" src={selectedCardImage_9} alt="Error"> </div>'
 
    #store the text output for each card
    selectedCardOutput_1 = MSSB.selectedCardOutput_1
    html_str1 = f'<p align="center">{selectedCardOutput_1} </p>'
    selectedCardOutput_2 = MSSB.selectedCardOutput_2
    html_str2 = f'<p align="center">{selectedCardOutput_2} </p>'
    selectedCardOutput_3 = MSSB.selectedCardOutput_3
    html_str3 = f'<p align="center">{selectedCardOutput_3} </p>'
    selectedCardOutput_4 = MSSB.selectedCardOutput_4
    html_str4 = f'<p align="center">{selectedCardOutput_4} </p>'
    selectedCardOutput_5 = MSSB.selectedCardOutput_5
    html_str5 = f'<p align="center">{selectedCardOutput_5} </p>'
    selectedCardOutput_6 = MSSB.selectedCardOutput_6
    html_str6 = f'<p align="center">{selectedCardOutput_6} </p>'
    selectedCardOutput_7 = MSSB.selectedCardOutput_7
    html_str7 = f'<p align="center">{selectedCardOutput_7} </p>'
    selectedCardOutput_8 = MSSB.selectedCardOutput_8
    html_str8 = f'<p align="center">{selectedCardOutput_8} </p>'
    selectedCardOutput_9 = MSSB.selectedCardOutput_9
    html_str9 = f'<p align="center">{selectedCardOutput_9} </p>'

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(html_img1, unsafe_allow_html=True)
        st.markdown(html_str1, unsafe_allow_html=True)
        st.markdown(html_img4, unsafe_allow_html=True)
        st.markdown(html_str4, unsafe_allow_html=True)
        st.markdown(html_img7, unsafe_allow_html=True)
        st.markdown(html_str7, unsafe_allow_html=True)
    with col2:
        st.markdown(html_img2, unsafe_allow_html=True)
        st.markdown(html_str2, unsafe_allow_html=True)
        st.markdown(html_img5, unsafe_allow_html=True)
        st.markdown(html_str5, unsafe_allow_html=True)
        st.markdown(html_img8, unsafe_allow_html=True)
        st.markdown(html_str8, unsafe_allow_html=True)
    with col3:
        st.markdown(html_img3, unsafe_allow_html=True)
        st.markdown(html_str3, unsafe_allow_html=True)
        st.markdown(html_img6, unsafe_allow_html=True)
        st.markdown(html_str6, unsafe_allow_html=True)
        st.markdown(html_img9, unsafe_allow_html=True)
        st.markdown(html_str9, unsafe_allow_html=True)
    
    with st.sidebar:
            packsOpenedStr = MSSB.packsOpenedStr
            st.header('Pack Opener Options')
            st.button('Open Next Pack', on_click=set_state, args = [1])
            st.write(MSSB.packsOpenedStr)
            st.button('End This Pack Opening', on_click=set_state, args = [2])
            st.write("Learn more about the MSSB Pack Opener at: https://docs.google.com/document/d/15mSM5e-75sTMnLULELV6tsG4GjSAjoVwGSOdWHuCewE/edit?usp=sharing")
