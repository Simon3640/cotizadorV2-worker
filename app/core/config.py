# app/config.py
from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    ENVIRONMENT: str = Field(...)
    DEBUGGER: bool = Field(..., env="DEBUGGER")

    EXCEPTIONS: dict = {
        "es": {
            400: "Solicitud al servidor incorrecta",
            401: "No autorizado",
            403: "Metodo incorrecto o no permitido",
            404: "No encontrado",
            409: "Conflicto con los datos ingresados",
            422: "Entidad en el esquema no procesable",
            500: "Error interno del servidor",
            "log": "Nombre de usuario o contraseña incorrecta",
            "magaya": "Usuario de magaya no existe",
        },
        "en": {
            400: "Bad request",
            401: "Not authorized",
            403: "Method not allowed",
            404: "Not found",
            409: "Conflict with entered data",
            422: "Unprocessable Entity",
            500: "Internal server error",
            "log": "Incorrect username or password",
            "magaya": "Magaya user does not exist",
        },
    }

   

    AMQP_DSN: str

    SCHEDULE_TIME: int = 20


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
