import random
import threading
import time
from typing import Callable
from threading import Thread, Semaphore, Lock


class H2O:
    def __init__(self):
        self.H2O_lock = Lock()
        self.locked_H_count: int = 0
        self.locked_O_count: int = 0
        self.H_sem = Semaphore(2)
        self.O_sem = Semaphore(1)
        self.H_sem.acquire()
        self.H_sem.acquire()
        self.O_sem.acquire()

    # 每一个线程只run一次hydrogen()方法然后就结束了, 在该方法内部也只产生一个H原子
    def hydrogen(self, releaseHydrogen: Callable) -> None:
        self.H2O_lock.acquire()
        try:
            self.locked_H_count += 1
            if self.locked_H_count >= 2 and self.locked_O_count >= 1:
                self.locked_H_count -= 2
                self.locked_O_count -= 1
                time.sleep(2)
                self.H_sem.release(2)
                self.O_sem.release(1)
        finally:
            self.H2O_lock.release()

        # 满额占用无额外空间可用的信号量导致占位请求等待
        # 对应 golang中empty buffered channel导致元素消费请求等待
        self.H_sem.acquire(blocking=True)
        # releaseHydrogen() outputs "H".
        releaseHydrogen()

    # 每一个线程只run一次oxygen()方法然后就结束了, 在该方法内部也只产生一个O原子
    def oxygen(self, releaseOxygen: Callable) -> None:
        self.H2O_lock.acquire()
        try:
            self.locked_O_count += 1
            if self.locked_H_count >= 2 and self.locked_O_count >= 1:
                self.locked_H_count -= 2
                self.locked_O_count -= 1
                time.sleep(2)
                self.H_sem.release(2)
                self.O_sem.release(1)
        finally:
            self.H2O_lock.release()
        self.O_sem.acquire(blocking=True)
        # releaseOxygen() outputs "O".
        releaseOxygen()


if __name__ == '__main__':
    chars: list[str] = (["H", "H", "O"] * 42)
    threads: list[Thread] = []
    h2o = H2O()
    for i in chars:
        if i == "H":
            t = Thread(target=h2o.hydrogen, args=(lambda: print("H", end=""),))
        else:
            t = Thread(target=h2o.oxygen, args=(lambda: print("O", end=""),))
        threads.append(t)

    random.shuffle(threads)
    for i in range(len(threads)):
        threads[i].start()
    random.shuffle(threads)
    for i in range(len(threads)):
        threads[i].join()


# 信号量对象
#
#
# 这是计算机科学史上最古老的同步原语之一，早期的荷兰科学家 Edsger W. Dijkstra 发明了它。
# （他使用名称 P() 和 V() 而不是 acquire() 和 release() ）。
# 一个信号量管理一个内部计数器，该计数器因 acquire() 方法的调用而递减，因 release() 方法的调用而递增。
# 计数器的值永远不会小于零；当 acquire() 方法发现计数器为零时，将会阻塞，直到其它线程调用 release() 方法。
#
#
# class threading.Semaphore(value=1)
#
#     该类实现信号量对象。
#     信号量对象管理一个原子性的计数器，代表 release() 方法的调用次数减去 acquire() 的调用次数再加上一个初始值。
#     如果需要， acquire() 方法将会阻塞直到可以返回而不会使得计数器变成负数。在没有显式给出 value 的值时，默认为1。
#     可选参数 value 赋予内部计数器初始值，默认值为 1 。如果 value 被赋予小于0的值，将会引发 ValueError 异常。
#
#     acquire(blocking=True, timeout=None)
#
#         获取一个信号量。
#
#         在不带参数的情况下调用时：
#             如果在进入时内部计数器的值大于零，则将其减一并立即返回 True。
#             如果在进入时内部计数器的值为零，则将会阻塞直到被对 release() 的调用唤醒。
#             一旦被唤醒（并且计数器的值大于 0），则将计数器减 1 并返回 True。
#             每次对 release() 的调用将只唤醒一个线程。 线程被唤醒的次序是不可确定的。
#
#         当 blocking 设置为 False 时调用，不会阻塞。 如果没有参数的调用会阻塞，立即返回 False；
#         否则，做与无参数调用相同的事情时返回 True。
#
#         当发起调用时如果 timeout 不为 None，则它将阻塞最多 timeout 秒。
#         请求在此时段时未能成功完成获取则将返回 False。 在其他情况下返回 True。
#
#
#     release(n=1)
#
#         释放一个信号量，将内部计数器的值增加 n。
#         当进入时值为零且有其他线程正在等待它再次变为大于零时，则唤醒那 n 个线程。


