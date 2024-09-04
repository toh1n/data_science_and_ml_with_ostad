# Sum all the odd numbers from 0 to 100 and print it to the screen.

sum = 0
i = 1
while i < 101:
    if i % 2 != 0:
        sum+= i
    i+=1

print(sum)
