import time

def get_odds_evens_count1(li):
    counteven = 0
    for num in li:
        counteven += num % 2 == 0
    return len(li) - counteven, counteven

def get_odds_evens_count2(li):
    counteven = 0
    for num in li:
        if num % 2 == 0:
            counteven += 1
    return len(li) - counteven, counteven

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

start_time1 = time.time()
result1 = get_odds_evens_count1(li)
end_time1 = time.time()
print(result1, "first is odd count and second is even")

start_time2 = time.time()
result2 = get_odds_evens_count2(li)
end_time2 = time.time()
print(result2, "first is odd count and second is even")

start_time3 = time.time()
result3 = get_odds_evens_count3(li)
end_time3 = time.time()
print(result3, "first is odd count and second is even")

start_time4 = time.time()
result4 = get_odds_evens_count4(li)
end_time4 = time.time()
print(result4, "first is odd count and second is even")

time_diff1 = end_time1 - start_time1
time_diff2 = end_time2 - start_time2
time_diff3 = end_time3 - start_time3
time_diff4 = end_time4 - start_time4

time_diffs = [time_diff1, time_diff2, time_diff3, time_diff4]

min_time = min(time_diffs)
min_index = time_diffs.index(min_time) + 1  

print(f"The least time-taking function is get_odds_evens_count{min_index} with time: {min_time}")

