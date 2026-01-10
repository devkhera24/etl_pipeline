import uuid
import json
from handlers.text_schema import TextSection

def _flatten(obj, parent_key="", sep="."):
    items = []

    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.extend(_flatten(v, new_key, sep))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_key = f"{parent_key}[{i}]"
            items.extend(_flatten(v, new_key, sep))
    else:
        items.append((parent_key, obj))

    return items

def parse_json(raw_text: str):
    try:
        data = json.loads(raw_text)
    except Exception:
        return [
            TextSection(
                section_id=str(uuid.uuid4()),
                format_type="json",
                content=raw_text,
                metadata={"invalid_json": True}
            )
        ]

    flattened = _flatten(data)

    sections = []

    for key, value in flattened:
        sections.append(
            TextSection(
                section_id=str(uuid.uuid4()),
                format_type="json",
                content=f"{key}: {value}",
                metadata={
                    "json_path": key,
                    "value": value
                }
            )
        )

    if not sections:
        sections.append(
            TextSection(
                section_id=str(uuid.uuid4()),
                format_type="json",
                content=json.dumps(data, indent=2),
                metadata={"raw": True}
            )
        )

    return sections
