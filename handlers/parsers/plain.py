import uuid
from handlers.text_schema import TextSection

def parse_plain(raw_text: str):
    chunks = [c.strip() for c in raw_text.split("\n\n") if c.strip()]

    sections = []
    for chunk in chunks:
        sections.append(
            TextSection(
                section_id=str(uuid.uuid4()),
                format_type="text",
                content=chunk,
                metadata={}
            )
        )

    return sections
