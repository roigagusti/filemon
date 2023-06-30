import requests
#import mysql.connector
     

class RompetechosAPI():
    def __init__(self,api_key,api_token):
        self.api_key = api_key
        self.api_token = api_token
    
    def regenToken(self):
        url = "https://www.rompetechos.011h.com/support/admin/user/auth/regenerate_jwtoken"
        header = {'X-Api-Key': self.api_key, 'X-Api-Token': self.api_token}
        body = {"token": self.api_token}
        response = requests.post(url, json=body)
        data = response.json()
        return data
    
    def get(self,component=''):
        if component == '':
            url = 'https://api.rompetechos.011h.com/v1/buildplatf/component/component-type?model_type=library&codes=eq%3A'
        else:
            url = 'https://api.rompetechos.011h.com/v1/buildplatf/component/component-type?model_type=library&code=eq%3A'+component
        header = {'x-api-key': self.api_key, 'x-api-token': self.api_token}
        response = requests.get(url, headers=header)
        data = response.json()
        return data


# class RompetechosDEV:
#     def __init__(self, credentials):
#         self.host, self.database, self.user, self.password, self.port = credentials

#     def connect(self):
#         try:
#             connection = mysql.connector.connect(
#                 host=self.host,
#                 database=self.database,
#                 user=self.user,
#                 password=self.password,
#                 port=self.port
#             )
#             print("Connected to the database successfully!")
#             return connection
#         except (Exception, mysql.connector.Error) as error:
#             print("Error while connecting to the database:", error)
#             return None

#     def list(self, table, columns=None, where=None, order_by=None, limit=None):
#         connection = self.connect()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 query = f"SELECT {', '.join(columns) if columns else '*'} FROM {table}"
#                 if where:
#                     query += f" WHERE {where}"
#                 if order_by:
#                     query += f" ORDER BY {order_by}"
#                 if limit:
#                     query += f" LIMIT {limit}"
#                 cursor.execute(query)
#                 rows = cursor.fetchall()
#                 return rows
#             except (Exception, mysql.connector.Error) as error:
#                 print("Error while fetching data from the database:", error)
#             finally:
#                 if cursor:
#                     cursor.close()
#                 connection.close()
#                 print("Connection to the database closed.")
#         else:
#             return None