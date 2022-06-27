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
lbl9 = Label(window, text="1y", font=("Arial Bold", 13))
lbl9.grid(column=1, row=22)
lbl9 = Label(window, text="199", font=("Arial Bold", 13))
lbl9.grid(column=1, row=23)

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


def clicked_get_device():
    kind_of_device = combo.get()
    # lbl.configure(text=combo.get())
    print(combo.get())


def print_something():
    cap = txt1.get()
    report_time = txt2.get()
    work_time = txt3.get()
    sleep_time = txt4.get()
    self_discharge = txt5.get()
    device = combo.get()
    mode = txt6.get()
    print("cap " + cap)
    print("report time " + report_time)
    print("work time " + work_time)
    print("sleep time " + sleep_time)
    print("device  " + device)
    print("MODE " + mode)


btn1 = Button(window, text="Get device", command=clicked_get_device)
btn1.grid(column=3, row=15)
btn2 = Button(window, text="Calculate", command=print_something)
btn2.grid(column=3, row=22)





class Devices(ABC):
    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, type_rep, bsd):
        self.type_rep = type_rep
        self.wrk_time = wrk_time
        self.bsd = bsd  # batt self discharge
        self.slp_time = slp_time
        self.rep_time = rep_time
        self.bat_cap = bat_cap

    @abstractmethod
    def calculate_battery_live(self):
        pass
    #
    # if not 'r' in self.type_rep:
    #     self.rep_energy = 0
    # else:
    #     self.rep_energy = self.AVG_CURRENT_CONSUMPTION_REPORT * self.rep_time
    #
    # if not 's' in self.type_rep:
    #     self.slp_energy = 0
    # else:
    #     self.slp_energy = self.AVG_CURRENT_CONSUMPTION_SLEEP * self.slp_time
    # if not 'w' in self.type_rep:
    #     self.wrk_energy = 0
    # else:
    #     self.wrk_energy = self.AVG_CURRENT_CONSUMPTION_WORK * self.wrk_time
    #
    # self.one_iter = CalculateIterationEnergy.calculate_iter_energy(self.type_rep, self.rep_energy, self.slp_energy,
    #                                                                self.wrk_energy)
    #
    # self.iteration_cap = CalculateIterationCap.calculate_iteration_capacity(self.type_rep,
    #                                                                         self.rep_energy, self.rep_time,
    #                                                                         self.slp_energy, self.slp_time,
    #                                                                         self.wrk_energy, self.wrk_time)


class TimeConverting:
    @staticmethod
    def time_convert(t):
        if t > 24 * 30 * 12:
            years = t // (24 * 30 * 12)
            months = (t - years * 24 * 30 * 12) // (24 * 30)
            return f"{int(years)} years {int(months)} months"
        elif t > 24 * 30:
            months = t // (24 * 30)
            days = (t - (months * 24 * 30)) // 24
            return f"{int(months)} months {int(days)} days "
        elif t > 24:
            days = t // 24
            hours = t - (days * 24)
            return f"{int(days)} days {int(hours)} hours"
        else:
            return f"{t} hours"


class BatterySelfDischarge:

    @staticmethod
    def calculate_self_discharge(discharge):
        one_year = 365 * 24
        discharge_per_hour = discharge / one_year
        return discharge_per_hour


class Atmega:
    AVG_CURRENT_CONSUMPTION_REPORT = None  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = None  # mA
    AVG_CURRENT_CONSUMPTION_WORK = None

    def __init__(self, rep_time, slp_time, wrk_time, type_rep):
        self.type_rep = type_rep
        self.wrk_time = wrk_time
        self.slp_time = slp_time
        self.rep_time = rep_time

        self.rep_energy = self.AVG_CURRENT_CONSUMPTION_REPORT * self.rep_time
        self.slp_energy = self.AVG_CURRENT_CONSUMPTION_SLEEP * self.slp_time
        self.wrk_energy = self.AVG_CURRENT_CONSUMPTION_WORK * self.wrk_time

        self.one_iter = CalculateIterationEnergy.calculate_iter_energy(self.type_rep, self.rep_energy, self.slp_energy,
                                                                       self.wrk_energy)

        self.iteration_cap = CalculateIterationCap.calculate_iteration_capacity(self.type_rep,
                                                                                self.rep_energy, self.rep_time,
                                                                                self.slp_energy, self.slp_time,
                                                                                self.wrk_energy, self.wrk_time)


class Extended_powered:
    CHARGING_TIME = None
    def __init__(self, external_voltage):
        self.external_voltage = external_voltage


class FR:
    pass


