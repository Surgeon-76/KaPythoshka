# lst_in = ['10', 'Питон - основы мастерства', '512']
# print(result) # для теста в IDE

import sys

# здесь объявляется класс StreamData
class StreamData:
    def create(self, fields, lst_values):
        print(*fields)

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        print('lst_in', *lst_in)
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
print(data, result)