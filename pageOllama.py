# %%
import ollama
import streamlit as st
import os

###########################################
#            Helper functions           #
###########################################

def get_ollama_model(model_name):
    try:
        # First check if Ollam service is running
        response = ollama.list()
        if not response or 'models' not in response:
            st.warning("No models found in Ollama response")

        models = [model.model.split(':')[0] for model in response.models]
        if not models:
            st.warning("No models installed. Please install models in the Settings tab")
        return models
    except ConnectionRefusedError:
        st.warning("Can not connect to Ollama. Please ensure Ollama is running on your system")
        return []
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Try running 'ollama serve' in your terminal")
        return []
    
def get_prompt():
    with open("promptTemp.md", "r") as file:
        return file.read()
    

###########################################
#            Streamlit page               #
###########################################

def page_chat():
    st.title("Chat with Ollama")
    st.image("assets/ollama.png", width=200)
    model = st.selectbox("Select a model", 
                              get_ollama_model(""),
                              index = 0,
                              help = "Select the available model to use for chat")
    # Initialize chat history in session state if it doesn't exist
    # --> The system prompt is added to the chat history
    #     The prompt is defined in the Prompts.md file
    #     The prompt is added as the first message in the chat history
    #     The chat history is stored in the session state
    #     The chat history is cleared when the Clear Chat button is clicked

    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Add the pre-defined promt as the first message
        st.session_state.messages.append({"role":"system", "content":get_prompt()})
    
    # Add clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        # Re-add the pre-defined prompt after clearing the chat history
        st.session_state.messages.append({"role":"system", "content":get_prompt()})
        st.rerun()

    # Display the chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt:= st.chat_input("what can I help you with?"):
        # Display the user message in the chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to the caht history
        st.session_state.messages.append({"role":"user", "content":prompt})

        try:
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                response =ollama.chat(
                    model= model, # Use selected model
                    messages = [{"role": m["role"], "content": m["content"]}
                                 for m in st.session_state.messages],
                                 stream=True,
                )
                full_response = ""
                for chunk in response: # Assuming response is an iterable of message chunks
                    full_response += chunk['message']['content']
                    message_placeholder.markdown(full_response)
            
            # Add assistant response to the chat history
            st.session_state.messages.append({"role":"assistant", "content":full_response})
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("make sure Ollama is running locally with the required model.")


if __name__ == "__main__":
    page_chat()




