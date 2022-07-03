from tkinter import *

from tkinter.ttk import *

from abc import ABC, abstractmethod

import math

window = Tk()
window.title("Battery Life Estimator ")

window.geometry("600x600")


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
lbl19 = Label(window, text="Mode", font=("Arial Bold", 15))
lbl19.grid(column=0, row=18)
lbl20 = Label(window, text="", font=("Arial Bold", 15))
lbl20.grid(column=0, row=19)
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



txt1 = Entry(window, width=10)
txt1.grid(column=2, row=2)
txt2 = Entry(window, width=10)
txt2.grid(column=2, row=8)
txt3 = Entry(window, width=10)
txt3.grid(column=2, row=10)
txt4 = Entry(window, width=10)
txt4.grid(column=2, row=12)
txt5 = Entry(window, width=10)
txt5.grid(column=2, row=16)
txt6 = Entry(window, width=10)
txt6.grid(column=2, row=18)

combo = Combobox(window)
combo['values'] = ("Findy bike", "Findy car", "Findy Raid", "Findy pet", "Water meter", "Test device")
combo.current(0)
combo.grid(column=0, row=6)

kind_of_device = ''
global batt_capacity
global report_time
global sleep_time
global work_time
global type_report
global batt_self_discharge
global class_device


class Calculations():
    @staticmethod
    def one_iteration_time(typ, rep, slp, wrk):
        iter_time = 0
        for ch in typ:
            if ch == 'r':
                iter_time += rep
            elif ch == 'w':
                iter_time += wrk
            elif ch == 's':
                iter_time += slp
        return iter_time

    @staticmethod
    def one_iteration_capacity(typ, rep, slp, wrk):
        iter_cap = 0
        for ch in typ:
            if ch == 'r':
                iter_cap += rep
            elif ch == 'w':
                iter_cap += wrk
            elif ch == 's':
                iter_cap += slp
        return iter_cap

    @staticmethod
    def time_convert(t):  # Отпечатва в удобен вид времето за живот на батерията
        if t > 24 * 30 * 12:
            years = t // (24 * 30 * 12)
            months = (t - years * 24 * 30 * 12) // (24 * 30)
            return f"{int(years)}y {int(months)}m"
        elif t > 24 * 30:
            months = t // (24 * 30)
            days = (t - (months * 24 * 30)) // 24
            return f"{int(months)}m {int(days)}d "
        elif t > 24:
            days = t // 24
            hours = t - (days * 24)
            return f"{int(days)}d {int(hours)}h"
        else:
            return f"{t}h"

    @staticmethod
    def calculate_time(bat, iter_cap, iter_time, discharge):
        # 1 year = 365d* 24h = 8760h,   730h = 1 month
        time = 0
        time_batt = 0
        while bat >= 0:
            bat -= iter_cap
            time += iter_time
            time_batt += iter_time
            if time_batt >= 730:
                bat *= (100 - discharge / 12) / 100
                time_batt = 0

        return time


class WaterMeter():
    #  inherit calculate_iterations and calculate_time methods

    AVG_CURRENT_CONSUMPTION_REPORT = 94  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 0.223  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 80  # Не е измерена, само за проба

    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, type_rep, bsd):
        super().__init__()
        self.type_rep = type_rep
        self.wrk_time = wrk_time  # време за работа(измерване)
        self.rep_time = rep_time  # време за репорт
        self.slp_time = slp_time  # време за сън
        self.bat_cap = bat_cap
        self.bsd = bsd

        self.rep_energy = self.AVG_CURRENT_CONSUMPTION_REPORT * self.rep_time
        self.slp_energy = self.AVG_CURRENT_CONSUMPTION_SLEEP * self.slp_time
        self.wrk_energy = self.AVG_CURRENT_CONSUMPTION_WORK * self.wrk_time

        self.iter_time = Calculations.one_iteration_time(self.type_rep, self.rep_time, self.slp_time, self.wrk_time)
        self.iter_cap = Calculations.one_iteration_capacity(self.type_rep, self.rep_energy, self.slp_energy,
                                                            self.wrk_energy)
        self.batt_life = Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd)
        self.batt_life_time = Calculations.time_convert(
            Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd))
        self.num_iterations = math.floor(self.batt_life / self.iter_time)


