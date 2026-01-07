def route(detected_format):
    if detected_format == "text":
        return "text_handler"

    if detected_format in ["pdf", "image"]:
        return "binary_handler"

    return "mixed_handler"
