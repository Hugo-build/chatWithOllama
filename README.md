# Chat with Ollama


## 1. Introduction
This is a simple chatbot application that allows you to chat with Ollama.

<img src="assets/ollama.png" alt="drawing" width="100"/>

Ollama is a lightweight, open-source, and easy-to-use chatbot framework. 
Ollama supports a list of models available on [ollama.com/library](https://ollama.com/library 'ollama model library')



**Newest models:** (Note: The deepseek-r1 model is the model with reasoning ability)

| Model              | Parameters | Size  | Download                       |
| ------------------ | ---------- | ----- | ------------------------------ |
| deepseek-r1        | 1.5B       | 1.1GB | `ollama run deepseek-r1:1.5b`  |
| deepseek-r1        | 7B         | 4.7GB | `ollama run deepseek-r1:7b`    |
| phi4               | 14B        | 9.1GB | `ollama run phi4`              |
| qwen2.5            | 7B         | 1.9GB | `ollama run qwen2.5`           |
| qwen2.5            | 3B         | 986MB | `ollama run qwen2.5:3b`        |
| qwen2.5            | 1.5B       | 986MB | `ollama run qwen2.5:1.5b`      |
| Llama 3.2          | 3B         | 2.0GB | `ollama run llama3.2`          |
| Llama 3.2          | 1B         | 1.3GB | `ollama run llama3.2:1b`       |
| Llama 3.1          | 8B         | 4.7GB | `ollama run llama3.1`          |




<img src="assets/streamlit.png" alt="drawing" width="150"/>

Streamlit is a Python library for building web applications.
The website can be found as [streamlit.io](https://streamlit.io 'streamlit website')



## 2. Usage
### Prerequisites

Install Ollama from [ollama.ai](https://ollama.ai 'ollama website'), and open at background.

### Run a chat page
1. Install the required packages
   ```
   pip install ollama streamlit
   ```
2. Run the page for chat
   ```
   streamlit run pageOllama.py
   ```
3. Chat with Ollama


### Additions
Can add the pre-defined prompt within 'promptTemp.md' file for instructing the AI model.