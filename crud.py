from sqlalchemy.orm import Session
from models import Document
from schemas import DocumentCreate
from fastapi import UploadFile

def create_document(file: UploadFile, db: Session):
    # Implementar lógica para criptografar e armazenar o documento
    pass

def get_document_by_id(document_id: int, db: Session):
    return db.query(Document).filter(Document.id == document_id).first()

def list_documents(db: Session):
    return db.query(Document).all()
