from __future__ import absolute_import

from collections import deque
from edtime import EDTime
from lrucache import LRUCache
from edrconfig import EDRConfig

class EDRBountyHuntingStats(object):
    def __init__(self):
        self.max = 0
        self.previous_max = 0
        self.min = 100.0
        self.previous_min = 0
        self.sum_scanned = 0
        self.sum_awarded = 0
        self.distribution = {"last_index": 0, "bins": [0]*25}
        self.scanned_nb = 0
        self.awarded_nb = 0
        self.awarded = deque(maxlen=20)
        self.scans = deque(maxlen=20)
        self.efficiency = deque(maxlen=20)
        self.max_efficiency = 1000000
        self.max_normal_bounty = 1000000 # probably fine with NPC but might be too low for players...
        now = EDTime.py_epoch_now()
        self.start = now
        self.current = now
        edr_config = EDRConfig()
        self.scans_cache = LRUCache(edr_config.lru_max_size(), edr_config.blips_max_age())
        self.last = {"timestamp": now, "bounty": None}

    def reset(self):

        self.max = 0
        self.previous_max = 0
        self.min = 100.0
        self.previous_min = 0
        self.sum_scanned = 0
        self.sum_awarded = 0
        self.distribution = {"last_index": 0, "bins": [0]*25}
        self.scanned_nb = 0
        self.awarded_nb = 0
        self.awarded = deque(maxlen=20)
        self.scans = deque(maxlen=20)
        self.efficiency = deque(maxlen=20)
        self.max_efficiency = 1000000
        now = EDTime.py_epoch_now()
        self.start = now
        self.current = now
        edr_config = EDRConfig()
        self.scans_cache = LRUCache(edr_config.lru_max_size(), edr_config.blips_max_age())
        self.last = {"timestamp": now, "bounty": None}

    def scanned(self, entry):
        if entry.get("event", None) != "ShipTargeted":
            return False
        if entry.get("ScanStage", 0) < 3:
            return False
        
        raw_pilot_name = entry.get("PilotName", None)
        if not raw_pilot_name:
            return False

        if self.__probably_previously_scanned(entry):
            return False
        
        self.scans_cache.set(raw_pilot_name, entry)
        now = EDTime.py_epoch_now()
        self.current = now
        self.scanned_nb += 1
        self.__update_efficiency()
        
        bounty = entry.get("Bounty", 0)

        self.last = {
            "timestamp": now,
            "bounty": 0
        }
        
        self.sum_scanned += bounty
        self.previous_max = self.max
        self.previous_min = self.min
        self.max = max(self.max, bounty)
        self.min = min(self.min, bounty)
        index = min(int(round(bounty/self.max_normal_bounty * (len(self.distribution["bins"])-1), 0)), len(self.distribution["bins"])-1)
        self.distribution["last_index"] = index
        self.distribution["bins"][index] += 1
        self.scans.append((now, bounty))
        self.last["bounty"] = bounty

    def __probably_previously_scanned(self, entry):
        raw_pilot_name = entry.get("PilotName", None)
        if not raw_pilot_name:
            return False
        
        last_scan = self.scans_cache.get(raw_pilot_name)
        if not last_scan:
            return False
        return (entry["LegalStatus"] != last_scan["LegalStatus"]) or (entry["Bounty"] != last_scan["Bounty"])
    
    def awarded(self, entry):
        if entry.get("event", None) != "Bounty":
            return
        now = EDTime.py_epoch_now()
        self.current = now
        
        total_rewards = 0
        rewards = entry.get("rewards", [])
        for reward in rewards:
            total_rewards += rewards[reward].get("Reward", 0)
        self.sum_awarded += total_rewards
        self.awarded_nb += 1
        self.awarded.append((now, total_rewards))
        self.__update_efficiency()

    def credits_per_hour(self):
        # TODO
        now = EDTime.py_epoch_now()
        self.current = now
        elapsed_time = self.current - self.start
        if elapsed_time:
            return self.sum_awarded / (elapsed_time / 3600.0)
        return 0
    
    def bounty_average(self):
        return (self.sum_scanned / self.scanned_nb) if self.scanned_nb else 0.0
    
    def reward_average(self):
        return (self.sum_awarded / self.awarded_nb) if self.scanned_nb else 0.0

    def __update_efficiency(self):
        now = EDTime.py_epoch_now()
        efficiency = self.credits_per_hour()
        self.efficiency.append((now, efficiency))
        self.max_efficiency = max(self.max_efficiency, efficiency)

    def __repr__(self):
        return str(self.__dict__)