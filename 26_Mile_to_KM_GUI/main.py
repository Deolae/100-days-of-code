from tkinter import *

FONT = ("Arial",16,"normal")

# Create window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200,height=150)
window.config(padx=25,pady=25)

# Labels:
miles_text = Label(text= "Miles", font=FONT, padx=5, pady=5)
miles_text.grid(row=0,column=2)

equal_text = Label(text= "is equal to", font=FONT, padx=5, pady=5)
equal_text.grid(row=1,column=0)

result_text = Label(text="0", font=FONT, padx=5, pady=5)
result_text.grid(row=1,column=1)

km_text = Label(text= "Km", font=FONT, padx=5, pady=5)
km_text.grid(row=1,column=2)

# Buttons:
def button_clicked():
    miles = float(input.get())
    km = round(number=miles * 1.609, ndigits=2)
    result_text.config(text=km)

button = Button(text="Calculate", command=button_clicked, padx=5, pady=5)
button.grid(row=2,column=1)

# Entry:
input = Entry(width=15)
input.grid(row=0,column=1)

# Keep the window open (Should be at the end of code)
window.mainloop()