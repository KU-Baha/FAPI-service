from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.schemas.user.users import CreateUser, SignInUser
from app.database.db import client

router = APIRouter()
db = client.users


@router.post(
    "/signUp", response_description="register new user", response_model=CreateUser
)
async def register(user: CreateUser = Body(...)):
    if not user.is_valid():
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN, content="Passwords do not match"
        )

    user = jsonable_encoder(user)
    new_user = await db["users"].insert_one(user)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


@router.post("/signIn", response_description="login user", response_model=SignInUser)
async def login(user: SignInUser = Body(...)):
    user = jsonable_encoder(user)
    get_user = await db["users"].find_one({"email": user.get("email")})
    if user.get("password") != get_user.get("password"):
         return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content="password or email invalid")

    return JSONResponse(status_code=status.HTTP_200_OK, content=get_user)
