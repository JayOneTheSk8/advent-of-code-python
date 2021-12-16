ZEROES = 'zeroes'
ONES = 'ones'

def convert_binary_string_to_decimal(binary_str):
    result = 0
    exponent = len(binary_str) - 1

    for char in binary_str:
        num = int(char)
        result += num * 2 ** exponent

        exponent -= 1

    return result

def calculate_power_consumption():
    counts = {}

    with open("day_3/input.txt") as f:
        lines = f.readlines()
        for bin in lines:
            binary_str = bin.replace('\n', '')

            for idx, bit in enumerate(binary_str, start=0):
                if counts.get(idx):

                    if bit == '1':
                        if counts[idx].get(ONES):
                            counts[idx][ONES] += 1
                        else:
                            counts[idx] = { **counts[idx], ONES: 1 }

                    elif bit == '0':
                        if counts[idx].get(ZEROES):
                            counts[idx][ZEROES] += 1
                        else:
                            counts[idx] = { **counts[idx], ZEROES: 1 }
                else:
                    if bit == '1':
                        counts[idx] = { ONES: 1 }
                    elif bit == '0':
                        counts[idx] = { ZEROES: 1 }
    
    gamma_rate = ''
    epsilon_rate = ''

    for index in counts:
        ones_count = counts[index][ONES]
        zeroes_count = counts[index][ZEROES]

        if ones_count >= zeroes_count:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    gamma_dec = convert_binary_string_to_decimal(gamma_rate)
    epsilon_dec = convert_binary_string_to_decimal(epsilon_rate)

    return gamma_dec * epsilon_dec

print(calculate_power_consumption())