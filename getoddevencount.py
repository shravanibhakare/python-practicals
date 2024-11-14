def get_odds_evens_count1(li):
	counteven = 0
	for num in li:
		counteven += num%2==0
	return len(li)-counteven,counteven
	
def get_odds_evens_count2(li):
	counteven = 0
	
	if num%2 ==0:
		counteven+=1
	return len(li)-counteven,counteven
	
def get_odds_evens_count3(li):
    count_even = 0
    count_odd = 0
    for num in li:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_odd, count_even
    
def get_odds_evens_count4(li):
    count_even = len(list(filter(lambda x: x % 2 == 0, li)))
    count_odd = len(li) - count_even
    return count_odd, count_even

li = [23, 45, 55, 43, 44]
result1 = get_odds_evens_count1(li)
print(result1, "first is odd count and second is even")

result2 = get_odds_evens_count2(li)
print(result2,"first is odd count and second is even")

result3 = get_odds_evens_count3(li)
print(result3,"first is odd count and second is even")

result4 = get_odds_evens_count4(li)
print(result1, "first is odd count and second is even")


