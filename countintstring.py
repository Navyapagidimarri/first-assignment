s="aabbcc121122@@"
digitC=0
alphaC=0
specialC=0
for i in s:
    if i.isdigit():
     digitC=digitC+1
    elif i.isalpha(): 
     alphaC=alphaC+1
    else:
     specialC=specialC+1
print("number of special charactors",specialC)
print("number of digit",digitC)
print("number of digit",alphaC)