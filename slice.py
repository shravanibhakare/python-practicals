def Slice(obj, slice_params):
    
    start, stop, step = slice_params + (None,) * (3 - len(slice_params))

    if step is None:
        step = 1

    if start is None:
        if step > 0:
        	start = 0
        else:
        	start = len(obj)-1
    if stop is None:
        
        if step > 0:
        	stop = 0
        else:
        	start =-1
    if start < 0:
        start += len(obj)
    if stop < 0:
        stop += len(obj)

    result = []
    index = start
    while (step > 0 and index < stop) or (step < 0 and index > stop):
        if 0 <= index < len(obj):
            result.append(obj[index])
        index += step

    if isinstance(obj, str):
        return ''.join(result)
    elif isinstance(obj, list):
        return result
    elif isinstance(obj, tuple):
        return tuple(result)

#for strings
print("\nFor String abcdefgh:")
text = "abcdefgh"

print(Slice(text, (-5, -1)))    
print(Slice(text, (6, 0, -1))) 

#for lists
print("\nFor list [0,1,2,3,4,5,6]:")
my_list = [0, 1, 2, 3, 4, 5, 6]
print(Slice(my_list, (-5, -1)))   
print(Slice(my_list, (6, 0, -1)))  

#for tuples
print("\nFor tuple (0,1,2,3,4,5,6)")
my_tuple = (0, 1, 2, 3, 4, 5, 6)
print(Slice(my_tuple, (-5, -1)))    
print(Slice(my_tuple, (6, 0, -1)))  

