# In python3 there are three types of numbers: int, float, complex
# There are four arithmetic operators: + - * /

print("Convertion between int and float is done with int and float constructor")
x = 28
print("The value of x is: " + str(x))
print("After converting x to a float the value is: " + str(float(x)))

y = 3.14
print("The value of y is: " + str(y))
y=int(y)
print("When using the int constructor on y the value is rounded and converted to an int")
print("The value of y is now: " + str(y))

print("We create 3 variables, a,b,c")
a = 2
b = 6.0
c = 12 + 0j
print("a: " + str(a), "b: " + str(b), "c: " + str(c))
print("When performing arithmetic operations on numbers they are widened to the largest type involved in the operation")
print("")
print("When adding a to b, we are adding an int to a float. This means variable a is converted to a float before the operation is performed")
print("The value of a + b is: " + str(a+b) + " and the type of  the result is " + str(type(a+b)))
print("")
print("When performing division, python3 returns a float when performing division by operator /")
print("b/a=" + str(b/a) + " and the result is type " + str(type(b/a)))

