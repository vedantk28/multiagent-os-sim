import time

class SimulationClock:
    def __init__(self, tick_duration=1.0):
        self.tick_duration= tick_duration
        self.current_tick=0

    def tick(self):
        time.sleep(self.tick_duration)
        self.current_tick += 1
        return self.current_tick
