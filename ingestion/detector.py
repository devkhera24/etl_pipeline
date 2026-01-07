import mimetypes
import chardet

def detect_format(source_name, raw_bytes, raw_text):
    mime_type, _ = mimetypes.guess_type(source_name)

    if raw_text is not None:
        return "text", "text/plain", "utf-8"

    encoding = chardet.detect(raw_bytes)["encoding"]

    if mime_type and "pdf" in mime_type:
        return "pdf", mime_type, encoding

    if mime_type and "image" in mime_type:
        return "image", mime_type, encoding

    return "binary", mime_type, encoding
