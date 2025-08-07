
def is_balanced(brackets: str) -> bool:
    # stack
    # ([{}])

    stack = [] 
    # push -> append
    # pop -> pop

    bracket_map = {'(' : ')', '[' : ']', '{' : '}'}

    for b in brackets:
        if b in bracket_map.keys():
        # open brace -> push onto the stack
            stack.append(b)

        if b in bracket_map.values():
            if len(stack) > 0 and b == bracket_map[stack[-1]]:
            # appropriate closed brace -> pop off the stack
                stack.pop()
            else:
            # wrong bracket -> false
            # closing bracket without any opening brackets
                return False
    
    if len(stack) == 0:
        return True 
    else:
        return False 
    
    # return len(stack) == 0


if __name__ == '__main__':
    brackets = '{([({})])}{}'

    print(is_balanced(brackets))