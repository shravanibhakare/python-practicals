def str_to_dec(num1, num2):
    # Remove leading zeros
    num1 = num1.lstrip('0') or '0'
    num2 = num2.lstrip('0') or '0'
    
    n1 = [ord(i) - 48 for i in num1]
    n2 = [ord(j) - 48 for j in num2]
    
    return n1[::-1], n2[::-1]  
    
def dec_addition(num1, num2):
    n1, n2 = str_to_dec(num1, num2)
    result = []
    carry = 0
    max_len = max(len(n1), len(n2))
    
    # Extend the shorter list with 0s to match lengths
    n1 += [0] * (max_len - len(n1))
    n2 += [0] * (max_len - len(n2))
    
    for i in range(max_len):
        total = n1[i] + n2[i] + carry
        carry = total // 10  # Update carry for next iterationdef str_to_dec(num1, num2):
    # Remove leading zeros
    num1 = num1.lstrip('0') or '0'
    num2 = num2.lstrip('0') or '0'
    
    n1 = [ord(i) - 48 for i in num1]
    n2 = [ord(j) - 48 for j in num2]
    
    return n1[::-1], n2[::-1]  
        result.append(total % 10)  # Append the current digit to the result
    
    # If there's a carry after the final addition, append it
    if carry:
        result.append(carry)
    
    # Convert the result back to a string and reverse it to get the correct order
    return ''.join(map(str, result[::-1]))


print(dec_addition("534", "63")) 
print(dec_addition("999", "1"))   
print(dec_addition("000675", "765"))  
print(dec_addition("00", "00"))   

