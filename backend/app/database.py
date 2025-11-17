from app.config import logger, settings
from motor.motor_asyncio import AsyncIOMotorClient
from urllib.parse import quote_plus


class MongoDB:
    client: AsyncIOMotorClient = None
    database = None


mongodb = MongoDB()


async def connect_to_mongo():
    """
    Connect asynchronously to MongoDB Atlas.
    Safely build URI with encoded credentials.
    """
    try:
        username = quote_plus(settings.mongo_user)
        password = quote_plus(settings.mongo_password)
        cluster = settings.mongo_cluster
        db_name = settings.database_name

        uri = f"mongodb+srv://{username}:{password}@{cluster}/{db_name}?retryWrites=true&w=majority"

        mongodb.client = AsyncIOMotorClient(settings.mongo_connection_url)

        mongodb.database = mongodb.client[db_name]

        logger.info("✅ Connected to MongoDB successfully")

    except Exception as e:
        logger.error(f"❌ MongoDB connection failed: {e}")
        raise e


async def close_mongo_connection():
    """Close the MongoDB client connection."""
    if mongodb.client:
        mongodb.client.close()
        logger.info("🔌 Disconnected from MongoDB")


def get_database():
    """Return the active MongoDB database instance."""
    return mongodb.database
