from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from app.routes.auth_routes import router as auth_router
from app.routes.products_routes import router as products_router

app = FastAPI(title="Catálogo de Produtos")

bearer_schema = HTTPBearer()

app.include_router(auth_router)
app.include_router(products_router, dependencies=[Depends(bearer_schema)])

@app.get("/")
async def health():
    return {"status da API": "ok"}
