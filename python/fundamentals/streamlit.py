import streamlit as st

# https://docs.streamlit.io/library/api-reference/
#
# st.title("This is the title")
# st.header("This is the header")
# st.text("This is the regulat text")
#
# some_dictionary = {
#     "Key": "Value",
#     "Key2": "Value2"
# }
#
# some_list = [1, 2, 3]
# some_another_dictionary = {
#     "key": "value",
#     "key2": "value2"
# }

option = st.sidebar.write("Options")

st.write(option)
