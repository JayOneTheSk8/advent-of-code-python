from bingo.bingo_card import BingoCard

def play_bingo():
    num_list = []
    bingo_cards = {}
    cards_in_play = set()

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
                bingo_cards[id_num] = bingo_card
                cards_in_play.add(id_num)

                id_num += 1
                rows = []

    remaining_card = None
    for called_num in num_list:
        if len(cards_in_play) == 1:
            card_id = list(cards_in_play)[0]
            last_card = bingo_cards[card_id]

            last_card.respond_to_number(called_num)

            if last_card.is_winning_card():
                remaining_card = last_card
                break

            continue
        
        remaining_cards = {}
        for cid in bingo_cards:
            if cid in cards_in_play:
                remaining_cards[cid] = bingo_cards[cid]

        for card_id in remaining_cards:
            card = bingo_cards[card_id]
            card.respond_to_number(called_num)
            
            if card.is_winning_card():
                cards_in_play.remove(card_id)

    if not remaining_card:
        return False
    
    remaining_card.print_card()
    win_styles = remaining_card.get_win_styles()

    print(f"Winner on number: {remaining_card.get_last_heard_number()}")
    for win_style in win_styles:
        print(f"With a: {win_style} win on the {win_styles[win_style]} {win_style}")
        

    return remaining_card.get_score()

print(play_bingo())