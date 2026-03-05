"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card.isalpha():
        if card == "J" or card == "Q" or card == "K":
            return 10
        return 1
    return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card_one.isalpha():
        if card_one == "J" or card_one == "Q" or card_one == "K":
            val_1 = 10
        else:
            val_1 = 1
    else:
        val_1 = int(card_one)
    if card_two.isalpha():
        if card_two == "J" or card_two == "Q" or card_two == "K":
            val_2 = 10
        else:
            val_2 = 1
    else:
        val_2 = int(card_two)
    if val_1 > val_2:
        return card_one
    elif val_2 > val_1:
        return card_two
    else:
        return card_one, card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if card_one.isalpha():
        if card_one == "J" or card_one == "Q" or card_one == "K":
            val_1 = 10
        else:
            val_1 = 11
    else:
        val_1 = int(card_one)
    if card_two.isalpha():
        if card_two == "J" or card_two == "Q" or card_two == "K":
            val_2 = 10
        else:
            val_2 = 11
    else:
        val_2 = int(card_two)
    if val_1 + val_2 + 11 > 21:
        return 1
    else:
        return 11
    


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    has_ace = False
    has_ten = False
    ten = ['10', 'K', 'Q', 'J']
    if card_one in ten or card_two in ten:
        has_ten = True
    if card_one == 'A'or card_two == 'A':
        has_ace = True
    if has_ace and has_ten:
        return True
    else:
        return False
    


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if card_one == card_two:
        return True
    heads = ['K', 'Q', 'J']
    if card_one in heads and card_two in heads:
        return True
    return False
    


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    if card_one.isalpha():
        if card_one == "J" or card_one == "Q" or card_one == "K":
            val_1 = 10
        else:
            val_1 = 1
    else:
        val_1 = int(card_one)
    if card_two.isalpha():
        if card_two == "J" or card_two == "Q" or card_two == "K":
            val_2 = 10
        else:
            val_2 = 1
    else:
        val_2 = int(card_two)

    if 9 <= val_1 + val_2 <= 11:
        return True
    return False
