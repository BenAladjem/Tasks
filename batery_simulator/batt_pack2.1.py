import colorsys
from tkinter import *
from tkinter.ttk import *
#from tkinter.ttk import Entry
import math
import datetime

#from Tkinter_test.create_desktop_app import window2

window = Tk()
window.title("Battery Life Estimator ")
window.geometry("665x660")
window.configure(bg="gray")

sv1 = StringVar()
sv2 = StringVar()
sv3 = StringVar()
sv4 = StringVar()
sv5 = StringVar()
sv6 = StringVar()
sv7 = StringVar()
sv8 = StringVar()

# trace wants a callback with nearly useless parameters, fixing with lambda.
sv1.trace('w', lambda nm, idx, mode, var=sv1: validate_float(var))
sv2.trace('w', lambda nm, idx, mode, var=sv2: validate_float(var))
sv3.trace('w', lambda nm, idx, mode, var=sv3: validate_float(var))
sv4.trace('w', lambda nm, idx, mode, var=sv4: validate_float(var))
sv5.trace('w', lambda nm, idx, mode, var=sv5: validate_float(var))
sv6.trace('w', lambda nm, idx, mode, var=sv6: validate_float(var))
sv7.trace('w', lambda nm, idx, mode, var=sv7: validate_float(var))
sv8.trace('w', lambda nm, idx, mode, var=sv8: validate_float(var))



txt_empty1 = Entry(window, width=0).grid(row=1, column=6)
txt_empty2 = Entry(window, width=1).grid(row=3, column=6)
txt_empty3 = Entry(window, width=1).grid(row=5, column=6)
txt_empty4 = Entry(window, width=1).grid(row=7, column=6)
txt_empty5 = Entry(window, width=1).grid(row=9, column=6)
txt_empty6 = Entry(window, width=1).grid(row=11, column=6)
txt_empty7 = Entry(window, width=1).grid(row=13, column=6)
txt_empty8 = Entry(window, width=1).grid(row=15, column=6)
txt_empty9 = Entry(window, width=1).grid(row=17, column=6)
txt_empty11 = Entry(window, width=1).grid(row=20, column=6)
txt_empty10 = Entry(window, width=1).grid(row=21, column=6)
txt_empty12 = Entry(window, width=1).grid(row=24, column=6)

lbl1 = Label(window, text="Battery capacity", font=("Arial Bold", 15))
lbl1.grid(column=0, row=0)
#lbl2 = Label(window,width=14, text="", font=("Arial Bold", 15))
#lbl2.grid(column=0, row=1)
lbl3 = Label(window, text="Capacity  ", font=("Arial Bold", 13))
lbl3.grid(column=0, row=2)
#lbl4 = Label(window,width=10, text="", font=("Arial Bold", 15))
#lbl4.grid(column=0, row=3)
lbl5 = Label(window, text="Device", font=("Arial Bold", 15))
lbl5.grid(column=0, row=4)
#lbl6 = Label(window, text="", font=("Arial Bold", 15))
#lbl6.grid(column=0, row=5)
#lbl7 = Label(window, text="", font=("Arial Bold", 15))
#lbl7.grid(column=0, row=7)
lbl8 = Label(window, text="Report time ", font=("Arial Bold", 13))
lbl8.grid(column=0, row=8)
#lbl7 = Label(window, text="", font=("Arial Bold", 15))
#lbl7.grid(column=0, row=9)
lbl9 = Label(window, text="Work time ", font=("Arial Bold", 13))
lbl9.grid(column=0, row=10)
#lbl7 = Label(window, text="", font=("Arial Bold", 15))
#lbl7.grid(column=0, row=11)
lbl10 = Label(window, text="Sleep time", font=("Arial Bold", 13))
lbl10.grid(column=0, row=12)
#lbl11 = Label(window, text="", font=("Arial Bold", 15))
#lbl11.grid(column=0, row=13)
lbl13 = Label(window, text="Battery self discharge", font=("Arial Bold", 15))
lbl13.grid(column=0, row=14)
#lbl14 = Label(window, text="", font=("Arial Bold", 15))
#lbl14.grid(column=0, row=15)
lbl15 = Label(window, text="self discharge", font=("Arial Bold", 13))
lbl15.grid(column=0, row=16)
#lbl16 = Label(window, text="", font=("Arial Bold", 15))
#lbl16.grid(column=0, row=17)
lbl19 = Label(window, text="Cyclic mode", font=("Arial Bold", 15))
lbl19.grid(column=0, row=18)
lbl21 = Label(window, text="Estimated battery lifetime", font=("Arial Bold", 15))
lbl21.grid(column=0, row=20)
#lbl22 = Label(window, text="", font=("Arial Bold", 15))
#lbl22.grid(column=0, row=21)
lbl23 = Label(window,width=10, text="Lifetime", font=("Arial Bold", 13))
lbl23.grid(column=0, row=22)
lbl24 = Label(window,width=10, text="Iterations", font=("Arial Bold", 13))
lbl24.grid(column=0, row=23)

