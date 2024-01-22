from blare import request

def get(params):
    model ='staff/'
    action = 'get'
    resp = request(model=model, action=action, params=params)
    return resp

def getlist(params):
    model ='staff/'
    action = 'getlist'
    resp = request(model=model, action=action, params=params)
    return resp