NEW_FISH_START_TIMER = 8
FISH_RESET_TIMER = 6

class LanternFish():

    def __init__(self, internal_timer):
        if self.__is_int(internal_timer):
            self.__internal_timer = internal_timer
            self.__children = []

    def get_internal_timer(self):
        return self.__internal_timer

    def spawn(self):
        return self.__children

    def has_children(self):
        return bool(self.__children)

    def take_spawn(self):
        if self.has_children():
            spawn = self.__children[0]
            self.__children = []
            return spawn

    def count_children(self, with_self=False):
        count = len(self.__children)
        plus_one = 1 if with_self else 0

        for child in self.__children:
            count += child.count_children()

        return count + plus_one

    def respond_to_day(self):
        if len(self.__children) > 0:
            for spawn in self.__children:
                spawn.respond_to_day()

        if self.__internal_timer > 0:
            self.__internal_timer -= 1
        else:
            self.__spawn()
            self.__internal_timer = FISH_RESET_TIMER

    def __spawn(self):
        self.__children.append(LanternFish(internal_timer=NEW_FISH_START_TIMER))

    def __is_int(self, el):
        return type(el).__name__ == 'int'