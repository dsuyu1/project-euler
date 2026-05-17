a, b = 1, 2
sum = 0

while a <= 4000000:
    if (a%2==0):
        sum = sum + a
    a, b = b, a+b 

print(sum)

# notes:
# previously used an extra b%2==0 conditional
# a becomes b on the next iteration, so no need to count b as well as a 
# as long as we count a, we will be fine.
