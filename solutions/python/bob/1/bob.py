def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob == "":
        return "Fine. Be that way!"
    yelling = hey_bob.isupper() and any(c.isalpha() for c in hey_bob)
    question = hey_bob.endswith("?")
    if yelling and question:
        return "Calm down, I know what I'm doing!"
    if yelling:
        return "Whoa, chill out!"
    if question:
        return "Sure."
    return "Whatever."
