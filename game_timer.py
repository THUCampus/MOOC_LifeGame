# -*- coding: utf-8 -*-
#
# @author SEMOOC

import math
import time


class GameTimer(object):
    """
    Timer of the game.

    Attributes:
        interval: timer interval, default 1.0 second.
        trigger: a function to call when timer triggered.
        is_running: a flag to show running status, to be used in asynchronous system.
    """

    def __init__(self, trigger, interval=1.0):
        self.interval = interval
        self.trigger = trigger
        self.is_running = False

    def start(self):
        """Start the timer. It triggers only when current time is around integer times of self.interval."""
        self.is_running = True
        while self.is_running:
            time.sleep(math.ceil(time.time() / self.interval) * self.interval - time.time())
            if self.is_running:
                self.trigger()

    def stop(self):
        """Stop the timer before next triggering. It works in asynchronous system."""
        self.is_running = False
