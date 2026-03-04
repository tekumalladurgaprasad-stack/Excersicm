"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """

    words = title.split()
    word = ""
    for index,ch in enumerate(words):
        if ch[0].islower():
            ch = ch[0].upper() + ch[1:]
            word += ch
        if index < len(words) - 1:
            word += " "
    return word


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """

    if sentence.endswith("."):
        return True
    return False


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """

    words = sentence.split()
    sentence = ""
    for i,ch in enumerate(words):
        if i < len(words) - 1:
            sentence += ch + " "
        else:
            sentence += ch
    return sentence


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """
    words = sentence.split()
    new_sentence = ""
    for index,word in enumerate(words):
        if word.endswith("."):
            n_word = word[:len(word) - 1]
            if n_word != old_word:
                new_sentence += n_word
            else:
                new_sentence += new_word + "."
        elif word != old_word:
            new_sentence += word
        else:
            new_sentence += new_word
        if index < len(words) - 1:
            new_sentence += " "
        if index == len(words) - 1 and word.endswith(".") and not new_sentence.endswith("."):
            new_sentence += "."
    return new_sentence
