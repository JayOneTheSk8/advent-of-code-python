COUNT = 'count'

class VentGrid():

    def __init__(self, row_count=1000):
        self.__create_grid(int(row_count))

    def mark_vent(self, line):
        if not self.__is_list(line) or not self.__is_list(line[0]) or not self.__is_list(line[1]):
            raise ValueError('Lines must be list of 2 lists')

        if len(line) != 2 or len(line[0]) != 2 or len(line[1]) != 2:
            raise Exception('Lines must be two points')

        # [ [2, 1], [2, 7] ]
        if line[0][0] == line[1][0]:
            x = line[0][0]
            y1 = line[0][1]
            y2 = line[1][1]
            self.__handle_vertical_line(x, min(y1, y2), max(y1, y2))

        # [ [7, 3], [2, 3] ]
        elif line[0][1] == line[1][1]:
            y = line[0][1]
            x1 = line[0][0]
            x2 = line[1][0]
            self.__handle_horizontal_line(y, min(x1, x2), max(x1, x2))

        else:
            pass
    
    def print_rows(self):
        for row in self.__rows:
            print(row)

    def get_rows(self):
        return self.__rows

    def get_points_where_lines_overlap(self):
        count = 0
        for row in self.__rows:
            for vent_marker in row:
                if vent_marker[COUNT] > 1:
                    count += 1

        return count 

    def __handle_vertical_line(self, x, start_y, end_y):
        for y in range(start_y, end_y + 1):
            self.__rows[y][x][COUNT] += 1

    def __handle_horizontal_line(self, y, start_x, end_x):
        for x in range(start_x, end_x + 1):
            self.__rows[y][x][COUNT] += 1

    def __handle_same_number_diagonal(self, start_num, end_num):
        for point in range(start_num, end_num + 1):
            self.__rows[point][point][COUNT] += 1

    def __create_vent_marker(self):
        return { COUNT: 0 }

    def __create_grid(self, row_count):
        rows = []
        for _ in range(row_count):
            finished_row = []
            for __ in range(row_count):
                vent_marker = self.__create_vent_marker()
                finished_row.append(vent_marker)

            rows.append(finished_row)

        self.__rows = rows

    def __is_list(self, arr):
        return type(arr).__name__ == 'list'