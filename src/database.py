import datetime
import os 

def save_today(current_time_studied):
    today = datetime.datetime.now()
    filename = f"data/{today.year}-{today.month}-{today.day}.txt"
    with open(filename, 'w') as f:
        f.write(f"Study session for {today.day}/{today.month}/{today.year}\n")
        f.write(f"Total study time: {current_time_studied} seconds\n")
    print(f"Data saved to {filename}")

def read_today():
    today = datetime.datetime.now()
    filename = f"data/{today.year}-{today.month}-{today.day}.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = f.readlines()
            studied_time = int(float(data[-1].split(" ")[-2]))
    else:
        print(f"No data found for {today.day}/{today.month}/{today.year}")

    return studied_time
