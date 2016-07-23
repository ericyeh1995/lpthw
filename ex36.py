from sys import exit


def infiniteHole(n):
    print "You can't escape, you are stucked in level %d" % n
    next = raw_input("> ")
    if next == "climb up":
        print "ok"
    else:
        infiniteHole(n - 1)
    print "climbing up to %d" % (n + 1)


def start():
    print "This is a fun game"
    print "Choose 1 for infiniteHole"
    next = raw_input("> ")
    if next == "1":
        infiniteHole(-1)
    else:
        print "x"

start()
