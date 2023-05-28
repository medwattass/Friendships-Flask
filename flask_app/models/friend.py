from ..config.mysqlconnection import connectToMySQL


class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.friend_first_name = data['friend_first_name']
        self.friend_last_name = data['friend_last_name']
        self.users_with_friends = []

    @classmethod
    def get_all_users_with_friends(cls):
        query = "SELECT users.id AS id, users.first_name AS first_name, users.last_name AS last_name, friends.first_name AS friend_first_name, friends.last_name AS friend_last_name FROM friendships LEFT JOIN users ON friendships.user_id = users.id LEFT JOIN users AS friends ON friendships.friend_id = friends.id;"
        users_with_friends = []
        results = connectToMySQL('friendships_schema').query_db(query)
        for row in results:
            if row['id'] == None:
                break
            data = {
                "id": row['id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "friend_first_name": row['friend_first_name'],
                "friend_last_name": row['friend_last_name']
            }
            users_with_friends.append(cls(row))
        return users_with_friends
    
    @classmethod
    def save_f(cls, data):
        existing = "SELECT id FROM friendships WHERE user_id = %(u_id)s AND friend_id = %(f_id)s;"
        results_existing = connectToMySQL('friendships_schema').query_db(existing, data)
        print(results_existing)
        if results_existing == () :
            query = "INSERT INTO friendships (user_id, friend_id) VALUES (%(u_id)s, %(f_id)s);"
            results = connectToMySQL('friendships_schema').query_db(query, data)
        else:
            results = "This friendship already exists"
        return results
