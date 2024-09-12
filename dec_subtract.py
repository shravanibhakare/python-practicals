def str_to_dec(num1, num2):
    # Remove leading zeros
    num1 = num1.lstrip('0') or '0'
    num2 = num2.lstrip('0') or '0'
    
    n1 = [ord(i) - 48 for i in num1]
    n2 = [ord(j) - 48 for j in num2]
    
    return n1[::-1], n2[::-1]  # Reverse for least significant digit subtraction

def compare_numbers(num1, num2):
    if len(num1) > len(num2):
        return 1
    elif len(num1) < len(num2):
        return -1
    else:
        for i in range(len(num1)):
            if num1[i] > num2[i]:
                return 1
            elif num1[i] < num2[i]:
                return -1
        return 0  # Both numbers are equal

def dec_subtraction(num1, num2):
    comparison = compare_numbers(num1, num2)
    
    if comparison == 0:
        return "0"  # If both numbers are equal, the result is zero
    
    # Ensure we're always subtracting the smaller number from the larger one
    if comparison == -1:
        num1, num2 = num2, num1
        is_negative = True
    else:
        is_negative = False
    
    n1, n2 = str_to_dec(num1, num2)
    result = []
    borrow = 0
    max_len = max(len(n1), len(n2))
    
    # Extend the shorter list with 0s to match lengths
    n1 += [0] * (max_len - len(n1))
    n2 += [0] * (max_len - len(n2))
    
    for i in range(max_len):
        sub = n1[i] - n2[i] - borrow
        if sub < 0:
            sub += 10
            borrow = 1
        else:
            borrow = 0
        result.append(sub)
    
    # Remove leading zeros from the result
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    # Convert result list back to a string
    final_result = ''.join(map(str, result[::-1]))  # Reverse back to the original order
    
    # Handle negative results
    if is_negative:
        final_result = '-' + final_result
    
    return final_result


print(dec_subtraction("534", "63"))  
print(dec_subtraction("63", "534")) 
print(dec_subtraction("000675", "0")) 
print(dec_subtraction("00", "00")) 
print(dec_subtraction("1000", "1")) 

