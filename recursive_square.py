# (n−1)2 = n2​​ − 2n+1
# =>  n2 = (n-1)2 + 2n -1

def my_Square(n):
    if n==0:
        return 0
    return my_Square(n-1) + (n*2) -1

print(my_Square(5))


