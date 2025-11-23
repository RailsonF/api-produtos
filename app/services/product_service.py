import httpx
from app.config import settings
from app.utils.convert_decimal import serialize_payload

POSTGREST = f"{settings.SUPABASE_URL}/rest/v1"

async def list_products(auth: str, user_id: str):
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(
            f"{POSTGREST}/{settings.TABLE_PRODUCTS}",
            headers={
                "apikey": settings.SUPABASE_ANON_KEY,
                "Authorization": auth,
                "Accept": "application/json"
            },
            params={
                "select": "*",
                "user_id": f"eq.{user_id}",
                "order": "id.desc"
            }
        )

    if r.status_code >= 400:
        raise Exception(r.text)
    return r.json()


async def create_product(auth: str, payload: dict, user_id: str):
    payload["user_id"] = user_id
    payload = serialize_payload(payload)

    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(
            f"{POSTGREST}/{settings.TABLE_PRODUCTS}",
            headers={
                "apikey": settings.SUPABASE_ANON_KEY,
                "Authorization": auth,
                "Content-Type": "application/json",
                "Prefer": "return=representation"
            },
            json=payload
        )

    if r.status_code >= 400:
        raise Exception(r.text)
    return r.json()


async def update_product(auth: str, product_id: int, payload: dict, user_id: str):
    payload = serialize_payload(payload),
    
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.patch(
            f"{POSTGREST}/{settings.TABLE_PRODUCTS}",
            headers={
                "apikey": settings.SUPABASE_ANON_KEY,
                "Authorization": auth,
                "Content-Type": "application/json",
                "Prefer": "return=representation"
            },
            params={"id": f"eq.{product_id}", "user_id": f"eq.{user_id}"},
            json=payload
        )

    if r.status_code >= 400:
        raise Exception(r.text)
    return r.json()


async def delete_product(auth: str, product_id: int, user_id: str):
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.delete(
            f"{POSTGREST}/{settings.TABLE_PRODUCTS}",
            headers={
                "apikey": settings.SUPABASE_ANON_KEY,
                "Authorization": auth
            },
            params={"id": f"eq.{product_id}", "user_id": f"eq.{user_id}"}
        )

    if r.status_code >= 400:
        raise Exception(r.text)

    return {"message": "Produto removido com sucesso"}
