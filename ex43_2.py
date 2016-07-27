from sys import exit


class Scene(object):

    def enter(self):
        print "This scene is not yet configured"
        exit(1)


class Engine(object):

    def __init__(self):
        pass

    def play(self):
        pass


class Map(object):

    def __init__(self):
        pass

    def next_scene(self):
        pass

    def opening_scene(self):
        pass


a_game = Engine()
a_game.start()
