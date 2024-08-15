from sqlalchemy import Column, Integer, String, LargeBinary
from database import Base

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    file_data = Column(LargeBinary)