from time import *


class Chrono:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = time()

    def stop(self):
        self.end_time = time()

    def get_duration(self):
        return self.end_time - self.start_time
