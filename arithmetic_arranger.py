

def check_conditions(problems: str):
    pass

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



result = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

print(result)
