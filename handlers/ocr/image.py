import uuid
from handlers.binary_schema import Page, Region

def ocr_image(doc):
    return [
        Page(
            page_id=str(uuid.uuid4()),
            page_number=1,
            regions=[
                Region(
                    region_id=str(uuid.uuid4()),
                    text="",
                    bbox=[0, 0, 0, 0],
                    confidence=0.0,
                    metadata={"stub": True}
                )
            ],
            metadata={"image": True}
        )
    ]
