#kwargs take in any number of key,value pairs. 
#like the *args
def concat(**kwargs): 
    concatted = ""
    for i in kwargs.values(): 
        concatted += i
    return concatted
    print(concatted)

concat(a="writing", b="python", c="functions")
