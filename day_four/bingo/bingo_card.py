ROW_ERROR = 'Rows must be list'
ROW_COUNT_ERROR = 'Must be 5 rows in card'
NUM = 'num'
MARKED = 'marked'
ROW_COUNT = 5

class BingoCard:

    def __init__(self, rows):
        if not self.__is_list(rows):
            raise AttributeError(ROW_ERROR)

        if len(rows) != ROW_COUNT:
            raise AttributeError(ROW_COUNT_ERROR)

        for row in rows:
            if not self.__is_list(row):
                raise AttributeError(ROW_ERROR)

            if len(row) != ROW_COUNT:
                raise AttributeError(ROW_COUNT_ERROR)
        
        self.__fill_rows(rows)
        self.__heard_numbers = []
        self.__is_winning_card = False

    def print_card(self):
        print(' B | I | N | G | O')
        print(f" {self.__rows[0][0][NUM]} {self.__rows[0][0][MARKED]} | {self.__rows[0][1][NUM]} {self.__rows[0][1][MARKED]} | {self.__rows[0][2][NUM]} {self.__rows[0][2][MARKED]} | {self.__rows[0][3][NUM]} {self.__rows[0][3][MARKED]} | {self.__rows[0][4][NUM]} {self.__rows[0][4][MARKED]} |")
        print(f" {self.__rows[1][0][NUM]} {self.__rows[1][0][MARKED]} | {self.__rows[1][1][NUM]} {self.__rows[1][1][MARKED]} | {self.__rows[1][2][NUM]} {self.__rows[1][2][MARKED]} | {self.__rows[1][3][NUM]} {self.__rows[1][3][MARKED]} | {self.__rows[1][4][NUM]} {self.__rows[1][4][MARKED]} |")
        print(f" {self.__rows[2][0][NUM]} {self.__rows[2][0][MARKED]} | {self.__rows[2][1][NUM]} {self.__rows[2][1][MARKED]} | {self.__rows[2][2][NUM]} {self.__rows[2][2][MARKED]} | {self.__rows[2][3][NUM]} {self.__rows[2][3][MARKED]} | {self.__rows[2][4][NUM]} {self.__rows[2][4][MARKED]} |")
        print(f" {self.__rows[3][0][NUM]} {self.__rows[3][0][MARKED]} | {self.__rows[3][1][NUM]} {self.__rows[3][1][MARKED]} | {self.__rows[3][2][NUM]} {self.__rows[3][2][MARKED]} | {self.__rows[3][3][NUM]} {self.__rows[3][3][MARKED]} | {self.__rows[3][4][NUM]} {self.__rows[3][4][MARKED]} |")
        print(f" {self.__rows[4][0][NUM]} {self.__rows[4][0][MARKED]} | {self.__rows[4][1][NUM]} {self.__rows[4][1][MARKED]} | {self.__rows[4][2][NUM]} {self.__rows[4][2][MARKED]} | {self.__rows[4][3][NUM]} {self.__rows[4][3][MARKED]} | {self.__rows[4][4][NUM]} {self.__rows[4][4][MARKED]} |")

    def is_winning_card(self):
        return self.__is_winning_card

    def get_row(self, row_num):
        return self.__rows[row_num]

    def get_b_column(self):
        return self.__get_column(0)

    def get_i_column(self):
        return self.__get_column(1)

    def get_n_column(self):
        return self.__get_column(2)

    def get_g_column(self):
        return self.__get_column(3)

    def get_o_column(self):
        return self.__get_column(4)
    
    def get_top_left_diagonal(self):
        diagonal = []
        column_num = 0

        for row in self.__rows:
            diagonal.append(row[column_num])
            column_num += 1

        return diagonal
    
    def get_top_right_diagonal(self):
        diagonal = []
        column_num = 4

        for row in self.__rows:
            diagonal.append(row[column_num])
            column_num -= 1

        return diagonal

    def get_heard_numbers(self):
        return self.__heard_numbers

    def get_last_heard_number(self):
        return self.__heard_numbers

    def respond_to_number(self, heard_number):
        self.__heard_numbers.append(heard_number)

        rows = self.__rows
        for row_num, row in enumerate(rows, start=0):
            for marker_idx, marker in enumerate(row, start=0):
                if marker[NUM] == heard_number:
                    self.__rows[row_num][marker_idx][MARKED] = True

        self.__check_wins()

    def __check_wins(self):
        for i in range(ROW_COUNT):
            row = self.get_row(i)

            if self.__check_win(row):
                self.__set_win()

        b_column = self.get_b_column()
        i_column = self.get_i_column()
        n_column = self.get_n_column()
        g_column = self.get_g_column()
        o_column = self.get_o_column()

        if self.__check_win(b_column):
            self.__set_win()

        if self.__check_win(i_column):
            self.__set_win()

        if self.__check_win(n_column):
            self.__set_win()

        if self.__check_win(g_column):
            self.__set_win()

        if self.__check_win(o_column):
            self.__set_win()

        top_left_diagonal = self.get_top_left_diagonal()
        if self.__check_win(top_left_diagonal):
            self.__set_win()

        top_right_diagonal = self.get_top_right_diagonal()
        if self.__check_win(top_right_diagonal):
            self.__set_win()


    def __check_win(self, line):
        print(line)
        marks = 0
        for marker in line:
            if marker[MARKED]:
                marks += 1

        return marks == ROW_COUNT

    def __set_win(self):
        self.__is_winning_card = True

    def __get_column(self, column_num):
        column = []
        for row in self.__rows:
            column.append(row[column_num])

        return column

    def __create_marker(self, num):
        return { NUM: num, MARKED: False }

    def __fill_rows(self, rows):
        final_board = []
        
        for row in rows:
            final_row = []

            for num in row:
                final_row.append(self.__create_marker(num))

            final_board.append(final_row)

        self.__rows = final_board

    def __is_list(self, arr):
        return type(arr).__name__ == 'list'
