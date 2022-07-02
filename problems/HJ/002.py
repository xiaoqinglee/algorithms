Char = str


def count_char(word: str, target_char: Char) -> int:
    result = 0
    word = word.upper()
    target_char = target_char.upper()
    for char in word:
        if char == target_char:
            result += 1
    return result


if __name__ == '__main__':
    print(count_char(input(), input()))
