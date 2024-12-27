s = input("Matn kriting: ")

for i in range(len(s) // 2):
    p = s[i] == s[-i -1]
    if p:
        continue
    else:
        break
    
print(p)