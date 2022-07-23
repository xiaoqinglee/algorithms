import bisect


class ExamRoom:

    def __init__(self, n: int):
        self.cap = n
        self.taken_seats: list[int] = []

    def seat(self) -> int:
        if len(self.taken_seats) == 0:
            self.taken_seats.append(0)
            return 0
        else:
            max_distance: int | float = -float("inf")
            this_seat: int = -1

            # 因为总是选择最小的座位, 所以判断座位间距的时候从左往右遍历

            if self.taken_seats[0] != 0:
                distance: int = self.taken_seats[0] - 0
                if distance > max_distance:
                    max_distance = distance
                    this_seat = 0

            for i, seat in enumerate(self.taken_seats):
                if i == 0:
                    continue
                distance: int = (seat - self.taken_seats[i-1]) // 2
                if distance > max_distance:
                    max_distance = distance
                    this_seat = self.taken_seats[i-1] + distance

            if self.taken_seats[-1] != self.cap - 1:
                distance: int = (self.cap - 1) - self.taken_seats[-1]
                if distance > max_distance:
                    max_distance = distance
                    this_seat = self.cap - 1

            bisect.insort(self.taken_seats, this_seat)
            return this_seat

    def leave(self, p: int) -> None:
        # It is guaranteed that there is a student sitting at seat p.
        self.taken_seats.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
