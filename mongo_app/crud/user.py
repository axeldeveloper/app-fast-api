from ..db.mongodb import AsyncIOMotorClient
from pydantic import EmailStr
from bson.objectid import ObjectId

from ..core.config import database_name, users_collection_name
from ..models.user import UserInCreate, UserInDB, UserInUpdate, UserInCreated
from datetime import datetime

async def get_user(conn: AsyncIOMotorClient, username: str) -> UserInDB:
    row = await conn[database_name][users_collection_name].find_one({"username": username})
    if row:
        return UserInDB(**row)


async def get_user_by_email(conn: AsyncIOMotorClient, email: EmailStr) -> UserInDB:
    row = await conn[database_name][users_collection_name].find_one({"email": email})
    if row:
        return UserInDB(**row)


async def create_user(conn: AsyncIOMotorClient, user: UserInCreated) -> UserInDB:
    dbuser = UserInDB(**user.dict())

    #article_doc = article.dict()
    #article_doc["slug"] = slug

    #dbuser.username =""
    #dbuser.email =""
    #dbuser.password =""
    dbuser.bio =""
    dbuser.image=""
    dbuser.change_password(user.password)
    dbuser.created_at = datetime.now()
    dbuser.updated_at = datetime.now()

    print( dbuser)

    row = await conn[database_name][users_collection_name].insert_one(dbuser.dict())

    dbuser.id = row.inserted_id
    #dbuser.created_at = ObjectId(dbuser.id ).generation_time
    #dbuser.updated_at = ObjectId(dbuser.id ).generation_time

    return dbuser


async def update_user(conn: AsyncIOMotorClient, username: str, user: UserInUpdate) -> UserInDB:
    dbuser = await get_user(conn, username)

    dbuser.username = user.username or dbuser.username
    dbuser.email = user.email or dbuser.email
    dbuser.bio = user.bio or dbuser.bio
    dbuser.image = user.image or dbuser.image
    if user.password:
        dbuser.change_password(user.password)

    updated_at = await conn[database_name][users_collection_name]\
        .update_one({"username": dbuser.username}, {'$set': dbuser.dict()})
    dbuser.updated_at = updated_at
    return dbuser