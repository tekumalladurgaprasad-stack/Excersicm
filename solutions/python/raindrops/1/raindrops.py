def convert(number):
    divisible_by_3 = number % 3 == 0
    divisible_by_5 = number % 5 == 0
    divisible_by_7 = number % 7 == 0

    if divisible_by_3:
        if divisible_by_5:
            if divisible_by_7:
                return "PlingPlangPlong"
            return "PlingPlang"
        elif divisible_by_7:
            return "PlingPlong"
        return "Pling"
    elif divisible_by_5:
        if divisible_by_7:
            return "PlangPlong"
        return "Plang"
    elif divisible_by_7:
        return "Plong"
    else:
        return str(number)
