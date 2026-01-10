from ingestion.schemas import DocumentObject
from handlers.text_schema import TextDocument
from handlers.parsers.dispatcher import parse_text

def handle_text(doc: DocumentObject) -> TextDocument:
    raw_text = _extract_text(doc)
    sections = parse_text(raw_text, doc.mime_type)

    return TextDocument(
        document_id=doc.document_id,
        language=doc.language,
        sections=sections,
        raw_text=raw_text
    )

def _extract_text(doc: DocumentObject) -> str:
    if doc.raw_text is not None:
        return doc.raw_text

    return doc.raw_bytes.decode(doc.encoding or "utf-8", errors="ignore")
