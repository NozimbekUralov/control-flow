n = int(input("Enter Number: "))
    
def devident(num):
    
    for i in range(1, num // 2 +1):
        if num % i == 0: print(i)
    
    print(num)

devident(n)