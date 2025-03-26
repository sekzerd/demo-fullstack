from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from config import Config

CONFIG = Config()

CONFIG.load()
WEB_PATH = CONFIG.web_path
app = FastAPI()


# handle root to index.html
@app.get("/")
async def root():
    return FileResponse(WEB_PATH + "index.html")


# configure web path
app.mount("/", StaticFiles(directory=WEB_PATH), name="static")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host=CONFIG.host, port=CONFIG.port, log_level="info")
