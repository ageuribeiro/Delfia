from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from typing import Dict

# Criação de um objeto de segurança básico
security = HTTPBasic()

# Criação de um contexto de criptografia para senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Simulação de banco de dados de usuários
fake_users_db: Dict[str, Dict[str, str]] = {
    "user1": {
        "username": "user1",
        "password": pwd_context.hash("password1"),
    },
    "user2": {
        "username": "user2",
        "password": pwd_context.hash("password2"),
    },
}

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha em texto simples corresponde à senha criptografada."""
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db: Dict[str, Dict[str, str]], username: str):
    """Obtém o usuário do banco de dados simulado."""
    return db.get(username)

def authenticate_user(db: Dict[str, Dict[str, str]], username: str, password: str):
    """Autentica o usuário verificando a senha."""
    user = get_user(db, username)
    if not user or not verify_password(password, user["password"]):
        return False
    return user

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    """Obtém o usuário atual a partir das credenciais fornecidas."""
    user = authenticate_user(fake_users_db, credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user