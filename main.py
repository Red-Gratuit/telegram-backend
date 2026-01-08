from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser Cloudflare Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/api/init")
async def init(request: Request):
    data = await request.json()
    return {
        "message": "Mini App connectée à Python",
        "data": data
    }
