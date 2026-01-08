from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser Cloudflare Pages (et tests locaux)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # plus tard on restreindra
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/api/ping")
def ping():
    return {"message": "pong"}
