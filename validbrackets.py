def check_validity(text: str) -> str:
    # Bracket symbols and their corresponding closing brackets
    bracket_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    open_brackets = set(bracket_pairs.values())
    stack = []
    
    for char in text:
        if char in open_brackets:
            stack.append(char)  # Push open brackets onto the stack
        elif char in bracket_pairs:
            if not stack or stack[-1] != bracket_pairs[char]:
                return f"Invalid: Mismatched or unbalanced bracket '{char}'"
            stack.pop()  # Pop if a matching closing bracket is found
        elif char.isalnum():
            continue  # Ignore alphanumeric characters
        else:
            return f"Invalid: Invalid character '{char}'"
    
    if stack:
        return "Invalid: Unbalanced brackets"
    return "Valid"


def get_valid_invalid_text_count(texts: list) -> tuple:
    valid_count = 0
    invalid_count = 0
    
    for item in texts:
        if isinstance(item, str):  # Check if item is a string
            validity = check_validity(item)
            if validity == "Valid":
                valid_count += 1
            else:
                print(f"Invalid text: {item} -> Reason: {validity}")
                invalid_count += 1
    
    return valid_count, invalid_count

void main:
# Example usage
	texts = ['[{(', 45, "()", "{1}", "(<)>", ")(", "{[<>]}", "+()"]
	result = get_valid_invalid_text_count(texts)
	print("Valid and Invalid counts:", result)

