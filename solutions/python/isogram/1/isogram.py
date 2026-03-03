def is_isogram(string):
    for index in range(len(string)):
        if not string[index].isalpha():
            continue
        if string[index].lower() in string[index + 1:].lower():
            return False
    return True
        
