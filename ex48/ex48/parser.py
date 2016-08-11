from lexicon import *


class ParseError(Exception):
    pass


class Sentence(object):

    def __init__(self, subj, verb, obj):
        self.subject = subj[1]
        self.verb = verb[1]
        self.object = obj[1]


def peek(words):
    if words:
        word = words[0]
        return word[0]
    else:
        return None


def match(words, expecting):
    if words:
        word = words.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(words, word_type):
    while peek(words) == word_type:
        match(words, word_type)


def parse_verb(words):
    skip(words, 'stop')

    if peek(words) == 'verb':
        return match(words, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(words):
    skip(words, 'stop')
    next_word = peek(words)

    if next_word == 'noun':
        return match(words, 'noun')
    elif next_word == 'direction':
        return match(words, 'direction')
    else:
        raise ParserError("Expected a noun or direction")


def parse_subject(words):
    skip(words, 'stop')
    next_word = peek(words)

    if next_word == 'noun':
        return match(words, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")


def parse_sentence(words):
    subj = parse_subject(words)
    verb = parse_verb(words)
    obj = parse_object(words)

    return Sentence(subj, verb, obj)
