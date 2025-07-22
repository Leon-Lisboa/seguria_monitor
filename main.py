from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="SegurIA Monitor - API")
app.include_router(router)