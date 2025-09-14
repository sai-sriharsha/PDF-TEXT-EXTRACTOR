import streamlit as st
import fitz  # PyMuPDF
from io import BytesIO

# Title of the app
st.title("PDF Text Extractor")

# PDF file upload
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Read the uploaded file as a byte stream
    pdf_data = uploaded_file.read()

    # Open the PDF using PyMuPDF
    pdf_document = fitz.open("pdf", pdf_data)

    # Extract text from each page
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    # Show the extracted text (first 1000 characters)
    st.write("### Extracted Text (first 1000 characters):")
    st.text(text[:1000])

    # Option to view all the text
    if st.checkbox("Show full extracted text"):
        st.text(text)

    # Option to search the extracted text
    search_term = st.text_input("Search for a word or phrase in the PDF:")
    if search_term:
        if search_term.lower() in text.lower():
            st.write(f"Found '{search_term}' in the PDF!")
        else:
            st.write(f"'{search_term}' not found in the PDF.")
else:
    st.write("Please upload a PDF file to get started.")