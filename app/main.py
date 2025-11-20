from fastapi import FastAPI

app = FastAPI(title="Catálogo de Produtos")


@app.get("/")
async def health():
    return {"status da API": "ok"}
