from sys import exit
import random

# a very simple procedurally generated world tree


class Engine(object):

    def __init__(self, world):
        print "initializing game..."
        self.world = world

    def play(self):
        print "game begin!\n"

        current_area = self.world.starting_area()  # root
        next_area_id = current_area.enter()
        current_area = self.world.next_area(next_area_id)  # first child

        while True:
            # TODO: enter from the map
            next_area_id = current_area.enter()
            current_area = self.world.next_area(next_area_id)


class Area(object):

    def enter(self):
        print "not yet configured area"
        exit(1)

    def select_next(self, num_branch):
        userInput = -1
        while True:
            try:
                userInput = int(raw_input("> "))
            except ValueError:
                print "please enter a number between 0 and %d" % num_branch
                continue
            if not(userInput >= 0 and userInput <= num_branch):
                print "please enter a number between 0 and %d" % num_branch
                continue
            else:
                break
        return userInput


class Area_0(object):

    def __init__(self, num_branch):
        self.area = Area()
        self.num_branch = num_branch

    def select_next(self):
        return self.area.select_next(self.num_branch)

    def enter(self):
        print "This is Area_0, your journey begins!"
        print "You have %r choices to move forward" % self.num_branch

        x = self.select_next()
        print "you've chosen %r\n" % x

        if x == 0:
            return 'Area_0'
        elif x == 1:
            return 'Area_1'
        elif x == 2:
            return 'Area_2'
        elif x == 3:
            return 'Area_3'
        else:
            print "you've broken the game..."
            exit(1)


# class Area_p(object):

#     def __init__(self, num_branch, area_id):
#         self.area = Area()
#         self.num_branch = num_branch
#         self.area_id = area_id

#     def select_next(self):
#         return self.area.select_next(self.brnach)

#     def enter(self):
#         print "This is Area_%d" % self.area_id
#         print "You have %d choices to move forward" % self.num_branch

#         if num_branch == 0:
#             print "you've reached a dead end"


# class Area_end(object):
#     def __init__(self, num_branch):
#         self.area = Area()


class World(object):

    def __init__(self):
        # area name and its class to call
        self.areas = {
            'Area_0': Area_0(2)
            #   'Area_end': Area_end()
        }

        self.next_area_id = 1

    def next_area(self, area_id):
        # if area_id is not in the areas dict, then add_area
        return self.areas.get(area_id)

    def starting_area(self):
        return self.areas.get('Area_0')

    def add_area(self):
        # generate a int for number of num_branch
        # create area objects
        # add id to the areas dictionary
        pass

world = World()
game = Engine(world)
game.play()
