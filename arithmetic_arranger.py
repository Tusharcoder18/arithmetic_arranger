

def operator_check(problems: list):
    for problem in problems:
        elements = problem.split()
        if ('+' not in elements) and ('-' not in elements):
            return True
    return False

def operand_check(problems: list):
    for problem in problems:
        elements = problem.split()
        if not elements[0].isdigit() or not elements[-1].isdigit():
            return True
    
    return False
        
def digit_length_check(problems: list):
    for problem in problems:
        elements = problem.split()
        if len(elements[0]) > 4 or len(elements[-1]) > 4:
            return True
    
    return False

def check_conditions(problems: list):
    if len(problems) > 5:
        print('Error: Too many problems.')
        return False
    elif operator_check(problems):
        print("Error: Operator must be '+' or '-'.")
        return False
    elif operand_check(problems):
        print('Error: Numbers must only contain digits.')
        return False
    elif digit_length_check(problems):
        print('Error: Numbers cannot be more than four digits.')
        return False
    else:
        return True



def calc_space(a: str, b: str, isSecond: bool):
    if (len(a) > len(b) or len(a) == len(b)) and isSecond == False:
        spaces = 2  
    elif len(a) < len(b) and isSecond:
        spaces = (len(b) - len(a)) + 1
    elif len(a) < len(b):
        spaces = (len(b) - len(a)) + 2
    else:
        spaces = 1
    
    result = [' ' for _ in range(spaces)]  
    return ''.join(result)
    
def calc_dashes(a: str, b: str ):
    dashes_count = max(len(a), len(b)) + 2
    return ''.join(['-' for _ in range(dashes_count)])

def calc_answers(problems: list, dashes: list):
    ops = {
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
    }
    result = ''
    answers = []
    for problem in problems:
        elements = problem.split()
        answer = ops[elements[1]] (int(elements[0]), int(elements[-1]))
        answers.append(str(answer))

    for index in range(len(answers)):
        space = len(dashes[index]) - len(answers[index])
        space = [' ' for _ in range(space)]
        space = ''.join(space)
        answers[index] = space + answers[index]
    
    for answer in answers:
        result += answer + '    '
    return result



def arithmetic_arranger(problems: list, answers = False):
    if check_conditions(problems):
        line1 = []
        line2 = []
        operators = []
        line1_space = []
        line2_space = []
        dashes = []
        for problem in problems:
            elements = problem.split()
            line1.append(elements[0])
            operators.append(elements[1])
            line2.append(elements[-1])
            line1_space.append(calc_space(elements[0], elements[-1], False))
            line2_space.append(calc_space(elements[-1], elements[0], True))
            dashes.append(calc_dashes(elements[0], elements[-1]))

        result = ''

        for index in range(len(line1)):
            result += line1_space[index] + line1[index] + '    '
        result += '\n'
        for index in range(len(line2)):
            result += operators[index] + line2_space[index] + line2[index] + '    '
        result += '\n'
        for index in range(len(dashes)):
            result += dashes[index] + '    '
        
        if answers:
            result += '\n'
            result += calc_answers(problems, dashes)

        return result
    
    return 



result = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)

print(result)

# ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
# ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]
# ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]
# ["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]
# ["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]
# ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]
# ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True
