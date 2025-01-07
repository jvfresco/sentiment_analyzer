from fastapi import APIRouter
from ..domain import TextInput
from ..infrastructure import get_sentiment_service

router = APIRouter()

sentiment_service = get_sentiment_service()

@router.post("/analyze", summary="Analyzes text sentiment")
def analyze_sentiment(input: TextInput):
    # Expects body {text: string}  #
    result = sentiment_service.analyze(input.text)
    return {"sentiment": result}