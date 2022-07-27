#import tkinter as tk
from tkinter import *
from tkinter.ttk import *

#validator1.3
# Do not use this validator
'''
class Validator:
    def __init__(self, master1):
        self.panel2 = tk.Frame(master1)
        self.panel2.grid()

        vcmd = (master1.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.lbl1 = tk.Label(window, text="Battery capacity", font=("Arial Bold", 15))
        self.lbl1.grid(column=0, row=0)
        self.lbl2 = tk.Label(window, text="", font=("Arial Bold", 15))
        self.lbl2.grid(column=0, row=1)
        self.lbl3 = tk.Label(window, text="Capacity  ", font=("Arial Bold", 13))
        self.lbl3.grid(column=0, row=2)
        self.lbl4 = tk.Label(window, text="", font=("Arial Bold", 15))
        self.lbl4.grid(column=0, row=3)
        self.lbl5 = tk.Label(window, text="Device", font=("Arial Bold", 15))
        self.lbl5.grid(column=0, row=4)
        self.lbl6 = tk.Label(window, text="", font=("Arial Bold", 15))
        self.lbl6.grid(column=0, row=5)
        self.lbl7 = tk.Label(window, text="", font=("Arial Bold", 15))
        self.lbl7.grid(column=0, row=7)
        self.lbl8 = tk.Label(window, text="Report time ", font=("Arial Bold", 13))
        self.lbl8.grid(column=0, row=8)
        self.lbl7 = tk.Label(window, text="", font=("Arial Bold", 15))
        self.lbl7.grid(column=0, row=9)
        self.lbl9 = tk.Label(window, text="Work time ", font=("Arial Bold", 13))
        self.lbl9.grid(column=0, row=10)
        self.lbl7 = tk.Label(window, text="", font=("Arial Bold", 15))
        self.lbl7.grid(column=0, row=11)
        self.lbl10 = tk.Label(window, text="Sleep time", font=("Arial Bold", 13))
        self.lbl10.grid(column=0, row=12)
        self.lbl11 = tk.Label(window, text="", font=("Arial Bold", 15))
        self.lbl11.grid(column=0, row=13)
        self.lbl13 = tk.Label(window, text="Battery self discharge", font=("Arial Bold", 15))
        self.lbl13.grid(column=0, row=14)
        self.lbl14 = tk.Label(window, text="", font=("Arial Bold", 15))
        self.lbl14.grid(column=0, row=15)
        self.lbl15 = tk.Label(window, text="self discharge", font=("Arial Bold", 13))
        self.lbl15.grid(column=0, row=16)
        self.lbl16 = tk.Label(window, text="", font=("Arial Bold", 15))
        self.lbl16.grid(column=0, row=17)
        self.lbl19 = tk.Label(window, text="Cyclic mode", font=("Arial Bold", 15))
        self.lbl19.grid(column=0, row=18)
        #self.lbl20 = tk.Label(window, text="", font=("Arial Bold", 15))
        #self.lbl20.grid(column=0, row=19)
        self.lbl21 = tk.Label(window, text="Estimated battery lifetime", font=("Arial Bold", 15))
        self.lbl21.grid(column=0, row=20)
        self.lbl22 = tk.Label(window, text="", font=("Arial Bold", 15))
        self.lbl22.grid(column=0, row=21)
        self.lbl23 = tk.Label(window, text="Lifetime", font=("Arial Bold", 13))
        self.lbl23.grid(column=0, row=22)
        self.lbl24 = tk.Label(window, text="Iterations", font=("Arial Bold", 13))
        self.lbl24.grid(column=0, row=23)

        self.lbl41 = tk.Label(window, text=".               .", font=("Arial Bold", 13))
        self.lbl41.grid(column=1, row=22)
        self.lbl42 = tk.Label(window, text=" ", font=("Arial Bold", 13))
        self.lbl42.grid(column=1, row=23)

        self.lbl61 = tk.Label(window, text="Ah", font=("Arial Bold", 13))
        self.lbl61.grid(column=3, row=2)
        self.lbl62 = tk.Label(window, text="s", font=("Arial Bold", 13))
        self.lbl62.grid(column=3, row=8)
        self.lbl63 = tk.Label(window, text="s", font=("Arial Bold", 13))
        self.lbl63.grid(column=3, row=10)
        self.lbl64 = tk.Label(window, text="s", font=("Arial Bold", 13))
        self.lbl64.grid(column=3, row=12)
        self.lbl65 = tk.Label(window, text="%", font=("Arial Bold", 13))
        self.lbl65.grid(column=3, row=16)

        self.txt1 = tk.Entry(window, validate='key', validatecommand=vcmd, width=10)
        self.txt1.grid(column=2, row=2)
        self.txt2 = tk.Entry(window, validate='key', validatecommand=vcmd, width=10)
        self.txt2.grid(column=2, row=8)
        self.txt3 = tk.Entry(window, validate='key', validatecommand=vcmd, width=10)
        self.txt3.grid(column=2, row=10)
        self.txt4 = tk.Entry(window, validate='key', validatecommand=vcmd, width=10)
        self.txt4.grid(column=2, row=12)
        self.txt5 = tk.Entry(window, validate='key', validatecommand=vcmd, width=10)
        self.txt5.grid(column=2, row=16)
        #self.txt6 = tk.Entry(window, validate='key', validatecommand=vcmd, width=10)
        #self.txt6.grid(column=2, row=18)
        self.txt_rep_cap = tk.Entry(window, validate='key', validatecommand=vcmd, width=10)
        self.txt_rep_cap.grid(column=4, row=9)
        self.txt_wrk_cap = tk.Entry(window, validate='key', validatecommand=vcmd, width=10)
        self.txt_wrk_cap.grid(column=4, row=11)
        self.txt_slp_cap = tk.Entry(window, validate='key', validatecommand=vcmd, width=10)
        self.txt_slp_cap.grid(column=4, row=13)

        # self.lbl100 = tk.Label(window, text="",width=10, font=("Arial Bold",13))
        # self.lbl100.grid(column=2, row=18)

        # self.text1 = tk.Entry(self.panel2, validate='key', validatecommand=vcmd)
        # self.text1.grid()
        # self.text1.focus()

        # self.text2 = tk.Entry(self.panel2, validate='key', validatecommand=vcmd)
        # self.text2.grid()
        # self.text2.focus()

    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False
'''

