from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('esquema_ususarios').query_db(query)
        #[
        #  {"nombre":"luciano", "edad":"29"}
        #  {"nombre":"luciano", "edad":"29"}
        #   {"nombre":"luciano", "edad":"29"}
        #   {"nombre":"luciano", "edad":"29"}
        # ]
        users = []
        for u in results:
            users.append(cls(u))#se transforma en objeto user
        return users

    @classmethod
    def guardar(cls, formulario):
        #data = {"first_name":"c" "last_name": "x", "email": "y"}
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        result = connectToMySQL('esquema_ususarios').query_db(query, formulario)
        return result

    @classmethod
    def borrar(cls, formulario):
        #formulario = {"id": "1"}
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_ususarios').query_db(query, formulario)
        return result

    @classmethod
    def mostrar(cls, formulario):
        #formulario = {"id": "1"}
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_ususarios').query_db(query, formulario)
        #[
        #   {'3', 'Juana', 'De Arco', juana@codingdojo.com', '2022-03-09 14:50:58', etc} esta es la posicion 0
        # ]
        usr = result[0]
        user = cls(usr)
        return user

    @classmethod
    def actualizar(cls , formulario):
        #formulario= {"id": "1", first_name":"c" "last_name": "x", "email": "y"}
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s"
        result = connectToMySQL('esquema_ususarios').query_db(query, formulario)
        return result
