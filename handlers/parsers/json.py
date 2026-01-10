import uuid
from handlers.text_schema import TextSection

def parse_json(raw_text: str):
    return [
        TextSection(
            section_id=str(uuid.uuid4()),
            format_type="json",
            content=raw_text,
            metadata={}
        )
    ]
