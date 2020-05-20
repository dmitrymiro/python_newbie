vari = {}


def string_format(input_string):
    result = input_string.replace(' ', '')
    while '--' in result or '++' in result or '-+' in result or '+-' in result:
        result = result.replace('--', '+')
        result = result.replace('++', '+')
        result = result.replace('-+', '-')
        result = result.replace('+-', '-')
    result = result.replace('-', ' - ').replace('+', ' + ').replace('*', ' * ')
    result = result.replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ')
    return result


def assign_chk(input_string):
    lst = input_string.split('=')
    lst = [x.strip() for x in lst]
    if len(lst) > 2:
        return print('Invalid assignment')
    elif not lst[0].isalpha():
        return print('Invalid identifier')
    elif lst[0].isalpha() and lst[1].isalpha():
        if lst[1] in vari.keys():
            vari.update({lst[0]: vari.get(lst[1])})
        else:
            return print('Unknown variable')
    elif lst[1].isdigit():
        vari.update({lst[0]: lst[1]})
    else:
        return print('Invalid assignment')


def calc(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '^':
        return op1 ^ op2


def post_eval(postfixlst):
    stack = []
    for token in postfixlst:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = calc(token, operand1, operand2)
            stack.append(result)
    return stack.pop()


def infix_to_postfix(s):
    rank = {}
    rank['^'] = 4
    rank['*'] = 3
    rank['/'] = 3
    rank['+'] = 2
    rank['-'] = 2
    rank['('] = 1
    stack = []
    rslt = []
    lst = s.split()
    for z in lst:
        if z.isdigit():
            rslt.append(z)
        elif z.isalpha():
            if z in vari.keys():
                rslt.append(vari.get(z))
            else:
                return print('Unknown variable')
        elif z == '(':
            stack.append(z)
        elif z == ')':
            top = stack.pop()
            while top != '(':
                rslt.append(top)
                top = stack.pop()
        else:
            while len(stack) > 0 and rank[stack[-1]] >= rank[z]:
                rslt.append(stack.pop())
            stack.append(z)
    while len(stack) > 0:
        rslt.append(stack.pop())
    return rslt


while True:
    string = input()
    if string.count('(') != string.count(')'):
        print('Invalid expression')
        continue
    if string.startswith('/'):
        if string == '/exit':
            print("Bye!")
            break
        if string == '/help':
            print("The program calculates complex expressions, operate with variables")
            continue
        else:
            print('Unknown command')
            continue
    if string == '':
        continue
    if '=' in string:
        assign_chk(string)
    else:
        try:
            string = string_format(string)
            print(int(post_eval(infix_to_postfix(string))))
        except(ValueError, IndexError):
            print('Invalid expression')
        except TypeError:
            print('Unknown variable')
