# implementação da API
# importando as bibliotecas necessárias para uso do sistema

from fastapi import FastAPI, Depends, HTTPException, status,UploadFile,File
from sqlalchemy.orm import Session
from crud import create_document, get_document_by_id, list_documents
from database import SessionLocal, engine
from models import Base
from security import get_current_user

# Inicializa o FastAPI
app = FastAPI()

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para upload de documentos
@app.post("/documents/")
def upload_document(
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_document(file, db)

# Endpoint para listar documentos
@app.get("/documents/")
def read_documents(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return list_documents(db)

# Endpoint para download de documento
@app.get("/documents/{document_id}")
def download_document(
    document_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    document = get_document_by_id(document_id, db)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document
