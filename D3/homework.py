def asc_sort(a): 
    a.sort()
    print(a) 

my_array = [34,23,524,32,626,453,32,24,76,675,455]

asc_sort(my_array)

def flatten_dict(d):
    """Flattens a nested dictionary.
  keys must be strings in all dictionaries for this to work.
    """
    result = dict()
    for i in d.keys():
        if type(d[i]) == dict:
            #the value is a dictionary, so we must flatten it
            for k,v in d[i].items():
              new_key = i + "." + k #make new key
              result[new_key] = v #add k:v pair
        else:
            #add the k:v pair to result dictionary
            result[i] = d[i]
    return result

print(flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}))

def unflatten_dict(d):
  """Unflattens a nested dictionary. (reverses flatten_dict)
  keys must be strings in all dictionaries for this to work.
    """
  result = dict()
  for i in d.keys():
    if "." in i:
      #this should become nested
      new_key, sep, inner_key = i.partition(".")
      #create dictionary if not yet created
      if new_key not in result.keys():
        result[new_key] = dict()
      #add elements to inner dictionary
      result[new_key][inner_key] = d[i]
    else:
      #add the k:v pair to result dictionary
      result[i] = d[i]
  return result

print(unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))

def treemap(func, lst):
  for i in range(len(lst)):
    if type(lst[i]) == list:
      lst[i] = treemap(func,lst[i])
    else:
      lst[i] = func(lst[i])

  return lst
  
print(treemap(lambda i: i*i, [1, 2, [3, 4, [5]]]))