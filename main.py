from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font = ("Sans", 68, 'bold')
background = "#ffff5c"
foreground = "#0f0f0f"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(column=1, row=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
