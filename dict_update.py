dict1 = {'a': '1','b': '2','c': '3'}
dict2 = {'d': '4','e':'5','f': '6'}

print(dict1.update(dict2))

def Merge(dict1, dict2):
    return(dict2.update(dict1))

print(Merge(dict2, dict1))



