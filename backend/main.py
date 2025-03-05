import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from backend.routes import upload_route

app = FastAPI()

app.include_router(upload_routes.router)  # Ensure the variable name is correct

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)  # Corrected Uvicorn path
