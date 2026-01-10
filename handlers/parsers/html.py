import uuid
from handlers.text_schema import TextSection

def parse_html(raw_text: str):
    return [
        TextSection(
            section_id=str(uuid.uuid4()),
            format_type="html",
            content=raw_text,
            metadata={}
        )
    ]
