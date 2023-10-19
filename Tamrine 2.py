a = int(input("Enter your A:"))
b = int(input("Enter you B:"))
c = int(input("Enter your C:"))

if a + b > c and a + c > b and b + c > a :
            print("Its a triangle")
else:
            print("its not a triangle")