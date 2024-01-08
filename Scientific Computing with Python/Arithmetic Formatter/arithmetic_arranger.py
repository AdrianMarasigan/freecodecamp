def arithmetic_arranger(problems, results=False):
    # Initialize variables to store the top, bottom, dashes, and answer lines
    top = ""
    bottom = ""
    dashes = ""
    answer = ""

    # Check if there are more than 5 problems, return an error if true
    if len(problems) > 5:
        return "Error: Too many problems."

    # Iterate through each problem in the list
    for problem in problems:
        # Split the problem into operands and operator
        operands = problem.split(' ')

        # Check if operands are valid digits
        if not (operands[0].isdigit() and operands[2].isdigit()):
            return "Error: Numbers must only contain digits."

        # Find the longest operand for formatting purposes
        res = max(operands, key=len)

        # Calculate the answer based on the operator
        if operands[1] == "+":
            problem_answer = int(operands[0]) + int(operands[2])
        elif operands[1] == "-":
            problem_answer = int(operands[0]) - int(operands[2])

        # Check if the numbers are more than four digits, return an error if true
        if len(res) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Check if the operator is multiplication or division, return an error if true
        if operands[1] == "*" or operands[1] == "/":
            return "Error: Operator must be '+' or '-'."

        # Format the lines based on the length of operands
        if len(operands[0]) < len(operands[2]):
            # Formatting for when the first operand is shorter
            b4_spaces = len(operands[2]) + 2
            problem_answer_length = len(str(problem_answer))
            row1_space = b4_spaces - len(operands[0])
            spacing = " " * row1_space
            top += spacing + operands[0] + "    "
            bottom += operands[1] + " " + operands[2] + "    "
            dashes += b4_spaces * "-" + "    "
            answer += " " * (b4_spaces - problem_answer_length) + str(problem_answer) + "    "

        # Continue similar formatting for other cases
        if len(operands[0]) == len(operands[2]):
            # Formatting for when both operands are of the same length
            b4_spaces = len(operands[0]) + 2
            row1_space = b4_spaces - len(operands[0])
            spacing = " " * row1_space
            top += spacing + operands[0] + "    "
            bottom += operands[1] + " " + operands[2] + "    "
            dashes += b4_spaces * "-" + "    "
            answer += spacing + str(problem_answer) + "    "

        if len(operands[0]) > len(operands[2]):
            # Formatting for when the first operand is longer
            spacing = " " * ((len(operands[0]) + 2) - (len(operands[2]) + 1))
            problem_answer_length = len(str(problem_answer))
            top += "  " + operands[0] + "    "
            bottom += operands[1] + spacing + operands[2] + "    "
            dashes += (len(operands[0]) + 2) * "-" + "    "
            answer += ((len(operands[0]) + 2) - problem_answer_length) * " " + str(problem_answer) + "    "

    # Remove trailing whitespaces and join lines
    top = top.rstrip()
    top += top.join("\n")
    bottom = bottom.rstrip()
    bottom += bottom.join("\n")
    dashes = dashes.rstrip()
    answer = answer.rstrip()

    # Combine the lines based on the specified format (with or without results)
    if results:
        dashes += dashes.join("\n")
        return top + bottom + dashes + answer
    else:
        return top + bottom + dashes
