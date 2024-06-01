from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from transformers import pipeline

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Cargar el modelo de análisis de sentimientos
clasificador = pipeline(
    "sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment"
)

@app.get("/analizar")
def analizar_sentimiento_hf(texto: str):
    resultado = clasificador(texto)
    return {
        "texto": texto,
        "label": resultado[0]["label"],
        "score": resultado[0]["score"],
    }
