class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.count_call = 0
        return cls.instance

    def get_count_call(self):
        return f"PostgreSQL{self.count_call}"

    def call(self):
        self.count_call += 1


class SingletonMongo:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.count_call = 0
        return cls.instance

    def get_count_call(self):
        return f"MongoDB{self.count_call}"

    def call(self):
        self.count_call += 1


# Створення змінних для двох "різних екземплярів класу SingletonPostgreSQL"
postgreSQL_1 = Singleton()
postgreSQL_2 = Singleton()

# Вивід стану для об'єктів SingletonPostgreSQL
print("SingletonPostgreSQL:")
print(f"Instance 1 count call: {postgreSQL_1.get_count_call()}")
print(f"Instance 2 count call: {postgreSQL_2.get_count_call()}")

# Виклик запиту до бази даних з різних екземплярів
postgreSQL_1.call()
postgreSQL_2.call()
postgreSQL_2.call()

# Вивід оновленого стану для об'єктів SingletonPostgreSQL
print("\nUpdated SingletonPostgreSQL:")
print(f"Instance 1 count call: {postgreSQL_1.get_count_call()}")
print(f"Instance 2 count call: {postgreSQL_2.get_count_call()}")

# Створення змінних для двох "різних екземплярів класу SingletonMongoDB"
mongoDB_1 = SingletonMongo()
mongoDB_2 = SingletonMongo()

# Вивід стану для об'єктів SingletonMongoDB
print("\nSingletonMongoDB:")
print(f"Instance 1 count call: {mongoDB_1.get_count_call()}")
print(f"Instance 2 count call: {mongoDB_2.get_count_call()}")

# Виклик запиту до бази даних з різних екземплярів
mongoDB_1.call()
mongoDB_1.call()
mongoDB_1.call()
mongoDB_2.call()
mongoDB_2.call()

# Вивід оновленого стану для об'єктів SingletonMongoDB
print("\nUpdated SingletonMongoDB:")
print(f"Instance 1 count call: {mongoDB_1.get_count_call()}")
print(f"Instance 2 count call: {mongoDB_2.get_count_call()}")
