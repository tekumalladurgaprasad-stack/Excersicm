def translate(text):
    vowels = ("a", "e", "i", "o", "u")
    result = []

    for word in text.split():

        # Rule 1: vowel sound
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            result.append(word + "ay")
            continue

        # Rule 2: "qu" at start
        if word.startswith("qu"):
            result.append(word[2:] + "quay")
            continue

        # Rule 3: consonant + "qu"
        if len(word) > 2 and word[1:3] == "qu":
            result.append(word[3:] + word[:3] + "ay")
            continue

        # Rule 4: consonant cluster (with y acting as a vowel unless first)
        i = 0
        while i < len(word):
            if word[i] in vowels or (word[i] == "y" and i != 0):
                break
            i += 1

        result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)