class FB():
    AVG_CURRENT_CONSUMPTION_REPORT = 50  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 1.8  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 69  # Не е измерена, само за проба

    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, type_rep, bsd):
        super().__init__()
        self.type_rep = type_rep
        self.wrk_time = wrk_time  # време за работа(измерване)
        self.rep_time = rep_time  # време за репорт
        self.slp_time = slp_time  # време за сън
        self.bat_cap = bat_cap
        self.bsd = bsd

        self.rep_energy = self.AVG_CURRENT_CONSUMPTION_REPORT * self.rep_time
        self.slp_energy = self.AVG_CURRENT_CONSUMPTION_SLEEP * self.slp_time
        self.wrk_energy = self.AVG_CURRENT_CONSUMPTION_WORK * self.wrk_time

        self.iter_time = Calculations.one_iteration_time(self.type_rep, self.rep_time, self.slp_time, self.wrk_time)
        self.iter_cap = Calculations.one_iteration_capacity(self.type_rep, self.rep_energy, self.slp_energy,
                                                            self.wrk_energy)
        self.batt_life = Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd)
        self.batt_life_time = Calculations.time_convert(
            Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd))
        self.num_iterations = math.floor(self.batt_life / self.iter_time)


class FC():
    AVG_CURRENT_CONSUMPTION_REPORT = 100  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 1  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 150  # Не е измерена, само за проба

    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, type_rep, bsd):
        super().__init__()
        self.type_rep = type_rep
        self.wrk_time = wrk_time  # време за работа(измерване)
        self.rep_time = rep_time  # време за репорт
        self.slp_time = slp_time  # време за сън
        self.bat_cap = bat_cap
        self.bsd = bsd

        self.rep_energy = self.AVG_CURRENT_CONSUMPTION_REPORT * self.rep_time
        self.slp_energy = self.AVG_CURRENT_CONSUMPTION_SLEEP * self.slp_time
        self.wrk_energy = self.AVG_CURRENT_CONSUMPTION_WORK * self.wrk_time

        self.iter_time = Calculations.one_iteration_time(self.type_rep, self.rep_time, self.slp_time, self.wrk_time)
        self.iter_cap = Calculations.one_iteration_capacity(self.type_rep, self.rep_energy, self.slp_energy,
                                                            self.wrk_energy)
        self.batt_life = Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd)
        self.batt_life_time = Calculations.time_convert(
            Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd))
        self.num_iterations = math.floor(self.batt_life / self.iter_time)


class F5():
    AVG_CURRENT_CONSUMPTION_REPORT = 105  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 0.35  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 84  # Не е измерена, само за проба

    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, type_rep, bsd):
        super().__init__()
        self.type_rep = type_rep
        self.wrk_time = wrk_time  # време за работа(измерване)
        self.rep_time = rep_time  # време за репорт
        self.slp_time = slp_time  # време за сън
        self.bat_cap = bat_cap
        self.bsd = bsd

        self.rep_energy = self.AVG_CURRENT_CONSUMPTION_REPORT * self.rep_time
        self.slp_energy = self.AVG_CURRENT_CONSUMPTION_SLEEP * self.slp_time
        self.wrk_energy = self.AVG_CURRENT_CONSUMPTION_WORK * self.wrk_time

        self.iter_time = Calculations.one_iteration_time(self.type_rep, self.rep_time, self.slp_time, self.wrk_time)
        self.iter_cap = Calculations.one_iteration_capacity(self.type_rep, self.rep_energy, self.slp_energy,
                                                            self.wrk_energy)
        self.batt_life = Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd)
        self.batt_life_time = Calculations.time_convert(
            Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd))
        self.num_iterations = math.floor(self.batt_life / self.iter_time)


class FR():
    AVG_CURRENT_CONSUMPTION_REPORT = 80  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 0.223  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 70  # Не е измерена, само за проба

    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, type_rep, bsd):
        super().__init__()
        self.type_rep = type_rep
        self.wrk_time = wrk_time  # време за работа(измерване)
        self.rep_time = rep_time  # време за репорт
        self.slp_time = slp_time  # време за сън
        self.bat_cap = bat_cap
        self.bsd = bsd

        self.rep_energy = self.AVG_CURRENT_CONSUMPTION_REPORT * self.rep_time
        self.slp_energy = self.AVG_CURRENT_CONSUMPTION_SLEEP * self.slp_time
        self.wrk_energy = self.AVG_CURRENT_CONSUMPTION_WORK * self.wrk_time

        self.iter_time = Calculations.one_iteration_time(self.type_rep, self.rep_time, self.slp_time, self.wrk_time)
        self.iter_cap = Calculations.one_iteration_capacity(self.type_rep, self.rep_energy, self.slp_energy,
                                                            self.wrk_energy)
        self.batt_life = Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd)
        self.batt_life_time = Calculations.time_convert(
            Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd))
        self.num_iterations = math.floor(self.batt_life / self.iter_time)


