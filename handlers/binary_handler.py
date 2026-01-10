from ingestion.schemas import DocumentObject
from handlers.binary_schema import BinaryDocument
from handlers.ocr.dispatcher import run_ocr

def handle_binary(doc: DocumentObject) -> BinaryDocument:
    pages = run_ocr(doc)

    return BinaryDocument(
        document_id=doc.document_id,
        pages=pages,
        metadata={
            "source_format": doc.detected_format,
            "mime_type": doc.mime_type
        }
    )