def clicked_get_device():
    pass


def print_something():
    pass

def print_r():
    global mode
    if len(mode) < 7:
        mode+="R"
    lbl100.configure(text=mode)
def print_s():
    global mode
    if len(mode) < 7:
        mode += "S"
    lbl100.configure(text=mode)
def print_w():
    global mode
    if len(mode) < 7:
        mode += "W"
    lbl100.configure(text=mode)
def clean():
    global mode
    mode = mode[:-1]
    lbl100.configure(text=mode)

mode = ""

window =Tk()
window.title("Battery Life Estimator ")
window.geometry("700x700")

sv1 = StringVar()
sv2 = StringVar()
sv3 = StringVar()
sv4 = StringVar()
sv5 = StringVar()
sv6 = StringVar()
sv7 = StringVar()
sv8 = StringVar()

def validate_float(var):
    new_value = var.get()
    try:
        new_value == '' or float(new_value)
        validate_float.old_value = new_value
    except:
        var.set(validate_float.old_value)

validate_float.old_value = ''  # Define function attribute.

# trace wants a callback with nearly useless parameters, fixing with lambda.
sv1.trace('w', lambda nm, idx, mode, var=sv1: validate_float(var))
sv2.trace('w', lambda nm, idx, mode, var=sv2: validate_float(var))
sv3.trace('w', lambda nm, idx, mode, var=sv3: validate_float(var))
sv4.trace('w', lambda nm, idx, mode, var=sv4: validate_float(var))
sv5.trace('w', lambda nm, idx, mode, var=sv5: validate_float(var))
sv6.trace('w', lambda nm, idx, mode, var=sv6: validate_float(var))
sv7.trace('w', lambda nm, idx, mode, var=sv7: validate_float(var))
sv8.trace('w', lambda nm, idx, mode, var=sv8: validate_float(var))

combo = Combobox(window)
combo['values'] = ("Findy bike", "Findy car", "Findy Raid", "Findy pet", "Water meter", "Test device")
combo.current(0)
combo.grid(column=0, row=6)

btn1 = Button(window, text="Device consumption", command=clicked_get_device)
btn1.grid(column=4, row=6)
btn2 = Button(window, text="Calculate", command=print_something)
btn2.grid(column=4, row=22)
btn_report = Button(window, text="Report", command=print_r)
btn_report.grid(column=1, row=19)
btn_work = Button(window, text="Work", command=print_w)
btn_work.grid(column=2, row=19)
btn_sleep = Button(window, text="Sleep", command=print_s)
btn_sleep.grid(column=3, row=19)
btn_clean = Button(window, text="X", command=clean)
btn_clean.grid(column=3, row=18)

