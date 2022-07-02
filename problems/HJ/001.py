def last_word_len(sentence: str) -> int:
    i = len(sentence) - 1
    while sentence[i] != " " and i >= 0:
        i -= 1
    return len(sentence) - 1 - i


if __name__ == '__main__':
    print(last_word_len(input()))
