import streamlit as st
from streamlit_chat import message

import pandas as pd
from graph2text import generate_response

from neo4j_driver import run_query
from english2cypher import generate_cypher

st.set_page_config(layout="wide")
st.title("Onomatopoeia dictionary")

def generate_context(prompt, context_data='generated'):
    context = []
    # If any history exists
    if "generated" in st.session_state:
        # Add the last three exchanges
        size = len(st.session_state['generated'])
        for i in range(max(size-5, 0), size):
            context.append(
                {'role': 'user', 'content': st.session_state['user_input'][i]})
            context.append(
                {'role': 'assistant', 'content': st.session_state[context_data][i]})
    # Add the latest user prompt
    context.append({'role': 'user', 'content': str(prompt)})
    return context

def get_text():
    input_text = st.text_input(
        "AMA about onomatopoeia", "", key="input")
    return input_text

user_input = get_text()


# Generated natural language
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
# Neo4j database results
if 'database_results' not in st.session_state:
    st.session_state['database_results'] = []
# User input
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = []
# Generated Cypher statements
if 'cypher' not in st.session_state:
    st.session_state['cypher'] = []

if user_input:

    cypher = generate_cypher(generate_context(user_input, 'database_results'))
    # st.session_state.user_input.append(user_input)
    # st.session_state.cypher.append("")
    # st.session_state.database_results.append("")
    # st.session_state.generated.append(cypher)

    if not "MATCH" in cypher:
        print('No Cypher was returned')
        st.session_state.user_input.append(user_input)
        st.session_state.generated.append(
            cypher)
        st.session_state.cypher.append(
            "No Cypher statement was generated")
        st.session_state.database_results.append("")
    else:
        # Query the database, user ID is hardcoded
        results = run_query(cypher)
        results = results[:10]
        # Graph2text
        answer = generate_response(generate_context(
            f"Question was {user_input} and the response should include only information that is given here: {str(results)}"))
        st.session_state.database_results.append(str(results))
        st.session_state.user_input.append(user_input)
        st.session_state.generated.append(answer)
        st.session_state.cypher.append(cypher)




if st.session_state['generated']:
    size = len(st.session_state['generated'])
    # Display only the last three exchanges

    for i in range(max(size-4, 0), size):
    #for i in range(len(st.session_state['generated'])-1, -1, -1):
        if st.session_state['user_input'][i]:

            message(st.session_state['user_input'][i],is_user=True, key=str(i) + '_user')
        
        if st.session_state["generated"][i]:

            message(st.session_state["generated"][i], key=str(i))
