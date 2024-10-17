#Завдання 6

keywords = ('for', 'if', 'else', 'in', ':')

code_structure = """
for each token in the postfix expression :
    if the token is a number :
        print('Convert it to an integer and add it to the end of values')
    else:
        print('Append the result to the end of values')
"""

def visualize_code_structure(code, keywords):
    lines = code.strip().split('\n')
    for line in lines:
        stripped_line = line.lstrip()
        indent_level = (len(line) - len(stripped_line)) // 4
        if any(keyword in stripped_line for keyword in keywords):
            print(' ' * 4 * indent_level + stripped_line)
        else:
            print(' ' * 4 * (indent_level + 1) + stripped_line)


visualize_code_structure(code_structure, keywords)