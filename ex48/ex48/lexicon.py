
def scan(user_in):
    words = user_in.lower().split()

    out = []
    TYPE_direction = ['north', 'south', 'east', 'west']
    TYPE_verb = ['go', 'kill', 'eat', 'run']
    TYPE_stop = ['the', 'in', 'of']
    TYPE_noun = ['bear', 'princess']

    for word in words:
        if word in TYPE_direction:
            out.append(('direction', word))
        elif word in TYPE_verb:
            out.append(('verb', word))
        elif word in TYPE_stop:
            out.append(('stop', word))
        elif word in TYPE_noun:
            out.append(('noun', word))
        elif convert_int(word) != None:
            out.append(('number', convert_int(word)))
        else:
            out.append(('error', word))

    return out


def convert_int(k):
    try:
        return int(k)
    except ValueError:
        return None
