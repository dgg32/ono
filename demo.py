import streamlit as st
from streamlit_chat import message
import requests

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)


st.header("Streamlit Chat - Demo")
st.markdown("[Github](https://github.com/ai-yash/st-chat)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def query(payload):
	response = "hello"
	return response

def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 


user_input = get_text()

if user_input:
    output = query({
        "inputs": {
            "past_user_inputs": st.session_state.past,
            "generated_responses": st.session_state.generated,
            "text": user_input,
        },"parameters": {"repetition_penalty": 1.33},
    })

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    size = len(st.session_state['generated'])
    for i in range(max(size-3, 0), size):
    #for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

