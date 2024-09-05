# 1. Write a program to make another list of duplicate elements from the following list
# [1, 5, 6, 5, 1, 2, 3]

list1 = [1, 5, 6, 5, 1, 2, 3]

# no duplicate eliments
list2 = []
print("No Duplicates:")
for x in list1:
    if x in list2:
        continue
    else:
        list2.append(x)

for v in list2:
    print(v)

# only duplicate elements
freq = {}
list3 = []
for x in list1:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

for i,c in freq.items():
    if c > 1:
        list3.append(i)
        
print("Only Duplicates:")
for v in list3:
    print(v)
