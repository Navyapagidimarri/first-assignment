s=input("input alpahabets:")
alphabets=[]
digits=[]
for k in s:
    if s.isalpha():
     alphabets.append(k)
    else:
        digits.append(k)
output=''.join(sorted(alphabets)+sorted(digits))
print(output)
