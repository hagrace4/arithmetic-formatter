def arithmetic_arranger(problems, solution=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_op = []
    second_op = []
    operator = []

    ## Output variables
    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for problem in problems:
        prbl = problem.split()
        first_op.append(prbl[0])
        operator.append(prbl[1])
        second_op.append(prbl[2])

    ## Error Messages
    if "/" in operator or "*" in operator:
        return "Error: Operator must be '+' or '-'."

    for i in range(len(first_op)):
        if not (first_op[i].isdigit() and second_op[i].isdigit()):
            return "Error: Numbers must only contain digits."

    for i in range(len(first_op)):
        if len(first_op[i]) > 4 or len(second_op[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    for i in range(len(first_op)):
        if len(first_op[i]) > len(second_op[i]):
            first_line.append(' ' * 2 + first_op[i])
        else:
            first_line.append(' ' * ((len(second_op[i]) - len(first_op[i])) + 2) + first_op[i])

    for i in range(len(second_op)):
        if len(first_op[i]) > len(second_op[i]):
            second_line.append(operator[i] + ' ' * (len(first_op[i]) - len(second_op[i]) + 1) + second_op[i])
        else:
            second_line.append(operator[i] + ' ' + second_op[i])

    for i in range(len(first_op)):
        third_line.append('-' * (max(len(first_op[i]), len(second_op[i])) + 2))

    if solution:
        for i in range(len(operator)):
            if operator[i] == "+":
                ans = str(int(first_op[i]) + int(second_op[i]))
            else:
                ans = str(int(first_op[i]) - int(second_op[i]))

            if len(ans) > max(len(first_op[i]), len(second_op[i])):
                fourth_line.append(" " + ans)
            else:
                fourth_line.append(" " * (max(len(first_op[i]), len(second_op[i])) - len(ans) + 2) + ans)

        arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(
            third_line) + '\n' + '    '.join(fourth_line)
    else:
        arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(third_line)

    return arranged_problems