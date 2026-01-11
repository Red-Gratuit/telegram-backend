from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Servir les fichiers statiques
app.mount("/static", StaticFiles(directory="static"), name="static")

# Page principale
@app.get("/")
async def root():
    return FileResponse("static/index.html")
