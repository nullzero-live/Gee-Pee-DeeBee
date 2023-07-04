from docs import *
from vector_store import *
import streamlit as st


#specify root directory to search for pdfs
root_directory = "./" #st.text_input("Enter the root directory to search for PDFs")

pdf_list = find_pdfs(root_directory)

docs_dic=convert_docs_fordb(pdf_list)
chunked_annual_reports, pdf_list = doc_handler()
upload_database(docs_dic)
convert_docs_fordb(pdf_list)
chunker(pdf_list)

# Initialize chat history list
'''chat_questions = []
chat_answers = []
chat_history = []

query = "What was Gradient Institutes Revenue in 2021? Format as $"
result = qa({"question": query, "chat_history": chat_history})

chat_history.append((query, result["answer"]))

chat_history
'''