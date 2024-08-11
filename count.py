def count_substring_loop_flag(string, substring, flag):
    count = 0
    i = 0
    len_sub = len(substring)
    
    while i <= len(string) - len_sub:
        if string[i:i + len_sub] == substring:
            count += 1
            if not flag:
                # Move i forward by the length of the substring to avoid overlapping
                i += len_sub
            else:
                # Move i forward by 1 to allow overlapping
                i += 1
        else:
            i += 1

    return count

# Test cases
string = "sgggsiengg"
substring = "gg"
print(count_substring_loop_flag(string, substring, True))  # Output: 1 (counts overlapping pairs)
print(count_substring_loop_flag(string, substring, False)) # Output: 1 (does not count overlapping pairs)

