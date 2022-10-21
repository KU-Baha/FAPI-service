from fastapi import Body, APIRouter
from fastapi.encoders import jsonable_encoder

from app.database.db import client
from app.schemas.advert.categories import Category

router = APIRouter()
db = client.advert


@router.post("/category", response_description="Create category", response_model=Category)
async def login(category: Category = Body(...)):
    user = jsonable_encoder(category)
    return {'user': user}
    # get_user = await db["users"].find_one({"email": user.get("email")})
    # if user.get("password") != get_user.get("password"):
    #     return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content="password or email invalid")
    #
    # return JSONResponse(status_code=status.HTTP_200_OK, content=get_user)
