from basics.data_structure.IntervalTree import AugmentedIntervalTree


class MyCalendar:
    def __init__(self):
        self.interval_tree = AugmentedIntervalTree()

    def book(self, start: int, end: int) -> bool:
        overlapping_intervals = self.interval_tree.get_overlapping_intervals((start, end-1))
        # print("try book ", start, end-1)
        # print("found", overlapping_intervals)
        if len(overlapping_intervals) > 0:
            return False
        else:
            self.interval_tree.add_interval(interval=(start, end-1))
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
