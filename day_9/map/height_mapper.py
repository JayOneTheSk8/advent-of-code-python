class HeightMapper():

    def __init__(self, number_map):
        self.__create_map(number_map)
        self.__low_points = []

    def print_map(self):
        for row in self.__number_map:
            print(row)

    def get_risk_level(self):
        low_points = self.get_low_points()
        risk_level = 0
        
        for low_point in low_points:
            low_point_num = self.__number_map[low_point[0]][low_point[1]]
            risk_level += low_point_num + 1
        
        return risk_level

    def get_low_points(self):
        if len(self.__low_points) > 0:
            return self.__low_points

        for row_num, row in enumerate(self.__number_map, start=0):
            for pos_idx, num in enumerate(row, start=0):
                low_point = self.__dip_in_row(row_num, pos_idx) and self.__dip_in_column(row_num, pos_idx)

                if low_point:
                    self.__low_points.append([row_num, pos_idx])
        
        return self.__low_points

    def __dip_in_row(self, row, pos):
        before_num = None
        after_num = None

        try:
            if not pos - 1 < 0:
                before_num = self.__number_map[row][pos - 1]
        except:
            pass

        try:
            after_num = self.__number_map[row][pos + 1]
        except:
            pass

        current_num = self.__number_map[row][pos]

        if before_num is None:
            return current_num < after_num
        elif after_num is None:
            return before_num > current_num
        else:
            return before_num > current_num and current_num < after_num

    def __dip_in_column(self, row, pos):
        top_num = None
        bottom_num = None

        try:
            if not row - 1 < 0:
                top_num = self.__number_map[row - 1][pos]
        except:
            pass
        
        try:
            bottom_num = self.__number_map[row + 1][pos]
        except:
            pass

        current_num = self.__number_map[row][pos]

        if top_num is None:
            return current_num < bottom_num
        elif bottom_num is None:
            return top_num > current_num
        else:
            return top_num > current_num and current_num < bottom_num

    def __create_map(self, number_map):
        self.__number_map = []
        for numbers in number_map:
            self.__number_map.append([int(n) for n in numbers])

