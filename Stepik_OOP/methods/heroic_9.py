import sys

# программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока

# lst_in = [["1", "Сергей", "35", "120000"],
#           ["2", "Федор", "23", "12000"],
#           ["3", "Иван", "13", "1200"]]

lst_in = ["1 Сергей 35 120000",
          "2 Федор 23 12000",
          "3 Иван 13 1200"]


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы

    def insert(self, data):
        for lst in data:
            self.lst_data.append(dict(zip(self.FIELDS, lst.split())))

    def select(self, a, b):
        b = min(b, len(self.lst_data))
        return self.lst_data[a:b]

db = DataBase()
db.insert(lst_in)
print(db.lst_data)
print()
print(db.select(2, 10))
