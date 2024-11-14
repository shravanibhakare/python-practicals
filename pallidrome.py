import time
def checkpal(text):
    if text == text[::-1]:
        return True
    else:
        return False

def fun(li):
    count = 0 

    for obj in li:
        if isinstance(obj, str):
            if len(obj) % 5 == 3:
                if checkpal(obj):  
                    count += 1
        elif isinstance(obj, int):
            obj = str(obj)
            if len(obj) % 5 == 3:
                if checkpal(obj):  
                    count += 1
        elif isinstance(obj, list):
            count += fun(obj)  
        elif isinstance(obj, tuple):
            count += fun(list(obj))  

    return count  
def fun3(li):
    count = 0 

    for obj in li:
        if isinstance(obj, (list,tuple,set)):
            count+=fun3(obj)
            
        elif isinstance(obj,int):
             obj = str(obj)
          
          
        count+= type(obj) == str and len(obj)%5 == 3 and checkpal(obj)

    return count  
def fun_sir(li):
    count = 0 
    for obj in li:
        if isinstance(obj, str):
            if len(obj) % 5 == 3:
               count += checkpal(obj)  
                    
        elif isinstance(obj, int):
            obj = str(obj)
            if len(obj) % 5 == 3:
                count += checkpal(obj) 
                    
        elif isinstance(obj, list):
            count += fun(obj)  
        elif isinstance(obj, tuple):
            count += fun(list(obj))  

    return count  
	
li = ["11234", 123, 11111111, ["abcba", 121]]
n =1000
start_timem1 = time.time()
for _ in range(n):
	result = fun(li)
print(result)
end_timem1 =time.time()

start_timem2 = time.time()
for _ in range(n):
	result = fun_sir(li)
print(result)
end_timem2 =time.time()

start_timem3 = time.time()
for _ in range(n):
	result = fun3(li)
print(result)
end_timem3 =time.time()

diffn1=end_timem1 - start_timem1
diffn2=end_timem2 - start_timem2
diffn3 = end_timem3 - start_timem3

if diffn2>diffn1 and diffn2 > diffn3:
	print("sirs method takes less time")
elif diffn3>diffn1 and diffn3 > diffn2:
	print("fun2 method is taking less time")
else:
	print("my method is taking less time")	
	
	

