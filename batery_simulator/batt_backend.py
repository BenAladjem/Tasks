from abc import ABC, abstractmethod


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


batt_capacity = 18000  # mAh
batt_self_discharge = 5

type_report = "rws"  # that means report, work, sleep
type_report2 = "rwswr"  # that means report, work, sleep, work, report

report_time = 0.5 / 60  # (h)
sleep_time = 5 / 60  # (h)
work_time = 0.5 / 60  # (h)

dog = F5(batt_capacity, report_time, sleep_time, work_time, type_report, batt_self_discharge)
# print(dog.one_iter)
print(f"dog {dog.calculate_iterations()}")
print(f"dog {dog.calculate_time()}")
print()

# period = TimeConverting()
# print(period.time_convert(9))

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

