from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Region:
    region_id: str
    text: str
    bbox: List[int]
    confidence: float
    metadata: Dict[str, Any]

@dataclass
class Page:
    page_id: str
    page_number: int
    regions: List[Region]
    metadata: Dict[str, Any]

@dataclass
class BinaryDocument:
    document_id: str
    pages: List[Page]
    metadata: Dict[str, Any]
