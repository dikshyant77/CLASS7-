#Identity operator (is , is not)
x= 10
if (type(x)is int):
    print("True")
else:
    print("False")

#create a float variable
x=2.789
if (type(x)is not float):
    print("True")
else:
    print("Flase")

x=20
y=20
if x is y:
    print("x and y are same identity")

x=20
y=25
if x is not y:
    print("x and y are different identity")


