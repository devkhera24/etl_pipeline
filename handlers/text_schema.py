from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class TextSection:
    section_id: str
    format_type: str
    content: str
    metadata: Dict[str, Any]

@dataclass
class TextDocument:
    document_id: str
    language: str | None
    sections: List[TextSection]
    raw_text: str
