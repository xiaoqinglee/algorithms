from basics.data_structure.Trie import Trie
from basics.sort.radix_sort.array import radix_sort_msd_using_trie
from problems.lc0815_BusRoutes import Solution
if __name__ == "__main__":
    t = Trie()
    t.insert("hello")
    print(t.search(""))
    print(t.startsWith(""))
    t.insert("")
    print(t.search(""))
    print(t.startsWith(""))
    t.delete("")
    print(t.search(""))
    print(t.startsWith(""))
    print("==============")
    t.delete("hello")
    print(t.search(""))
    print(t.startsWith(""))
    result = radix_sort_msd_using_trie(["nihao", "ni", "", "", "", "weljkjdkfj", "z", "aaa"])
    print(result)


