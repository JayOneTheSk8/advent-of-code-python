OPEN_PAREN = '('
CLOSE_PAREN = ')'
OPEN_BRACE ='{'
CLOSE_BRACE = '}'
OPEN_BRACKET ='['
CLOSE_BRACKET = ']'
OPEN_ANGLE_BRACKET = '<'
CLOSE_ANGLE_BRACKET = '>'

open_block = [
    OPEN_PAREN,
    OPEN_BRACE,
    OPEN_BRACKET,
    OPEN_ANGLE_BRACKET,
]

close_block = [
    CLOSE_PAREN,
    CLOSE_BRACE,
    CLOSE_BRACKET,
    CLOSE_ANGLE_BRACKET,
]

scores = {
    CLOSE_PAREN: 3,
    CLOSE_BRACE: 1197,
    CLOSE_BRACKET: 57,
    CLOSE_ANGLE_BRACKET: 25137,
}

def find_paren_syntax_error(paren_str):
    parens = []

    for paren in paren_str:
        if len(parens) == 0 and paren not in close_block:
            parens.append(paren)
            continue
        
        if paren in open_block:
            parens.append(paren)
        else:
            if len(parens) == 0:
                return scores[paren]

            if paren == CLOSE_PAREN:
                if parens[-1] == OPEN_PAREN:
                    parens.pop()
                else:
                    return scores[paren]

            elif paren == CLOSE_BRACE:
                if parens[-1] == OPEN_BRACE:
                    parens.pop()
                else:
                    return scores[paren]
                
            elif paren == CLOSE_BRACKET:
                if parens[-1] == OPEN_BRACKET:
                    parens.pop()
                else:
                    return scores[paren]
                
            elif paren == CLOSE_ANGLE_BRACKET:
                if parens[-1] == OPEN_ANGLE_BRACKET:
                    parens.pop()
                else:
                    return scores[paren]

    return 0

def get_nav_system_syntax_errors():
    nav_subsystem = []

    with open('day_10/input.txt') as f:
        nav_subsystem += f.read().splitlines()
    
    final_score = 0

    for paren_str in nav_subsystem:
        final_score += find_paren_syntax_error(paren_str)

    return final_score

print(get_nav_system_syntax_errors())