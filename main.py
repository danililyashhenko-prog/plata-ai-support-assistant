import os
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# OpenAI SDK v1+
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


app = FastAPI(
    title="Plata Support AI",
    description="ИИ-ассистент поддержки банка Plata",
    version="1.0.0",
)

SYSTEM_PROMPT = (
    "Ты — эксперт поддержки банка Plata. "
    "Отвечай вежливо на языке клиента."
)


# ----------------------------
# Request / Response models
# ----------------------------

class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    source: str


# ----------------------------
# OpenAI helper
# ----------------------------

def generate_ai_response(user_question: str) -> str:
    """
    Генерирует ответ через OpenAI API.

    Если API-ключ отсутствует, возвращает mock-ответ,
    что удобно для локальной разработки и портфолио-проекта.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return (
            f"Mock-ответ от поддержки Plata: "
            f"мы получили ваш вопрос '{user_question}'. "
            f"Для получения реального ответа подключите OPENAI_API_KEY."
        )

    if OpenAI is None:
        raise HTTPException(
            status_code=500,
            detail="Пакет openai не установлен. Выполните: pip install openai"
        )

    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_question,
                },
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка при обращении к OpenAI API: {str(exc)}",
        )


# ----------------------------
# API endpoints
# ----------------------------

@app.get("/")
def healthcheck():
    """
    Проверка работоспособности сервиса.
    """
    return {
        "status": "ok",
        "service": "Plata Support AI",
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Основной endpoint для общения с ботом.

    Пример запроса:
    {
        "question": "Как перевести деньги на другую карту?"
    }
    """

    answer = generate_ai_response(request.question)

    return ChatResponse(
        answer=answer,
        source="openai" if os.getenv("OPENAI_API_KEY") else "mock",
    )


# ----------------------------
# Local run
# ----------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
