import datetime
import time
import tkinter as tk

class AlarmClock:
    def __init__(self):
        self.alarm_time = None

    def set_alarm(self, hour, minute, second):
        self.alarm_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, hour, minute, second)

    def check_alarm(self):
        current_time = datetime.datetime.now()
        if current_time >= self.alarm_time:
            return True
        else:
            return False

    def snooze(self):
        self.alarm_time += datetime.timedelta(minutes=10)

class AlarmClockGUI:
    def __init__(self, alarm_clock):
        self.alarm_clock = alarm_clock

        self.root = tk.Tk()
        self.root.title("Alarm Clock")

        self.hour_label = tk.Label(self.root, text="Hour:")
        self.hour_entry = tk.Entry(self.root)
        self.hour_label.grid(row=0, column=0)
        self.hour_entry.grid(row=0, column=1)

        self.minute_label = tk.Label(self.root, text="Minute:")
        self.minute_entry = tk.Entry(self.root)
        self.minute_label.grid(row=1, column=0)
        self.minute_entry.grid(row=1, column=1)

        self.second_label = tk.Label(self.root, text="Second:")
        self.second_entry = tk.Entry(self.root)
        self.second_label.grid(row=2, column=0)
        self.second_entry.grid(row=2, column=1)

        self.set_alarm_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.grid(row=3, column=0)

        self.snooze_button = tk.Button(self.root, text="Snooze", command=self.snooze)
        self.snooze_button.grid(row=3, column=1)

        self.root.mainloop()

    def set_alarm(self):
        hour = int(self.hour_entry.get())
        minute = int(self.minute_entry.get())
        second = int(self.second_entry.get())

        self.alarm_clock.set_alarm(hour, minute, second)

    def snooze(self):
        self.alarm_clock.snooze()

def main():
    alarm_clock = AlarmClock()
    alarm_clock_gui = AlarmClockGUI(alarm_clock)

    while True:
        if alarm_clock.check_alarm():
            # Play an alarm sound here
            alarm_clock_gui.root.bell()
            time.sleep(10)
            alarm_clock.snooze()

if __name__ == "__main__":
    main()
