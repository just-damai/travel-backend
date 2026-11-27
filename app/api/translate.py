from fastapi import APIRouter

from app.schemas import TranslateRequest, TranslateResponse
from app.services.translator import translate

router = APIRouter()

@router.post("/translate", response_model=TranslateResponse)
def translate_endpoint(request: TranslateRequest):
    result = translate(text=request.text, emotion=request.emotion)
    return TranslateResponse(
        original=request.text,
        translation=result,
        emotion=request.emotion,
    )