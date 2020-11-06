import cmath

print(" The Standard form of a Quadratic Equation is : ")
print(" ax^2 + bx + c = 0 , where a, b and c are real numbers and a!=0")

print("Enter the Value of a,b and c :")
a,b,c= [ int(a) for a in input().split() ]

d=(b**2)-(4*a*c)

ans1= ((-b-cmath.sqrt(d))/(2*a))
ans2= ((-b+cmath.sqrt(d))/(2*a))
print("The solutions of the Quadratic equation are {0} and {1}".format(ans1,ans2))
