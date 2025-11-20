import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])

class RegisterRequest(BaseModel):
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/register")
async def register(data: RegisterRequest):
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(
            f"{settings.SUPABASE_URL}/auth/v1/signup",
            headers={
                "apikey": settings.SUPABASE_ANON_KEY,
                "Content-Type": "application/json",
            },
            json={
                "email": data.email,
                "password": data.password
            }
        )

    if r.status_code >= 400:
        raise HTTPException(r.status_code, r.text)

    return r.json()

@router.post("/login")
async def login(data: LoginRequest):
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(
            f"{settings.SUPABASE_URL}/auth/v1/token?grant_type=password",
            headers={
                "apikey": settings.SUPABASE_ANON_KEY,
                "Content-Type": "application/json",
            },
            json={
                "email": data.email,
                "password": data.password
            }
        )

    if r.status_code >= 400:
        raise HTTPException(r.status_code, r.text)

    return r.json()
