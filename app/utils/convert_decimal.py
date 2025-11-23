from decimal import Decimal

def serialize_payload(payload: dict):
    for k, v in payload.items():
        if isinstance(v, Decimal):
            payload[k] = float(v)
    return payload
