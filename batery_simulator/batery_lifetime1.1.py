from abc import ABC, abstractmethod


class Devices(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_battery_live(self):
        pass


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
    def __init__(self):
        pass


class Extended_powered:
    def __init__(self, external_voltage):
        self.external_voltage = external_voltage


class BatteryPowered:
    # @staticmethod
    def __init__(self):
        self.bat_cap = None
        # self.typ = None
        # self.rep = None
        # self.slp = None
        # self.wrk = None

    def calculate_iterations(self):
        it = 0
        bc = self.bat_cap
        #one_iteration = CalculateIterationEnergy.calculate_iter_energy(self.typ, self.rep, self.slp, self.wrk)
        while bc > 0:
            bc -= (self.one_iter)  # да се извика метод, който събира енергиите в зависиност от типа на доклада
            it += 1
        return f"iterations = {it}"

    def calculate_time(self):
        time = self.bat_cap / self.iteration_cap
        return f"life time = {TimeConverting.time_convert(time)}"


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

    AVG_CURRENT_CONSUMPTION_REPORT = 94  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 1.9  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 100  # не е измервана, само за проба

    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, type_rep, bsd):

        self.type_rep = type_rep
        self.wrk_time = wrk_time
        self.bsd = bsd  # batt self discharge
        self.slp_time = slp_time
        self.rep_time = rep_time
        self.bat_cap = bat_cap

        self.bat_sd_per_hour = BatterySelfDischarge.calculate_self_discharge(self.bsd)

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

        self.one_iter = CalculateIterationEnergy.calculate_iter_energy(self.type_rep, self.rep_energy, self.slp_energy, self.wrk_energy)

        self.iteration_cap = CalculateIterationCap.calculate_iteration_capacity(self.type_rep,
                                                                                self.rep_energy, self.rep_time,
                                                                                self.slp_energy, self.slp_time,
                                                                                self.wrk_energy, self.wrk_time)


class WaterMeter(BatteryPowered):
    #  inherit calculate_iterations and calculate_time methods

    AVG_CURRENT_CONSUMPTION_REPORT = 94  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 0.223  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 80  # Не е измерена, само за проба

    def __init__(self, bat_cap, rep_time, slp_time, wrk_time, bsd):
        self.wrk_time = wrk_time  # време за работа(измерване)
        self.rep_time = rep_time  # време за репорт
        self.slp_time = slp_time  # време за сън
        self.bat_cap = bat_cap
        self.bsd = bsd

        self.report_energy = self.AVG_CURRENT_CONSUMPTION_REPORT * self.rep_time
        self.sleep_energy = self.AVG_CURRENT_CONSUMPTION_SLEEP * self.slp_time
        self.work_energy = self.AVG_CURRENT_CONSUMPTION_WORK * self.wrk_time

        self.iteration_cap = (self.report_energy + self.sleep_energy) / (self.rep_time + self.slp_time)
        # self.iteration_cap = (self.report_elergy + self.work_energy + self.sleep_energy) /
        # (self.report_time + self.work_time + self.sleep_time)

    # def calculate_iterations(self):
    #     it = 0
    #     bc = self.bat_cap
    #     while bc > 0:
    #         bc -= (self.active_energy + self.sleep_energy)
    #         it += 1
    #     return f"iterations = {it}"
    #
    # def calculate_time(self):
    #     time = self.bat_cap / self.iteration_cap
    #     return f"lifetime = {TimeConverting.time_convert(time)}"


class FR(Atmega, Extended_powered):
    pass


batt_capacity = 18000  # mAh
batt_self_discharge = 5
type_report = "rws"
report_time = 0.5 / 60  # (h)
sleep_time = 5 / 60  # (h)
work_time = 0.5 / 60  # (h)

dog = F5(batt_capacity, report_time, sleep_time, work_time, type_report, batt_self_discharge)
#print(dog.one_iter)
print(f"dog {dog.calculate_iterations()}")
print(f"dog {dog.calculate_time()}")

# period = TimeConverting()
# print(period.time_convert(9))

# wm = WaterMeter(18000, 0.0115589, 12, 0)
# print(f"WM {wm.calculate_iterations()}")
# print(f"WM {wm.calculate_time()}")
