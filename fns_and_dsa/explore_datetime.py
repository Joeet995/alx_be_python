from datetime import datetime, date, timedelta

def display_current_datetime():
    date = datetime.now()
    current_date = date.strftime("%Y-%M-%d %H-%M-%S")

    print(f"Current date and time: {current_date}")

def calculate_future_date():
    Number_of_days = int(input("Enter the number of days to add to the current date: "))
    delta = timedelta(days=Number_of_days)
    day = datetime.today()
    future_date = day + delta
    result = future_date.strftime("%Y-%M-%d")

    print(f"Future date: {result}")

display_current_datetime()
calculate_future_date()