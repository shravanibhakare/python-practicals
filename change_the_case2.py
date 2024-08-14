def create_lookup_tables():
    lower_to_upper = {}
    upper_to_lower = {}
    
    # Manually map lowercase to uppercase
    for lower, upper in zip('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        lower_to_upper[lower] = upper
        upper_to_lower[upper] = lower
    
    return lower_to_upper, upper_to_lower

lower_to_upper, upper_to_lower = create_lookup_tables()

def alternate_v6(string):
    if not string:
        return ''
    
    result = ''
    first_char_upper = string[0] in upper_to_lower  # Check if first character is uppercase
    
    for i in range(len(string)):
        char = string[i]
        if i % 2 == 0:  # Even index
            if first_char_upper:
                result += upper_to_lower.get(char, char)  # Convert to lowercase
            else:
                result += lower_to_upper.get(char, char)  # Convert to uppercase
        else:  # Odd index
            if first_char_upper:
                result += lower_to_upper.get(char, char)  # Convert to uppercase
            else:
                result += upper_to_lower.get(char, char)  # Convert to lowercase
    
    return result

def change_case(text, style):
    if style == "c" or style == "C":
        # Convert entire text to uppercase
        result = ''
        for char in text:
            result += lower_to_upper.get(char, char)
        return result
    elif style == "s" or style == "S":
        # Convert entire text to lowercase
        result = ''
        for char in text:
            result += upper_to_lower.get(char, char)
        return result
    elif style == "r" or style == "R":
        # Swap the case of each character
        result = ''
        for char in text:
            if char in lower_to_upper:
                result += lower_to_upper[char]
            elif char in upper_to_lower:
                result += upper_to_lower[char]
            else:
                result += char
        return result
    elif style == "u" or style == "U":
        return alternate_v6(text)

# Test cases
print(change_case("shravani", "c"))  # Expected output: "SHRAVANI"
print(change_case("shravani", "s"))  # Expected output: "shravani"
print(change_case("sHraVani", "r"))  # Expected output: "ShRAvANI"
print(change_case("Shravani", "u"))  # Expected output: "sHRaVaNI"

