from blare import request

def get(payload):
    model ='staff/'
    action = 'get'
    resp = request(model=model, action=action, payload=payload)
    return resp

def getlist(payload):
    model ='staff/'
    action = 'getlist'
    resp = request(model=model, action=action, payload=payload)
    return resp