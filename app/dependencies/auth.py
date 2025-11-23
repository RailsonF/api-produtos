from fastapi import Header, HTTPException, status

async def get_user_token(authorization: str = Header(..., alias="Authorization")):
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Header da autorização inválido. Experado: Bearer <token>"
        )
    return authorization