class BatteryPowered:

    def __init__(self):
        self.one_iter = None
        self.bat_cap = None
        self.iteration_cap = None

    def calculate_iterations(self):
        it = 0
        bc = self.bat_cap
        # one_iteration = CalculateIterationEnergy.calculate_iter_energy(self.typ, self.rep, self.slp, self.wrk)
        while bc > 0:
            bc -= (self.one_iter)  # да се извика метод, който събира енергиите в зависиност от типа на доклада
            it += 1
        return f"iterations = {it}"

    def calculate_time(self):
        time = self.bat_cap / self.iteration_cap
        return f"battery life time = {TimeConverting.time_convert(time)}"


class CalculateIterationEnergy:
    @staticmethod
    def calculate_iter_energy(typ, rep, slp, wrk):
        energy = 0
        for ch in typ:

            if ch == 'r':
                energy += rep
            elif ch == 'w':
                energy += wrk
            elif ch == 's':
                energy += slp

        return energy


class CalculateIterationCap:
    @staticmethod
    def calculate_iteration_capacity(typ, rep, rep_t, slp, slp_t, wrk, wrk_t):
        global iteration_cap
        energy = 0
        tim = 0
        for ch in typ:

            if ch == 'r':
                energy += rep
                tim += rep_t
            elif ch == 'w':
                energy += wrk
                tim += wrk_t
            elif ch == 's':
                energy += slp
                tim += slp_t
        if energy != 0:
            iteration_cap = energy / tim
        return iteration_cap


class F5(BatteryPowered):
    #  inherit calculate_iterations and calculate_time methods

    #  добре е стойностите да се валидират със getter / setter
    AVG_CURRENT_CONSUMPTION_REPORT = 48  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 1.82  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 60  # не е измервана, само за проба

    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, type_rep, bsd):

        super().__init__()
        self.type_rep = type_rep
        self.wrk_time = wrk_time
        self.bsd = bsd  # batt self discharge
        self.slp_time = slp_time
        self.rep_time = rep_time
        self.bat_cap = bat_cap

        # self.bat_sd_per_hour = BatterySelfDischarge.calculate_self_discharge(self.bsd)

        if not 'r' in self.type_rep:
            self.rep_energy = 0
        else:
            self.rep_energy = self.AVG_CURRENT_CONSUMPTION_REPORT * self.rep_time

        if not 's' in self.type_rep:
            self.slp_energy = 0
        else:
            self.slp_energy = self.AVG_CURRENT_CONSUMPTION_SLEEP * self.slp_time
        if not 'w' in self.type_rep:
            self.wrk_energy = 0
        else:
            self.wrk_energy = self.AVG_CURRENT_CONSUMPTION_WORK * self.wrk_time

        self.one_iter = CalculateIterationEnergy.calculate_iter_energy(self.type_rep, self.rep_energy, self.slp_energy,
                                                                       self.wrk_energy)

        self.iteration_cap = CalculateIterationCap.calculate_iteration_capacity(self.type_rep,
                                                                                self.rep_energy, self.rep_time,
                                                                                self.slp_energy, self.slp_time,
                                                                                self.wrk_energy, self.wrk_time)


class WaterMeter(BatteryPowered):
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

        self.one_iter = CalculateIterationEnergy.calculate_iter_energy(self.type_rep, self.rep_energy, self.slp_energy,
                                                                       self.wrk_energy)

        self.iteration_cap = CalculateIterationCap.calculate_iteration_capacity(self.type_rep,
                                                                                self.rep_energy, self.rep_time,
                                                                                self.slp_energy, self.slp_time,
                                                                                self.wrk_energy, self.wrk_time)


class FB(Atmega, BatteryPowered):
    AVG_CURRENT_CONSUMPTION_REPORT = 50  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 1.8  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 69

    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, type_rep, bsd):
        super().__init__(rep_time, slp_time, wrk_time, type_rep)
        self.bsd = bsd
        self.type_rep = type_rep
        self.bat_cap = bat_cap


class FC(Atmega, BatteryPowered):
    AVG_CURRENT_CONSUMPTION_REPORT = 100  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 1  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 150

    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, type_rep, bsd):
        super().__init__(rep_time, slp_time, wrk_time, type_rep)
        self.bsd = bsd
        self.type_rep = type_rep
        self.bat_cap = bat_cap


class ARGA:
    def __init__(self):
        pass


class FR(Atmega, Extended_powered):
    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, type_rep, bsd):
        super().__init__(rep_time, slp_time, wrk_time, type_rep)
'''
    cap = txt1.get()
    report_time = txt2.get()
    work_time = txt3.get()
    sleep_time = txt4.get()
    self_discharge = txt5.get()
    device = combo.get()
    mode = txt6.get()
'''

batt_capacity = 18000  # mAh
batt_self_discharge = 5

type_report = "rws"  # that means report, work, sleep
type_report2 = "rwswr"  # that means report, work, sleep, work, report

report_time = 0.5 / 60  # (h)
sleep_time = 5 / 60  # (h)
work_time = 0.5 / 60  # (h)


print(batt_capacity)
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



window.mainloop()
