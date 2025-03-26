from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse,FileResponse


WEB_PATH = "../web/"
app = FastAPI()

# handle root to index.html
@app.get("/")
async def root():
    return FileResponse(WEB_PATH + "index.html")

# configure web path
app.mount("/", StaticFiles(directory=WEB_PATH), name="static")

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info")