from distutils.command.config import config
from pydantic import BaseSettings
from typing import Optional
from dotenv import load_dotenv

#Criando classe de configuração para chamar URI, que é uma str, para conectar com o banco de dados
class Config(BaseSettings):
    DATABASE_URI: Optional[str] = None
    
    
#a classe carrega as variaveis declaradas no .env
def start_config():
    load_dotenv()
    return Config()



config = start_config()