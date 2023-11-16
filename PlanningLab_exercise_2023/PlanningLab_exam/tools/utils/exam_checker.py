import numpy as np

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
    
    
def check_1_1(env_name, policy): 
    print("Environment: {}\n".format(env_name))
    
    if env_name != 'SlipperyFrozenLakeEnv-v0':
        print(bcolors.BOLD + "Be careful, you are working on the wrong environment!"+ bcolors.ENDC)
        print("Hint: try to run cells again from the beginning of the notebook")
        return
        
    print("Your solution:\n{}\n".format(policy))
    solution = np.array([['D','R','D','L'],['D','D','D','L'],['R','D','D','D'],['R','R','R','L']])
    if not np.all(policy == solution):
        print(bcolors.FAIL + "Your solution is not correct")
    else:
        print(bcolors.BOLD + bcolors.OKGREEN + 'Your solution is correct!\n'+ bcolors.ENDC)
        
        
def check_1_2(action):
    if action == 'D' or action == 3:
        print(bcolors.BOLD + bcolors.OKGREEN + 'Your solution is correct!\n'+ bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Your solution is not correct")
        
        
def check_1_3(env_name, policy): 
    print("Environment: {}\n".format(env_name))
    
    if env_name != 'ModifiableFrozenLakeEnv-v0':
        print(bcolors.BOLD + "Be careful, you are working on the wrong environment!"+ bcolors.ENDC)
        print("Hint: try to run cells again from the beginning of the notebook")
        return
        
    print("Your solution:\n{}\n".format(policy))
    solution = np.array([['L', 'U', 'U', 'U'], ['L', 'L', 'D', 'U'], ['U', 'D', 'L', 'D'], ['R', 'R', 'R', 'L']])
    if not np.all(policy == solution):
        print(bcolors.FAIL + "Your solution is not correct")
    else:
        print(bcolors.BOLD + bcolors.OKGREEN + 'Your solution is correct!\n'+ bcolors.ENDC)
        
        
def check_2_1(admissible):
    if admissible:
        print(bcolors.BOLD + bcolors.OKGREEN + 'Your solution is correct!\n'+ bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Your solution is not correct")
        
        
def check_2_2(env_name, path, time_cost, space_cost):
    
    print("Environment: {}\n".format(env_name))
    if env_name != 'BigFrozenLakeEnv-v0':
        print(bcolors.BOLD + "Be careful, you are working on the wrong environment!"+ bcolors.ENDC)
        print("Hint: try to run cells again from the beginning of the notebook")
        return
    
    if path != [(1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5), (6, 5), (7, 5), (7, 6), (7, 7)]:
        print(bcolors.FAIL + "Your solution is not correct" + bcolors.ENDC)
    elif time_cost != 6473:
        print(bcolors.FAIL + "The number of node explored is not correct, should be: 103723\n" + bcolors.ENDC)
    elif space_cost != 4855:
        print(bcolors.FAIL + "The max number of nodes in memory is not correct, should be: 77791\n" + bcolors.ENDC)
    else:
        print(bcolors.BOLD + bcolors.OKGREEN + 'Your solution is correct!\n'+ bcolors.ENDC)
        
        
def check_2_3(env_name, path, time_cost, space_cost):
    
    print("Environment: {}\n".format(env_name))
    if env_name != 'LeftFrozenLakeEnv-v0':
        print(bcolors.BOLD + "Be careful, you are working on the wrong environment!"+ bcolors.ENDC)
        print("Hint: try to run cells again from the beginning of the notebook")
        return
    
    if path != [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (6, 1), (6, 2), (5, 2), (4, 2), (3, 2), (2, 2)]:
        print(bcolors.FAIL + "Your solution is not correct" + bcolors.ENDC)
    elif time_cost != 113:
        print(bcolors.FAIL + "The number of node explored is not correct, should be: 113\n" + bcolors.ENDC)
    elif space_cost != 31:
        print(bcolors.FAIL + "The max number of nodes in memory is not correct, should be: 31\n" + bcolors.ENDC)
    else:
        print(bcolors.BOLD + bcolors.OKGREEN + 'Your solution is correct!\n'+ bcolors.ENDC)
        