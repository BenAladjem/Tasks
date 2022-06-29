from tkinter import *

from tkinter.ttk import *

from abc import ABC, abstractmethod

window = Tk()
window.title("Battery Life Estimator ")

window.geometry("500x600")

lbl1 = Label(window, text="Battery capacity", font=("Arial Bold", 15))
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text="", font=("Arial Bold", 15))
lbl2.grid(column=0, row=1)
lbl3 = Label(window, text="Capacity  ", font=("Arial Bold", 13))
lbl3.grid(column=0, row=2)
lbl4 = Label(window, text="", font=("Arial Bold", 15))
lbl4.grid(column=0, row=3)
lbl5 = Label(window, text="Report time ", font=("Arial Bold", 13))
lbl5.grid(column=0, row=4)
lbl6 = Label(window, text="Work time ", font=("Arial Bold", 13))
lbl6.grid(column=0, row=5)
lbl7 = Label(window, text="Sleep time", font=("Arial Bold", 13))
lbl7.grid(column=0, row=6)
lbl8 = Label(window, text="Ah", font=("Arial Bold", 13))
lbl8.grid(column=3, row=2)
lbl9 = Label(window, text="s", font=("Arial Bold", 13))
lbl9.grid(column=3, row=4)
lbl10 = Label(window, text="s", font=("Arial Bold", 13))
lbl10.grid(column=3, row=5)
lbl11 = Label(window, text="s", font=("Arial Bold", 13))
lbl11.grid(column=3, row=6)
lbl12 = Label(window, text="", font=("Arial Bold", 15))
lbl12.grid(column=0, row=7)
lbl13 = Label(window, text="Battery self discharge", font=("Arial Bold", 15))
lbl13.grid(column=0, row=8)
lbl14 = Label(window, text="", font=("Arial Bold", 15))
lbl14.grid(column=0, row=9)
lbl15 = Label(window, text="self discharge", font=("Arial Bold", 13))
lbl15.grid(column=0, row=10)
lbl16 = Label(window, text="%", font=("Arial Bold", 13))
lbl16.grid(column=3, row=10)
lbl17 = Label(window, text="", font=("Arial Bold", 15))
lbl17.grid(column=0, row=12)
lbl18 = Label(window, text="Device", font=("Arial Bold", 15))
lbl18.grid(column=0, row=13)
lbl19 = Label(window, text="", font=("Arial Bold", 15))
lbl19.grid(column=0, row=14)
lbl20 = Label(window, text="", font=("Arial Bold", 15))
lbl20.grid(column=0, row=17)
lbl21 = Label(window, text="Mode", font=("Arial Bold", 15))
lbl21.grid(column=0, row=18)
lbl22 = Label(window, text="", font=("Arial Bold", 15))
lbl22.grid(column=0, row=19)
lbl23 = Label(window, text="Estimated battery lifetime", font=("Arial Bold", 15))
lbl23.grid(column=0, row=20)
lbl24 = Label(window, text="", font=("Arial Bold", 15))
lbl24.grid(column=0, row=21)
lbl25 = Label(window, text="Lifetime", font=("Arial Bold", 13))
lbl25.grid(column=0, row=22)
lbl26 = Label(window, text="Iterations", font=("Arial Bold", 13))
lbl26.grid(column=0, row=23)
lbl27 = Label(window, text="1y", font=("Arial Bold", 13))
lbl27.grid(column=1, row=22)
lbl28 = Label(window, text="199", font=("Arial Bold", 13))
lbl28.grid(column=1, row=23)

txt1 = Entry(window, width=10)
txt1.grid(column=2, row=2)
txt2 = Entry(window, width=10)
txt2.grid(column=2, row=4)
txt3 = Entry(window, width=10)
txt3.grid(column=2, row=5)
txt4 = Entry(window, width=10)
txt4.grid(column=2, row=6)
txt5 = Entry(window, width=10)
txt5.grid(column=2, row=10)
txt6 = Entry(window, width=10)
txt6.grid(column=2, row=18)