lbl_lifetime = Label(window, width=10, text="                         ", font=("Arial Bold", 13))
lbl_lifetime.grid(column=1, row=22)
lbl_iterations = Label(window,width=10, text="                         ", font=("Arial Bold", 13))
lbl_iterations.grid(column=1, row=23)

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

lbl100 = Label(window, text="                                  ", width=10, font=("Arial Bold", 13))
lbl100.grid(column=2, row=18)

lbl_rep_cap = Label(window, text="report cap", width=12, font=("Arial Bold", 13))
lbl_rep_cap.grid(column=4, row=8)
lbl101 = Label(window, text="mA", width=3, font=("Arial Bold", 13))
lbl101.grid(column=5, row=8)
lbl_wrc_cap = Label(window, text="work cap", width=12, font=("Arial Bold", 13))
lbl_wrc_cap.grid(column=4, row=10)
lbl102 = Label(window, text="mA", width=3, font=("Arial Bold", 13))
lbl102.grid(column=5, row=10)
lbl_slp_cap = Label(window, text="sleep cap", width=12, font=("Arial Bold", 13))
lbl_slp_cap.grid(column=4, row=12)
lbl103 = Label(window, text="mA", width=3, font=("Arial Bold", 13))
lbl103.grid(column=5, row=12)

txt_batt_cap = Entry(window, validate='key', textvariable=sv1, width=10)
txt_batt_cap.grid(column=2, row=2)
txt_rep_time = Entry(window, validate='key', textvariable=sv2, width=10)
txt_rep_time.grid(column=2, row=8)
txt_wrk_time = Entry(window, validate='key', textvariable=sv3, width=10)
txt_wrk_time.grid(column=2, row=10)
txt_slp_time = Entry(window, validate='key', textvariable=sv4, width=10)
txt_slp_time.grid(column=2, row=12)
txt_bsd = Entry(window, validate='key', textvariable=sv5, width=10)
txt_bsd.grid(column=2, row=16)

combo = Combobox(window)
combo['values'] = ("Findy Bike", "Findy Car", "Findy Raid", "Findy Pet", "Water meter", "Test Device")
combo.current(0)
combo.grid(column=0, row=6)

mode = " "
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
            if ch == 'R':
                iter_time += rep
            elif ch == 'W':
                iter_time += wrk
            elif ch == 'S':
                iter_time += slp
        return iter_time

    @staticmethod
    def one_iteration_capacity(typ, rep, slp, wrk):
        iter_cap = 0
        for ch in typ:
            if ch == 'R':
                iter_cap += rep
            elif ch == 'W':
                iter_cap += wrk
            elif ch == 'S':
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
            return f"{int(t)}h"

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
    AVG_CURRENT_CONSUMPTION_REPORT = 64  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 0.332  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 9.8

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
    AVG_CURRENT_CONSUMPTION_REPORT = 52.8  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 7.6  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 22.3

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
    AVG_CURRENT_CONSUMPTION_REPORT = 52  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 1.85  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 40  # Не е измерена, само за проба

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
    AVG_CURRENT_CONSUMPTION_REPORT = 139  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 0.223  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 1.89  # Не е измерена, само за проба

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
        self.wrk_cap = wrk_cap  # въвежда се от менюто
        self.slp_cap = slp_cap  # въвежда се от менюто
        self.rep_cap = rep_cap  # въвежда се от менюто
        self.type_rep = type_rep  # въвежда се от менюто
        self.wrk_time = wrk_time  # време за работа(измерване)
        self.rep_time = rep_time  # време за репорт
        self.slp_time = slp_time  # време за сън
        self.bat_cap = bat_cap  # въвежда се от менюто
        self.bsd = bsd  # въвежда се от менюто

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


flag = False


