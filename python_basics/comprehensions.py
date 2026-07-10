def demonstrate_append_extend(numbers):
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    result = []
    for n in numbers:
        result.append(n)
    result.extend([99, 100])
    return result

def make_word_lengths(words):
    if not isinstance(words, list) or not all(isinstance(w, str) for w in words):
        raise TypeError("words must be a list of strings")
    return {word: len(word) for word in words}

if __name__ == "__main__":
    print(f"Append and Extend: {demonstrate_append_extend([1, 2, 3])}")
    print(f"Word lengths: {make_word_lengths(['python', 'code'])}")
