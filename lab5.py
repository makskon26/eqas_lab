import re
import json

class Product:
    def __init__(self, name, ip, status):
        self.name = name
        self.ip = ip
        self.status = status

    def Name(self):
        return self.name

    def Ip(self):
        return self.ip

    def Status(self):
        return self.status

    def Data(self, name, ip, status):
        self.name = name
        self.ip = ip
        self.status = status


class User:
    def __init__(self, name, ip, email):
        self.name = name
        self.ip = ip
        self.email = email

    def Name(self):
        return self.name

    def Ip(self):
        return self.ip

    def Email(self):
        return self.email

    def Data(self, name, ip, email):
        self.name = name
        self.ip = ip
        self.email = email


class Order:
    def __init__(self, ip, status):
        self.ip = ip
        self.status = status

    def Ip(self):
        return self.ip

    def Status(self):
        return self.status

    def Data(self, ip, status):
        self.ip = ip
        self.status = status


class MainValid:
    def obj(self, obj):
        self.my_obj = obj

    def valid_data(self):
        pass

    def save_request(self):
        pass

    def forming_answer(self, code, status):
        json_data = self.generate_json(code, status)
        print(json_data)

    def generate_json(self, code, status):
        return json.dumps({"code": code, "status": status})


class ProductValid(MainValid):
    valid_name = r"^[a-zA-Z']{2,}$"
    valid_ip = r"^\d{8,}$"

    def valid_data(self, new_name, new_ip, new_status):
        if re.match(self.valid_name, new_name):
            if re.match(self.valid_ip, str(new_ip)):
                if isinstance(new_status, bool):
                    self.save_request(new_name, new_ip, new_status)
                else:
                    print("Помилковий Статус")
            else:
                print("Помилковий IP")
        else:
            print("Помилкове ім'я")

    def save_request(self, new_name, new_ip, new_status):
        self.my_obj.Data(new_name, new_ip, new_status)

        self.forming_answer(new_ip, new_status)


class UserValid(MainValid):
    valid_name = r"^[a-zA-Z']{2,}$"
    valid_ip = r"^\d{8,}$"
    valid_email = r"^[0-9a-z-_\.]+\@[0-9a-z-]{2,}\.[a-z]{2,5}$"

    def valid_data(self, new_name, new_ip, new_email):
        if re.match(self.valid_name, new_name):
            if re.match(self.valid_ip, str(new_ip)):
                if re.match(self.valid_email, new_email):
                    self.save_request(new_name, new_ip, new_email)
                else:
                    print("Помилковий Статус")
            else:
                print("Помилковий IP")
        else:
            print("Помилкове ім'я")

    def save_request(self, new_name, new_ip, new_email):
        self.my_obj.Data(new_name, new_ip, new_email)
        self.forming_answer(new_ip, True)


class OrderValid(MainValid):
    vaild_ip = r"^\d{8,}$"

    def valid_data(self, new_ip, new_status):
        if re.match(self.vaild_ip, str(new_ip)):
            if isinstance(new_status, bool):
                self.save_request(new_ip, new_status)
            else:
                print("Помилковий Статус")
        else:
            print("Помилковий IP")

    def save_request(self, new_ip, new_status):
        self.my_obj.Data(new_ip, new_status)
        self.forming_answer(new_ip, new_status)

    def generate_json(self, code, status):
        return json.dumps({"code": code, "status": status})


# Client code

tovar1 = Product("Potato", 10000001, False)
print(tovar1.Ip())
print(tovar1.Name())
print(tovar1.Status())

prod_valid = ProductValid()
prod_valid.obj(tovar1)
prod_valid.valid_data("Tomato", 10000002, True)
print(tovar1.Ip())
print(tovar1.Name())
print(tovar1.Status())

print(' ')
user1 = User("John", 10000003, "john_doe@gmail.com")
print(user1.Name())
print(user1.Ip())
print(user1.Email())

user_valid = UserValid()
user_valid.obj(user1)
user_valid.valid_data("Jane", 10000004, "jane_doe@gmail.com")
print(user1.Name())
print(user1.Ip())
print(user1.Email())

print(' ')
order1 = Order(10000005, False)
print(order1.Ip())
print(order1.Status())

order_valid = OrderValid()
order_valid.obj(order1)
order_valid.valid_data(10000006, True)
print(order1.Ip())
print(order1.Status())