from sys import exit


class Scene(object):

    def enter(self):
        print "This scene is not yet configured"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        print "initializing game..."
        self.scene_map = scene_map

    def play(self):
        print "game begin!"
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('Scene_4')

        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # current_scene.enter()


class Scene_1(Scene):

    def enter(self):
        print "this is scene 1"
        print "enter 2 to enter scene 2, enter 5 to enter scene 5"
        x = raw_input('> ')

        if x == '2':
            return 'Scene_2'
        elif x == '5':
            return 'Scene_5'
        else:
            print "try again"
            return 'Scene_1'


class Scene_2(Scene):

    def enter(self):
        print "this is scene 2"
        print "enter 3 to enter scene 3, enter 5 to enter scene 5"
        x = raw_input('> ')

        if x == '3':
            return 'Scene_3'
        elif x == '5':
            return 'Scene_5'
        else:
            print "try again"
            return 'Scene_2'


class Scene_3(Scene):

    def enter(self):
        print "this is scene 3"
        print "enter 4 to enter scene 4, enter 5 to enter scene 5"
        x = raw_input('> ')

        if x == '4':
            return 'Scene_4'
        elif x == '5':
            return 'Scene_5'
        else:
            print "try again"
            return 'Scene_3'


class Scene_4(Scene):

    def enter(self):
        print "this is scene 4, the ending scene"
        print "you've won"
        print "restart?"
        x = raw_input('> ')

        if x == '1':
            return 'Scene_1'
        else:
            print 'have a good day!'
            exit(1)


class Scene_5(Scene):

    def enter(self):
        print "this is they dying scene"
        print "retry?"
        x = raw_input('> ')

        if x == '1':
            return 'Scene_1'
        else:
            print 'goodbye'
            exit(1)


class Map(object):
    Scenes = {'Scene_1': Scene_1(),
              'Scene_2': Scene_2(),
              'Scene_3': Scene_3(),
              'Scene_4': Scene_4(),
              'Scene_5': Scene_5()
              }

    def __init__(self, begin_scene):
        self.k = begin_scene

    def next_scene(self, scene_name):
        return self.Scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.k)


a_map = Map('Scene_1')
a_game = Engine(a_map)
a_game.play()
