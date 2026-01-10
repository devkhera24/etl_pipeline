from handlers.ocr.image import ocr_image
from handlers.ocr.pdf import ocr_pdf

def run_ocr(doc):
    if doc.detected_format == "image":
        return ocr_image(doc)

    if doc.detected_format == "document":
        return ocr_pdf(doc)

    raise ValueError("Unsupported binary format")
