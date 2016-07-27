# import io from sys


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        print "Game started"
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scnee = self.scene_map.next_scene(next_scene_name)

        current_scnee.enter()


class Scene(object):

    def enter(self):
        pass


class Death(Scene):

    def enter(self):
        print "You've enterted Death scene, you died."


class CentralCorridor(Scene):

    def enter(self):
        print "You've enterted the Central Corridor scene"
        print "1 pass 2 die"

        action = raw_input("> ")

        if action == "1":
            pass
        elif action == "2":
            pass
        else:
            print "please enter again"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You've enterted the Laser Weapon Armory scene"
        print "1 pass 2 die"

        action = raw_input("> ")

        if action == "1":
            pass
        elif action == "2":
            pass
        else:
            print "please enter again"
            return 'laser_weapon_armory'


class TheBridge(Scene):

    def enter(self):
        print "You've enterted The Bridge scene"
        print "1 pass 2 die"

        action = raw_input("> ")

        if action == "1":
            pass
        elif action == "2":
            pass
        else:
            print "please enter again"
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print "You've enterted Escape Pod scene"
        print "1 pass 2 die"

        action = raw_input("> ")

        if action == "1":
            pass
        elif action == "2":
            pass
        else:
            print "please enter again"
            return 'escape_pod'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
