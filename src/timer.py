import time
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.breaks = []
        self.elapsed_study_time = 0
        self.paused = False
        self.break_start_time = None
        self.running = False  # Track if the timer is running
        self.current_session_start_time = None  # Track when current session started

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
        self.root.geometry('400x300')
        self.root.title("Study Timer")
        self.root.configure(bg='#f0f0f0')  # Light gray background

        # Main frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Title Label
        title_label = tk.Label(main_frame, text="Pomodoro Timer", font=("Arial", 18, "bold"), bg='#f0f0f0')
        title_label.pack(pady=(0, 20))

        # Current Session Label
        self.current_session_label = tk.Label(main_frame, text="Current Session: 00:00:00", 
                                           font=("Arial", 16), bg='#f0f0f0')
        self.current_session_label.pack(pady=5)

        # Timer Label
        self.time_label = tk.Label(main_frame, text="Total Study Time: 00:00:00", 
                                 font=("Arial", 14), bg='#f0f0f0')
        self.time_label.pack(pady=10)

        # Break time label
        self.break_label = tk.Label(main_frame, text="Break Time: 00:00:00",
                                  font=("Arial", 12), bg='#f0f0f0')
        self.break_label.pack(pady=5)

        # Status label
        self.status_label = tk.Label(main_frame, text="Not Started", 
                                   font=("Arial", 10), bg='#f0f0f0', fg='#666666')
        self.status_label.pack(pady=5)

        # Button frame
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(pady=20)

        # Buttons with improved styling
        button_style = {'font': ('Arial', 10), 'width': 10, 'height': 2}
        
        self.start_button = tk.Button(button_frame, text="Start Timer", 
                                    command=self.start_timer,
                                    bg='#4CAF50', fg='white', **button_style)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.pause_button = tk.Button(button_frame, text="Take Break", 
                                    command=self.start_break,
                                    bg='#2196F3', fg='white', **button_style)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(button_frame, text="Stop", 
                                   command=self.end_timer,
                                   bg='#f44336', fg='white', **button_style)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.update_timer_display()
        self.root.mainloop()

    def update_timer_display(self):
        """Updates the timer display every second."""
        if self.running:
            if not self.paused:
                elapsed = self.get_current_time() - self.start_time - sum(self.breaks)
                current_session = self.get_current_time() - self.current_session_start_time
                self.current_session_label.config(text=f"Current Session: {self.format_time(current_session)}")
                self.time_label.config(text=f"Total Study Time: {self.format_time(elapsed)}")
                self.status_label.config(text="Studying", fg='#4CAF50')
            else:
                break_time = self.get_current_time() - self.break_start_time
                self.break_label.config(text=f"Break Time: {self.format_time(break_time)}")
                self.status_label.config(text="On Break", fg='#2196F3')
        
        self.root.after(1000, self.update_timer_display)

    def start_timer(self):
        """Starts the study timer."""
        if not self.running:
            self.start_time = self.get_current_time()
            self.current_session_start_time = self.get_current_time()
            self.running = True
            self.status_label.config(text="Studying", fg='#4CAF50')
            self.start_button.config(state='disabled')

    def start_break(self):
        """Pauses the timer and starts a break."""
        if self.running and not self.paused:
            self.paused = True
            self.break_start_time = self.get_current_time()
            self.pause_button.config(text="End Break", bg='#FFA726')
            self.status_label.config(text="On Break", fg='#2196F3')
            self.pause_button.config(command=self.end_break)

    def end_break(self):
        """Resumes the study timer after a break."""
        if self.running and self.paused:
            break_duration = self.get_current_time() - self.break_start_time
            self.breaks.append(break_duration)
            self.paused = False
            self.current_session_start_time = self.get_current_time()  # Reset current session time
            self.pause_button.config(text="Take Break", bg='#2196F3')
            self.status_label.config(text="Studying", fg='#4CAF50')
            self.pause_button.config(command=self.start_break)

    def end_timer(self):
        """Stops the timer and shows the summary."""
        if self.running:
            self.end_time = self.get_current_time()
            total_study_time = self.get_total_study_time()
            total_break_time = sum(self.breaks)
            
            # Create summary window
            summary = tk.Toplevel(self.root)
            summary.title("Session Summary")
            summary.geometry("300x200")
            summary.configure(bg='#f0f0f0')
            
            # Add summary information
            tk.Label(summary, text="Session Summary", font=("Arial", 14, "bold"), 
                    bg='#f0f0f0').pack(pady=10)
            
            tk.Label(summary, text=f"Total Study Time: {self.format_time(total_study_time)}", 
                    font=("Arial", 12), bg='#f0f0f0').pack(pady=5)
            
            tk.Label(summary, text=f"Total Break Time: {self.format_time(total_break_time)}", 
                    font=("Arial", 12), bg='#f0f0f0').pack(pady=5)
            
            # Calculate average study session
            num_breaks = len(self.breaks)
            if num_breaks > 0:
                avg_study = total_study_time / (num_breaks + 1)
                tk.Label(summary, text=f"Average Study Session: {self.format_time(avg_study)}", 
                        font=("Arial", 12), bg='#f0f0f0').pack(pady=5)
            
            self.running = False
            self.start_button.config(state='normal')
            self.status_label.config(text="Session Ended", fg='#f44336')

    def get_total_study_time(self):
        """Calculates the total study time excluding breaks."""
        if not self.running:
            return 0
        total_time = self.get_current_time() - self.start_time - sum(self.breaks)
        return total_time 