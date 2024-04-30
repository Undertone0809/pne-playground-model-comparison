import promptulate as pne
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel, Field

load_dotenv()
app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello, Flask!"}


class ChatRequest(BaseModel):
    model: str = Field(..., title="Model name")
    messages: list = Field(..., title="List of messages")


@app.post("/chat/completions")
def api_completion(request: ChatRequest) -> str:
    try:
        response: str = pne.chat(messages=request.messages, model=request.model)
        return response
    except Exception as e:
        print(e)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=4000, log_level="info", reload=True)
