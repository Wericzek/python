import threading as th
from time import sleep
import os


nPhil = 4
philosophers = []
forks = []


class Filozof(th.Thread):
    def __init__(self, index):
        th.Thread.__init__(self)
        self.index = index

    def run(self):
        left_fork_index = self.index
        right_fork_index = (self.index - 1) % nPhil
        fork_pair = ForkPair(left_fork_index, right_fork_index)
        while True:
            fork_pair.pickUp()
            print("Philosopher", self.index, "eats.")
            fork_pair.putDown()

class ForkPair:
    def __init__(self, left_fork_index, right_fork_index):
        if left_fork_index > right_fork_index:
            left_fork_index, right_fork_index = right_fork_index, left_fork_index
        self.first_fork = forks[left_fork_index]
        self.second_fork = forks[right_fork_index]

    def pickUp(self):
        self.first_fork.acquire()
        self.second_fork.acquire()

    def putDown(self):
        self.first_fork.release()
        self.second_fork.release()


if __name__ == "__main__":
    for i in range(0, nPhil):
        philosophers.append(Filozof(i))
        forks.append(th.Lock())

    for philosopher in philosophers:
        philosopher.start()

    try:
        while True: sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        os._exit(0)