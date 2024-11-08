import streamlit as st
import requests

# Streamlit app title and description
st.title("Text Summarization App")
st.write("Enter a passage and get a concise summary using the Text Summarization API.")

# Input text area for user to paste text
text = st.text_area("Enter text to summarize", height=200, placeholder="Paste or type text here...")

# Button to trigger the summarization
if st.button("Summarize"):
    if text.strip():  # Ensure text is not empty
        with st.spinner("Generating summary..."):
            try:
                # Make a request to the FastAPI predict endpoint
                response = requests.post("http://localhost:8000/predict", json={"text": text})
                
                if response.status_code == 200:
                    summary = response.json().get("summary", "No summary available.")
                    # Display the summary in a box
                    st.subheader("Summary")
                    st.write(summary)
                else:
                    st.error("Error: Could not get a summary. Please try again later.")
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred while connecting to the API: {e}")
    else:
        st.warning("Please enter some text to summarize.")
