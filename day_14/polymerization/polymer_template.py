class PolymerTemplate():

    def __init__(self, base_string, rules):
        self.__polymer = [s for s in base_string]
        self.__rules = rules
    
    def get_polymer(self):
        return ''.join(self.__polymer)

    def get_element_counts(self):
        el_counts = {}
        for el in self.__polymer:
            if el in el_counts:
                el_counts[el] += 1
            else:
                el_counts[el] = 1

        return el_counts

    def get_highest_count(self):
        counts = self.get_element_counts()
        
        highest_count = 0

        for el in counts:
            if highest_count < counts[el]:
                highest_count = counts[el]
        
        return highest_count

    def get_lowest_count(self):
        counts = self.get_element_counts()
        
        lowest_count = 0

        for idx, el in enumerate(counts, start=0):
            if idx == 0:
                lowest_el = el
                lowest_count = counts[el]
                continue

            if lowest_count > counts[el]:
                lowest_count = counts[el]
        
        return lowest_count

    def get_rules(self):
        return self.__rules

    def grow_polymer(self):
        updated_polymer = [self.__polymer[0]]

        for idx, element in enumerate(self.__polymer, start=0):
            next_el = None
            try:
                next_el = self.__polymer[idx + 1]
            except:
                continue

            pair = element + next_el

            new_el = ''
            if pair in self.__rules:
                new_el = self.__rules[pair]
            
            updated_pair = new_el + next_el
            updated_polymer += [e for e in updated_pair]
        
        self.__polymer = updated_polymer