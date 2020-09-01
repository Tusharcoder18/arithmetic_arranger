

def check_conditions(problems: str):
    pass

def calc_space(a: str, b: str, isSecond: bool):
    if len(a) > len(b):
        spaces = 1  
    elif len(a) < len(b):
        spaces = (len(b) - len(a)) + 1
    elif len(a) < len(b) and isSecond:
        spaces = (len(b) - len(a)) + 1
    else:
        spaces = 1
    
    # result = [' ' for _ in range(spaces)]  
    # return ''.join(result)
    return spaces
    



def arithmetic_arranger(problems: list):
    line1 = []
    line2 = []
    line1_space = []
    line2_space = []
    for problem in problems:
        elements = problem.split()
        line1.append(elements[0])
        line2.extend(elements[1:])
        line1_space.append(calc_space(elements[0], elements[-1], False))
        line2_space.append(calc_space(elements[-1], elements[0], True))
    
    print(line1)
    print(line1_space)
    print(line2)
    print(line2_space)
    return -1


#inputs
problems = input('Enter problems').split(',')

result = arithmetic_arranger(problems)

print(result)
