def count(obj, lst): # подсчитывает количество вхождений обекта obj в листе lst
    # count obj in lst
    count = 0
    for e in lst:
        if e == obj:
            count = count + 1
    return count

def is_in(obj, lst):  # проверяет вхождение объекта в листе и возвращает True or False
    # checks the occurrence of an object in the sheet and returns true or false  
    for e in lst:
        if e == obj:
            return True
    return False

def reverse(lst): # создается новый список в котором разворачивается предидущий список
    # a new list is created in which the previous list is reversed
    reversed = []
    for i in range(len(lst)-1, -1, -1): # step through the original list backwards
        reversed.append(lst[i])
    return reversed

def index(obj, lst): # найти индекс значения в списке
    # find the index of a value in a list
    for i in range(len(lst)):
        if lst[i] == obj:
            return i
    return -1

def insert(obj, index, lst): # вставить значение obj по указаному индексу в определенном списке
    # insert the value obj at the specified index in a specific list
    newlst = []
    for i in range(len(lst)):
        if i == index:
            newlst.append(obj)
        newlst.append(lst[i])
    return newlst

lst = [0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
print(count(1, lst))
print(is_in(4, lst))
print(reverse(lst))
print(index(2, lst))
print(insert('cat', 4, lst))
