def describe_number(num):
    match num:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case _ if num > 1 and num < 10:
            return "A single-digit positive number"
        case _:
            return "Other"

print(describe_number(5))   # Output: A single-digit positive number
print(describe_number(0))   # Output: Zero
print(describe_number(-3))  # Output: Other
print("complited implimetation of First method of using switch case")
print()
def case_one():
    return "This is case one"

def case_two():
    return "This is case two"

def default_case():
    return "This is the default case"

# Dictionary mapping for switch-case functionality
switch = {
    1: case_one,
    2: case_two
}

# Function to simulate switch-case
def switch_case(case):
    return switch.get(case, default_case)()

# Usage
print(switch_case(1))  # Output: "This is case one"
print(switch_case(2))  # Output: "This is case two"
print(switch_case(3))  # Output: "This is the default case"
print("complited implimetation of Second method of using switch case")
print()
def switch_case(case):
    if case == 1:
        return "This is case one"
    elif case == 2:
        return "This is case two"
    else:
        return "This is the default case"

# Usage
print(switch_case(1))  # Output: "This is case one"
print(switch_case(2))  # Output: "This is case two"
print(switch_case(3))  # Output: "This is the default case"
print("complited implimetation of Third method of using switch case")
print()
