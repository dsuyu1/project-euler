#project euler question 0
sum = 0

for i in range(0,330000):
    square = i*i 
    if square%2 != 0:
        sum = sum + square
        
print(sum)