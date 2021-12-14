ENERGY_LEVEL = 'energy level'

class Octomap():

    def __init__(self, number_map):
        self.__create_octomap(number_map)
        self.__exclude_pos = []
        self.__flash_count = 0

    def get_flash_count(self):
        return self.__flash_count

    def handle_one_step(self):
        self.__add_one_to_energy_levels()
        octopi_changing = self.__handle_flashed_octopi()

        while octopi_changing:
            octopi_changing = self.__handle_flashed_octopi()

        self.__rest_octopi()

    def __add_one_to_energy_levels(self):
        # Add 1 to every energy level
        for octopus_row in self.__octomap:
            for octopus in octopus_row:
                octopus[ENERGY_LEVEL] += 1

    def __handle_flashed_octopi(self):
        octopus_changed = False

        for row_idx, octopus_row in enumerate(self.__octomap, start=0):
            for pos_idx, octopus in enumerate(octopus_row, start=0):

                # If octopus' level is above 9 and 
                if octopus[ENERGY_LEVEL] > 9 and [row_idx, pos_idx] not in self.__exclude_pos:
                    self.__handle_initial_octopus(row_idx, pos_idx)
                    self.__exclude_pos.append([row_idx, pos_idx])
                    octopus_changed = True
        
        return octopus_changed

    def __handle_initial_octopus(self, row, pos):
        top_left_octo = None
        top_octo = None
        top_right_octo = None

        left_octo = None
        right_octo = None

        bottom_left_octo = None
        bottom_octo = None
        bottom_right_octo = None

        # TOP
        try:
            if row - 1 >= 0 and pos - 1 >= 0:
                top_left_octo = self.__octomap[row - 1][pos - 1]
        except:
            pass

        try:
            if row - 1 >= 0:
                top_octo = self.__octomap[row - 1][pos]
        except:
            pass

        try:
            if row - 1 >= 0:
                top_right_octo = self.__octomap[row - 1][pos + 1]
        except:
            pass

        # SIDES
        try:
            if pos - 1 >= 0:
                left_octo = self.__octomap[row][pos - 1]
        except:
            pass

        try:
            right_octo = self.__octomap[row][pos + 1]
        except:
            pass

        # BOTTOM
        try:
            if pos - 1 >= 0:
                bottom_left_octo = self.__octomap[row + 1][pos - 1]
        except:
            pass

        try:
            bottom_octo = self.__octomap[row + 1][pos]
        except:
            pass

        try:
            bottom_right_octo = self.__octomap[row + 1][pos + 1]
        except:
            pass            

        # Add 1 to every octopus around
        if top_left_octo:
            top_left_octo[ENERGY_LEVEL] += 1

        if top_octo:
            top_octo[ENERGY_LEVEL] += 1

        if top_right_octo:
            top_right_octo[ENERGY_LEVEL] += 1

        if left_octo:
            left_octo[ENERGY_LEVEL] += 1

        if right_octo:
            right_octo[ENERGY_LEVEL] += 1

        if bottom_left_octo:
            bottom_left_octo[ENERGY_LEVEL] += 1

        if bottom_octo:
            bottom_octo[ENERGY_LEVEL] += 1

        if bottom_right_octo:
            bottom_right_octo[ENERGY_LEVEL] += 1

    def __rest_octopi(self):
        for octopus_row in self.__octomap:
            for octopus in octopus_row:

                if octopus[ENERGY_LEVEL] > 9:
                    self.__flash_count += 1
                    octopus[ENERGY_LEVEL] = 0
        
        self.__exclude_pos = []

    def __create_octopus(self, energy_level):
        return { ENERGY_LEVEL: energy_level}

    def __create_octomap(self, number_map):
        if not self.__is_list(number_map):
            raise ValueError('Number map must be list')

        self.__octomap = []

        for row in number_map:
            result = []
            if not self.__is_list(row):
                raise ValueError('Values of number map must be list')
            for nrg_level in row:
                result.append(self.__create_octopus(nrg_level))
            
            self.__octomap.append(result)

    def __is_list(self, arr):
        return type(arr).__name__ == 'list'
