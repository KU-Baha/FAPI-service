from fastapi import FastAPI
import uvicorn

from app.api.users import router as user_router
from app.api.adverts import router as advert_router

app = FastAPI(openapi_url="/api/v1/users/openapi.json", docs_url="/api/v1/users/docs")

app.include_router(user_router, prefix="/api/v1/users", tags=["users"])
app.include_router(advert_router, prefix="/api/v1/advert", tags=["advert"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
