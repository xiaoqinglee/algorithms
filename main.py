def merge_unique(array1: list[int], array2: list[int]) -> list[int]:
    if len(array1) == 0:
        return array2
    if len(array2) == 0:
        return array1

    new_array: list[int] = []

    array1_next: int = 0
    array2_next: int = 0

    while array1_next <= len(array1) - 1 and array2_next <= len(array2) - 1:
        if array1[array1_next] < array2[array2_next]:
            new_array.append(array1[array1_next])
            array1_next += 1
        elif array1[array1_next] > array2[array2_next]:
            new_array.append(array2[array2_next])
            array2_next += 1
        else:
            new_array.append(array1[array1_next])
            array1_next += 1
            array2_next += 1
    while array1_next <= len(array1) - 1:
        new_array.append(array1[array1_next])
        array1_next += 1
    while array2_next <= len(array2) - 1:
        new_array.append(array2[array2_next])
        array2_next += 1

    return new_array


if __name__ == '__main__':
    a1 = [9, 22, 35, 72]
    a2 = [2, 14, 22, 35, 41, 42]
    print(merge_unique(a1, a2))
