## Application page for regex playground
# Must NEVER include private data -- only filepaths!

import re
import streamlit as st
from utils import get_regexs, get_strings

st.title('NLP Playground')

st.sidebar.title("How it works")
st.sidebar.info(
"""
1. Paste the text document in the first box. 

2. Enter a regex pattern  

3. Press Enter to see the results. 
The text **is colored** if your pattern is correct (produces nonzero matches)
""")

regexs = get_regexs()
test_strings = get_strings()

# -- UI


def get_results(text: str) ->  tuple[list[re.Match], list[str]]:
    findall_results = []
    if c_patt:
        findall_results = re.findall(c_patt, text)
        
    m = re.search(c_patt, text) # re.finiter returns all matches
    counter = 0
    pprint_results = list(text)

# Add color to appropriate characters 
    if m: 
        gl1, gl2, gl = [str(digit) for digit in m.groups()]
        start = m.span()[0]
        end = m.span()[1]
        pprint_results.insert(start+counter, ':red-background[')
        pprint_results.insert(end+1+counter, ']')
        counter +=2 # List has lengthened by two

    pprint_results ="".join(pprint_results)
    return findall_results, pprint_results, [gl1, gl2, gl] if m else []


sentence = st.text_input('Hello! Input your text here:', value=test_strings[0]) 
pattern = st.text_input(
'Enter pattern to find here. **NOTE: must contain three groups**',
                        value=regexs['regex_total_last'])
c_patt = ""
HACK_FLAG = False 
try:
   c_patt = re.compile(pattern)
except Exception as e:
    st.text(f"Oops! Bad regex input. Error message:: {e}")
    HACK_FLAG = True

if not HACK_FLAG:

    findall_results, pprint_results, m = get_results(sentence)
    if len(pattern) == 0:
        st.text("Waiting For Pattern")
        st.markdown(sentence)
    elif not findall_results: 
        st.text("Pattern Not Found")
        st.markdown(sentence)
    else:
        count_message = "Pattern Found at **" + str(len(findall_results)) + "** location(s)"
        st.markdown(count_message)
        st.markdown(''+ pprint_results + '')
    st.markdown('---')
    st.markdown('## Full test')

    for text in test_strings:
        findall_results, pprint_results, m = get_results(text)
        num = str(len(findall_results)) 
        scores = ', '.join(m)
        if num == str(0):
            st.markdown(f':red-background[NO results] |  {pprint_results}')
            continue
        elif num == str(1):
            st.markdown(
                f':green-background[{num:0>2}] results | '
                f'{pprint_results} |'
                f' {scores}'
            )
        else:
            st.markdown(
                f':red-background[{num:0>2}] results | ' 
                f'{pprint_results} |'
                f' {scores}'
            )

    st.markdown('---')
    st.markdown('*Hope that helped! :cat:*')
