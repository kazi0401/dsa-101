
def eval_rpn(expression: list) -> int:
    mystack = []
    result = None
    for element in expression:
        if element == "+" or element == "-" or element == "/" or element == "*":
            lastelement = mystack.pop()
            secondtolastelement = mystack.pop()
            if element == "+":
                result = secondtolastelement + lastelement
            elif element == "-":
                result = secondtolastelement - lastelement
            elif element == "/":
                result = secondtolastelement // lastelement
            elif element == "*":
                result = secondtolastelement * lastelement
            mystack.append(result)
        else:
            num = eval(element)
            mystack.append(num)
    return mystack[0]


