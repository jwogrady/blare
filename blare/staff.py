from blare.utils import request

def staff_get(params):
    model ='staff/'
    action = 'get'
    resp = request(model=model, action=action, params=params)
    return resp

def staff_getlist(params):
    model ='staff/'
    action = 'getlist'
    resp = request(model=model, action=action, params=params)
    return resp