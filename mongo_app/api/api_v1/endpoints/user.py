from fastapi import APIRouter, Body, Depends

from ....core.jwt import get_current_user_authorizer
from ....crud.shortcuts import check_free_username_and_email
from ....crud.user import update_user, create_user
from ....db.mongodb import AsyncIOMotorClient, get_database
from ....models.user import User, UserInResponse, UserInUpdate, UserInCreate

router = APIRouter()


@router.get("/user", response_model=UserInResponse, tags=["users"])
async def retrieve_current_user(user: User = Depends(get_current_user_authorizer())):
    
    return UserInResponse(user=user)


@router.post("/user", response_model=UserInResponse, tags=["users"])
async def create_current_user(
    user: UserInCreate = Body(..., embed=True),
    db: AsyncIOMotorClient = Depends(get_database)
    ):
    
   
    dbuser = await create_user(db, user)

    return UserInResponse(user=user)



@router.put("/user", response_model=UserInResponse, tags=["users"])
async def update_current_user(
    user: UserInUpdate = Body(..., embed=True),
    current_user: User = Depends(get_current_user_authorizer()),
    db: AsyncIOMotorClient = Depends(get_database),
):
    if user.username == current_user.username:
        user.username = None
    if user.email == current_user.email:
        user.email = None

    await check_free_username_and_email(db, user.username, user.email)

    dbuser = await update_user(db, current_user.username, user)
    return UserInResponse(user=User(**dbuser.dict(), token=current_user.token))