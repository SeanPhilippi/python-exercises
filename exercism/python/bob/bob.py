def response(hey_bob):
    # simple question, 'Sure.' not uppercased
    if hey_bob.strip().endswith('?') and not hey_bob.isupper():
        return 'Sure.'
    # no characters, only white space in string
    elif hey_bob.isspace() or hey_bob == '':
        return 'Fine. Be that way!'
    # all caps, 'Whoa, chill out!'
    elif hey_bob.isupper() and not hey_bob.endswith('?'):
        return 'Whoa, chill out!'
    # all caps question, 'Calm down, I know what I'm doing!' 
    elif hey_bob.isupper() and hey_bob.strip().endswith('?'):
        return "Calm down, I know what I'm doing!"
    # default 'Whatever.'
    else:
        return 'Whatever.'

