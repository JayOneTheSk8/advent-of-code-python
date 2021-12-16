MARKED = 'marked'
X = 'x'
Y = 'y'

class PaperMap():

    def __init__(self, width, height):
        self.__create_map(width, height)

    def get_marked_count(self):
        marked_count = 0
        for row in self.__paper_map:
            for marker in row:
                if marker[MARKED]:
                    marked_count += 1

        return marked_count

    def print_paper_map(self):
        for row in self.__paper_map:
            print([f"{'#' if m[MARKED] else '_'}" for m in row])

    def mark_paper(self, coord):
        if not self.__is_list(coord):
            raise ValueError('Coord must be list')

        if len(coord) != 2:
            raise ValueError('Coord must have two items')

        x, y = coord
        self.__paper_map[y][x][MARKED] = True

    def fold_paper(self, instruction):
        if X in instruction:
            return self.__fold_with_x(instruction[X])
        if Y in instruction:
            return self.__fold_with_y(instruction[Y])

    def __fold_with_x(self, point):
        # first_row = self.__paper_map[0]
        # fold_line = first_row[point]
        for row in self.__paper_map:
            left_half = row[:point]
            right_half = row[point + 1:]

            left_half_pointer = len(left_half) - 1
            right_half_pointer = 0

            at_paper_edge = False
            while not at_paper_edge:
                if right_half[right_half_pointer][MARKED]:
                    left_half[left_half_pointer][MARKED] = True
                
                left_half_pointer -= 1
                right_half_pointer += 1

                try:
                    left_half[left_half_pointer]
                    right_half[right_half_pointer]
                except:
                    at_paper_edge = True
        
        updated_map = []
        for row in self.__paper_map:
            updated_map.append(row[:point])
        
        self.__paper_map = updated_map

    def __fold_with_y(self, point):
        # fold_line = self.__paper_map[point]
        top_half = self.__paper_map[:point]
        bottom_half = self.__paper_map[point + 1:]

        top_half_pointer = len(top_half) - 1
        bottom_half_pointer = 0

        at_paper_edge = False
        while not at_paper_edge:
            row_above = top_half[top_half_pointer]
            row_below = bottom_half[bottom_half_pointer]

            for mark_idx, below_marker in enumerate(row_below, start=0):
                if below_marker[MARKED]:
                    row_above[mark_idx][MARKED] = True

            top_half_pointer -= 1
            bottom_half_pointer += 1

            try:
                top_half[top_half_pointer]
                bottom_half[bottom_half_pointer]
            except:
                at_paper_edge = True

        self.__paper_map = self.__paper_map[:point]

    def __create_marker(self):
        return { MARKED: False }

    def __create_map(self, width, height):
        self.__paper_map = []
        while len(self.__paper_map) < height:
            row = []
            while len(row) < width:
                row.append(self.__create_marker())

            self.__paper_map.append(row)

    def __is_list(self, arr):
        return type(arr).__name__ == 'list'