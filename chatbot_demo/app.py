import uvicorn
from fastapi import FastAPI
from langserve import add_routes

from .agent import configure_agent

app = FastAPI()
add_routes(app, configure_agent(), path="/openai", playground_type="default")


@app.get("/")
async def root():
    return {"message": "Hello World"}


def dev():
    """Run the FastAPI development server."""
    uvicorn.run("chatbot_demo.app:app", host="0.0.0.0", port=5000, reload=True)
