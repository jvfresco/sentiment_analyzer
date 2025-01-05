from fastapi import APIRouter
from sentiment_analysis.domain import TextInput

router = APIRouter()

@router.post("/analyze", summary="Analyzes text sentiment")
def analyze_sentiment(input: TextInput):
    # Expects body {text: string}  #
    return {"sentiment": "ok"}