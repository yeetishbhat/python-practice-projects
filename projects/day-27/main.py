from math import floor
from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.60934)
    result.config(text=f"{km}")


window = Tk()
window.title("miles to km")
window.configure(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_lable = Label(text="miles")
miles_lable.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

result = Label(text="0")
result.grid(row=1, column=1)

km_label = Label(text="km")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate" , command=miles_to_km)
calculate_button.grid(row=2, column=1)



window.mainloop()