lbl1 = Label(window, text="Battery capacity", font=("Arial Bold", 15))
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text="", font=("Arial Bold", 15))
lbl2.grid(column=0, row=1)
lbl3 = Label(window, text="Capacity  ", font=("Arial Bold", 13))
lbl3.grid(column=0, row=2)
lbl4 = Label(window, text="", font=("Arial Bold", 15))
lbl4.grid(column=0, row=3)
lbl5 = Label(window, text="Device", font=("Arial Bold", 15))
lbl5.grid(column=0, row=4)
lbl6 = Label(window, text="", font=("Arial Bold", 15))
lbl6.grid(column=0, row=5)
lbl7 = Label(window, text="", font=("Arial Bold", 15))
lbl7.grid(column=0, row=7)
lbl8 = Label(window, text="Report time ", font=("Arial Bold", 13))
lbl8.grid(column=0, row=8)
lbl7 = Label(window, text="", font=("Arial Bold", 15))
lbl7.grid(column=0, row=9)
lbl9 = Label(window, text="Work time ", font=("Arial Bold", 13))
lbl9.grid(column=0, row=10)
lbl7 = Label(window, text="", font=("Arial Bold", 15))
lbl7.grid(column=0, row=11)
lbl10 = Label(window, text="Sleep time", font=("Arial Bold", 13))
lbl10.grid(column=0, row=12)
lbl11 = Label(window, text="", font=("Arial Bold", 15))
lbl11.grid(column=0, row=13)
lbl13 = Label(window, text="Battery self discharge", font=("Arial Bold", 15))
lbl13.grid(column=0, row=14)
lbl14 = Label(window, text="", font=("Arial Bold", 15))
lbl14.grid(column=0, row=15)
lbl15 = Label(window, text="self discharge", font=("Arial Bold", 13))
lbl15.grid(column=0, row=16)
lbl16 = Label(window, text="", font=("Arial Bold", 15))
lbl16.grid(column=0, row=17)
lbl19 = Label(window, text="Cyclic mode", font=("Arial Bold", 15))
lbl19.grid(column=0, row=18)
lbl21 = Label(window, text="Estimated battery lifetime", font=("Arial Bold", 15))
lbl21.grid(column=0, row=20)
lbl22 = Label(window, text="", font=("Arial Bold", 15))
lbl22.grid(column=0, row=21)
lbl23 = Label(window, text="Lifetime", font=("Arial Bold", 13))
lbl23.grid(column=0, row=22)
lbl24 = Label(window, text="Iterations", font=("Arial Bold", 13))
lbl24.grid(column=0, row=23)

lbl41 = Label(window, text=".               .", font=("Arial Bold", 13))
lbl41.grid(column=1, row=22)
lbl42 = Label(window, text=" ", font=("Arial Bold", 13))
lbl42.grid(column=1, row=23)

lbl61 = Label(window, text="Ah", font=("Arial Bold", 13))
lbl61.grid(column=3, row=2)
lbl62 = Label(window, text="s", font=("Arial Bold", 13))
lbl62.grid(column=3, row=8)
lbl63 = Label(window, text="s", font=("Arial Bold", 13))
lbl63.grid(column=3, row=10)
lbl64 = Label(window, text="s", font=("Arial Bold", 13))
lbl64.grid(column=3, row=12)
lbl65 = Label(window, text="%", font=("Arial Bold", 13))
lbl65.grid(column=3, row=16)

txt1 = Entry(window, validate='key', textvariable=sv1, width=10)
txt1.grid(column=2, row=2)
txt2 = Entry(window, validate='key', textvariable=sv2, width=10)
txt2.grid(column=2, row=8)
txt3 = Entry(window, validate='key', textvariable=sv3, width=10)
txt3.grid(column=2, row=10)
txt4 = Entry(window, validate='key', textvariable=sv4, width=10)
txt4.grid(column=2, row=12)
txt5 = Entry(window, validate='key', textvariable=sv5, width=10)
txt5.grid(column=2, row=16)
txt_rep_cap = Entry(window, validate='key', textvariable=sv6, width=10)
txt_rep_cap.grid(column=4, row=9)
txt_wrk_cap = Entry(window, validate='key', textvariable=sv7, width=10)
txt_wrk_cap.grid(column=4, row=11)
txt_slp_cap = Entry(window, validate='key', textvariable=sv8, width=10)
txt_slp_cap.grid(column=4, row=13)


lbl100 = Label(window, text=".                    .",width=10, font=("Arial Bold",13))
lbl100.grid(column=2, row=18)

lbl_rep_cap = Label(window, text="report cap",width=10, font=("Arial Bold",13))
lbl_rep_cap.grid(column=4, row=8)
lbl101 = Label(window, text="mA",width=10, font=("Arial Bold",13))
lbl101.grid(column=5, row=8)
lbl_wrc_cap = Label(window, text="work cap",width=10, font=("Arial Bold",13))
lbl_wrc_cap.grid(column=4, row=10)
lbl102 = Label(window, text="mA",width=10, font=("Arial Bold",13))
lbl102.grid(column=5, row=10)
lbl_slp_cap = Label(window, text="sleep cap",width=10, font=("Arial Bold",13))
lbl_slp_cap.grid(column=4, row=12)
lbl103 = Label(window, text="mA",width=10, font=("Arial Bold",13))
lbl103.grid(column=5, row=12)






window.mainloop()
