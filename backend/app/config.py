import logging
import time
from logging.config import dictConfig
from typing import Optional

from pydantic_settings import BaseSettings
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class Settings(BaseSettings):
    # =====================
    # 🔹 DATABASE (MongoDB Atlas)
    # =====================
    # You can either define the full MongoDB URI in .env as MONGODB_URL,
    # or define components (user, password, cluster) and assemble it dynamically if you prefer.
    mongodb_url: Optional[str] = None
    mongo_user: Optional[str] = None
    mongo_password: Optional[str] = None
    mongo_cluster: Optional[str] = None
    database_name: str = "splitapp_db"

    # =====================
    # 🔹 JWT Auth
    # =====================
    secret_key: str = "your-super-secret-jwt-key-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30

    # =====================
    # 🔹 Firebase
    # =====================
    firebase_project_id: Optional[str] = None
    firebase_service_account_path: str = (
        r"C:\Projects_Magi\Portfolio projects\3. Splitwiser\backend\config\splitapp-756d5-firebase-adminsdk-fbsvc-2dc320326e.json"
    )

    # Optional: for environment-variable-based Firebase configs
    firebase_type: Optional[str] = None
    firebase_private_key_id: Optional[str] = None
    firebase_private_key: Optional[str] = None
    firebase_client_email: Optional[str] = None
    firebase_client_id: Optional[str] = None
    firebase_auth_uri: Optional[str] = None
    firebase_token_uri: Optional[str] = None
    firebase_auth_provider_x509_cert_url: Optional[str] = None
    firebase_client_x509_cert_url: Optional[str] = None

    # =====================
    # 🔹 App & CORS
    # =====================
    debug: bool = False
    allowed_origins: str = (
        "http://localhost:3000,http://localhost:5173,http://127.0.0.1:3000,http://localhost:8081"
    )
    allow_all_origins: bool = False

    class Config:
        env_file = ".env"
        extra = "ignore"  # 👈 Prevents “extra inputs not permitted” errors

    # =====================
    # 🔹 Helper: build Mongo URI dynamically if needed
    # =====================
    @property
    def mongo_connection_url(self) -> str:
        """
        Returns a valid MongoDB connection URI for Motor (AsyncIOMotorClient).
        If mongodb_url is provided, uses it directly.
        Otherwise, builds a standard MongoDB Atlas URI.
        """
        if self.mongodb_url:
            return self.mongodb_url

        if self.mongo_user and self.mongo_password and self.mongo_cluster:
            from urllib.parse import quote_plus

            user = quote_plus(self.mongo_user)
            password = quote_plus(self.mongo_password)
            cluster = self.mongo_cluster
            return f"mongodb+srv://{user}:{password}@{cluster}/{self.database_name}?retryWrites=true&w=majority"

        raise ValueError("MongoDB connection info is missing in environment variables.")


settings = Settings()

# =====================
# 🔹 Logging
# =====================
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {"format": "%(asctime)s - %(levelname)s - %(message)s"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "default"},
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("Splitwiser")


# =====================
# 🔹 Request/Response Logging Middleware
# =====================
class RequestResponseLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger = logging.getLogger("Splitwiser")
        logger.info(f"Incoming request: {request.method} {request.url}")

        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        logger.info(
            f"Response status: {response.status_code} for {request.method} {request.url}"
        )
        logger.info(f"Response time: {process_time:.2f} seconds")

        return response
