def capital(string):
    result = ''
    for char in string:
        if 'a' <= char <= 'z':  
            result += chr(ord(char) - 32)  
        else:
            result += char  
    return result

def small(string):
    result = ''
    for char in string:
        if 'A' <= char <= 'Z': 
            result += chr(ord(char) + 32)  
        else:
            result += char  
    return result
    
def swapthec(string):
    result = ''
    for char in string:
        if 'a' <= char <= 'z':
            result = result + chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) +32)
    return result 
    
def alternate(string):
    if not string:
        return ''
    
    result = ''
    first_char = string[0]
    
    
    if 65 <= ord(first_char) <= 90:  
        for i in range(len(string)):
            char = string[i]
            if i % 2 == 0:  
                if 65 <= ord(char) <= 90:  
                    result += chr(ord(char) + 32)
                else:
                    result += char
            else:  
                if 97 <= ord(char) <= 122:  
                    result += chr(ord(char) - 32)
                else:
                    result += char
    else:  
        for i in range(len(string)):
            char = string[i]
            if i % 2 == 0: 
                if 97 <= ord(char) <= 122:  
                    result += chr(ord(char) - 32)
                else:
                    result += char
            else:  
                if 65 <= ord(char) <= 90:  
                    result += chr(ord(char) + 32)
                else:
                    result += char
    
    return result

def change_case(text, style):
    if style == "c" or style == "C":
        return capital(text)
    elif style == "s" or style == "S":
        return small(text)
    elif style == "r" or style == "R":
        return swapthec(text) 
    elif style == "u" or style == "U":
        return alternate(text)


print(change_case("shravani", "c"))  
print(change_case("shravani", "s")) 
print(change_case("sHraVani", "r"))  
print(change_case("Shravani", "u"))  

