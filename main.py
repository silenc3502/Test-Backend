from fastapi import FastAPI

from app.core.config import settings
from app.routers import items

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(items.router)


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
