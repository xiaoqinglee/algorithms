import threading
import time
from collections.abc import Callable
from threading import Thread, Condition


# https://leetcode.cn/problems/print-in-order/
class Foo(object):
    def __init__(self):
        self.turn_cv: Condition = Condition()
        self.turn: int = 1  # protected by cv, values are enum type

    def first(self, print_first: Callable) -> None:  # print_first() outputs "first". Do not change or remove this line.
        self.turn_cv.acquire()
        try:
            while self.turn != 1:
                self.turn_cv.wait()
            print_first()
            self.turn += 1
            self.turn_cv.notify_all()
        finally:
            self.turn_cv.release()

    def second(self, print_second: Callable) -> None:
        self.turn_cv.acquire()
        try:
            while self.turn != 2:
                self.turn_cv.wait()
            print_second()
            self.turn += 1
            self.turn_cv.notify_all()
        finally:
            self.turn_cv.release()

    def third(self, print_third: Callable) -> None:
        self.turn_cv.acquire()
        try:
            while self.turn != 3:
                self.turn_cv.wait()
            print_third()
            self.turn += 1
            self.turn_cv.notify_all()
        finally:
            self.turn_cv.release()


def test_foo() -> None:
    # 三个不同的线程 A、B、C 将会共用一个 Foo 实例。
    #
    #     线程 A 将会调用 first() 方法
    #     线程 B 将会调用 second() 方法
    #     线程 C 将会调用 third() 方法
    #
    # 请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。

    foo = Foo()
    t1 = Thread(name="thread_1",
                target=foo.first,
                args=(lambda: (print(threading.current_thread().name + " first"), time.sleep(2)),))
    t2 = Thread(name="thread_2",
                target=foo.second,
                args=(lambda: (print(threading.current_thread().name + " second"), time.sleep(2)),))
    t3 = Thread(name="thread_3",
                target=foo.third,
                args=(lambda: (print(threading.current_thread().name + " third"), time.sleep(2)),))

    foo2 = Foo()
    t4 = Thread(name="thread_4",
                target=foo2.first,
                args=(lambda: (print(threading.current_thread().name + " first"), time.sleep(2)),))
    t5 = Thread(name="thread_5",
                target=foo2.second,
                args=(lambda: (print(threading.current_thread().name + " second"), time.sleep(2)),))
    t6 = Thread(name="thread_6",
                target=foo2.third,
                args=(lambda: (print(threading.current_thread().name + " third"), time.sleep(2)),))
    t1.start()
    t2.start()
    t3.start()

    t6.start()
    t5.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()

    t6.join()
    t5.join()
    t4.join()

# threading --- 基于线程的并行
# https://docs.python.org/zh-cn/3/library/threading.html


# 条件对象
#
# 条件变量总是与某种类型的锁对象相关联，锁对象可以通过传入获得，或者在缺省的情况下自动创建。
# 当多个条件变量需要共享同一个锁时，传入一个锁很有用。
# 锁是条件对象的一部分，你不必单独地跟踪它。
# (POSIX C 编程时需要手动跟踪这个锁, 来保证共享变量被修改这个动作的发生是互斥的, 见 OSTEP 线程API相关章节.
# 但在python里, Condition.acquire()调用时就获得了这个锁,  Condition.release()调用时就释放了这个锁.)
#
# 条件变量遵循 上下文管理协议 ：
# 使用 with 语句会在它包围的代码块内获取关联的锁。
# acquire() 和 release() 方法也能调用关联锁的相关方法。
#
# 其它方法必须在持有关联的锁的情况下调用。
# wait() 方法释放锁，然后阻塞直到其它线程调用 notify() 方法或 notify_all() 方法唤醒它。
# 一旦被唤醒， wait() 方法重新获取锁并返回。它也可以指定超时时间。
#
# The notify() method wakes up one of the threads waiting for the condition variable, if any are waiting.
# The notify_all() method wakes up all threads waiting for the condition variable.
#
# 注意：
# notify() 方法和 notify_all() 方法并不会释放锁，这意味着被唤醒的线程不会立即从它们的 wait() 方法调用中返回，
# 而是会在调用了 notify() 方法或 notify_all() 方法的线程最终放弃了锁的所有权后返回。


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


# golang goroutine 条件变量的 API 也和 POSIX C 类似
# https://pkg.go.dev/sync#Cond


#     // Cond implements a condition variable, a rendezvous point
#     // for goroutines waiting for or announcing the occurrence
#     // of an event.
#     //
#     // Each Cond has an associated Locker L (often a *Mutex or *RWMutex),
#     // which must be held when changing the condition and
#     // when calling the Wait method.
#     //
#     // A Cond must not be copied after first use.
#     type Cond struct {
#         noCopy noCopy
#
#         // L is held while observing or changing the condition
#         L Locker
#
#         notify  notifyList
#         checker copyChecker
#     }
#
#     // NewCond returns a new Cond with Locker l.
#     func NewCond(l Locker) *Cond
#
#     // Wait atomically unlocks c.L and suspends execution
#     // of the calling goroutine. After later resuming execution,
#     // Wait locks c.L before returning. Unlike in other systems,
#     // Wait cannot return unless awoken by Broadcast or Signal.
#     //
#     // Because c.L is not locked when Wait first resumes, the caller
#     // typically cannot assume that the condition is true when
#     // Wait returns. Instead, the caller should Wait in a loop:
#     //
#     //    c.L.Lock()
#     //    for !condition() {
#     //        c.Wait()
#     //    }
#     //    ... make use of condition ...
#     //    c.L.Unlock()
#     //
#     func (c *Cond) Wait()
#
#     // Signal wakes one goroutine waiting on c, if there is any.
#     //
#     // It is allowed but not required for the caller to hold c.L
#     // during the call.
#     func (c *Cond) Signal()
#
#     // Broadcast wakes all goroutines waiting on c.
#     //
#     // It is allowed but not required for the caller to hold c.L
#     // during the call.
#     func (c *Cond) Broadcast()
