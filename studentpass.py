Telugu=int(input("Enter Tel marks:"))
Hindi=int(input("Enter Hindi marks:"))
English=int(input("Enter English marks:"))
Maths=int(input("Enter Maths marks:"))
Science=int(input("Enter science marks:"))
Social=int(input("Enter Social marks:"))
total=(Telugu+Hindi+English+Maths+Science+Social)
print(total)
if (total<=210):
    print("sorry,you have failed - Better luck Next time ")
else:
     print("Congratulations,you have passed the Examination")
