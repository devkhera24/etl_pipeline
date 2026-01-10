def route(detected_format):
    if detected_format == "text":
        return "text_handler"

    if detected_format == "structured":
        return "text_handler"

    if detected_format in ["image", "document"]:
        return "binary_handler"

    return "mixed_handler"
