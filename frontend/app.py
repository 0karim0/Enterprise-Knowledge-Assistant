import streamlit as st
import requests
from ui_config import APP_TITLE, APP_DESCRIPTION

API_URL = "http://localhost:8000/query"

st.set_page_config(page_title=APP_TITLE, layout="wide")

st.title(APP_TITLE)
st.caption(APP_DESCRIPTION)

question = st.text_input(
    "Ask a question",
    placeholder="How does the deployment pipeline work?"
)

if st.button("Ask") and question:
    with st.spinner("Thinking..."):
        response = requests.post(
            API_URL,
            json={"question": question}
        ).json()

    st.subheader("Answer")
    st.write(response["answer"])

    st.subheader("Confidence")
    st.progress(response["confidence"])

    st.subheader("Sources")
    for cite in response["citations"]:
        st.markdown(f"- **{cite['source']}** (chunk: {cite['chunk_id']})")
