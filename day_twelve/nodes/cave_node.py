import re

BIG = 'big'
SMALL = 'small'

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
        
        if self.type == SMALL:
            exclude_ids.append(self.id)

        paths = []
        for cave_child in self.children(exclude_ids):
            for path in cave_child.paths(list(exclude_ids)):
                paths.append([self.id] + path)

        return list(filter(lambda p: p[-1] == 'end', paths))
        
