import random
import threading
import time
from collections.abc import Callable
from threading import Thread, Condition


# https://leetcode.cn/problems/the-dining-philosophers/
class DiningPhilosophers:
    N_PHILOSOPHERS = 5

    def __init__(self):
        # index: fork_id
        self.fork_is_available_cv: list[Condition] = [Condition()] * self.N_PHILOSOPHERS
        # index: fork_id value: philosopher_id
        self.fork_is_taken_by: list[int | None] = [None] * self.N_PHILOSOPHERS

    def fork_is_available(self, fork: int) -> bool:
        return self.fork_is_taken_by[fork] is None

    @classmethod
    def left_side_fork(cls, philosopher: int) -> int:
        return philosopher

    @classmethod
    def right_side_fork(cls, philosopher: int) -> int:
        return (philosopher + 1) % cls.N_PHILOSOPHERS

    @classmethod
    def is_right_hand_first(cls, philosopher: int) -> bool:
        return philosopher == cls.N_PHILOSOPHERS - 1

    # 一个哲学家吃一次饭的完整动作序列.
    # 函数调用方指定哪个哲学家开始想办法自己吃饭, 哲学家怎样安排吃饭的动作序列由该函数内部实现.
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: Callable,
                   pickRightFork: Callable,
                   eat: Callable,
                   putLeftFork: Callable,
                   putRightFork: Callable) -> None:

        # print(threading.current_thread().name + " started.")
        first, second = self.left_side_fork(philosopher), self.right_side_fork(philosopher)
        if self.is_right_hand_first(philosopher):
            first, second = second, first
            pickLeftFork, pickRightFork = pickRightFork, pickLeftFork
            putLeftFork, putRightFork = putRightFork, putLeftFork

        self.fork_is_available_cv[first].acquire()
        # print(threading.current_thread().name + f" cv {first} acquired")
        try:
            while not self.fork_is_available(first):
                # print(threading.current_thread().name + f" cv {first} not available")
                self.fork_is_available_cv[first].wait()
                # print(threading.current_thread().name + f" cv {first} might available")
            self.fork_is_taken_by[first] = philosopher
            # pick up first fork
            pickLeftFork()

            self.fork_is_available_cv[second].acquire()
            # print(threading.current_thread().name + f" cv {second} acquired")
            try:
                while not self.fork_is_available(second):
                    # print(threading.current_thread().name + f" {second} not available")
                    self.fork_is_available_cv[second].wait()
                    # print(threading.current_thread().name + f" {second} might available")
                self.fork_is_taken_by[second] = philosopher
                # pick up second fork
                pickRightFork()
                # eat
                eat()
                # put down second fork
                putRightFork()
                self.fork_is_taken_by[second] = None
                self.fork_is_available_cv[second].notify()
                # print(threading.current_thread().name + f" cv {second} notified")
            finally:
                self.fork_is_available_cv[second].release()
                # print(threading.current_thread().name + f" cv {second} released")

            # put down first fork
            putLeftFork()
            self.fork_is_taken_by[first] = None
            self.fork_is_available_cv[first].notify()
            # print(threading.current_thread().name + f" cv {first} notified")
        finally:
            self.fork_is_available_cv[first].release()
            # print(threading.current_thread().name + f" cv {first} released")


def test_the_dining_philosophers() -> None:
    dp = DiningPhilosophers()
    threads: list[Thread] = []
    for i in range(DiningPhilosophers.N_PHILOSOPHERS):
        t = Thread(name=f"thread_{i}",
                   target=dp.wantsToEat,
                   args=(i,
                         lambda: print(threading.current_thread().name + " pick left fork"),
                         lambda: print(threading.current_thread().name + " pick right fork"),
                         lambda: (print(threading.current_thread().name + " eat"), time.sleep(2)),
                         lambda: print(threading.current_thread().name + " put left fork"),
                         lambda: print(threading.current_thread().name + " put right fork"),
                         )
                   )
        threads.append(t)

    random.shuffle(threads)
    for i in range(DiningPhilosophers.N_PHILOSOPHERS):
        threads[i].start()
    print("all threads started. count:", threading.active_count())
    random.shuffle(threads)
    for i in range(DiningPhilosophers.N_PHILOSOPHERS):
        threads[i].join()
    print("all threads finished.")


if __name__ == '__main__':
    test_the_dining_philosophers()
