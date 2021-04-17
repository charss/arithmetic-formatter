
def arithmetic_arranger(problems, answer=False):
    arr = []
    spaces = ' ' * 4
    to_print = ''
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        temp = problem.split(' ')
        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."
        elif len(temp[0]) > 4 or len(temp[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        elif not (temp[0].isdigit() and temp[2].isdigit()):
            return "Error: Numbers must only contain digits."
        arr += [temp]
    number1 = [x[0] for x in arr]
    operator = [x[1] for x in arr]
    number2 = [x[2] for x in arr]
    for i in range(len(number1)):
        padding = max(len(number1[i]), len(number2[i])) + 2
        to_print += ' ' * (padding - len(number1[i])) + number1[i]
        if i != len(number1) - 1:
            to_print += spaces
    to_print += '\n'
    for i in range(len(number2)):
        padding = max(len(number1[i]), len(number2[i])) + 2
        to_print += operator[i] + ' ' * (padding - len(number2[i]) - 1) + number2[i]
        if i != len(number2) - 1:
            to_print += spaces
    to_print += '\n'
    for i in range(len(number2)):
        padding = max(len(number1[i]), len(number2[i])) + 2
        to_print += '-' * padding
        if i != len(number2) - 1:
            to_print += spaces
    if answer == False:
        return to_print
    to_print += '\n'
    for i in range(len(number1)):
        padding = max(len(number1[i]), len(number2[i])) + 2
        ans_plus = str(int(number1[i]) + int(number2[i])).rjust(padding)
        ans_minus = str(int(number1[i]) - int(number2[i])).rjust(padding)
        if operator[i] == '+':
            to_print += ' ' * (padding - len(ans_plus)) + ans_plus
        else:
            to_print += ' ' * (padding - len(ans_minus)) + ans_minus
        if i != len(number1) - 1:
            to_print += spaces
    return to_print
print(arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49']))
