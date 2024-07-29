import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes

from .agent import configure_agent

app = FastAPI()
add_routes(app, configure_agent(), path="/openai", playground_type="default")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


def dev():
    """Run the FastAPI development server."""
    uvicorn.run("chatbot_demo.app:app", host="0.0.0.0", port=5000, reload=True)
