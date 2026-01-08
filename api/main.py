from fastapi import FastAPI
from api.routes.query import router

app = FastAPI(
    title="Enterprise Knowledge Assistant",
    version="1.0"
)

app.include_router(router)