class TestDevice():
    # dev = class_device(batt_capacity, report_time, report_cap, sleep_time,
    # sleep_cap, work_time, work_cap, type_report, batt_self_discharge)
    def __init__(self, bat_cap, rep_time, rep_cap, slp_time, slp_cap, wrk_time, wrk_cap, type_rep, bsd):
        self.wrk_cap = wrk_cap   # въвежда се от менюто
        self.slp_cap = slp_cap   # въвежда се от менюто
        self.rep_cap = rep_cap   # въвежда се от менюто
        self.type_rep = type_rep # въвежда се от менюто
        self.wrk_time = wrk_time  # време за работа(измерване)
        self.rep_time = rep_time  # време за репорт
        self.slp_time = slp_time  # време за сън
        self.bat_cap = bat_cap    # въвежда се от менюто
        self.bsd = bsd            # въвежда се от менюто

        self.rep_energy = self.rep_cap * self.rep_time
        self.slp_energy = self.slp_cap * self.slp_time
        self.wrk_energy = self.wrk_cap * self.wrk_time

        self.iter_time = Calculations.one_iteration_time(self.type_rep, self.rep_time, self.slp_time, self.wrk_time)
        self.iter_cap = Calculations.one_iteration_capacity(self.type_rep, self.rep_energy, self.slp_energy,
                                                            self.wrk_energy)
        self.batt_life = Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd)
        self.batt_life_time = Calculations.time_convert(
            Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd))
        self.num_iterations = math.floor(self.batt_life / self.iter_time)


def clicked_get_device():
    kind_of_device = combo.get()

    lbl81 = Label(window, text="        ", font=("Arial Bold", 13))
    lbl81.grid(column=4, row=8)
    lbl83 = Label(window, text="        ", font=("Arial Bold", 13))
    lbl83.grid(column=4, row=10)
    lbl84 = Label(window, text="        ", font=("Arial Bold", 13))
    lbl84.grid(column=4, row=12)
    if kind_of_device == "Test device":
        txt7 = Entry(window, width=10)
        txt7.grid(column=4, row=8)
        txt8 = Entry(window, width=10)
        txt8.grid(column=4, row=10)
        txt9 = Entry(window, width=10)
        txt9.grid(column=4, row=12)

        lbl91 = Label(window, text="mA", font=("Arial Bold", 13))
        lbl91.grid(column=5, row=8)
        lbl92 = Label(window, text="mA", font=("Arial Bold", 13))
        lbl92.grid(column=5, row=10)
        lbl93 = Label(window, text="mA", font=("Arial Bold", 13))
        lbl93.grid(column=5, row=12)
    else:
        global class_device

        device = combo.get()
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
        else:
            class_device = TestDevice

        dev1 = class_device(100, 30, 30, 30, "type_report", 10)

        lbl81 = Label(window, text=dev1.AVG_CURRENT_CONSUMPTION_REPORT, font=("Arial Bold", 13))
        lbl81.grid(column=4, row=8)
        lbl83 = Label(window, text=dev1.AVG_CURRENT_CONSUMPTION_WORK, font=("Arial Bold", 13))
        lbl83.grid(column=4, row=10)
        lbl84 = Label(window, text=dev1.AVG_CURRENT_CONSUMPTION_SLEEP, font=("Arial Bold", 13))
        lbl84.grid(column=4, row=12)

        lbl91 = Label(window, text="mA", font=("Arial Bold", 13))
        lbl91.grid(column=5, row=8)
        lbl92 = Label(window, text="mA", font=("Arial Bold", 13))
        lbl92.grid(column=5, row=10)
        lbl93 = Label(window, text="mA", font=("Arial Bold", 13))
        lbl93.grid(column=5, row=12)

    print(class_device)


def print_something(txt7=None, txt8=None, txt9=None):
    clicked_get_device()
    global class_device
    batt_capacity = float(txt1.get())
    report_time = float(txt2.get()) / 3600
    work_time = float(txt3.get()) / 3600
    sleep_time = float(txt4.get()) / 3600
    batt_self_discharge = float(txt5.get())
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
    else:
        class_device = TestDevice

    if class_device == TestDevice:
        report_cap = float(txt7.get())
        work_cap = float(txt8.get())
        sleep_cap = float(txt9.get())

        dev = class_device(batt_capacity, report_time, report_cap, sleep_time,
                           sleep_cap, work_time, work_cap, type_report, batt_self_discharge)
    else:
        dev = class_device(batt_capacity, report_time, sleep_time, work_time, type_report, batt_self_discharge)

    # print(dev.bat_cap, dev.rep_time, dev.slp_time, dev.wrk_time, dev.type_rep, dev.bsd)
    # print(dev.calculate_iterations())

    lbl41.configure(text=dev.batt_life_time)
    lbl42.configure(text=dev.num_iterations)

    print(f"cap   {batt_capacity}")
    print(f"report time  {report_time}")
    print(f"work time   {work_time}")
    print(f"sleep time   {sleep_time}")
    print(f"device   {device}")
    print(f"MODE  {type_report}")
    print()


btn1 = Button(window, text="Device consumption", command=clicked_get_device)
btn1.grid(column=4, row=6)
btn2 = Button(window, text="Calculate", command=print_something)
btn2.grid(column=4, row=22)

window.mainloop()

