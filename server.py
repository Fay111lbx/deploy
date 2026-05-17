import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

@app.get("/bg-pet.mp4")
def serve_video():
    return FileResponse("bg-pet.mp4", media_type="video/mp4")

@app.get("/{full_path:path}")
def catch_all(full_path: str):
    return FileResponse("index.html", media_type="text/html; charset=utf-8")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
