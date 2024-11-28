import gen_random

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]

data2 = gen_random.gen_random(10,0,7)

data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        # Нужно реализовать __next__ 
        while True:
            key = next(self.items)
            key = key.lower() if self.ignore_case and isinstance(key, str) else key
            if key not in self.seen:
                self.seen.add(key)
                return key


def main():
    for i in Unique(data3,ignore_case=False):print(i, end=', ')
    print('\n')
    for i in Unique(data3,ignore_case=True):print(i, end=', ')
    print('\n')
    for i in Unique(data2):print(i, end=', ')
    print('\n')
    for i in Unique(data2,ignore_case=True):print(i, end=', ')
    print('\n')
    for i in Unique(data1):print(i, end=', ')
    
    
    
if __name__ == "__main__":
    main()
