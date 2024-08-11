def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

print(flatten_and_sort([[3, 2, 1], [6, 5, 4]]))


# def flatten_and_sort(iterable):
#     # Use a tuple to accumulate elements
#     arr = ()
#     for item in iterable:
#         for i in iter(item):
#             arr += (i,)
#     return tuple(sorted(arr))

print(flatten_and_sort([[3, 2, 1], [6, 5, 4]]))

# List of lists
print(flatten_and_sort([[3, 2, 1], [6, 5, 4]]))
# Output: (1, 2, 3, 4, 5, 6)

# List of tuples
print(flatten_and_sort([(3, 2), (1, 4)]))
# Output: (1, 2, 3, 4)

# List of sets
print(flatten_and_sort([{5, 3}, {2, 4, 1}]))
# Output: (1, 2, 3, 4, 5)

# Nested mixed iterable
print(flatten_and_sort([{5, 3}, (2, 4, 1), [6, 7]]))
# Output: (1, 2, 3, 4, 5, 6, 7)

print(flatten_and_sort([{5, 3}]))


class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    # Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"
        
    # Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
    class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price):
    
    def boost(self):
        self.max_speed *= 2
        
    # Define another class that inherits Podracer and call this one SebulbasPod. 
    # This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
    class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price):
    
    def flame_jet(self,other):
        other.condition = "trashed"
