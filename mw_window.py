import datetime
import time


class mc:
    def __init__(self, start):
        self.maint_window_start_hours = start



def next_mw_time(module_config):
    # type: (ConfigurationRLIC) -> datetime.datetime
    return datetime.datetime.now().replace(hour=module_config.maint_window_start_hours,
                                           minute=0,
                                           second=0,
                                           microsecond=0)

def compute_prefilter_time(module_config, module_state):
    # type: (ConfigurationRLIC, ModuleState) -> datetime.datetime
    return next_mw_time(module_config) + datetime.timedelta(days=1, minutes=-120)



def next_mw_time_2(module_config):
    # type: (ConfigurationRLIC) -> datetime.datetime
    now = datetime.datetime.now().replace(microsecond=0)
    mw = now.replace(hour=module_config.maint_window_start_hours,minute=0,second=0)
    if mw < now:
        return mw + datetime.timedelta(days=1)
    return mw

def compute_prefilter_time_2(module_config, module_state):
    # type: (ConfigurationRLIC, ModuleState) -> datetime.datetime
    return next_mw_time(module_config) + datetime.timedelta(minutes=-120)





mc_1 = mc(0)
now_1 = datetime.datetime.now().replace(microsecond=0)
mw_1 = next_mw_time(mc_1)
print("NOW: {}\nMW: {}\nMW in past: {}".format(now_1, mw_1, now_1<mw_1))


mc_2 = mc(0)
now_2 = datetime.datetime.now().replace(microsecond=0)
mw_2 = next_mw_time_2(mc_2)
print("NOW: {}\nMW: {}\nMW in past: {}".format(now_2, mw_2, now_2<mw_2))