def extract_numeric_elements(l):
    numeric_elements = []
    
    
    for obj in l:
        if isinstance(obj, (int, float)): 
            numeric_elements.append(obj)
        elif isinstance(obj, (tuple, list, set)):  
            for elem in obj:
                if isinstance(elem, (int, float)):
                    numeric_elements.append(elem)
        elif isinstance(obj, dict):  
            for key, value in obj.items():
                if isinstance(key, (int, float)):
                    numeric_elements.append(key)
                if isinstance(value, (int, float)):
                    numeric_elements.append(value)
    
    return numeric_elements

def get_second_smallest_largest(l):
    
    numeric_elements = extract_numeric_elements(l)
    
    if len(numeric_elements) == 0:
        return "No numeric elements found"
    if len(numeric_elements) == 1:
        return f"Only one numeric element: {numeric_elements[0]}"
    
    numeric_elements = sorted(set(numeric_elements))
    
    if len(numeric_elements) < 2:
        return "Not enough unique numbers for second smallest/largest"
    
    second_smallest = numeric_elements[1]
    second_largest = numeric_elements[-2]
    
    return f"Second smallest number is {second_smallest}, second largest number is {second_largest}"


li = [2345, 34, "shravani", [34, 55], (345, 43, "anna"), {23: "sh", 34: 44, "anna": "sibling"}, {34, 22, "shrau"}, "3+4i", "parth"]
result = get_second_smallest_largest(li)
print(result)

