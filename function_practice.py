def greeting():
    print("Hi this is working")

def pack(a,b,c):
    return [a,b,c]

def eat_lunch(my_lst):
    if len(my_lst) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_lst)):
        if i == 0:
            print(f"First I eat {my_lst[0]}")
        else:
            print(f"Next I eat {my_lst[i]}")

            
print(pack("red", "blue", "green"))
greeting()