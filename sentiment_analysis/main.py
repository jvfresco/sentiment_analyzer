from fastapi import FastAPI
from .controllers import sentiment

app = FastAPI()

app.include_router(sentiment.router, prefix="/sentiment", tags=["Sentiment Analyzer"])