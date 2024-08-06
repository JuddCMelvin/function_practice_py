# arb_args — Takes in any number of arguments and prints them one at a time. 

def arb_args(*args):
  for a in args:
    print(a)

# inner_func — Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.

def inner_func(x,y):
  def inner_1():
    return x+y
  def inner_2():
    return x-y
  print(inner_1()+inner_2())

def inner_func(int1, int2):
    def getExponentOf(a, b):
        return a ** b
    
    def getModulus(c, d):
        return c % d
    
    e = getExponentOf(int1, int2)
    print(e)

    m = getModulus(int1, int2)
    print(m)

    return e + m

r = inner_func(5, 2)
print(r)

# lunch_lady — Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady(name, lunch="Mystery Meat"):
  print(name, lunch)

def lunch_lady(name, pref="Mystery Meat"):
    print(name + " wants to have: " + pref)

lunch_lady("Cody")
lunch_lady("Tenario", "Pizza")

# sum_n_product — Accepts two integers and returns both the sum and the product.
def sum_n_product(x,y):
  return x+y,x*y

def sum_n_product(int1, int2):
    sum = int1 + int2
    product = int1 * int2
    return sum, product

print(sum_n_product(77,55))

# alias_arb_args — Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args

# arb_mean — Accepts any number of integers and prints their average.
def arb_mean(*args):
  total = 0
  for a in args:
    total += a
  print(a/len(args))


def arb_mean(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)

print(arb_mean(1,2,3))
print(arb_mean(1234,3456456,124234))
# arb_longest_string — Accepts any number of strings and returns the longest one.
def arb_longest_string(*args):
  long = 0
  longest = ""
  for a in args:
    if len(a) > long:
      long = len(a)