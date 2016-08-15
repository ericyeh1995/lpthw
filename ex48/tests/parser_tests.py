from nose.tools import *
from ex48.parser import *
from ex48 import lexicon


def test_parser():
    x = parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(x.subject, 'player')


def test_parser2():
    sentence = "run north"
    x = parse_sentence(lexicon.scan(sentence))
    assert_equal(x.subject, 'player')


def test_parser3():  # test stop words
    sentence = "run the in of bear"
    x = parse_sentence(lexicon.scan(sentence))
    assert_equal(x.subject, 'player')
    assert_equal(x.verb, 'run')
    assert_equal(x.object, 'bear')


def test_parser4():  # test order
    sentence = "the the the run bear"
    x = parse_sentence(lexicon.scan(sentence))
    assert_equal(x.subject, 'player')
    assert_equal(x.verb, 'run')
    assert_equal(x.object, 'bear')
