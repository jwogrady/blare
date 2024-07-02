
from blare.utils import request

def packages_getlist(page, status):
    model = 'packages/'
    action = 'getlist'
    params = {'page': page, 'status': status}
    resp = request(model=model, action=action, params=params)
    return resp

def packages_getall(company_id, status):
    model = 'packages/'
    action = 'getall'
    params = {'company_id': company_id, 'status': status}
    resp = request(model=model, action=action, params=params)
    return resp