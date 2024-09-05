# 1. Write a program to sort by ascending order from the following list. (Create a function to solve it)
# List = [1, 5, 2, 9, 3, 22, 13]

def sort_list_ascending(l):
    l.sort()
    return l

list1 = [1, 5, 2, 9, 3, 22, 13]
ans = sort_list_ascending(list1)
print(ans)
