import uuid
import csv
from io import StringIO
from handlers.text_schema import TextSection

def parse_csv(raw_text: str):
    reader = csv.reader(StringIO(raw_text))
    rows = list(reader)

    if not rows:
        return []

    header = rows[0]
    data_rows = rows[1:] if len(rows) > 1 else []

    sections = []

    for idx, row in enumerate(data_rows):
        row_dict = {
            header[i]: row[i] if i < len(row) else ""
            for i in range(len(header))
        }

        content = " | ".join(
            f"{key}: {value}" for key, value in row_dict.items()
        )

        sections.append(
            TextSection(
                section_id=str(uuid.uuid4()),
                format_type="csv",
                content=content,
                metadata={
                    "row_index": idx,
                    "columns": header,
                    "row": row_dict
                }
            )
        )

    if not sections and header:
        sections.append(
            TextSection(
                section_id=str(uuid.uuid4()),
                format_type="csv",
                content=", ".join(header),
                metadata={"header_only": True}
            )
        )

    return sections