def clicked_get_device():
    kind_of_device = combo.get()
    global class_device, txt_rep_cap, txt_wrk_cap, txt_slp_cap, flag
    if kind_of_device == "Test Device":
        flag = True
    if kind_of_device == "Test Device":
        txt_rep_cap = Entry(window, validate='key', textvariable=sv6, width=10)
        txt_rep_cap.grid(column=4, row=9)
        txt_wrk_cap = Entry(window, validate='key', textvariable=sv7, width=10)
        txt_wrk_cap.grid(column=4, row=11)
        txt_slp_cap = Entry(window, validate='key', textvariable=sv8, width=10)
        txt_slp_cap.grid(column=4, row=13)

        lbl_rep_cap.configure(text="report cap")
        lbl_wrc_cap.configure(text="work cap")
        lbl_slp_cap.configure(text="sleep cap")
    else:
        if flag:
            txt_rep_cap.delete(0, END)
            txt_wrk_cap.delete(0, END)
            txt_slp_cap.delete(0, END)

        device = combo.get()
        if device == "Findy Bike":
            class_device = FB
        elif device == "Findy Car":
            class_device = FC
        elif device == "Findy Pet":
            class_device = F5
        elif device == "Findy Raid":
            class_device = FR
        elif device == "Water Meter":
            class_device = WaterMeter
        else:
            class_device = TestDevice
        print(class_device)

        lbl_rep_cap.configure(text=class_device.AVG_CURRENT_CONSUMPTION_REPORT)
        lbl_wrc_cap.configure(text=class_device.AVG_CURRENT_CONSUMPTION_WORK)
        lbl_slp_cap.configure(text=class_device.AVG_CURRENT_CONSUMPTION_SLEEP)


def check_valid_data():
    flag1 = False

    if len(txt_batt_cap.get()) == 0:
        lbl_iterations.configure(text="batt cap")
        print("Enter batt cap")
    elif len(txt_rep_time.get()) == 0:
        lbl_iterations.configure(text="report time")
        print("Enter rep time")
    elif len(txt_wrk_time.get()) == 0:
        lbl_iterations.configure(text="work time")
        print("Enter work time")
    elif len(txt_slp_time.get()) == 0:
        lbl_iterations.configure(text="sleep time")
        print("Enter sleep time")
    elif mode == '' or mode == ' ':
        lbl_iterations.configure(text="")
        lbl_iterations.configure(text="mode")
        print("Enter mode")
    else:
        flag1 = True

    if not combo.get() == "Test Device":
        if flag1:
            print_result()
    else:
        clicked_get_device()
        if flag1:
            if len(txt_rep_cap.get()) == 0:
                lbl_lifetime.configure(text="Enter")
                lbl_iterations.configure(text="report cap")
                print("Enter rep cap")
            elif len(txt_wrk_cap.get()) == 0:
                lbl_lifetime.configure(text="Enter")
                lbl_iterations.configure(text="work cap")
                print("Enter wrk cap")
            elif len(txt_slp_cap.get()) == 0:
                lbl_lifetime.configure(text="Enter")
                lbl_iterations.configure(text="sleep cap")
                print("Enter slp cap")
            else:
                print_result()
    if flag1 == False:
        lbl_lifetime.configure(text="Enter")


def print_result():
    result_dict = {}
    clicked_get_device()
    global class_device
    batt_capacity = float(txt_batt_cap.get())
    report_time = float(txt_rep_time.get()) / 3600
    work_time = float(txt_wrk_time.get()) / 3600
    sleep_time = float(txt_slp_time.get()) / 3600



    if len(txt_bsd.get()) == 0:
        batt_self_discharge = 0
    else:
        batt_self_discharge = float(txt_bsd.get())
    device = combo.get()
    type_report = mode
    print(type_report)

    if device == "Findy Bike":
        class_device = FB
    elif device == "Findy Car":
        class_device = FC
    elif device == "Findy Pet":
        class_device = F5
    elif device == "Findy Raid":
        class_device = FR
    elif device == "Water Meter":
        class_device = WaterMeter
    else:
        class_device = TestDevice

    if class_device == TestDevice:
        report_cap = float(txt_rep_cap.get())
        work_cap = float(txt_wrk_cap.get())
        sleep_cap = float(txt_slp_cap.get())

        result_dict["report cap"] = report_cap
        result_dict["work cap"] = work_cap
        result_dict["sleep cap"] = sleep_cap

        dev = class_device(batt_capacity, report_time, report_cap, sleep_time,
                           sleep_cap, work_time, work_cap, type_report, batt_self_discharge)
    else:
        dev = class_device(batt_capacity, report_time, sleep_time, work_time, type_report, batt_self_discharge)

        result_dict["report cap"] = dev.AVG_CURRENT_CONSUMPTION_REPORT
        result_dict["work cap"] = dev.AVG_CURRENT_CONSUMPTION_WORK
        result_dict["sleep cap"] = dev.AVG_CURRENT_CONSUMPTION_SLEEP

    lbl_lifetime.configure(text=dev.batt_life_time)
    lbl_iterations.configure(text=dev.num_iterations)

    print(f"cap   {batt_capacity}")
    print(f"device   {device}")
    print(f"MODE  {type_report}")
    print()

    result_dict["batt self discharge"] = batt_self_discharge
    result_dict["cycling mode"] = type_report
    result_dict["device"] = device
    result_dict["batt capacity"] = batt_capacity
    result_dict["report time"] = txt_rep_time.get()
    result_dict["work time"] = txt_wrk_time.get()
    result_dict["sleep time"] = txt_slp_time.get()
    result_dict["lifetime"] = dev.batt_life_time
    result_dict["iterations"] = dev.num_iterations


    return result_dict


