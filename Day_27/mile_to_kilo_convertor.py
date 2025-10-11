from tkinter import *

def miles_to_km():
    miles = float(mile_entry.get())
    km = miles * 1.609
    kilo_result_label.config(text=f"{km:.2f}")

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=150, height=150)
window.config(padx=20, pady=20)

mile_entry = Entry(width=10)
mile_entry.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

kilo_result_label = Label(text="0")
kilo_result_label.grid(column=1, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)

window.mainloop()