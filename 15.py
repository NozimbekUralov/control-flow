key = True
n = []

print("Enter -1 to stop:")

while key:
    temp = int(input("Enter Number: "))
    n.append(temp)
    if temp == -1: key = False

for i in range(len(n)):
    if n[i] % 3 == 0 and n[i] % 2 == 1: print(n[i])
