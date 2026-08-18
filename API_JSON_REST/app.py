from fastapi import FastAPI
import uvicorn
from routes import router as items_router

app = FastAPI(title="Items API")

app.include_router(items_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)