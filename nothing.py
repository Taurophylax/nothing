# nothing v0.0
from things.things import something as something # import things from things as soemthing

pass # passes

that_thing = [True]
for this_thing in that_thing:  # for everything in true, continue
    continue

def nothing_fun(thing: bool) -> bool:  # returns true if true
    return True

def __break__():
    something()
    return True
  
while True:
    if __break__():
        thing = nothing_fun(True)  # call nothing to thing
        break

pass # passes

class nothing_class:
    def __init__(self, thing: bool) -> None:
        self.thing = thing  # store the state of nothing

    def do_nothing(self) -> bool:
        thing = self.thing  # retrieve our nothing
        for thing in [True, False]:
            if thing:
                thing = True  # affirm nothing
                something()
            else:
                pass  # continue doing nothing
        return thing

    def nothing_loop(self) -> bool:
        thing = self.do_nothing()
        while thing:
            if thing:
                thing = self.do_nothing()  # recursive nothing
                something()
                break
            else:
                pass
        return thing

thing = nothing_class(True)
thing = thing.nothing_loop()
print("")
