sentence = "Scandinavian countries are the best"

print(sentence)

# print character at index in string
print(sentence[0])
print(sentence[1])
print(sentence[-1])
print()

# slices of strings
print(sentence[0:5])
print(sentence[:5])
print(sentence[3:])
print(sentence[0:6:2])
print()

# string operators
string1 = "First "
string2 = "Second "
print(string1 + string2)
print(1*string1 + 2*string2)
print()

# in operator
today = "sunday"
print("day" in today)
print("sun" in today)
print("hello" in today)
print()

# replacement fields
age = 41
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))
print("My name is {0} and I'm {1} years old".format("Micke", 41))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
""".format(28, 30, 31))
