from threading import Condition


class Foo(object):
    def __init__(self):
        self.first_is_done_cv: Condition = Condition()
        self.first_is_done: bool = False
        self.second_is_done_cv: Condition = Condition()
        self.second_is_done: bool = False

    def first(self, print_first):  # print_first() outputs "first". Do not change or remove this line.
        self.first_is_done_cv.acquire()
        try:
            print_first()
            self.first_is_done = True
            self.first_is_done_cv.notify()
        finally:
            self.first_is_done_cv.release()

    def second(self, print_second):
        self.second_is_done_cv.acquire()
        try:

            self.first_is_done_cv.acquire()
            try:
                while not self.first_is_done:
                    self.first_is_done_cv.wait()
                print_second()
            finally:
                self.first_is_done_cv.release()

            self.second_is_done = True
            self.second_is_done_cv.notify()

        finally:
            self.second_is_done_cv.release()

    def third(self, print_third):
        self.second_is_done_cv.acquire()
        try:
            while not self.second_is_done:
                self.second_is_done_cv.wait()
            print_third()
        finally:
            self.second_is_done_cv.release()


# threading --- 基于线程的并行
# https://docs.python.org/zh-cn/3/library/threading.html


# class threading.Condition(lock=None)
#
#     This class implements condition variable objects.
#     A condition variable allows one or more threads to wait until they are notified by another thread.
#
#     If the lock argument is given and not None,
#     it must be a Lock or RLock object, and it is used as the underlying lock.
#     Otherwise, a new RLock object is created and used as the underlying lock.


# 使用条件变量的典型编程风格是将锁用于同步某些共享状态的权限，
# 那些对状态的某些特定改变感兴趣的线程，它们重复调用 wait() 方法，直到看到所期望的改变发生；
# 而对于修改状态的线程，它们将当前状态改变为可能是等待者所期待的新状态后，调用 notify() 方法或者 notify_all() 方法。
# 例如，下面的代码是一个通用的无限缓冲区容量的生产者-消费者情形：
#
# # Consume one item
# with cv:
#     while not an_item_is_available():
#         cv.wait()
#     get_an_available_item()
#
# # Produce one item
# with cv:
#     make_an_item_available()
#     cv.notify()


# 在 with 语句中使用锁、条件和信号量
#
# 这个模块提供的带有 acquire() 和 release() 方法的对象，可以被用作 with 语句的上下文管理器。
# 当进入语句块时 acquire() 方法会被调用，退出语句块时 release() 会被调用。因此，以下片段:
#
# with some_lock:
#     # do something...
#
# 相当于:
#
# some_lock.acquire()
# try:
#     # do something...
# finally:
#     some_lock.release()
