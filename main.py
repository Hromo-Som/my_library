from contextlib import asynccontextmanager

from database import engine, Model
from fastapi import FastAPI

from models.books import BookModel
from routers.books import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

    yield

app = FastAPI(
    title='MyLibrary',
    lifespan=lifespan
)


app.include_router(router)
