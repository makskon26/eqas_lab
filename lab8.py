class MySQL:
    def __init__(self):
        self.select = "*"
        self.where = False
        self.limit = "*"


class PostgreSQL:
    def __init__(self):
        self.select = "*"
        self.where = False
        self.limit = "*"


class BuildSQL:
    def __init__(self):
        self.sql = None

    def addSELECT(self, select):
        raise NotImplementedError

    def addWHERE(self, where):
        raise NotImplementedError

    def addLIMIT(self, limit):
        raise NotImplementedError

    def getSQL(self):
        raise NotImplementedError


class BuildMySQL(BuildSQL):
    def __init__(self):
        super().__init__()
        self.sql = MySQL()

    def addSELECT(self, select):
        self.sql.select = select
        return self

    def addWHERE(self, where):
        self.sql.where = where
        return self

    def addLIMIT(self, limit):
        self.sql.limit = limit
        return self

    def getSQL(self):
        sql_query = f"SELECT {self.sql.select} WHERE {self.sql.where} LIMIT {self.sql.limit};"
        print(sql_query)
        return self.sql


class BuildPostgreSQL(BuildSQL):
    def __init__(self):
        super().__init__()
        self.sql = PostgreSQL()

    def addSELECT(self, select):
        self.sql.select = select
        return self

    def addWHERE(self, where):
        self.sql.where = where
        return self

    def addLIMIT(self, limit):
        self.sql.limit = limit
        return self

    def getSQL(self):
        sql_query = f"SELECT {self.sql.select}\nWHERE {self.sql.where}\nLIMIT {self.sql.limit};"
        print(sql_query)
        return self.sql


# Створення нашого запиту та передача параметрів
request_MySQL_1 = BuildMySQL().addSELECT("all").addWHERE("flowers == tulip").addLIMIT("colour != yellow").getSQL()
print(request_MySQL_1)

request_PostgreSQL_1 = BuildPostgreSQL().addWHERE("flowers == rose").getSQL()
