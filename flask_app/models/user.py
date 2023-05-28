from ..config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.users = []
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT id, first_name, last_name FROM users;"
        users = []
        results = connectToMySQL('friendships_schema').query_db(query)
        for row in results:
            if row['id'] == None:
                break
            data = {
                "id": row['id'],
                "first_name": row['first_name'],
                "last_name": row['last_name']
            }
            users.append(cls(row))
        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        return connectToMySQL('friendships_schema').query_db(query, data)
