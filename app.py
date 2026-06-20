import streamlit as st
from utils import get_questions, evaluate_answer

st.set_page_config(page_title="AI Interview Assistant", page_icon="🤖")

st.title("🤖 AI Interview Preparation Assistant")

topic = st.selectbox("Choose Topic", ["Python", "Machine Learning", "Java"])

if st.button("Generate Questions"):
    questions = get_questions(topic)

    st.subheader("Interview Questions:")
    for q in questions:
        st.write("👉", q)

answer = st.text_area("Write your answer here")

if st.button("Evaluate Answer"):
    if answer.strip() == "":
        st.warning("Please write an answer")
    else:
        result = evaluate_answer(answer)
        st.subheader("Result:")
        st.write(result)