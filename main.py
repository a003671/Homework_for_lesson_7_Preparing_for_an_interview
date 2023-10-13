from stack import MyStack


def bracket_balance(string: str) -> str:
    my_stack = MyStack()
    pattern_int = '[({'
    pattern_out = '])}'
    flag = True
    for elem in string:
        if elem in pattern_int:
            my_stack.push(elem)
        else:
            if my_stack.size() > 0 and pattern_out.index(elem) == pattern_int.index(my_stack.peek()):
                my_stack.pop()
            else:
                 flag = False
                 break
    
    print('Сбалансированно' if flag else 'Несбалансированно')


if __name__ == '__main__':
    string = '(((([{}]))))'
    # string ='}{}'
    # string = '[([])((([[[]]])))]{()}'
    # string = '{{[()]}}'
    # string = '{{[(])]}}'
    # string = '[[{())}]'
    bracket_balance(string)