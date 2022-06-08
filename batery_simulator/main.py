
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

    def calculate_iterations(self):
        it = 0
        bc = self.bat_cap
        while bc > 0:
            bc -= (self.active_energy + self.sleep_energy)
            it += 1
        return f"iterations = {it}"

    def calculate_time(self):
        time = self.bat_cap / self.iteration_cap
        return f"life time = {TimeConverting.time_convert(time)}"


class F5(BatteryPowered):
    #  inherit calculate_iterations and calculate_time methods

    AVG_CURRENT_CONSUMPTION_ACTIVE = 94  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 1.9  # mA
    def __init__(self, bat_cap, act_avg_c, act_time, slp_avg_c, slp_time, bsd):

        self.bsd = bsd # batt self discharge
        self.slp_time = slp_time
        self.slp_avg_c = slp_avg_c
        self.act_time = act_time
        self.act_avg_c = act_avg_c
        self.bat_cap = bat_cap

        self.bat_sd_per_hour = BatterySelfDischarge.calculate_self_discharge(self.bsd)

        self.active_energy = self.AVG_CURRENT_CONSUMPTION_ACTIVE * self.act_time
        self.sleep_energy = self.AVG_CURRENT_CONSUMPTION_SLEEP * self.slp_time
        #self.iteration_cap = (self.active_energy + self.sleep_energy + self.bat_sd_per_hour) / (self.act_time + self.slp_time + 1)
        self.iteration_cap = (self.active_energy + self.sleep_energy) / (self.act_time + self.slp_time)

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

class WaterMeter(BatteryPowered):
    #  inherit calculate_iterations and calculate_time methods

    AVG_CURRENT_CONSUMPTION_ACTIVE = 94  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 0.223  # mA

    def __init__(self, bat_cap, act_time, slp_time, bsd):
        self.slp_time = slp_time
        self.act_time = act_time
        self.bat_cap = bat_cap
        self.bsd = bsd

        self.active_energy = self.AVG_CURRENT_CONSUMPTION_ACTIVE * self.act_time
        self.sleep_energy = self.AVG_CURRENT_CONSUMPTION_SLEEP * self.slp_time
        self.iteration_cap = (self.active_energy + self.sleep_energy) / (self.act_time + self.slp_time)

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
batt_self_disch = 5

active_avg_current = 300  # mA
active_time = 0.5 / 60  # (h)

sleep_avg_current = 70  # mA
sleep_time = 5 / 60  # (h)

# batt_capacity = 18000  # mAh
# batt_self_disch = 10
# active_avg_current = 1  # mA
# active_time = 5 / 600  # (h)
#
# sleep_avg_current = 1  # mA
# sleep_time = 5 / 60  # (h)

constants = [active_avg_current, sleep_avg_current]
variables = [active_time, sleep_time]

active_energy = active_time * active_avg_current
sleep_energy = sleep_time * sleep_avg_current



dog = F5(batt_capacity, active_avg_current, active_time, sleep_avg_current, sleep_time, batt_self_disch)
print(f"dog {dog.calculate_iterations()}")
print(f"dog {dog.calculate_time()}")

# period = TimeConverting()
# print(period.time_convert(9))

wm = WaterMeter(18000, 0.0115589, 12, 0)
print(f"WM {wm.calculate_iterations()}")
print(f"WM {wm.calculate_time()}")