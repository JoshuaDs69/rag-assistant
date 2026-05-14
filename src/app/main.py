from fastapi import FastAPI

from src.app.api.routes import router


app = FastAPI()


@app.get("/")
def healthcheck():
    return {"status": "ok"}


app.include_router(router)