from pydantic import BaseModel

class DocumentCreate(BaseModel):
    filename: str
    file_data: bytes
