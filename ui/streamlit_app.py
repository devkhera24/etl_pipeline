import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
from ingestion.loader import ingest

st.set_page_config(page_title="ETL Ingestion")

st.title("ETL Pipeline — Ingestion")

uploaded_file = st.file_uploader(
    "Upload file",
    type=["txt", "pdf", "png", "jpg", "jpeg", "html", "csv", "json", "md", "docx", "webp"]
)

text_input = st.text_area("Or paste text")

if st.button("Run Ingestion"):
    try:
        doc = ingest(file=uploaded_file, text=text_input)

        st.write("FORMAT:", doc.detected_format)
        st.write("MIME:", doc.mime_type)
        st.write("ROUTE:", doc.routing_target)

        st.json({
            "document_id": doc.document_id,
            "detected_format": doc.detected_format,
            "mime_type": doc.mime_type,
            "encoding": doc.encoding,
            "routing_target": doc.routing_target,
            "metadata": doc.metadata
        })

    except Exception as e:
        st.error(str(e))
