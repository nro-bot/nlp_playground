## Application page for regex playground

import re
import streamlit as st
from utils import get_regexs, get_strings

st.title('Regex Playground')

# st.sidebar.title("How it works")
# st.sidebar.info(
# """
# 1. Paste the text document in the first box. 


# 2. Try Creating a regular expression pattern to fit the word or string that you want to find. For example the twitter handle of Ron Miller - "@[a-z_]+"
# 3. Press Enter - the text **is colored** if your pattern is correct.
# """)

regexs = get_regexs()
strings = get_strings()

# -- UI
sentence = st.text_input('Input your text here:', value=strings[0]) 
pattern = st.text_input('Enter pattern to find here',
                        value=regexs['regex_total_last'])


c_patt = ""
try:
   c_patt = re.compile(pattern)
except Exception as e:
    st.text("Wrong Pattern", e)

findall_results = []
if c_patt:
    findall_results = re.findall(c_patt, sentence)
    

text = sentence
matches = re.finditer(c_patt, text)
counter = 0
listext = list(text)

# Add color to appropriate characters 
for m in matches:
    #listext.insert(i.span()[0]+counter,":blue-background[:red[")
    start = m.span()[0]
    end = m.span()[1]
    listext.insert(start+counter, ':blue[')
    listext.insert(end+1+counter, ']')
    counter +=2 # List has lengthened by two

listext ="".join(listext)


if len(pattern) == 0:
    st.text("Waiting For Pattern")
    st.markdown(sentence)
elif not findall_results: 
    st.text("Pattern Not Found")
    st.markdown(sentence)
else:
    count_message = "Pattern Found at " + str(len(findall_results)) + " location(s)"
    st.text(count_message)
    st.markdown(''+ listext + '')
st.markdown('---')

st.markdown('Now testing all strings...')


st.markdown(':tada: Hope that helped! :cat:')
