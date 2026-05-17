import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

@app.get("/{full_path:path}")
def catch_all(full_path: str):
    # 所有请求都返回 index.html（所有资源已内联为 base64）
    return FileResponse("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
