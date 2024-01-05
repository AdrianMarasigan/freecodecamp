def arithmetic_arranger(problems, results=False):
    top = ""
    bottom = ""
    dashes = ""
    answer = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        operands = problem.split(' ')

        if not (operands[0].isdigit() and operands[2].isdigit()):
            return "Error: Numbers must only contain digits."

        res = max(operands, key=len)

        if operands[1] == "+":
            problem_answer = int(operands[0]) + int(operands[2])
        elif operands[1] == "-":
            problem_answer = int(operands[0]) - int(operands[2])

        if len(res) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operands[1] == "*" or operands[1] == "/":
            return "Error: Operator must be '+' or '-'."

        if len(operands[0]) < len(operands[2]):
            b4_spaces = len(operands[2]) + 2
            problem_answer_length = len(str(problem_answer))
            row1_space = b4_spaces - len(operands[0])
            spacing = " " * row1_space
            top += spacing + operands[0] + "    "
            bottom += operands[1] + " " + operands[2] + "    "
            dashes += b4_spaces * "-" + "    "
            answer += " " * (b4_spaces - problem_answer_length) + \
                str(problem_answer) + "    "

        if len(operands[0]) == len(operands[2]):
            b4_spaces = len(operands[0]) + 2
            row1_space = b4_spaces - len(operands[0])
            spacing = " " * row1_space
            top += spacing + operands[0] + "    "
            bottom += operands[1] + " " + operands[2] + "    "
            dashes += b4_spaces * "-" + "    "
            answer += spacing + str(problem_answer) + "    "

        if len(operands[0]) > len(operands[2]):
            spacing = " " * ((len(operands[0]) + 2) - (len(operands[2]) + 1))
            problem_answer_length = len(str(problem_answer))
            top += "  " + operands[0] + "    "
            bottom += operands[1] + spacing + operands[2] + "    "
            dashes += (len(operands[0]) + 2) * "-" + "    "
            answer += ((len(operands[0]) + 2) - problem_answer_length) * \
                " " + str(problem_answer) + "    "

    top = top.rstrip()
    top += top.join("\n")
    bottom = bottom.rstrip()
    bottom += bottom.join("\n")
    dashes = dashes.rstrip()
    answer = answer.rstrip()

    if results:
        dashes += dashes.join("\n")
        return top + bottom + dashes + answer

    else:
        return top + bottom + dashes
