import requests
def geocode(address):
    parameters = {'address': address, 'key': '2a5845d4c0e5bc3fdc0485dabcf68e46'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    answer = response.json()
    if answer['count'] == '0':
        return "error", "", "", ""
    dz = answer['geocodes'][0]['formatted_address']
    qu = answer['geocodes'][0]['city'] + answer['geocodes'][0]['district']
    adcode = answer['geocodes'][0]['adcode']
    location = answer['geocodes'][0]['location']
    return dz, qu, adcode, location

print(geocode('华中农业大学'))
