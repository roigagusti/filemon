import requests

class Airtable:
    def __init__(self, token, base_id):
        self.token = token
        self.base_id = base_id

    def list(self, table, max_records=500, view='API',fields=None,filter=None):
        url = f'https://api.airtable.com/v0/{self.base_id}/{table}'
        params = {
            'maxRecords': max_records,
            'view': view
        }
        if filter != None:
            params['filterByFormula'] = filter
        if fields != None:
            for field in fields:
                params['fields[]'] = field
            
        data = []

        while True:
            response = requests.get(url, params=params, headers={'Authorization': 'Bearer ' + self.token})
            response_data = response.json()
            data.extend(response_data.get('records', []))
            offset = response_data.get('offset', None)
            if not offset:
                break
            params['offset'] = offset

        return {'records': data}
    
    def insert(self, table, data):
        url = f'https://api.airtable.com/v0/{self.base_id}/{table}'
        response = requests.post(url, json={'fields': data}, headers={'Authorization': 'Bearer ' + self.token})
        return response.json()