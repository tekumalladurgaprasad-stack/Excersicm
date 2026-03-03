def is_armstrong_number(number):
    digits = len(str(number))
    original = number
    total = 0
    while number > 0:
        digit = number % 10
        total += digit**digits
        number //= 10
    if total == original:
        return True
    return False