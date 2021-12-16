import re

BIG = 'big'
SMALL = 'small'

START = 'start'
END = 'end'

class CaveNode():

    def __init__(self, id):
        self.id = id
        if id == id.upper():
            self.type = BIG
        else:
            self.type = SMALL

        self.__children = []
    
    def add_child(self, child_cave):
        self.__children.append(child_cave)

    def children(self, exclude_ids):
        filtered_children = []
        for child in self.__children:
            if child.id not in exclude_ids:
                filtered_children.append(child)
        
        return filtered_children
    
    def paths(self, exclude_ids=None):
        if exclude_ids is None:
            exclude_ids = []

        if len(self.children(exclude_ids)) == 0:
            return [[self.id]]
        
        if self.type == SMALL and self.id != START:
            exclude_ids.append(self.id)

        paths = []
        for cave_child in self.children(exclude_ids):
            for path in cave_child.paths(list(exclude_ids)):
                paths.append([self.id] + path)

        return list(filter(lambda p: p[-1] == END, paths))

    def children_with_first_small_cave_twice(self, exclude_ids):
        excluded_caves = []
        # if len(exclude_ids) > 1:
        if 2 in exclude_ids.values():
            excluded_caves = list(exclude_ids.keys())

        filtered_children = []
        for child in self.__children:
                
            # if exclude_ids.count(child.id) < 2:
            if child.id not in excluded_caves:
                filtered_children.append(child)
        
        return filtered_children

    def get_paths_visiting_small_caves_twice(self, exclude_ids=None):
        if exclude_ids is None:
            exclude_ids = {}

        initial_children = self.children_with_first_small_cave_twice(exclude_ids)
        if len(initial_children) == 0:
            if self.id == END:
                return [[self.id]]

        if self.type == SMALL and self.id != START:
            if self.id in exclude_ids:
                exclude_ids[self.id] += 1
            else:
                exclude_ids[self.id] = 1

        paths = []
        for cave_child in self.children_with_first_small_cave_twice(exclude_ids):
            for path in cave_child.get_paths_visiting_small_caves_twice(dict(exclude_ids)):
                paths.append([self.id] + path)

        return paths