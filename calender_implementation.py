def is_leap_year(year):
    """Check if the given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    """Return the number of days in a given month and year."""
    if month in [4, 6, 9, 11]:  
        return 30
    elif month == 2:  
        return 29 if is_leap_year(year) else 28
    else:
        return 31

def zeller_congruence(day, month, year):
    """Calculate the day of the week using Zeller's Congruence."""
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) - (2 * j)) % 7
    return (h + 5) % 7  

def print_month_calendar(month, year):
    """Print the calendar for a specific month and year."""
    days = days_in_month(month, year)
    start_day = zeller_congruence(1, month, year)
    
    print(f"\n{month}/{year}".center(20))
    print("Su Mo Tu We Th Fr Sa")
    
    print("   " * start_day, end="")
    
    for day in range(1, days + 1):
        print(f"{day:2} ", end="")
        if (start_day + day) % 7 == 0:  
            print()
    print()

def print_year_calendar(year):
    """Print the entire calendar for a given year."""
    for month in range(1, 13):
        print_month_calendar(month, year)

#def main():
    # User input
user_input = input("Enter year, or year and month, or year, month, and day (space-separated): ")
inputs = list(map(int, user_input.split()))
    
if len(inputs) == 1:  
        year = inputs[0]
        print_year_calendar(year)
elif len(inputs) == 2:  
        year, month = inputs
        print_month_calendar(month, year)
elif len(inputs) == 3:  
        year, month, day = inputs
        day_of_week = zeller_congruence(day, month, year)
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        print(f"The day of the week for {day}/{month}/{year} is {days[day_of_week]}.")
else:
        print("Invalid input. Please enter a valid date.")

#if __name__ == "__main__":
#    main()

