print("detector loaded")

import mimetypes
import chardet

TEXT_MIME_PREFIXES = [
    "text/"
]

STRUCTURED_MIME_TYPES = [
    "application/json",
    "text/csv",
    "text/html",
    "application/xml",
    "text/markdown"
]

DOCUMENT_MIME_TYPES = [
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
]

IMAGE_MIME_PREFIXES = [
    "image/"
]

def detect_format(source_name, raw_bytes, raw_text):
    mime_type, _ = mimetypes.guess_type(source_name)

    if raw_text is not None:
        return "text", "text/plain", "utf-8"

    encoding = chardet.detect(raw_bytes)["encoding"]

    if mime_type:
        if any(mime_type.startswith(p) for p in IMAGE_MIME_PREFIXES):
            return "image", mime_type, encoding

        if mime_type in DOCUMENT_MIME_TYPES:
            return "document", mime_type, encoding

        if mime_type in STRUCTURED_MIME_TYPES:
            return "structured", mime_type, encoding

        if any(mime_type.startswith(p) for p in TEXT_MIME_PREFIXES):
            return "text", mime_type, encoding

    return "binary", mime_type, encoding
