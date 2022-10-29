def build_word_grid(word):
    return [_capitalize(word, i) for i in range(len(word))]
def _capitalize(word, i):
    return "".join(x.upper() if i == n else x.lower() for n, x in enumerate(word))
