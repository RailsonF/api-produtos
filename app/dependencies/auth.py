# from fastapi import Header, HTTPException, status

# async def get_user_token(authorization: str = Header(default=None)):
#     if not authorization or not authorization.lower().startswith("bearer "):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Missing or invalid Authorization header"
#         )
#     return authorization
from fastapi import Header, HTTPException, status

async def get_user_token(authorization: str = Header(..., alias="Authorization")):
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authorization header. Expected: Bearer <token>"
        )
    return authorization