# 锁对象
#
#
# 原始锁是一个在锁定时不属于特定线程的同步基元组件。
#
# 原始锁处于 "锁定" 或者 "非锁定" 两种状态之一。
# 它被创建时为非锁定状态。它有两个基本方法， acquire() 和 release() 。
# 当状态为非锁定时， acquire() 将状态改为 锁定 并立即返回。
# 当状态是锁定时， acquire() 将阻塞至其他线程调用 release() 将其改为非锁定状态，然后 acquire() 调用重置其为锁定状态并返回。
# release() 只在锁定状态下调用； 它将状态改为非锁定并立即返回。如果尝试释放一个非锁定的锁，则会引发 RuntimeError  异常。
#
# 当多个线程在 acquire() 等待状态转变为未锁定被阻塞，然后 release() 重置状态为未锁定时，只有一个线程能继续执行；
# 至于哪个等待线程继续执行没有定义，并且会根据实现而不同。
#
# 所有方法的执行都是原子性的。
#
# class threading.Lock
#
#     实现原始锁对象的类。一旦一个线程获得一个锁，会阻塞随后尝试获得锁的线程，直到它被释放；任何线程都可以释放它。
#
#     acquire(blocking=True, timeout=- 1)
#
#         可以阻塞或非阻塞地获得锁。
#         当调用时参数 blocking 设置为 True （缺省值），阻塞直到锁被释放，然后将锁锁定并返回 True 。
#         在参数 blocking 被设置为 False 的情况下调用，将不会发生阻塞。
#         如果调用时 blocking 设为 True 会阻塞，并立即返回 False ；否则，将锁锁定并返回 True。
#         当参数 timeout 使用设置为正值的浮点数调用时，最多阻塞 timeout 指定的秒数，在此期间锁不能被获取。
#         设置 timeout 参数为 -1 specifies an unbounded wait.
#         It is forbidden to specify a timeout when blocking is False 。
#         如果成功获得锁，则返回 True，否则返回 False (例如发生 超时 的时候)。

#
#     release()
#
#         释放一个锁。这个方法可以在任何线程中调用，不单指获得锁的线程。
#         当锁被锁定，将它重置为未锁定，并返回。如果其他线程正在等待这个锁解锁而被阻塞，只允许其中一个允许。
#         当在未锁定的锁上发起调用时，会引发 RuntimeError。
#         没有返回值。


# 栅栏对象
#
#
# 栅栏类提供一个简单的同步原语，用于应对固定数量的线程需要彼此相互等待的情况。
# 线程调用 wait() 方法后将阻塞，直到所有线程都调用了 wait() 方法。此时所有线程将被同时释放。
#
# 栅栏对象可以被多次使用，但进程的数量不能改变。
#
# 这是一个使用简便的方法实现客户端进程与服务端进程同步的例子：
#
# b = Barrier(2, timeout=5)
#
# def server():
#     start_server()
#     b.wait()
#     while True:
#         connection = accept_connection()
#         process_server_connection(connection)
#
# def client():
#     b.wait()
#     while True:
#         connection = make_connection()
#         process_client_connection(connection)
#
# class threading.Barrier(parties, action=None, timeout=None)
#
#     创建一个需要 parties 个线程的栅栏对象。
#     如果提供了可调用的 action 参数，它会在所有线程被释放时在其中一个线程中自动调用。
#     timeout 是默认的超时时间，如果没有在 wait() 方法中指定超时时间的话。
#
#     wait(timeout=None)
#
#         冲出栅栏。当栅栏中所有线程都已经调用了这个函数，它们将同时被释放。
#         如果提供了 timeout 参数，这里的 timeout 参数优先于创建栅栏对象时提供的 timeout 参数。
#
#         函数返回值是一个整数，取值范围在0到 parties -- 1，
#         在每个线程中的返回值不相同。可用于从所有线程中选择唯一的一个线程执行一些特别的工作。例如：
#
#         i = barrier.wait()
#         if i == 0:
#             # Only one thread needs to print this
#             print("passed the barrier")
