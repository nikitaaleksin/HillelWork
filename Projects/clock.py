import tkinter as tk
import time

def update_clock():
    present_time = time.strftime("%H:%M:%S")
    ceas.config(text=present_time)
    ceas.after(1000, update_clock)
app = tk.Tk()
app.title("Бурмалдильник")
ceas = tk.Label(app, text="", font=("Tahoma", 106))
ceas.pack()
update_clock()
app.mainloop()