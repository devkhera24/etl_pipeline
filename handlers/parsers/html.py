import uuid
from bs4 import BeautifulSoup
from handlers.text_schema import TextSection

BLOCK_TAGS = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li"]

def parse_html(raw_text: str):
    soup = BeautifulSoup(raw_text, "lxml")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    sections = []

    for elem in soup.find_all(BLOCK_TAGS):
        text = elem.get_text(strip=True)
        if not text:
            continue

        sections.append(
            TextSection(
                section_id=str(uuid.uuid4()),
                format_type="html",
                content=text,
                metadata={
                    "tag": elem.name
                }
            )
        )

    if not sections:
        body_text = soup.get_text(separator="\n", strip=True)
        if body_text:
            sections.append(
                TextSection(
                    section_id=str(uuid.uuid4()),
                    format_type="html",
                    content=body_text,
                    metadata={"fallback": True}
                )
            )

    return sections
