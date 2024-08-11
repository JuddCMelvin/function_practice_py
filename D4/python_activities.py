grades = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_grades = sorted(grades, key = lambda x: x[1])
print(sorted_grades)

cubed = lambda x: [i**3 for i in x]

def cubed2(lst):
    newLst = []
    for i in lst:
        newLst.append(i**3)
    return newLst

print(cubed2([3,6,9,2]))

#Problem 3: Write a lambda function to determine whether 
# a number is even or odd (the function should return True or False), 
# and then use the function and a list comprehension to create a new 
# list of booleans, where even numbers are True and odd numbers are False.

even_odd = lambda x: True if x%2 == 0 else False
print([even_odd(x) for x in [3,6,9,2]])


nums = [i for i in range(1,101)]
print(nums)

sent = "The quick brown fox jumped over the fence."
print({word:len(word) for word in sent.split()})