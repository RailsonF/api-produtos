from fastapi import APIRouter, Depends
from app.schemas.product_schemas import ProductCreate, ProductUpdate
from app.dependencies.auth import get_user_token
from app.services.product_service import list_products, create_product, update_product, delete_product
from app.utils.jwt_tools import extract_user_id_from_jwt



router = APIRouter(prefix="/products", tags=["products"])

def get_user_id_from_token(auth: str):
    # O payload do JWT do Supabase contém "sub" = user_id
    return extract_user_id_from_jwt(auth)  # frente cuidará de decodificar se precisar
    # MAS podemos melhorar isso depois

@router.get("/")
async def route_list(auth=Depends(get_user_token)):
    user_id = get_user_id_from_token(auth)
    return await list_products(auth, user_id)


@router.post("/", status_code=201)
async def route_create(payload: ProductCreate, auth=Depends(get_user_token)):
    user_id = get_user_id_from_token(auth)
    return await create_product(auth, payload.model_dump(), user_id)


@router.patch("/{product_id}")
async def route_update(product_id: int, payload: ProductUpdate, auth=Depends(get_user_token)):
    user_id = get_user_id_from_token(auth)
    data = {k: v for k, v in payload.model_dump().items() if v is not None}
    return await update_product(auth, product_id, data, user_id)


@router.delete("/{product_id}")
async def route_delete(product_id: int, auth=Depends(get_user_token)):
    user_id = get_user_id_from_token(auth)
    return await delete_product(auth, product_id, user_id)
