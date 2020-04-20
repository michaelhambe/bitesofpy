def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    w2 = sorted(words, key=str.lower)
    return [w for w in w2 if w[0].isalpha()]+[w for w in w2 if w[0].isnumeric()]