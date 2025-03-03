from fastapi import FastAPI
from backend.routes import upload_routes

app = FastAPI()

app.include_router(upload_routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
