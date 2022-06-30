
from tkinter import *



window = Tk()
window.title("Test window")
window.geometry("400x400")
sv = StringVar()

def validate_float(var):
    new_value = var.get()
    try:
        new_value == '' or float(new_value)
        validate_float.old_value = new_value
    except:
        var.set(validate_float.old_value)

validate_float.old_value = ''  # Define function attribute.

# trace wants a callback with nearly useless parameters, fixing with lambda.
sv.trace('w', lambda nm, idx, mode, var=sv: validate_float(var))
ent = Entry(window, textvariable=sv)
ent.grid(column=0,row=1)
ent.pack()
ent.focus_set()



window.mainloop()