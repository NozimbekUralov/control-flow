from math import sqrt


n = int(input("Enter Number: "))
    
def is_prime(num):
    for i in range(2, int(sqrt(num)) +1):
        if num % i == 0: return False
    
    return True

for i in range(2, n):
    if is_prime(i): print(i)