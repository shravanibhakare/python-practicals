def modulo(n, m):
    if m == 0:
        return "Error: can't divide by 0"
    
    if n != 0 :
        q = n // m
        result = n - (m * q)
        return abs(result)

    elif n < 0 and m > 0:
        q = n // m
        q= q+1
        result = n - (m * q)
        return abs(m + result) if result != 0 else 0
    
    elif n == 0:
       
        return 0

# Test cases
print(modulo(4, 7))    
print(modulo(-4, 7))  
print(modulo(14, -5))  
print(modulo(-14, -5)) 
print(modulo(0, 5))    
print(modulo(14, 0))   

