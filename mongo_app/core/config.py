import os

from dotenv import load_dotenv
from starlette.datastructures import CommaSeparatedStrings, Secret
from databases import DatabaseURL
import urllib.parse


API_V1_STR = "/api"

JWT_TOKEN_PREFIX = "Token"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week

load_dotenv(".env")

MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))
SECRET_KEY = Secret(os.getenv("SECRET_KEY", "123456"))

PROJECT_NAME = os.getenv("PROJECT_NAME", "FastAPI example application")
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))

MONGODB_URL = os.getenv("MONGODB_URL", "")  # deploying without docker-compose
#MONGODB_URL = os.getenv("DB_CONNECTION", "")  # deploying without docker-compose


if not MONGODB_URL:
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_USER = os.getenv("MONGO_USER", "admin")
    MONGO_PASS = os.getenv("MONGO_PASSWORD", "markqiu")
    MONGO_DB = os.getenv("MONGO_DB", "fastapi")

    MONGODB_URL = DatabaseURL(
        f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    )
else:
    print("else" , MONGODB_URL)
    username = urllib.parse.quote_plus('axel')
    password = urllib.parse.quote_plus("Axel@193")
    #MONGODB_URL=mongodb+srv://axel:Axel@193@cluster0.lqmxu.mongodb.net/test?retryWrites=true&w=majority
    url = "mongodb+srv://{}:{}@cluster0.lqmxu.mongodb.net/test?retryWrites=true&w=majority".format(username, password)
    # MONGODB_URL = DatabaseURL(MONGODB_URL)
    MONGODB_URL = DatabaseURL(url)

MONGO_DB = os.getenv("MONGO_DB", "")

print("DN" , MONGO_DB) 

#database_name = "test"
database_name = MONGO_DB
article_collection_name = "articles"
favorites_collection_name = "favorites"
tags_collection_name = "tags"
users_collection_name = "users"
comments_collection_name = "commentaries"
followers_collection_name = "followers"