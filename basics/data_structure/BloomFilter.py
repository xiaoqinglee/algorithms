from bitarray import bitarray
import mmh3


class BloomFilter:
    def __init__(self, len_: int, hash_count: int, hash_seed: int = 42):
        self.bit_array_len = len_
        self.hash_count = hash_count
        self.hash_seed = hash_seed
        self.bit_array = bitarray(self.bit_array_len)
        self.bit_array.setall(0)

    def add(self, key: str) -> None:
        for i in range(self.hash_count):
            offset = mmh3.hash(key, self.hash_seed + i, signed=False) % self.bit_array_len
            self.bit_array[offset] = 1

    def lookup(self, key: str) -> bool:
        for i in range(self.hash_count):
            offset = mmh3.hash(key, self.hash_seed + i, signed=False) % self.bit_array_len
            if self.bit_array[offset] == 0:
                return False
        return True


if __name__ == '__main__':
    bf = BloomFilter(500000, 7)

    bf.add("1997")
    bf.add("peter")
    bf.add("jeff")

    print(bf.lookup("1997"))
    print(bf.lookup("peter"))
    print(bf.lookup("jeff"))

    print(bf.lookup("jack"))
    print(bf.lookup("rose"))
    print(bf.lookup("putin"))
