def validate_input(detected_format, raw_bytes, raw_text):
    if detected_format == "text" and not raw_text:
        raise ValueError("Empty text input")

    if detected_format != "text" and raw_bytes is None:
        raise ValueError("Binary input missing bytes")

    return True
