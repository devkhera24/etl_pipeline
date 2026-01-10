import json
import subprocess
from pathlib import Path
import tempfile

def run_chandra_cli(raw_bytes: bytes, document_id: str):
    base_dir = Path("data/ocr_outputs") / document_id
    base_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".bin") as tmp:
        tmp.write(raw_bytes)
        tmp_path = tmp.name

    try:
        cmd = [
        "chandra",
        tmp_path,
        str(base_dir)
    ]


        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )

    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Chandra OCR failed: {e.stderr}"
        )

    finally:
        Path(tmp_path).unlink(missing_ok=True)

    json_path = base_dir / "ocr.json"

    if not json_path.exists():
        raise RuntimeError("Chandra OCR did not produce ocr.json")

    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)
