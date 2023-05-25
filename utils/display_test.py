class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def display_test_header(header: str):
    print(f"{bcolors.OKBLUE}\n{header}\n{bcolors.ENDC}")

def display_test_results(func, args, correct_res, res):
    print(f"{func.__name__}({', '.join(args)}) should output: {correct_res}. Real ouput: {res}. Passes: ", f"{bcolors.OKGREEN}Pass{bcolors.ENDC}" if res == correct_res else f"{bcolors.FAIL}Fail{bcolors.ENDC}")