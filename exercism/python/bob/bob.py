def response(hey_bob):
    if hey_bob.strip().endswith('?') and not hey_bob.isupper():
        return 'Sure.'
    elif hey_bob.isspace() or hey_bob == '':
        return 'Fine. Be that way!'
    elif hey_bob.isupper() and not hey_bob.strip().endswith('?'):
        return 'Whoa, chill out!'
    elif hey_bob.isupper() and hey_bob.strip().endswith('?'):
        return "Calm down, I know what I'm doing!"
    else:
        return 'Whatever.'
