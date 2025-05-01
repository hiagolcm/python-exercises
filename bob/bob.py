def response(hey_bob):
    hey_bob = hey_bob.strip()

    silence = not hey_bob

    if silence:
        return 'Fine. Be that way!'

    yelling = any([c.isalpha() for c in hey_bob]) and hey_bob.upper() == hey_bob
    questioning = hey_bob[-1] == '?'

    if yelling and questioning:
        return "Calm down, I know what I'm doing!"

    if questioning:
        return "Sure."

    if yelling:
        return "Whoa, chill out!"

    return "Whatever."
