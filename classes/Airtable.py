import requests


class Airtable():
    def __init__(self,token,base_id):
        self.token = token
        self.base_id = base_id

    def list(self, table, maxrecords=100, view='API'):
        url = 'https://api.airtable.com/v0/' + self.base_id + '/' + table
        numero = '?maxRecords=' + str(maxrecords)
        grid = '&view='+view
        fields = ''
        filtre = ''
        sort = ''
        
        rest = url + numero + grid + fields + filtre + sort
        key = 'Bearer ' + self.token
        header = {'Authorization': key}
        response = requests.get(rest, headers=header)
        data = response.json()
        return data