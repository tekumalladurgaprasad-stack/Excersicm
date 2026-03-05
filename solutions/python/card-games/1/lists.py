"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    rounds = []
    for num in range(3):
        rounds.append(number + num)
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return True if number in rounds else False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    if len(hand) % 2 == 0:
        mid = len(hand) // 2 - 1
    else:
        mid = len(hand) // 2
    total = 0
    for num in hand:
        total += num
    avg = total / len(hand)
    avg_1 = (hand[0] + hand[len(hand) - 1]) / 2
    avg_2 = hand[mid]

    if avg == avg_1 or avg == avg_2:
        return True
    return False

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd_sum = 0
    odd = 0
    even_sum = 0
    even = 0
    odd_avg = 0
    even_avg = 0
    for index, num in enumerate(hand):
        if index % 2 == 0:
            even_sum += num
            even += 1
        else:
            odd_sum += num
            odd += 1
    if odd > 0:
        odd_avg = odd_sum / odd
    if even > 0:
        even_avg = even_sum / even
    if odd_avg == even_avg:
        return True
    return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
    return hand
