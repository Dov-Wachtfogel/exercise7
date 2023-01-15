import threading
import random
import math


def run_thread(my_counter):
    #print('thread')
    while True:
        x, y = random.random(), random.random()
        in_circle = x ** 2 + y ** 2 < 1
        work = my_counter.increamenr(in_circle)
        if not work:
            break


class counter:
    def __init__(self, end):
        self.lock = threading.Lock()
        self.points = 0
        self.points_in_area = 0
        self.end = end * 10 ** 6
        self.pi = math.pi

    def increamenr(self, in_circle):
        self.lock.acquire()
        try:
            self.points = self.points + 1
            if in_circle:
                self.points_in_area = self.points_in_area + 1
        except Exception as e:
            raise e

        finally:
            self.lock.release()
        if self.points % 10 ** 6 == 0:
            print(self.pi, 4 * self.points_in_area / self.points, self.points)
        return self.points < self.end


if __name__ == '__main__':
    my_counter = counter(int(input('enter num in millions')))
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=run_thread, args=(my_counter,)))
        threads[-1].start()
    #print(4 * my_counter.points_in_area / my_counter.points)