combo = Combobox(window)
combo['values'] = ("Findy bike", "Findy car", "Findy Raid", "Findy pet", "Water meter")
combo.current(0)
combo.grid(column=0, row=15)

kind_of_device = ''
global batt_capacity
global report_time
global sleep_time
global work_time
global type_report
global batt_self_discharge
global class_device

class F5():
    #  inherit calculate_iterations and calculate_time methods

    #  добре е стойностите да се валидират със getter / setter
    AVG_CURRENT_CONSUMPTION_REPORT = 48  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 1.82  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 60  # не е измервана, само за проба

    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, type_rep, bsd):

        self.type_rep = type_rep
        self.wrk_time = wrk_time
        self.bsd = bsd  # batt self discharge
        self.slp_time = slp_time
        self.rep_time = rep_time
        self.bat_cap = bat_cap
        
        
def clicked_get_device():
    kind_of_device = combo.get()
    # lbl.configure(text=combo.get())
    print(combo.get())




def print_something():
    global class_device
    batt_capacity = txt1.get()
    report_time = txt2.get()
    work_time = txt3.get()
    sleep_time = txt4.get()
    batt_self_discharge = txt5.get()
    device = combo.get()
    type_report = txt6.get()
    
    if device == "Findy bike":
        class_device = FB
    elif device == "Findy car":
        class_device = FC
    elif device == "Findy pet":
        class_device = F5
    elif device == "Findy Raid":
        class_device = FR
    elif device == "Water meter":
        class_device = WaterMeter
    
    dev = class_device(batt_capacity, report_time, sleep_time, work_time, type_report, batt_self_discharge)
    
    print(dev.bat_cap, dev.rep_time, dev.slp_time, dev.wrk_time, dev.type_rep, dev.bsd)
    lbl27.configure(text=dev.bat_cap)
    lbl28.configure(text=dev.type_rep)
    print("cap " + batt_capacity)
    print("report time " + report_time)
    print("work time " + work_time)
    print("sleep time " + sleep_time)
    print("device  " + device)
    print("MODE " + type_report)


btn1 = Button(window, text="Get device", command=clicked_get_device)
btn1.grid(column=3, row=15)
btn2 = Button(window, text="Calculate", command=print_something)
btn2.grid(column=3, row=22)






'''
    cap = txt1.get()
    report_time = txt2.get()
    work_time = txt3.get()
    sleep_time = txt4.get()
    self_discharge = txt5.get()
    device = combo.get()
    mode = txt6.get()
'''

#batt_capacity = cap  # mAh
#batt_self_discharge = self_discharge

#type_report = mode  # that means report, work, sleep
#type_report2 = "rwswr"  # that means report, work, sleep, work, report
'''
report_time = 0.5 / 60  # (h)
sleep_time = 5 / 60  # (h)
work_time = 0.5 / 60  # (h)
'''
'''
dog = F5(batt_capacity, report_time, sleep_time, work_time, type_report, batt_self_discharge)
# print(dog.one_iter)
print(f"dog {dog.calculate_iterations()}")
print(f"dog {dog.calculate_time()}")
print()



wm = WaterMeter(18000, 0.0115589, 12, 4, "rwswr", 0)
wm2 = WaterMeter(2500, 0.05, 10, 2, "rs", 0)
print(f"WM {wm.calculate_iterations()}")
print(f"WM {wm.calculate_time()}")

print(f"WM2 {wm2.calculate_iterations()}")
print(f"WM2 {wm2.calculate_time()}")
print()

car = FC(batt_capacity, report_time, sleep_time, work_time, type_report, batt_self_discharge)
print(f"FindyCar {car.calculate_iterations()}")
print(f"FindyCar {car.calculate_time()}")
print()

bike = FB(batt_capacity, report_time, sleep_time, work_time, type_report2, batt_self_discharge)
print(f"FindyBike {bike.calculate_iterations()}")
print(f"FindyBike {bike.calculate_time()}")
print()
'''
#print(device)

window.mainloop()

