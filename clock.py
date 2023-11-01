import time
# When using this, make sure to use reset_lasttime()
# whenever you want to start a new count.
# Everything else is pretty straight forward
class Clock:
    def __init__(self):
        self.time = time.time()
        self.lasttime = self.time

    def _update_time(self):
        self.time = time.time()
    
    def get_time_since_last(self):
        self._update_time()
        return self.time - self.lasttime

    def reset_lasttime(self):
        self.lasttime = self.time