from nose.tools import *
from ex47.game import Room


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's
                a door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})


def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)


def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, oyu can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)


def test_hallway():
    k_0 = Room("k_0", "0th room")
    k_1 = Room("k_1", "1st room")
    k_2 = Room("k_2", "2nd room")
    k_3 = Room("k_3", "3rd room")
    k_4 = Room("k_4", "4th room")

    # fwd, bk
    k_0.add_paths({'fwd': k_1})
    k_1.add_paths({'bk': k_0, 'fwd': k_2})
    k_2.add_paths({'bk': k_1, 'fwd': k_3})
    k_3.add_paths({'bk': k_2, 'fwd': k_4})
    k_4.add_paths({'bk': k_3})

    assert_equal(k_0.go('fwd').go('fwd').go('fwd').go('fwd'), k_4)
