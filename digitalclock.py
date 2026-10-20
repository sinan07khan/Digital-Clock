#digital clock using tkinter

import tkinter as ui
import time
window = ui.Tk()
window.title('your digital Clock')
use_24_hour_format = False

def update_clock():
    hours = time.strftime('%H' if use_24_hour_format else '%I')
    minutes = time.strftime('%M')
    seconds = time.strftime('%S')
    am_or_pm = '' if use_24_hour_format else time.strftime('%p')
    time_text = hours + ':' + minutes + ':' + seconds + am_or_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)

def toggle_time_format(event=None):
    global use_24_hour_format
    use_24_hour_format = not use_24_hour_format

digital_clock_lbl = ui.Label(window, text="00:00:00", font=("Comic Sans MS", 40),fg="white")
digital_clock_lbl.pack()
digital_clock_lbl.configure(bg="black")
window.bind('h', toggle_time_format)
window.bind('H', toggle_time_format)

update_clock()
window.mainloop()