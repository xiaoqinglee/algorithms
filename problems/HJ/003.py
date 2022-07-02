if __name__ == '__main__':
    n_nums: int = int(input())
    num_set: set[int] = set()
    for i in range(n_nums):
        num_set.add(int(input()))
    for num in sorted(num_set):
        print(num)
