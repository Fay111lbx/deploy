import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()
app.mount("/萌宠形象", StaticFiles(directory="萌宠形象"), name="images")

@app.get("/{full_path:path}")
def catch_all(full_path: str):
    return FileResponse("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