def print_r():
    global mode
    if len(mode) < 7 and not mode[-1] == "R":
        mode += "R"
    lbl100.configure(text=mode)


def print_s():
    global mode
    if len(mode) < 7 and not mode[-1] == "S":
        mode += "S"
    lbl100.configure(text=mode)


def print_w():
    global mode
    if len(mode) < 7 and not mode[-1] == "W":
        mode += "W"
    lbl100.configure(text=mode)


def clean():
    global mode
    if len(mode) > 1:
        mode = mode[:-1]
    lbl100.configure(text=mode)


def validate_float(var):
    new_value = var.get()
    try:
        new_value == '' or float(new_value)
        validate_float.old_value = new_value
    except:
        var.set(validate_float.old_value)

num = 1
def generate_report():
    info = {}
    info = print_result()
    global num
    window2 = Tk()
    window2.title("Saved data")
    window2.geometry("400x600")
    #btn_save = Button(window2, command=generate_report).grid(column=4, row=23)
    num +=1
    info["number protocol"] = num
    date = datetime.datetime.now()
    date_format = date.strftime("%Y-%m-%d %H:%M:%S")
    info["date"] = date_format
    print(info)


    num_protocol = info["number protocol"]
    data = info["date"]
    device = info["device"]
    batt_capacity = info["batt capacity"]
    report_time = info["report time"]
    report_cap = info["report cap"]
    work_time = info["work time"]
    work_cap = info["work cap"]
    sleep_time = info["sleep time"]
    sleep_cap = info["sleep cap"]
    batt_self_discharge = info["batt self discharge"]
    cycling_mode = info["cycling mode"]
    batt_life_time = info["lifetime"]
    iterations = info["iterations"]



    # t=f"num protocol:{num}" \
    #   f"\n\n data:{date_format}"\
    #   f"\n\n device: "\
    #   f"\n\n batt capacity:"
    #   f"\n\n report time:"
    #                                  f"\n\n report cap:"
    #                                  f"\n\n work time:"
    #                                  f"\n\n work_cap:"
    #                                  f"\n\n sleep time:"
    #                                  f"\n\n sleep cap:"
    #                                  f"\n\n batt self discharge:"
    #                                  f"\n\n cycling mode:"
    #                                  f"\n\n batt life time:"
    #                                  f"\n\n iterations:"

    #lbl_protocol=Label(window2, text=f"num protocol:{num} \n\n data: {date_format}.pack() \n\n  ")
    lbl_protocol=Label(window2, text=f"num protocol:{num_protocol}"
                                     f"\n\n data: {data}"
                                     f"\n\n device: {device}"
                                     f"\n\n batt capacity: {batt_capacity} mA"
                                     f"\n\n report time: {report_time}s"
                                     f"\n\n report cap: {report_cap}"
                                     f"\n\n work time: {work_time}s"
                                     f"\n\n work_cap: {work_cap}"
                                     f"\n\n sleep time: {sleep_time}s "
                                     f"\n\n sleep cap: {sleep_cap}"
                                     f"\n\n batt self discharge: {batt_self_discharge} %"
                                     f"\n\n cycling mode: {cycling_mode}"
                                     f"\n\n batt life time: {batt_life_time}"
                                     f"\n\n iterations: {iterations}").pack()



btn_device = Button(window, text="Device consumption", command=clicked_get_device)
btn_device.grid(column=4, row=6)
btn_calculate = Button(window,width=14,  text="        Calculate       ", command=check_valid_data)
btn_calculate.grid(column=4, row=22)
btn_save = Button(window, width=6, text = "Save",command=generate_report).grid(column=4, row=25)

btn_report = Button(window, text="Report", command=print_r)
btn_report.grid(column=1, row=19)
btn_work = Button(window, text="Work", command=print_w)
btn_work.grid(column=2, row=19)
btn_sleep = Button(window, text="Sleep", command=print_s)
btn_sleep.grid(column=3, row=19)
btn_clean = Button(window, text="X", command=clean)
btn_clean.grid(column=3, row=18)

validate_float.old_value = ''  # Define function attribute.
window.mainloop()