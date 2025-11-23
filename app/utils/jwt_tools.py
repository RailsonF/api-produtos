from jose import jwt

def extract_user_id_from_jwt(auth_header: str) -> str:
    """
    Extrai o user_id (campo 'sub') do JWT de autenticação do Supabase.
    O Front/Swagger envia algo como:
        Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
    Este método pega o token, decodifica sem validar assinatura
    (pois só precisamos do payload) e retorna o valor de 'sub'.
    """

    # Remove o texto "Bearer "
    token = auth_header.split(" ")[1]

    # Obtém o payload do JWT sem validar assinatura
    payload = jwt.get_unverified_claims(token)

    # O Supabase sempre contém o user_id no campo "sub"
    return payload["sub"]
