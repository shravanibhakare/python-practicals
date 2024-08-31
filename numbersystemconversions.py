def dec_to_bin(num, convert_sys):
    binary = ""
    if num == 0:
        return "0"
    while num > 0:
        remainder = num % int(convert_sys)
        binary = str(remainder) + binary
        num = num // int(convert_sys)
    return binary

def convert_to_dec(number, base_system):
    if number == "0":
        return 0
    n = 0
    number = number[::-1]
    for i in range(len(number)):
        a = int(number[i], 36)  # Supports digits and letters (0-9, A-Z)
        n += a * (int(base_system) ** i)
    return n

def convert_number(number, base_system, convert_system):
    decimal_value = convert_to_dec(number, base_system)
    if convert_system == '27':
        return intToRoman(decimal_value)
    elif convert_system == '10':
        return str(decimal_value)
    return dec_to_bin(decimal_value, convert_system)

def intToRoman(num: int) -> str:
    roman_dict = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    out = ""
    for n in sorted(roman_dict.keys(), reverse=True):
        while num >= n:
            out += roman_dict[n]
            num -= n
    return out

def romanToInt(s: str) -> int:
    s = s.replace("IV", "IIII")  # 4
    s = s.replace("IX", "VIIII")  # 9
    s = s.replace("XL", "XXXX")  # 40
    s = s.replace("XC", "LXXXX")  # 90
    s = s.replace("CD", "CCCC")  # 400
    s = s.replace("CM", "DCCCC")  # 900
    num = 0
    for ch in s:
        if ch == 'I':
            num += 1
        elif ch == 'V':
            num += 5
        elif ch == 'X':
            num += 10
        elif ch == 'L':
            num += 50
        elif ch == 'C':
            num += 100
        elif ch == 'D':
            num += 500
        elif ch == 'M':
            num += 1000
    return num

# Input handling
print("Enter the number, base system, and the number system to which it is to be converted:")
print("For bases 0-9, enter 0-9, and for bases from 10-36, use A/a to Z/z.")

num = input("Number: ")
base_system = input("Base system: ")
convert_system = input("Conversion system: ")

# Handling alphabetic bases for the base and conversion systems
alpha_dict = {
    'a': "10", 'b': "11", 'c': "12", 'd': "13", 'e': "14", 'f': "15", 'g': "16", 'h': "17", 'i': "18",
    'j': "19", 'k': "20", 'l': "21", 'm': "22", 'n': "23", 'o': "24", 'p': "25", 'q': "26", 'r': "27",
    's': "28", 't': "29", 'u': "30", 'v': "31", 'w': "32", 'x': "33", 'y': "34", 'z': "35"
}

if base_system.isalpha():
    base_system = alpha_dict[base_system.lower()]

if convert_system.isalpha():
    convert_system = alpha_dict[convert_system.lower()]

# Convert the number from the base system to the desired system
converted_number = convert_number(num, base_system, convert_system)
print(f"Converted number: {converted_number}")

