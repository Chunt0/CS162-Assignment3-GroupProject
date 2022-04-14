def input_num(prompt, num, low=1):
    """Checks validity of input"""
    while True:
        str = input(prompt)
        if len(str) > 0 and str.isnumeric():
            val = int(str) - low
            if val in range(num):
                return val + low
        print(f'Are you daft?! You only have to type in a number between 1 and {num}.')


#------------------------------------------------------------------------------------------
def input_options(prompt, options):
    opt_str = prompt + '\n'
    for idx,opt in enumerate(options):
        opt_str += f"  {idx+1:2}. {opt}\n"
    return input_num(opt_str, len(options))

#------------------------------------------------------------------------------------------
def input_yes_no():
    """Yes or No questions"""
    num = input_num("1. Yes \n2. No\n", 2)
    while True:
        if num == 1:
            return True
        elif num == 2:
            return False
        else:
            "Please only enter 1 or 2"

