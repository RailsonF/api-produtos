from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router


app = FastAPI(title="Catálogo de Produtos")
app.include_router(auth_router)

@app.get("/")
async def health():
    return {"status da API": "ok"}
