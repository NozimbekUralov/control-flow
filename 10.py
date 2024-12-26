s = input("Matn kriting: ")

s = s.split(" ")

longest = [len(i) for i in s]

print(s[longest.index(max(longest))])