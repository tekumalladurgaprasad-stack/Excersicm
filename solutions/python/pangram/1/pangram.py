def is_pangram(sentence):
    characters = "abcdefghijklmnopqrstuvwxyz"
    for ch in characters:
        if ch not in sentence.lower():
            return False
    return True
