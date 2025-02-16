import time, sys
import tkinter as tk
from datetime import datetime

months_number = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.breaks = []
        self.elapsed_study_time = 0
        self.paused = False
        self.break_start_time = None
        self.running = False  # Track if the timer is running

    def get_current_time(self):
        """Returns the current time in seconds."""
        return time.time()

    def format_time(self, seconds):
        """Converts seconds into HH:MM:SS format."""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def init(self):
        """Initializes the Timer GUI."""
        self.root = tk.Tk()
        self.root.geometry('300x200')
        self.root.title("Study Timer")

        # Timer Label
        self.time_label = tk.Label(self.root, text="Study Time: 00:00:00", font=("Arial", 14))
        self.time_label.grid(column=0, row=1, columnspan=3, pady=10)

        # Buttons
        self.start_button = tk.Button(self.root, text="Start Timer", command=self.start_timer)
        self.start_button.grid(column=0, row=0)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.start_break)
        self.pause_button.grid(column=1, row=0)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.end_timer)
        self.stop_button.grid(column=2, row=0)

        self.update_timer_display()
        self.root.mainloop()

    def update_timer_display(self):
        """Updates the timer display every second in HH:MM:SS format."""
        if self.running and not self.paused:
            elapsed = self.get_current_time() - self.start_time - sum(self.breaks)
            self.time_label.config(text=f"Study Time: {self.format_time(elapsed)}")
        self.root.after(1000, self.update_timer_display)  # Refresh every second

    def start_timer(self):
        """Starts the study timer."""
        if not self.running:
            self.start_time = self.get_current_time()
            self.running = True
            print("Timer started.")
        else:
            print("Timer is already running.")

    def start_break(self):
        """Pauses the timer and starts a break."""
        if self.running and not self.paused:
            self.paused = True
            self.break_start_time = self.get_current_time()
            self.pause_button.config(text="Unpause", command=self.end_break)
            print("Break started.")

    def end_break(self):
        """Resumes the study timer after a break."""
        if self.running and self.paused:
            break_duration = self.get_current_time() - self.break_start_time
            self.breaks.append(break_duration)
            self.paused = False
            self.pause_button.config(text="Pause", command=self.start_break)
            print(f"Break ended. Duration: {self.format_time(break_duration)}.")

    def end_timer(self):
        """Stops the timer and calculates total study time."""
        if self.running:
            self.end_time = self.get_current_time()
            total_time = self.get_total_study_time()
            print(f"Total study time: {self.format_time(total_time)}")
            self.running = False
            self.save_results()
        else:
            print("Timer was not started.")

    def get_total_study_time(self):
        """Calculates the total study time excluding breaks."""
        if not self.running:
            return 0
        total_time = self.get_current_time() - self.start_time - sum(self.breaks)
        return total_time

    def save_results(self):
        """Saves study results."""
        print("Saving results...")
        print(f"Total break time: {self.format_time(sum(self.breaks))}")

class Time():
    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month 
        self.day = day 
        self.hour = hour 
        self.minute = minute        
        self.second = second 

    def print(self):
        print(f"Current date: {months_number[self.month]}, {self.day}, {self.year} \nCurrent time: {self.hour:02}:{self.minute:02}:{self.second:02}")

def time_diff(time1: Time, time2: Time):
    """
    Takes 2 different times and returns the time between them.
    For now more or less assumes no study session takes longer than 24h.
    """
    dt1 = datetime(time1.year, time1.month, time1.day, time1.hour, time1.minute, time1.second)
    dt2 = datetime(time2.year, time2.month, time2.day, time2.hour, time2.minute, time2.second)
    
    delta = dt2 - dt1  

    print(delta.seconds)

    hours = int(delta.seconds / 3600)
    minutes = int(delta.seconds % 60)
    seconds = int(delta.seconds % 3600)

    print(minutes)

    return (hours, minutes, seconds)

def get_current_time():
    """
    Function to get the current time. Includes year, month, day, hour, minute, second as an instance of the class Time
    """
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    second = time.localtime().tm_sec
    return Time(year, month, day, hour, minute, second)

if __name__ == '__main__':
    timer = Timer()
    timer.init()

    # t1 = Time(2025, 5, 4, 12, 30, 45)
    # t2 = Time(2025, 5, 4, 13, 30, 46)

    # difference = time_diff(t1, t2)
    # print(difference)