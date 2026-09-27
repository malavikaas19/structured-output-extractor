import json
import streamlit as st
from pypdf import PdfReader
from extractor import extract_information


st.set_page_config(
    page_title="Structured Output Extractor",
    page_icon="🤖",
    layout="wide"
)


# Custom CSS
st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)


# Title
st.markdown(
    '<div class="main-title">🤖 AI Structured Output Extraction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Convert unstructured documents into validated JSON using Ollama and Pydantic'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# File upload
uploaded_file = st.file_uploader(
    "📄 Upload a TXT or PDF file",
    type=["txt", "pdf"]
)


# Manual text input
text = st.text_area(
    "Or enter unstructured text manually",
    height=250,
    placeholder="""Example:

Rahul Kumar joined ABC Technologies as a
Software Engineer in July 2026.
He works in Bengaluru.
"""
)


# Read uploaded file
if uploaded_file is not None:

    if uploaded_file.name.lower().endswith(".txt"):

        text = uploaded_file.read().decode("utf-8")

    elif uploaded_file.name.lower().endswith(".pdf"):

        pdf = PdfReader(uploaded_file)

        text = ""

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    st.success(f"File uploaded: {uploaded_file.name}")

    st.text_area(
        "📄 Extracted Text",
        text,
        height=250
    )


st.divider()


# Extract information
if st.button("🔍 Extract Information", use_container_width=True):

    if not text.strip():

        st.warning(
            "Please upload a TXT/PDF file or enter some text."
        )

    else:

        with st.spinner(
            "Extracting information using Ollama..."
        ):

            try:

                result = extract_information(text)

                st.success(
                    "Information extracted successfully!"
                )

                st.subheader("📋 Extracted Information")

                # Convert Pydantic model to dictionary
                data = result.model_dump()

                # Display fields in two columns
                col1, col2 = st.columns(2)

                with col1:

                    st.write("👤 **Name**")
                    st.info(data["name"])

                    st.write("🏢 **Company**")
                    st.info(data["company"])

                    st.write("💼 **Role**")
                    st.info(data["role"])

                with col2:

                    st.write("📍 **Location**")
                    st.info(data["location"])

                    st.write("📅 **Joining Date**")
                    st.info(data["joining_date"])


                # JSON output
                st.subheader("🔧 JSON Data")

                st.json(data)


                # Convert to JSON
                json_data = json.dumps(
                    data,
                    indent=4
                )


                # Download JSON
                st.download_button(
                    label="⬇️ Download JSON",
                    data=json_data,
                    file_name="extracted_information.json",
                    mime="application/json"
                )

            except Exception as e:

                st.error(f"Error: {e}")