s = "saekjfkqhjffffffs"

n = []

count = 1

for i in range(len(s) -1):
    if s[i] == s[i+1]: count +=1
    else:
        print(f"{s[i]}{count}", end="")
        count = 1
