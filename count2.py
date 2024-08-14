def custom_len(string):
    # Custom implementation of len()
    count = 0
    for _ in string:
        count += 1
    return count

def compare_substrings(string, substring, start):
    # Compare substring with a part of the main string starting at index `start`
    for j in range(custom_len(substring)):
        if string[start + j] != substring[j]:
            return False
    return True

def count_substring_loop_flag_v2(string, substring, flag):
    count = 0
    i = 0
    len_sub = custom_len(substring)  # Get length of substring using custom len function
    len_string = custom_len(string)  # Get length of string using custom len function
    
    while i <= len_string - len_sub:
        if compare_substrings(string, substring, i):  # Compare substrings manually
            count += 1
            if not flag:
                i += len_sub  # Move past the found substring to avoid overlap
            else:
                i += 1  # Allow overlapping
        else:
            i += 1

    return count

# Test cases
string = "sgggsiengg"
substring = "gg"
print(count_substring_loop_flag_v2(string, substring, True))   # Expected output: 3 (overlapping)
print(count_substring_loop_flag_v2(string, substring, False))  # Expected output: 2 (non-overlapping)

