import cmath

def root_of_quadratic_equation(a,b,c):
    #find the discriminant
    dis = cmath.sqrt(b**2 - a*a*c)
    
    #find the roots
    root1 = (-b + dis) / (2*a)
    root2 = (-b - dis) / (2*a)
    
    return root1, root2

a=int(input("Enter coefficient of a: "))
b=int(input("Enter coefficient of b: "))
c=int(input("Enter coefficient of c: "))

roots = root_of_quadratic_equation(a,b,c)
print(f"First root is {roots[0]}")
print(f"Seccond root is {roots[1]}")