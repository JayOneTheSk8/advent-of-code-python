from bingo.bingo_card import BingoCard

def play_bingo():
    num_list = []
    bingo_cards = []
    game_finished = False

    with open('day_4/input.txt') as f:
        lines = f.readlines()

        parsed_lines = []
        for line in lines:
            parsed_lines.append(line.replace('\n', ''))
        
        id_num = 1
        rows = []

        for idx, parsed_line in enumerate(parsed_lines, start=0):
            if idx == 0:
                str_num_list = parsed_line.split(',')
                num_list = list(map(lambda s: int(s), str_num_list))
                continue
            
            if len(parsed_line) == 0:
                continue

            row = list(filter(lambda l: len(l) != 0, parsed_line.split(' ')))
            parsed_row = list(map(lambda s: int(s), row))
            rows.append(parsed_row)

            if (len(rows) == 5):
                bingo_card = BingoCard(id=id_num, rows=rows)
                bingo_cards.append(bingo_card)

                id_num += 1
                rows = []

    winning_card = None
    for called_num in num_list:
        if game_finished:
            break

        for card in bingo_cards:
            card.respond_to_number(called_num)
            if card.is_winning_card():
                game_finished = True
                winning_card = card
    
    if not winning_card:
        return False
    
    winning_card.print_card()
    win_styles = winning_card.get_win_styles()

    print(f"Winner on number: {winning_card.get_last_heard_number()}")
    for win_style in win_styles:
        print(f"With a: {win_style} win on the {win_styles[win_style]} {win_style}")
        

    return winning_card.get_score()

print(play_bingo())