from src.services.holders import get_holders
import json

def holders(event, context):
    holders_data = get_holders()

    body = {
        "message": "CHIA COIN - serverlees frame work - DevCristobalvc!",
        "holders": holders_data
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
 
    return response
