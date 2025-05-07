import streamlit as st

col1,col2 = st.columns([2,3])

with col1:
    st.title('이도경')
with col2:
    st.title('여철준')
    st.checkbox('양정우')

col1.subheader('나는 철이다')
col2.checkbox('나는 금이다')
