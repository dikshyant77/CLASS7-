print("enter marks obtained in 5 subjects")
s1 = int(input("enter your marks"))
s2 = int(input("enter your marks"))
s3 = int(input("enter your marks"))
s4 = int(input("enter your marks"))
s5 = int(input("enter your marks"))
totalmarks = s1 + s2 + s3 + s4 + s5 
avg = totalmarks/5
if avg >= 91 and avg <=100:
    print("your grade is a1")
elif avg >= 81 and avg <=91:
    print("your grade is a2")
elif avg >= 71 and avg <=81:
    print("your grade is b1")
elif avg >= 61 and avg <=71:
    print("your grade is b2")
else:
    print("your grade is e2 ")
