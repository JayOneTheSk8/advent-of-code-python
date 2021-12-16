INPUTS = 'inputs'
OUTPUTS = 'outputs'

def get_available_signal_output_values():
    signals = []

    with open('day_8/input.txt') as f:
        lines = f.read().splitlines()
        delimeter = ' | '

        for line in lines:
            l = line.split(delimeter)
            signals.append({ INPUTS: l[0].split(' '), OUTPUTS: l[1].split(' ') })

    one_signal_length = 2
    four_signal_length = 4
    seven_signal_length = 3
    eight_signal_length = 7

    available_count = 0

    for signal in signals:
        outputs = signal[OUTPUTS]
        for output in outputs:
            if len(output) == one_signal_length \
                or len(output) == four_signal_length \
                or len(output) == seven_signal_length \
                or len(output) == eight_signal_length:
                    available_count += 1
    
    return available_count

print(get_available_signal_output_values())