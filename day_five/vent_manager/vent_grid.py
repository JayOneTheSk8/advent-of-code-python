COUNT = 'count'

class VentGrid():

    def __init__(self, row_count=1000, count_diagonals=False):
        self.__create_grid(int(row_count))
        self.__count_diagonals = count_diagonals

    def mark_vent(self, line):
        if not self.__is_list(line) or not self.__is_list(line[0]) or not self.__is_list(line[1]):
            raise ValueError('Lines must be list of 2 lists')

        if len(line) != 2 or len(line[0]) != 2 or len(line[1]) != 2:
            raise Exception('Lines must be two points')

        # [ [1, 1], [3, 3] ]
        if line[0][0] == line[0][1] and line[1][0] == line[1][1]:
            if self.__count_diagonals:
                self.__handle_same_number_diagonal(line[0][0], line[1][0])
        
        # [ [9, 7], [7, 9] ]
        elif line[0][0] == line[1][1] and line[0][1] == line[1][0]:
            if self.__count_diagonals:
                start_point = line[0][0]
                end_point = line[0][1]
                self.__handle_swap_num_diagonal(min(start_point, end_point), max(start_point, end_point))

        # [ [2, 1], [2, 7] ]
        elif line[0][0] == line[1][0]:
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

        # [ [2, 0], [6, 4]]
        elif line[0][0] - line[1][0] == line[0][1] - line[1][1]:
            if self.__count_diagonals:
                larger_nums = line[1]
                smaller_nums = line[0]

                if max(line[0][0], line[1][0]) == line[0][0]:
                    larger_nums = line[0]
                    smaller_nums = line[1]

                self.__handle_growing_diagonal(smaller_nums[0], smaller_nums[1], larger_nums[0], larger_nums[1])

        # [ [8, 2], [5, 5] ]
        elif abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1]):
            if self.__count_diagonals:
                larger_nums = line[1]
                smaller_nums = line[0]

                if max(line[0][0], line[1][0]) == line[0][0]:
                    larger_nums = line[0]
                    smaller_nums = line[1]

                self.__handle_shrinking_diagonal(larger_nums[0], larger_nums[1], smaller_nums[0], smaller_nums[1])

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

    def __handle_growing_diagonal(self, x, y, limit_x, limit_y):
        iter_x = x
        iter_y = y

        while iter_x <= limit_x and iter_y <= limit_y:
            self.__rows[iter_y][iter_x][COUNT] += 1

            iter_x += 1
            iter_y += 1

    def __handle_shrinking_diagonal(self, x, y, lower_limit_x, lower_limit_y):
        iter_x = x
        iter_y = y

        while iter_y <= lower_limit_y and iter_x >= lower_limit_x:
            self.__rows[iter_y][iter_x][COUNT] += 1

            iter_x -= 1
            iter_y += 1

    def __handle_swap_num_diagonal(self, start_point, end_point):
        offset = 0

        for row_idx in range(start_point, end_point + 1):
            self.__rows[row_idx][end_point - offset][COUNT] += 1
            offset += 1

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