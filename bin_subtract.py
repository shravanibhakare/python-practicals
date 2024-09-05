def binary_subtraction(a, b):

    num1 = a[::-1]
    num2 = b[::-1]
    result = []
    carry = 0
    
    for i in range(max(len(num1), len(num2))):
        bit1 = int(num1[i]) if i < len(num1) else 0
        bit2 = int(num2[i]) if i < len(num2) else 0
        
        if bit1 - bit2 - carry == 0:
            result.append(0)
            carry = 0
        elif bit1 - bit2 - carry == 1:
            result.append(1)
            carry = 0
        elif bit1 - bit2 - carry == -1:
            result.append(1)
            carry = 1
        else:  # bit1 - bit2 - carry == -2
            result.append(0)
            carry = 1

   
    while len(result) > 1 and result[-1] == 0:
        result.pop()
        
    return ''.join(map(str, result[::-1]))


print(binary_subtraction('1110', '0001'))

